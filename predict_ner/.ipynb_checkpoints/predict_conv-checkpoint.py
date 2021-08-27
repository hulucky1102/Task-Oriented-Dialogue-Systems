import tensorflow as tf
import json
import numpy as np

params = {
    'batch_size': 64,
    'lr' : 0.001,
    'max_sent_len': 20,
    'epochs': 500,
    'drops' : [0.1]
         }

with open('/home/ai/hgm/home_nlp/ner_model/char_conv_625.json', mode='r', encoding='utf-8') as f:
    dicts = json.load(f)

char2id = dicts['char2id']
id2intent = dicts['id2intent']
id2slot = dicts['id2slot']

params['intent_num'] = len(id2intent)
params['slot_num'] = len(id2slot)
max_sent_len = params["max_sent_len"]

def label_c(x):
    val = tf.argmax(x,axis=-1)
    val = tf.reshape(val,[params['batch_size'],1])
    return val

def ln(c_in):
    x = c_in[0]
    geta = c_in[1]
    #geta = tf.squeeze(geta)
#     beta = c_in[2]
    #beta = tf.squeeze(beta)
    x = tf.keras.layers.LayerNormalization(center=False,scale=False)(x)
#     x = geta * x + beta
    x = tf.multiply(x,geta)
    return x

tf.keras.backend.clear_session()
text_inputs = tf.keras.layers.Input(shape=(20,),name='Input')
embed = tf.keras.layers.Embedding(500,32)(text_inputs)
bilstm = tf.keras.layers.Bidirectional(tf.keras.layers.GRU(64,return_sequences=True))(embed)
x_in = tf.keras.layers.LayerNormalization()(bilstm)
x_conv = tf.keras.layers.GlobalAveragePooling1D()(x_in)
pre_intent = tf.keras.layers.Dense(params['intent_num'],\
            activation='sigmoid',name = 'pre_intent')(x_conv)
x_ner  = tf.keras.layers.LayerNormalization()(bilstm)
pre_slot = tf.keras.layers.Dense(params['slot_num'],activation='sigmoid',name = 'pre_ner')(x_ner)
model = tf.keras.Model(text_inputs,[pre_intent,pre_slot])

model.load_weights('/home/ai/hgm/home_nlp/ner_model_weight/model_conv_625.h5')

def trans2labelid(vocab, labels, max_sent_len):
    labels = [vocab[label] for label in labels]
    if len(labels) < max_sent_len:
        labels += [0] * (max_sent_len - len(labels))
    else:
        labels = labels[:max_sent_len]
    labels = np.expand_dims(labels,axis=0)
    return labels

def predict(x):
    x = list(x)
    pre_data = trans2labelid(char2id, x, max_sent_len)
    pre_data = model.predict([pre_data])
    pre_intent = pre_data[0]
    pre_intent = id2intent[str(np.argmax(pre_intent))]
    pre_slot = pre_data[1]
    pre_slot = np.squeeze(pre_slot)[:len(x)]
    pre_ner = []
    for i in pre_slot:
        if len(id2slot[str(np.argmax(i))]) > 2:
            pre_ner.append(id2slot[str(np.argmax(i))][2:])
        else:
            pre_ner.append(id2slot[str(np.argmax(i))])

    entities_dic = {}
    for entities in set(pre_ner):
        if entities != 'O':
            index = [i for i, val in enumerate(pre_ner) if val == entities]
            values = ''
            # strat = index[0]
            # end = index[-1]
            for i in index:
                values += x[i]
            entities_dic.update({entities: values})
            # entities_dic.update({entities: text[st]})

    entities = [key for key in entities_dic.keys()]

    print('intent:{} \n slot:{}'.format( pre_intent, entities_dic))
    return [pre_intent], entities,entities_dic
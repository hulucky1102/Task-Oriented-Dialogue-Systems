import tensorflow as tf
import json
import numpy as np
import os

os.environ["CUDA_VISIBLE_DEVICES"] = '1'
gpus = tf.config.experimental.list_physical_devices(device_type='GPU')
# for gpu in gpus:
#     tf.config.experimental.set_memory_growth(gpu, True)

params = {
    'batch_size': 64,
    'lr' : 0.001,
    'epochs': 500,
    'drops' : [0.1]
         }

with open('./DM_model/DM_char.json', mode='r', encoding='utf-8') as f:
    dicts = json.load(f)

action2id = dicts['action2id']
intent2id = dicts['intent2id']
slots2id = dicts['entities2id']
id2action = dicts['id2action']

previous_action_len = len(action2id)
slots_len = len(slots2id)
user_intent_len = len(intent2id)

# tf.keras.backend.clear_session()
# previous_action_inputs = tf.keras.layers.Input(shape=(previous_action_len,), name = 'previous_action_inputs')
# slots_inputs = tf.keras.layers.Input(shape = (slots_len,), name = 'slots_inputs')
# user_intent_inputs = tf.keras.layers.Input(shape = (user_intent_len,), name = 'user_intent_inputs')
#
# previous_action_embed = tf.keras.layers.Embedding(128,32)(previous_action_inputs)
# slots_embed = tf.keras.layers.Embedding(128,32)(slots_inputs)
# user_intent_embed = tf.keras.layers.Embedding(128,32)(user_intent_inputs)
#
# utter_inputs = tf.keras.layers.concatenate([previous_action_embed,slots_embed,user_intent_embed],axis=1)
# bilstm = tf.keras.layers.Bidirectional(tf.keras.layers.GRU(64,return_sequences=True))(utter_inputs)
# x_in = tf.keras.layers.LayerNormalization()(bilstm)
# x_conv = tf.keras.layers.GlobalAveragePooling1D()(x_in)
# pre_action = tf.keras.layers.Dense(previous_action_len, activation='sigmoid',name = 'pre_action')(x_conv)
# model = tf.keras.Model([previous_action_inputs,slots_inputs,user_intent_inputs],pre_action)
#
# model.load_weights('/home/ai/hgm/home_nlp/DM_model_weight/DM_weight_629.h5')

model_dir = './DM_model_weight/DM_weight.h5'
model = tf.keras.models.load_model(model_dir)


def trans2labelid(vocab, x):
    max_len = len(vocab)
    labels = [vocab[label] for label in x]
    label_onehot = np.eye(max_len)[labels]
    values = sum(label_onehot)
    values = np.expand_dims(values, axis=0)
    return values

def predict(x):
    x = list(x)
    previous_action_inputs = x[0]
    slots_inputs = x[1]
    user_intent_inputs = x[2]
    previous_action_inputs = trans2labelid(action2id,previous_action_inputs)
#     print(previous_action_inputs)
    slots_inputs = trans2labelid(slots2id,slots_inputs)
#     print(slots_inputs)
    user_intent_inputs = trans2labelid(intent2id,user_intent_inputs)
#     print(user_intent_inputs)
    pre_data= model.predict([previous_action_inputs,slots_inputs,user_intent_inputs])
    pre_action = id2action[str(np.argmax(pre_data))]
    print('　text: {} \n action:{} \n '.format(x,pre_action))
    return  pre_action

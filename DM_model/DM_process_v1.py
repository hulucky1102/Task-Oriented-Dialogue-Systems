import numpy as np

def split_data(dataset):
    # 以对话历史最长为3分割，以数组形式储存数据
    data_set = []
    for dic in dataset:
        data = dic['steps']
        for index in range(0,len(data),2):
            actions = []
            slots = []
            user_intent = []

            current_intent  =  data[index]['intent']
            # print("*************")
            # print(data[index])
            if 'entities' in data[index].keys():
                current_slot = data[index]['entities']
            elif 'entities' not in data[index].keys():
                current_slot = []

            current_action = data[index+1]['action']

            pre_intent = []
            pre_slot = []
            pre_action = []

            pre_history_1 = index-2
            if pre_history_1 >= 0:
                pre_intent = data[pre_history_1]['intent']
                if 'entities' in data[pre_history_1].keys():
                    pre_slot = data[pre_history_1]['entities']
                pre_action = [data[pre_history_1+1]['action']]

            if pre_action == []:
                pre_action = ['PAD']

            actions = [current_action]

            slots_sum = [current_slot, pre_slot]

            for i in slots_sum:
                if i  != [] and i is not None:
                    for val in i:
                        for key, j in val.items():
                            if key not in slots:
                                slots.append((key))
            if slots == []:
                slots = ['PAD']

            data_set.append({'previous_action':pre_action, 'slots':slots,'user_intent':[current_intent], 'action':actions})
    return data_set

def trans2labelid(vocab, x):
    max_len = len(vocab)
    labels = [vocab[label] for label in x]
    label_onehot = np.eye(max_len)[labels]
    values = sum(label_onehot)
    return values


def extract_conv_data(data_set,action2id,entities2id,intent2id):
    dataset_previous_action = []
    dataset_slots = []
    dataset_user_intent = []
    dataset_action = []
    for i in data_set:
        previous_action = i['previous_action']
        dataset_previous_action.append(trans2labelid(action2id, previous_action))
        slots = i['slots']
        dataset_slots.append(trans2labelid(entities2id, slots))
        user_intent = i['user_intent']
        dataset_user_intent.append(trans2labelid(intent2id, user_intent))
        action = i['action']
        dataset_action.append(trans2labelid(action2id, action))

    return np.array(dataset_previous_action), np.array(dataset_slots), \
           np.array(dataset_user_intent), np.array(dataset_action)
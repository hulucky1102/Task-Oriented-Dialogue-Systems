import numpy as np

def split_data(dataset):
    # 以对话历史最长为3分割，以数组形式储存数据
    data_set = []
    num = 0
    for val in dataset:
        data = val['steps']
        #         num += 1
        #          print(num)
        for index in range(0, len(data), 2):

            previous_action = []
            actions = []
            slots = []
            user_intent = []

            # 当前状态
            current_intent = data[index]['intent']
            if 'entities' in data[index].keys():
                current_slot = data[index]['entities']
            elif 'entities' not in data[index].keys():
                current_slot = []
            current_action = data[index + 1]['action']

            # 前一时刻状态
            pre1_intent = []
            pre1_slot = []
            pre1_action = []

            # 前二时刻状态
            pre2_intent = []
            pre2_slot = []
            pre2_action = []

            pre_history_1 = index - 2
            pre_history_2 = index - 4

            # 判断对话历史是否存在
            if pre_history_1 >= 0:
                pre1_intent = data[pre_history_1]['intent']
                if 'entities' in data[pre_history_1].keys():
                    pre1_slot = data[pre_history_1]['entities']
                pre1_action = data[pre_history_1 + 1]['action']

            if pre_history_2 >= 0:
                pre2_intent = data[pre_history_2]['intent']
                if 'entities' in data[pre_history_2].keys():
                    pre2_slot = data[pre_history_2]['entities']
                pre2_action = data[pre_history_2 + 1]['action']

            previous_action_sum = [pre1_action, pre2_action]
            for i in previous_action_sum:
                if i != []:
                    previous_action.append(i)
            if previous_action == []:
                previous_action = ['PAD']
            #             print('previous_action: ', previous_action)

            actions = [current_action]
            #             print('actions: ',actions)

            slots_sum = [current_slot, pre1_slot, pre2_slot]
            
            for i in slots_sum:
                if i  != [] and i is not None:
                    for val in i:
                        for key, j in val.items():
                            if key not in slots:
                                slots.append((key))
            if slots == []:
                slots = ['PAD']

            user_intent_sum = [current_intent, pre1_intent, pre2_intent]
            for i in user_intent_sum:
                if i != []:
                    user_intent.append(i)
            if user_intent == []:
                user_intent = ['PAD']
            #             print('user_intent: ',user_intent)

            data_set.append(
                {'previous_action': previous_action, 'slots': slots, 'user_intent': user_intent, 'action': actions})
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


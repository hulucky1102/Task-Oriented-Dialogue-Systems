import re
import os
import sys
CURRENT_DIR = os.path.split(os.path.abspath("./"))[0]  # 当前目录
sys.path.append(CURRENT_DIR)
from dialogue_pipeline.State_Form import *

state_dic = dic

# 判断是否支持当前设备
def check_device(intent,device_name,state_dic,device=[]):

    if re.findall(device_name,intent) :
        match_device = re.findall(device_name, intent)
        device_slot = match_device[0] + '_slot_state'
        if state_dic[device_slot]['device'] != '':
            flag = 1
        else:
            flag = 0

    elif device != []:
        device_slot = device[0] + '_slot_state'
        print('device_slot: ', state_dic[device_slot]['device'])
        if state_dic[device_slot]['device'] != '':
            flag = 1
        else:
            flag = 0
    else:
        flag = 0
    return flag


# 得到当前设备相匹配的状态表 intent entities action
def get_device_form(input,device_name,device = []):

    intent = input[0]
    entities = input[1]
    if len(input) > 2:
        action = input[2][0]
    else:
        action = []

    if re.findall(device_name,intent):
        match_device = re.findall(device_name,intent)
    elif device != []:
        match_device = device
    else:
        match_device = [ ]

    for key in state_dic:
        if match_device[0] in key:
            if 'slot' in key:
                entities_dic = key
            elif 'Intent' in key:
                intent_dic = key
            # elif 'action' in key:
            #     action_dic = key
            else:
                action_dic = key

    for key, val in entities.items():
        state_dic[entities_dic].update({key:val})

    if intent != []:
        state_dic[intent_dic].append(intent)
    if action != []:
        state_dic[action_dic].append(action)


    # if intent != [] and intent not in state_dic[intent_dic]:
    #     state_dic[intent_dic].append(intent)
    # if action != [] and action not in state_dic[action_dic]:
    #     state_dic[action_dic].append(action)

    return state_dic[intent_dic], state_dic[entities_dic],state_dic[action_dic], match_device

# 将状态表中 意图 实体 动作 数据进行处理符合DM模型输入
def  get_DM_input(input,device= [],device_name = device_name):

    DM_intent, entities_dic, DM_action, match_device = get_device_form(input,device_name,device)


    while len(DM_intent) > 2:
        DM_intent.pop(0)

    while len(DM_action) > 1:
        DM_action.pop(0)

    DM_entities = []
    for key, val in entities_dic.items():
        if val != '':
            DM_entities.append(key)

    if DM_intent == []:
        DM_intent.append('PAD')

    if DM_entities == []:
        DM_entities.append('PAD')

    if DM_action == []:
        DM_action.append('PAD')

    if 'PAD' in DM_intent and len(DM_intent) > 1:
        for index, val in enumerate(DM_intent):
            if val == 'PAD':
                DM_intent.pop(index)

    if 'PAD' in DM_entities and len(DM_entities) > 1:
        for index, val in enumerate(DM_entities):
            if val == 'PAD':
                DM_entities.pop(index)


    if 'PAD' in DM_action and len(DM_action) > 1:
        for index, val in enumerate(DM_action):
            if val == 'PAD':
                DM_action.pop(index)

    return [DM_action, DM_entities,DM_intent],match_device,state_dic


# 状态表 状态重置
def From_Reset(match_device,state_dic,flags=0):

    for key in state_dic:
        if match_device[0] in key:
            if 'slot' in key:
                entities_dic = key
            elif 'Intent' in key:
                intent_dic = key
            elif 'action' in key:
                action_dic = key

    while len(state_dic[intent_dic]) > 2:
        state_dic[intent_dic].pop()
    while  len(state_dic[action_dic]) > 2:
        state_dic[action_dic].pop()
    if flags ==1:
        state_dic[intent_dic] = []
        state_dic[action_dic] = []
        for key,val in state_dic[entities_dic].items():
            if key == 'device' or key == 'address':
                pass
            else:
                state_dic[entities_dic].update({key:''})







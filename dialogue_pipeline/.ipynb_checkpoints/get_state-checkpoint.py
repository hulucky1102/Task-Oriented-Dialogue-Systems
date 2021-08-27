import re
import os
import sys
CURRENT_DIR = os.path.split(os.path.abspath("./"))[0]  # 当前目录
sys.path.append(CURRENT_DIR)
from dialogue_pipeline.State_Form import *

device_name = 'AC|Lamp|Fan'
state_dic = dic

def get_device_form(input,device_name,):

    intent = input[0][0]
    entities = input[1]
    if len(input) > 2:
        action = input[2][0]
    else:
        action = []

    match_device = re.findall(device_name,intent)

    for key in state_dic:
        if match_device[0] in key:
            if 'slot' in key:
                entities_dic = key
            elif 'Intent' in key:
                intent_dic = key
            elif 'action' in key:
                action_dic = key
        # else:
        #     raise Exception('the equipment value not in Device_List').

    for key, val in entities.items():
        state_dic[entities_dic].update({key:val})

    if intent != [] and intent not in state_dic[intent_dic]:
        state_dic[intent_dic].append(intent)
    if action != [] and action not in state_dic[action_dic]:
        state_dic[action_dic].append(action)

    return state_dic[intent_dic], state_dic[entities_dic],state_dic[action_dic]

def get_DM_input(input,device_name = device_name):

    DM_intent, entities_dic, DM_action= get_device_form(input,device_name)


    while len(DM_intent) > 1:
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

    return [DM_action, DM_entities,DM_intent],state_dic

def From_Reset(intent,state_dic = state_dic, dic = dic):

    match_device = re.findall(device_name, intent[0])

    for key in state_dic:
        if match_device[0] in key:
            if 'slot' in key:
                entities_dic = key
            elif 'Intent' in key:
                intent_dic = key
            elif 'action' in key:
                action_dic = key

    state_dic[intent_dic] = []
    state_dic[action_dic] = []

    for key ,val in state_dic[entities_dic].items():
        state_dic[entities_dic].update({key:''})
    return state_dic






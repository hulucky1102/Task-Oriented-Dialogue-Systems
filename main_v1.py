
import predict_ner.predict_conv as ner
import predict_DM.predict_DM as DM
import dialogue_pipeline.get_state as trackers
import random
from  actions.Run_action import  action_run ,action_basic_run
from dialogue_pipeline.State_Form import *
from actions.story_map import *
from actions.intent2action_verification import i2c_check
import re

state_dic = dic

def Dialogue(input_text,state_dic = dic,device=[]):

    intent, entities, entities_dic = ner.predict(input_text)
    if re.findall(chatbot, intent):
        action = intent
        bot_utter = action_basic_run(action)
    else:
        # 状态追踪 继承intent entities
        tracker, device, _ = trackers.get_DM_input([intent, entities_dic], device)
        # device状态判断
        flag = trackers.check_device(intent, device_name, state_dic,device)
        # 判断是否支持当前设备 以及设备槽位是否填充
        if flag == 0:
            action = 'No_device'
            bot_utter = action_basic_run(action)
        else:

            # 判断是否能进行路径匹配
            action, flag_1 = story2action(tracker[1:], stories)
            if flag_1 == 0:
                action = [DM.predict(tracker)]
                print('模式选择 mode')
            else:
                action = action
                print('模式选择 rule')
            # 检查action设备是否与intent一致，intent为表明设备时继承上一轮设备
            action = i2c_check(intent, action, device_name, device)
            #  状态追踪 继承action
            tracker, device, state_dic = trackers.get_DM_input([intent, entities_dic, action], device)
            # 系统回复
            bot_utter, flags = action_run(action, state_dic)
            # 状态表单更新
            trackers.From_Reset(device, state_dic, flags)
            # print(state_dic)

    return bot_utter, device



if __name__ == '__main__':

    index = 1
    default_utter = random.choice(["再见", "拜拜", "后会有期", "有需要再招呼我哈"])

    while 1:
        print("**********************第{}轮对话 开始**********************".format(index))
        input_text = input("User:")

        if input_text == "再见":
            print("BotUtterence: {}".format(default_utter))
            print("**********************第{}轮对话 结束**********************".format(index))
            break

        bot_utter,device = Dialogue(input_text,state_dic,device)
        print("Bot Utter : ", bot_utter)
        index += 1

'''

        # 抽取NLU值
        intent, entities, entities_dic = ner.predict(input_text)
        if re.findall(chatbot, intent):
            action = intent
            action_basic_run(action)
        else:
            flag = trackers.check_device(intent, device_name,device)
            if flag == 0:
                action = 'No_device'
                action_basic_run(action)
            else:
                # 状态追踪 继承intent entities
                tracker,device, _ = trackers.get_DM_input([intent, entities_dic],device)
                # 判断是否能进行路径匹配
                action, flag_1 = story2action(tracker[1:], stories)
                if flag_1 == 0:
                    action = [DM.predict(tracker)]
                    print('模式选择 mode')
                else:
                    action = action
                    print('模式选择 rule')
                # 检查action设备是否与intent一致，intent为表明设备时继承上一轮设备
                action = i2c_check(intent,action,device_name,device)
                #  状态追踪 继承action
                tracker,device, state_dic = trackers.get_DM_input([intent, entities_dic, action],device)
                # 系统回复
                action_run(action,state_dic)
                # 状态表单更新
                trackers.From_Reset(device, state_dic)
                # state_dic = trackers.From_Reset(device,state_dic)
'''


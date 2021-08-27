
import predict_ner.predict_conv as ner
import predict_DM.predict_DM as DM
import dialogue_pipeline.get_state as trackers
import random
from  actions.Run_action import  action_run
from dialogue_pipeline.State_Form import *
from actions.story_map import *
from actions.intent2action_verification import i2c_check

if __name__ == '__main__':

    index = 1
    device = []
    default_utter = random.choice(["再见", "拜拜", "后会有期", "有需要再招呼我哈"])

    while 1:
        print("**********************第{}轮对话 开始**********************".format(index))
        input_text = input("User:")

        if input_text == "再见":
            print("BotUtterence: {}".format(default_utter))
            print("**********************第{}轮对话 结束**********************".format(index))
            break

        intent, entities, entities_dic = ner.predict(input_text)
        tracker,device, _ = trackers.get_DM_input([intent, entities_dic],device)
        # print('tracker :',  tracker[1:])
        action, flag = story2action(tracker[1:], stories,list(intent))
        if flag == 0:
            action = [DM.predict(tracker)]
            print('模式选择 mode')
        else:
            action = action
            print('模式选择 rule')
        action = i2c_check(intent,action,device_name,device)
        tracker,device, state_dic = trackers.get_DM_input([intent, entities_dic, action],device)
        # print('tracker: ', tracker)
        # print('action {}  type {}'.format(action,type(action)))
        action_run(action,state_dic)
        state_dic = trackers.From_Reset(device,state_dic)
        # print('state_dic: ', state_dic)

        index += 1

import sys
import os
CURRENT_DIR = os.path.split(os.path.abspath("./"))[0]  # 当前目录
sys.path.append(CURRENT_DIR)
from actions.Universal_expression import *
from  actions.Action import Action_utter, AC_Action_Utter, Lamp_Action_Utter,Fan_Action_Utter
import re
from dialogue_pipeline.State_Form import *

def  get_from(action, tracker,device_name = device_name):

    if isinstance(action,list):
        action = action[0]
    elif isinstance(action, str):
        action = action

    print('action: ', action)
    match_device = re.findall(device_name, action)
    print('match_device:', match_device)

    entities_dic =  match_device[0] + '_slot_state'

    # for key in tracker:
    #     print("key:", key)
    #     if match_device[0].upper() in key:
    #         print('key: ', key)
    #         if 'slot' in key:
    #             entities_dic = key
    #         else:
    #             pass
    #     else:
    #         entities_dic = "demo测试哦"
    return action, tracker[entities_dic]


def decide_ACaction(action, state):

    ac_utter = AC_Action_Utter(action,state)
    ac_action = Action_utter(action,state)

    if action == "Control-AC_Timing": # 空调定时操作
        if state["address"] == "": # 如果状态表中没有找到具体的空调设备名称 进行询问
            return utter_ac_req_device
        else:
            if state["time"] == "":
                return utter_ac_req_time
            elif state["operation"] == "":
                return utter_ac_req_operation
            else:
                return ac_action.device_inform_timing()

    elif action == "Control-AC_Mode":  # 空调模式控制操作
        if state["address"] == "":  # 如果状态表中没有找到具体的空调设备名称 进行询问
            return utter_ac_req_device
        else:
            if state["mode"] == "":
                return utter_ac_req_mode
            else:
                return ac_action.device_inform_mode()

    elif action == "Control-AC_State":  # 空调打开和关闭操作
        if state["address"] == "":  # 如果状态表中没有找到具体的空调设备名称 进行询问
            return utter_ac_req_device
        else:
            if state["operation"] == "":  # 询问具体操作 打开或者关闭
                return utter_ac_req_operation
            else:
                return ac_action.device_inform_runstate() # 槽位信息齐全 执行打开关闭操作

    elif action == "Control-AC_Temp":  # 空调温度调节操作
        if state["address"] == "":  # 如果状态表中没有找到具体的空调设备名称 进行询问
            return utter_ac_req_device
        else:
            if state["operation"] not in ["调高", "调低"] and state["temperature"] == "":
                return utter_ac_req_updown
            else:
                return ac_utter.ac_inform_temp()

    elif action == "action_controlDeviceWind":
        if state["address"] == "":  # 如果状态表中没有找到具体的空调设备名称 进行询问
            return utter_ac_req_device
        else:
            if state["operation"] not in ["调高", "调低"] and state["windspeed"] == "":
                return utter_ac_req_windspeed
            else:
                return ac_utter.ac_inform_windspeed()
    else:
        return "暂未理解您的意图"


def decide_LampAction(action, state):
    '''
    灯控设备的动作回复函数
    :param action: 用户query表达的意图
    :param state: 状态槽位表
                Lamp_state = {
                        "address": "", # 灯具设备房间修饰词
                        "device": "", # 具体灯具名称，射灯/筒灯/台灯 等等
                        "mode": "", # 灯具的模式槽位
                        "time": "", # 灯具定时时长
                        "operation": "", # 灯具打开/关闭/灯操作 调亮 调暗
                        "lamplight": "" # 灯具亮度槽位值
                    }
    :return: 用户的Utterence 回复和 对话任务完成与否布尔值
    '''
    # 不与其他设备共用的技能操作情况 独有的技能 亮度调节
    lamp_utter = Lamp_Action_Utter(action,state)
    # 可以与其他设备共用的技能操作情况，如 运行状态的控制，模式的控制，定时的控制
    lamp_action = Action_utter(action,state)
    # 灯具设备运行状态意图
    if action == "Control-Lamp_State":
        # 当房间名称以及设备名称都为空的话则需要询问设备名称
        if state["address"] == "" :
            return utter_lamp_req_device
        else:
            if state["operation"] == "":  # 询问具体操作 打开或者关闭
                return utter_lamp_req_operation
            else:
                return lamp_action.device_inform_runstate() # 槽位信息齐全 执行打开关闭操作

    # 灯具设备定时控制状态意图
    elif action == "Control-Lamp_Timing":
        if state["address"] == "" and state["device"] == "":
            return utter_lamp_req_device
        else:
            pass
        if state["operation"] == "":
            return utter_lamp_req_operation
        elif state["time"] == "":
            return utter_lamp_req_time
        else:
            return lamp_action.device_inform_timing()

    # 灯具设备模式控制状态意图
    elif action == "Control-Lamp_Mode":
        # 如果状态表中没有找到具体的空调设备名称 进行询问
        if state["address"] == "" and state["device"] == "":
            return utter_lamp_req_device
        else:
            if state["mode"] == "":
                return utter_lamp_req_mode
            else:
                return lamp_action.device_inform_mode()

    # 灯具设备灯光亮度控制状态意图
    elif action == "Control-Lamp_Lightness":
        if state["address"] == "" and state["device"] == "":
            return utter_lamp_req_device
        else:
            if state["operation"] in ["调亮", "调暗"] or state["lamplight"] != "":
                return lamp_utter.lamp_inform_light()
            else:
                return utter_lamp_req_updown
    # 其他意图
    else:
        return "暂未理解您的意图"


def decide_FanAction(action, state):
    '''

    :param action: 用户意图
    :param state: 该设备操作下的操作状态表 风扇槽位表
            Fan_state = {
            "address": "",  # 风扇设备房间修饰词
            "mode": "",  # 风扇设备模式值
            "operation": "",  # 风扇设备操作值
            "gear": "", # 风扇档位操作值
            "windspeed": "",  # 风扇设备风速值
            "time": "",  # 风扇设备定时操作具体时间值
            }
    :return: 用户的Utterence 回复和 对话任务完成与否布尔值
    '''

    # 不与其他设备共用的技能操作情况 独有的技能 档位控制，风速控制
    fan_utter = Fan_Action_Utter(action,state)
    # 可以与其他设备共用的技能操作情况，如 运行状态的控制，模式的控制，定时的控制
    fan_action = Action_utter(action,state)  # 传入一个默认的设备名称
    # 如果需求为用户query表达中没有提及设备修饰名称 address 则默认赋值一个初始值，在意图的判断中，动作执行不受address槽位值的影响
    # state.update({"address": "客厅"})
    state_address = state.get("address")

    if action == "Control-Fan_State":
        if state["address"] == "":  # 如果状态表中没有找到具体的风扇设备名称 进行询问
            return utter_fan_req_device
        else:
            if state["operation"] == "":  # 询问具体操作 打开或者关闭
                return utter_fan_req_operation
            else:
                return fan_action.device_inform_runstate()  # 槽位信息齐全 执行打开关闭操作
    elif action == "Control-Fan_Mode":
        if state["address"] == "":  # 如果状态表中没有找到具体的风扇设备名称 进行询问
            return utter_fan_req_device
        else:
            if state["mode"] == "":
                return utter_fan_req_mode
            else:
                return fan_action.device_inform_mode()
    elif action == "Control-Fan_Timing":
        if state["address"] == "":  # 如果状态表中没有找到具体的风扇设备名称 进行询问
            return utter_fan_req_device
        else:
            if state["time"] == "":
                return utter_fan_req_time
            elif state["operation"] == "":
                return utter_fan_req_operation
            else:
                return fan_action.device_inform_timing()
    elif action == "Control-Fan_Gear":
        if state["address"] == "":  # 如果状态表中没有找到具体的风扇设备名称 进行询问
            return utter_fan_req_device
        else:
            if state["operation"] not in ["调高", "调低"] and state["gear"] == "":
                return utter_fan_req_gear
            else:
                return fan_utter.fan_inform_gear()
    elif action == "FanWind":
        if state["address"] == "":  # 如果状态表中没有找到具体的空调设备名称 进行询问
            return utter_fan_req_device
        else:
            if state["operation"] not in ["调高", "调低"] and state["windspeed"] == "":
                return utter_fan_req_windspeed
            else:
                return fan_utter.fan_inform_windspeed()
    else:
        return "暂未理解您的意图"

def action_run(action, tracker):

    action, entities = get_from(action,tracker)
    if "AC" in action:
        bot_utter = decide_ACaction(action, entities)
    elif "Fan" in action:
        bot_utter = decide_FanAction(action, entities)
    elif "Lamp" in action:
        bot_utter = decide_LampAction(action, entities)
    else:
        bot_utter = '暂未理解您的意图'
    print('BotUtterence: {}'.format(bot_utter))

import re

class Action_utter():

    def __init__(self, action, state):
        self.action = action
        self.state = state

        if "device" in state.keys():
            if state["address"] and state["device"]:
                self.combine_device = state["address"] + state["device"]
            else:
                self.combine_device = state["device"]


    def device_inform_timing(self):
        operation = self.state.get("operation")
        time = self.state.get("time")
        if self.combine_device:
            result = "已为您定时{}后{}{}".format(time, operation, self.combine_device)
        return result

    def device_inform_runstate(self):
        operation = self.state.get("operation")
        if self.combine_device:
            result = "正在为您{}{}".format(operation,self.combine_device)
        return result

    def device_inform_mode(self):
        mode = self.state.get("mode")
        if self.combine_device:
            result = "正在为您将{}调整为{}".format(self.combine_device,mode)
        return result


class AC_Action_Utter:
    def __init__(self,action, state):
        self.action = action
        self.state = state

        if "device" in state.keys():
            if state["address"] and state["device"]:
                self.combine_device = state["address"] + state["device"]
            else:
                self.combine_device = state["device"]

    # 控制空调温度控制的话术回复
    def ac_inform_temp(self):
        temp = self.state.get("temperature")
        operation = self.state.get("operation")
        if temp != "":
            result = "正在为您将{}的温度设置为{}".format(self.combine_device,temp)
        else:
            result = "默认为您将{}的温度{}一度".format(self.combine_device,operation)
        return result

    # 控制空调风速的任务完成话术回复
    def ac_inform_windspeed(self):
        windspeed = self.state.get("windspeed")
        operation = self.state.get("operation")
        if windspeed != "":
            result = "正在为您将{}的风速设置为{}".format(self.combine_device, windspeed)
        else:
            result = "默认为您将{}的风速{}".format(self.combine_device,operation)
        return result



class Lamp_Action_Utter:
    def __init__(self, action, state):
        self.action = action
        self.state = state

        if "device" in state.keys():
            if state["address"] and state["device"]:
                self.combine_device = state["address"] + state["device"]
            else:
                self.combine_device = state["device"]

    # 控制灯光亮度调节的话术回复
    def lamp_inform_light(self):
        lamplight = self.state.get("lamplight")
        operation = self.state.get("operation")
        # 确定好灯具名称
        lamp_name = self.combine_device

        if lamplight:
            result = "正在为您将{}亮度调整为{}".format(lamp_name, lamplight)
        elif operation == "调亮":
            result = "正在为您将{}亮度调亮".format(lamp_name)
        elif operation == "调暗":
            result = "正在为您将{}亮度调暗".format(lamp_name)
        else:
            result = "正在为您调节{}的亮度".format(lamp_name)

        return result


class Fan_Action_Utter:
    def __init__(self, action, state):
        self.action = action
        self.state = state

        if "device" in state.keys():
            if state["address"] and state["device"]:
                self.combine_device = state["address"] + state["device"]
            else:
                self.combine_device = state["device"]

    # 控制风扇档位控制的话术动作
    def fan_inform_gear(self):
        gear_level = self.state.get("gear")
        operation = self.state.get("operation")
        if operation and not gear_level:
            # 有操作没有具体的档位级别值
            result = "已为您将{}档位{}".format(self.combine_device, operation)
        elif gear_level and not operation:
            # 有具体的档位值没操作名称
            result = "已为您将{}档位调到{}".format(self.combine_device, gear_level)
        elif gear_level and operation:
            # 有操作 也有具体的档位级别值
            result = "已为您将{}档位{}至{}".format(self.combine_device, operation, gear_level)
        else:
            result = "{}操作出现了些问题".format(self.combine_device)
        return result

    # 控制风扇风速控制的话术动作
    def fan_inform_windspeed(self):
        windspeed = self.state.get("windspeed")
        operation = self.state.get("operation")
        if windspeed != "":
            result = "正在为您将{}的风速设置为{}".format(self.combine_device, windspeed)
        else:
            result = "默认为您将{}的风速{}".format(self.combine_device, operation)
        return result

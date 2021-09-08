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
        if operation == '调高' or operation == '调低':
            result = "正在为您将{}的温度{}{}".format(self.combine_device, operation,temp)
        elif temp != "":
            result = "正在为您将{}的温度设置为{}".format(self.combine_device,temp)
        else:
            result = "默认为您将{}的温度{}一度".format(self.combine_device,operation)
        return result

    # 控制空调风速的任务完成话术回复
    def ac_inform_windspeed(self):
        sensorvalue = self.state.get('sensorvalue')
        operation = self.state.get("operation")
        if sensorvalue != "":
            result = "正在为您将{}的风速设置为{}".format(self.combine_device, sensorvalue)
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
        gear_level = self.state.get("sensorvalue")
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
        windspeed = self.state.get("sensorvalue")
        operation = self.state.get("operation")

        if windspeed != "":
            result = "正在为您将{}的风速设置为{}".format(self.combine_device, windspeed)
        else:
            result = "默认为您将{}的风速{}".format(self.combine_device, operation)
        return result


# 窗帘控制
class Curtain_Action_Utter:
    def __init__(self, action, state):
        self.action = action
        self.state = state

        if "device" in state.keys():
            if state["address"] and state["device"]:
                self.combine_device = state["address"] + state["device"]
            else:
                self.combine_device = state["device"]

    # 控制窗帘调节的话术回复
    def Curtain_inform_runstate(self):
        operation = self.state.get("operation")
        sensorvalue = self.state.get("sensorvalue")
        time = self.state.get("time")
        data_time = self.state.get('data_time')
        if operation and not sensorvalue:
            result = "正在为您{}{}".format(operation, self.combine_device)
        else:
            result = "正在为您将{}{}{}".format(operation,sensorvalue,self.combine_device)
        return result

    def Curtain_inform_timing(self):
        operation = self.state.get("operation")
        time = self.state.get("time")
        date_time = self.state.get('date_time')
        if date_time != '':
            result = "已为您设置{}{}后{}{}".format(date_time, time, operation, self.combine_device)
        else:
            result = "已为您定时{}后{}{}".format(time, operation, self.combine_device)

        return result

# 烤箱控制
class Oven_Action_Utter:
    def __init__(self, action, state):
        self.action = action
        self.state = state

        if "device" in state.keys():
            self.combine_device = state["device"]

    # 控制烤箱调节的话术回复
    def Oven_inform_runstate(self):
        operation = self.state.get("operation")
        result = "正在为您{}{}".format(operation, self.combine_device)
        return result

    def Oven_inform_timing(self):
        operation = self.state.get("operation")
        time = self.state.get("time")
        result = "已为您定时{}后{}{}".format(time, operation, self.combine_device)
        return result

    # 控制烤箱温度的话术回复
    def Oven_inform_temp(self):
        temp = self.state.get("temperature")
        result = "正在为您将{}的温度设置为{}".format(self.combine_device, temp)
        return result

    def Oven_inform_Mode(self):
        mode = self.state.get('mode')
        result = "正在为您将{}的模式设置为{}".format(self.combine_device, mode)
        return result

# 加湿器控制
class Humidifier_Action_Utter:
    def __init__(self, action, state):
        self.action = action
        self.state = state

        if "device" in state.keys():
            self.combine_device = state["device"]

    # 控制烤箱调节的话术回复
    def Humidifier_inform_runstate(self):
        operation = self.state.get("operation")
        result = "正在为您{}{}".format(operation, self.combine_device)
        return result

    def Humidifier_inform_timing(self):
        operation = self.state.get("operation")
        time = self.state.get("time")
        result = "已为您定时{}后{}{}".format(time, operation, self.combine_device)
        return result

    def Humidifier_inform_Gear(self):
        Gear = self.state.get("sensorvalue")
        if self.combine_device:
            result = "正在为您将{}调整为{}".format(self.combine_device,Gear)
        return result


# 电饭煲控制
class RiceCooker_Action_Utter:
    def __init__(self, action, state):
        self.action = action
        self.state = state

        if "device" in state.keys():
            self.combine_device = state["device"]

    # 控制烤箱调节的话术回复
    def RiceCooker_inform_runstate(self):
        operation = self.state.get("operation")
        result = "正在为您{}{}".format(operation, self.combine_device)
        return result

    def RiceCooker_inform_timing(self):
        operation = self.state.get("operation")
        time = self.state.get("time")
        result = "已为您定时{}后{}{}".format(time, operation, self.combine_device)
        return result

    def RiceCooker_inform_mode(self):
        mode = self.state.get("mode")
        if self.combine_device:
            result = "正在为您将{}调整为{}".format(self.combine_device, mode)
        return result





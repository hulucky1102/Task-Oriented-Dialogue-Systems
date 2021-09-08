
# default
default_utterence = "暂未理解您要表达的意思，请再说一遍"
utter_none_device = '设备未识别，请重新表述'

# 空调相关的固定话术回复
utter_ac_req_device = "请问要控制哪个房间的空调"
utter_ac_req_operation = "请问要对空调执行什么操作"
utter_ac_req_updown = "请问要调高温度还是调低温度"
utter_ac_req_time = "请问要定时多长时间"
utter_ac_req_mode = "请问要调整成什么模式"
utter_ac_req_windspeed = "请问风速调到多少"
utter_ac_req_winddirect = "请问怎么调节风向"

# 灯控相关的固定话术回复
utter_lamp_req_device = "请问要控制哪个房间的灯"
utter_lamp_req_operation = "请问要执行什么操作"
utter_lamp_req_updown = "请问要调高亮度还是调低亮度"
utter_lamp_req_time = "请问要定时多长时间"
utter_lamp_req_mode = "请问要调整成什么模式"

# 风扇相关的固定话术回复
utter_fan_req_device = "请问要控制哪个风扇"
utter_fan_req_operation = "请问要对风扇执行什么操作"
utter_fan_req_gear = "请问是要调高档位还是调低档位"
utter_fan_req_windspeed = "请问风扇风速调节到多少"
utter_fan_req_time = "请问需要将风扇定时多长时间"
utter_fan_req_mode = "请问要将风扇调整成什么模式"

# 窗帘相关的固定话术回复
utter_Curtain_req_device = "请问要控制哪个房间的窗帘"
utter_Curtain_req_time = "请问需要将窗帘定时多长时间"
utter_Curtain_req_operation = "请问要对窗帘执行什么操作"

# 烤箱相关的固定话术回复
utter_Oven_req_time = "请问需要将烤箱定时多长时间"
utter_Oven_req_operation = "请问要对烤箱执行什么操作"
utter_Oven_req_temperature = "请问要将烤箱的温度设置为多少"
utter_Oven_req_mode = "请问要将烤箱设置为什么模式"

# 加湿器相关的的固定话术回复
utter_Humidifier_req_time = "请问需要将加湿器定时多长时间"
utter_Humidifier_req_operation = "请问要对加湿器执行什么操作"
utter_Humidifier_req_mode = "请问要将加湿器设置为什么模式"
utter_Humidifier_add_Gear = "已经为您将加湿器调高一档"
utter_Humidifier_reduce_Gear = "已经为您将加湿器降低一档"

# 电饭煲相关的的固定话术回复
utter_RiceCooker_req_time = "请问需要将电饭煲定时多长时间"
utter_RiceCooker_req_operation = "请问要对电饭煲执行什么操作"
utter_RiceCooker_req_mode = "请问要将电饭煲设置为什么模式"

import random
# thanks
utter_answer_thanks = random.choice(["嗯呢。不用客气~","这是我应该做的，主人"])

# deny
utter_answer_deny = "怎么了，主人？"

# whoareyou
utter_answer_whoareyou = "您好！我是小芯呀，您的AI智能助理"

# whattodo
utter_answer_whattodo = "您好！很高兴为您服务，我目前可以用来[测试控制部分家电对话]"

# greet
utter_answer_greet = random.choice(["您好！请问我可以帮到您吗？",'很高兴为您服务。','请问我可以为您做什么。'])

# goodbye
utter_answer_goodbye = random.choice(["嗯嗯，下次需要时随时记得我哟~",'后会有期','期待下次再见！'])






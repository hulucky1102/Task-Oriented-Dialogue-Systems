
device_name = 'AC|Lamp|Fan|Curtain|Oven|Humidifier|RiceCooker'


dic = {
    'AC_slot_state':{
        "address": "", # 空调设备房间修饰词
        "temperature": "", # 空调设备温度值
        "mode": "", # 空调设备模式值
        "operation": "", # 空调设备操作值
        "time": "", # 空调设备定时操作具体时间值
        "sensorvalue": "",# 空调设备风速值
    },

    'AC_Intent' : [],

    'AC_action' : [],

    'Lamp_slot_state' : {
        "address": "", # 灯具设备房间修饰词
        "device": "", # 具体灯具名称，射灯/筒灯/台灯 等等
        "mode": "", # 灯具的模式槽位
        "time": "", # 灯具定时时长
        "operation": "", # 灯具打开/关闭/灯操作 调亮 调暗
        "lamplight": "" # 灯具亮度槽位值
    },

    'Lamp_Intent' : [],
    'Lamp_action' : [],

    'Fan_slot_state' : {
        "address": "",  # 风扇设备房间修饰词
        "mode": "",  # 风扇设备模式值
        "operation": "",  # 风扇设备操作值
        "gear": "", # 风扇档位操作值
        "sensorvalue": "",  # 风扇设备风速值
        "time": "",  # 风扇设备定时操作具体时间值
        "device": "", # 设备名
    },

    'Fan_Intent' : [],
    'Fan_action': [],

    'Curtain_slot_state' : {
        "address": "",  # 窗帘设备房间修饰词
        "operation": "",  # 窗帘设备操作值
        "data_time": "",  # 窗帘控设备定时操作的日期
        "time": "",  # 窗帘设备定时操作具体时间值
        "sensorvalue": "",  # 窗帘的数值
        "device": "", # 设备名
    },

    'Curtain_Intent' : [],
    'Curtain_action': [],

    'Oven_slot_state' : {
        "operation": "",  # 烤箱设备操作值
        "time": "",  # 烤箱设备定时操作具体时间值
        "temperature ": "",  # 烤箱温度的数值
        'mode': "",  # 烤箱模式
        "device": "", # 设备名
    },

    'Oven_Intent' : [],
    'Oven_action': [],

    'Humidifier_slot_state' : {
        "operation": "",  # 加湿器设备操作值
        "time": "",  # 加湿器设备定时操作具体时间值
        "mode": "",  # 加湿器的模式
        "device": "", # 设备名
    },

    'Humidifier_Intent' : [],
    'Humidifier_action': [],

    'RiceCooker_slot_state' : {
        "operation": "",  # 电饭煲设备操作值
        "time": "",  # 电饭煲设备定时操作具体时间值
        "mode": "",  # 电饭煲的模式
        "device": "", # 设备名
    },

    'RiceCooker_Intent' : [],
    'RiceCooker_action': [],

}
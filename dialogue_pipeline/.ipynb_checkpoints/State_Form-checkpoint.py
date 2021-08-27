
device_name = 'AC|Lamp|Fan'


dic = {
    'AC_slot_state':{
        "address": "", # 空调设备房间修饰词
        "temperature": "", # 空调设备温度值
        "mode": "", # 空调设备模式值
        "operation": "", # 空调设备操作值
        "windspeed": "", # 空调设备风速值
        "time": "", # 空调设备定时操作具体时间值
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
        "windspeed": "",  # 风扇设备风速值
        "time": "",  # 风扇设备定时操作具体时间值
    },

    'Fan_Intent' : [],
    'Fan_action': []
}
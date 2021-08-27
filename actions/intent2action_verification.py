import re

def i2c_check(intent, action,device_name, device):

    if isinstance(action,list):
        action = action[0]
    elif isinstance(action, str):
        action = action

    if re.findall(device_name,intent):
        match_device = re.findall(device_name,intent)
    elif device != []:
        match_device = device
    else:
        match_device = []
    print("*************")
    print("intent: ", intent)
    print("action:",action)
    print("match_device: ", match_device)
    print("*************")

    if isinstance(match_device,list):
        match_device = match_device[0]
    elif isinstance(action, str):
        match_device = match_device

    if match_device in action:
        action = action
    elif re.findall(device_name,intent) :
        action = intent
    elif re.findall(device_name,action):
        match_device_v1 = re.findall(device_name,action)
        match_device_v1 =match_device_v1[0]
        action = action.replace(match_device_v1,match_device)


    return [action]




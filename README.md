## **家居领域对话系统**

简单实现设备有 空调、窗帘、灯、电饭煲、风扇、微波炉、加湿器 
加入固定语句，实现基本打招呼与功能询问。

### 意图识别和实体抽取
 *1 ner_model 模型文件
 
 *2 ner_model_weight 模型权重
 
 *3 forward_ner_model 模型前向
 
 *4 predict_ner 模型预测
 
### 状态追踪

 *1 dialogue_pipeline  State_Form.py 设备状态表
 
 *2 dialogue_pipeline  get_state.py  得到当前设备，将意图和槽位传入状态表。
 
### 动作选择

一、 模型

 *1 DM_model 模型文件
 
 *2 DM_model_weight 模型权重
 
 *3 forward_DM_model 模型前向
 
 *4 predict_DM 模型预测

二、 规则

 *1 DM_model construct_story_map.ipynb  将story数据集构建为story_map
 
 *2 actions story_map  将输入与story数据集进行匹配，匹配成功则输出相对应的action
 
### action回复

 *1 actions Action 定义各类回复
 
 *2 actions Universal_expression 定义各类固定回复
 
 *3 actions Run_action 根据action抽取相对应槽值进行回复，当缺少必要槽值时进行询问
 
### main.py

    # 意图识别槽位抽取 
    intent, entities, entities_dic = ner.predict(input_text)
    # 根据意图判断是闲聊还是设备控制
    if re.findall(chatbot, intent):
        action = intent
        bot_utter = action_basic_run(action)
    else:
        # 状态追踪 继承intent entities
        tracker, device, _ = trackers.get_DM_input([intent, entities_dic], device)
        # device状态判断
        flag = trackers.check_device(intent, device_name, state_dic,device)
        # 判断是否支持当前设备 以及设备槽位是否填充，减少回复错误概率
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
            # 状态表单更新  falgs标志位判断任务是否完成，完成则清空状态表中非必须槽位
            trackers.From_Reset(device, state_dic, flags)


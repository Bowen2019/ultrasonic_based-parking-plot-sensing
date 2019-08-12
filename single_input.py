import numpy as np

infofile = open("./single_data/BUSMASTERLogFile_0.log", "r")  # 打开某路径文件，只读模式



'''Rear_RS_EMIT_RS_RX = [[time,distance]] '''

Rear_RS_EMIT_RS_RX = []
Front_RS_EMIT_RS_RX = []
Rear_LS_EMIT_LS_RX = []
Front_LS_EMIT_LS_RX = []


while True:
    infolinedata_initial = str(infofile.readline())  # 按行读取数据
    KongGe_array = infolinedata_initial.split(" ")  # 用空格将消息分割成字符串数组


    if len(infolinedata_initial) < 5:        #检测到读取结束
        break

    if len(KongGe_array) ==15:

        if KongGe_array[3] == '0929':  # 检测到是message_1  0x3A1
            single_1 = [KongGe_array[0], int(KongGe_array[6])*2]
            Rear_RS_EMIT_RS_RX.append(single_1)

        if KongGe_array[3] == '0930':  # 检测到是message_2  0x3A2
            single_2 = [KongGe_array[0],int(KongGe_array[9]) * 2]
            single_3 = [KongGe_array[0],int(KongGe_array[13]) * 2]
            Rear_LS_EMIT_LS_RX.append(single_2)
            Front_LS_EMIT_LS_RX.append(single_3)

        if KongGe_array[3] == '0931':  # 检测到是message_3  0x3A3
            single_4 = [KongGe_array[0], int(KongGe_array[9]) * 2]
            Front_RS_EMIT_RS_RX.append(single_4)










import matplotlib.pyplot as plt
import numpy as np
from  fliter import  Filter
infofile = open("./signal_data/BUSMASTERLogFile_10.log", "r")  # 打开某路径文件，只读模式


#数据容器初始化
Rear_RS_EMIT_RS_RX_Time =[]
Rear_RS_EMIT_RS_RX_Distance = []
Rear_LS_EMIT_LS_RX_Distance = []
Rear_LS_EMIT_LS_RX_Time = []
Front_LS_EMIT_LS_RX_Distance = []
Front_LS_EMIT_LS_RX_Time = []
Front_RS_EMIT_RS_RX_Distance = []
Front_RS_EMIT_RS_RX_Time = []
Rear_RS_EMIT_RS_RX_Flited_Distance =[]
Front_LS_EMIT_LS_RX_Flited_Distance = []
Front_RS_EMIT_RS_RX_Flited_Distance = []
Rear_LS_EMIT_LS_RX_Flited_Distance = []

for i in range(0,300):
    Rear_RS_EMIT_RS_RX_Time.append(0)
    Rear_RS_EMIT_RS_RX_Distance.append(0)
    Rear_LS_EMIT_LS_RX_Distance.append(0)
    Rear_LS_EMIT_LS_RX_Time.append(0)
    Front_LS_EMIT_LS_RX_Distance.append(0)
    Front_LS_EMIT_LS_RX_Time.append(0)
    Front_RS_EMIT_RS_RX_Distance.append(0)
    Front_RS_EMIT_RS_RX_Time.append(0)
    Rear_RS_EMIT_RS_RX_Flited_Distance.append(0)
    Front_LS_EMIT_LS_RX_Flited_Distance.append(0)
    Front_RS_EMIT_RS_RX_Flited_Distance.append(0)
    Rear_LS_EMIT_LS_RX_Flited_Distance.append(0)




#figure初始化
fig, axes = plt.subplots(nrows=2, ncols=2)
axes[0,0].set(title='Front_LS_EMIT_LS_RX')
axes[0,1].set(title='Front_RS_EMIT_RS_RX')
axes[1,0].set(title='Rear_LS_EMIT_LS_RX')
axes[1,1].set(title='Rear_RS_EMIT_RS_RX')

'''
plt.xlim((0,300))
plt.ylim((0,1000))
'''
x = np.arange(0, 300, 1)

#打开交互模式
plt.ion()

#主循环
while True:

    infolinedata_initial = str(infofile.readline())  # 按行读取数据
    KongGe_array = infolinedata_initial.split(" ")  # 用空格将消息分割成字符串数组


    if len(infolinedata_initial) < 5:        #检测到读取结束
        break

    if len(KongGe_array) ==15:

        if KongGe_array[3] == '0929':  # 检测到是message_1  0x3A1
            signal_1 = KongGe_array[0]                  #提取需要需要Signal
            signal_2 = int(KongGe_array[6]) * 2
            try:                       #移除上次所画线条
                axes[1][1].lines.remove(lines_1[0])
                #axes[1][1].lines.remove(lines_2[0])
            except Exception:
                pass

            Rear_RS_EMIT_RS_RX_Distance.pop(0)
            Rear_RS_EMIT_RS_RX_Distance.append(signal_2)
            Rear_RS_EMIT_RS_RX_Time .pop(0)
            Rear_RS_EMIT_RS_RX_Time .append(signal_1)
            #Rear_RS_EMIT_RS_RX_Flited_1_Distance = Filter(InputSignal=Rear_RS_EMIT_RS_RX_Distance,OutSignal=Rear_RS_EMIT_RS_RX_Flited_Distance,SigmaX=1,KernalSize=9,FilterType=1)
            #0Rear_RS_EMIT_RS_RX_Flited_Distance = Rear_RS_EMIT_RS_RX_Flited_1_Distance.main()
            lines_1 = axes[1][1].plot(x, Rear_RS_EMIT_RS_RX_Distance,color = 'red')
            #lines_2 = axes[1][1].plot(x, Rear_RS_EMIT_RS_RX_Flited_Distance,color = 'blue')

        if KongGe_array[3] == '0930':  # 检测到是message_2  0x3A2
            signal_1 = KongGe_array[0]
            signal_2 = int(KongGe_array[9]) * 2
            signal_3 = int(KongGe_array[13]) * 2


            try:                       #移除上次所画线条
                axes[1][0].lines.remove(lines_3[0])
                axes[0][0].lines.remove(lines_4[0])
                #axes[1][0].lines.remove(lines_5[0])
                #axes[0][0].lines.remove(lines_6[0])

            except Exception:
                pass

            Rear_LS_EMIT_LS_RX_Distance.pop(0)
            Rear_LS_EMIT_LS_RX_Distance.append(signal_2)
            Rear_LS_EMIT_LS_RX_Time .pop(0)
            Rear_LS_EMIT_LS_RX_Time .append(signal_1)
            Front_LS_EMIT_LS_RX_Distance.pop(0)
            Front_LS_EMIT_LS_RX_Distance.append(signal_3)
            Front_LS_EMIT_LS_RX_Time .pop(0)
            Front_LS_EMIT_LS_RX_Time .append(signal_1)

            #Front_LS_EMIT_LS_RX_Flited_1_Distance = Filter(InputSignal=Front_LS_EMIT_LS_RX_Distance,OutSignal=Front_LS_EMIT_LS_RX_Flited_Distance,SigmaX=1,KernalSize=9,FilterType=1)
            #Front_LS_EMIT_LS_RX_Flited_Distance = Front_LS_EMIT_LS_RX_Flited_1_Distance.main()

            #Rear_LS_EMIT_LS_RX_Flited_1_Distance = Filter(InputSignal=Rear_LS_EMIT_LS_RX_Distance,OutSignal=Rear_LS_EMIT_LS_RX_Flited_Distance,SigmaX=1,KernalSize=9,FilterType=1)
            #Rear_LS_EMIT_LS_RX_Flited_Distance =Rear_LS_EMIT_LS_RX_Flited_1_Distance.main()
            lines_3 = axes[1][0].plot(x, Rear_LS_EMIT_LS_RX_Distance,color = 'red')
            lines_4 = axes[0][0].plot(x,Front_LS_EMIT_LS_RX_Distance, color='red')
            #lines_5 = axes[1][0].plot(x, Rear_LS_EMIT_LS_RX_Flited_Distance,color = 'blue')
            #lines_6 = axes[0][0].plot(x,Front_LS_EMIT_LS_RX_Flited_Distance, color='blue')

        if KongGe_array[3] == '0931':  # 检测到是message_3  0x3A3
            signal_1 = KongGe_array[0]
            signal_2 = int(KongGe_array[6]) * 2
            try:                       #移除上次所画线条
                axes[0][1].lines.remove(lines_7[0])
            except Exception:
                pass

            Front_RS_EMIT_RS_RX_Distance.pop(0)
            Front_RS_EMIT_RS_RX_Distance.append(signal_2)
            Front_RS_EMIT_RS_RX_Time .pop(0)
            Front_RS_EMIT_RS_RX_Time .append(signal_1)
            lines_7 = axes[0][1].plot(x, Front_RS_EMIT_RS_RX_Distance,color = 'red')







    plt.pause(0.001)  # 暂停一秒
    plt.ioff()  # 关闭画图的窗口








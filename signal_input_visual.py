import matplotlib.pyplot as plt
import numpy as np

infofile = open("./signal_data/BUSMASTERLogFile_0.log", "r")  # 打开某路径文件，只读模式


#数据容器初始化
Rear_RS_EMIT_RS_RX_Time =[]
Rear_RS_EMIT_RS_RX_Distance = []
Front_RS_EMIT_RS_RX_Time =[]
Front_RS_EMIT_RS_RX_Distance = []
Rear_LS_EMIT_LS_RX_Time =[]
Rear_LS_EMIT_LS_RX_Distance = []
Front_LS_EMIT_LS_RX_Time =[]
Front_LS_EMIT_LS_RX_Distance = []
for i in range(0,300):
    Rear_RS_EMIT_RS_RX_Time.append(0)
    Rear_RS_EMIT_RS_RX_Distance.append(0)
    Front_RS_EMIT_RS_RX_Time.append(0)
    Front_RS_EMIT_RS_RX_Distance.append(0)
    Rear_LS_EMIT_LS_RX_Time.append(0)
    Rear_LS_EMIT_LS_RX_Distance.append(0)
    Front_LS_EMIT_LS_RX_Time.append(0)
    Front_LS_EMIT_LS_RX_Distance.append(0)



#figure初始化
fig, axes = plt.subplots(nrows=2, ncols=2)
axes[0,0].set(title='Rear_RS_EMIT_RS_RX')
axes[0,1].set(title='Front_RS_EMIT_RS_RX')
axes[1,0].set(title='Rear_LS_EMIT_LS_RX')
axes[1,1].set(title='Front_LS_EMIT_LS_RX')


plt.xlim((0,300))
plt.ylim((0,500))
x = np.arange(0, 300, 1)

plt.ion()


while True:

    infolinedata_initial = str(infofile.readline())  # 按行读取数据
    KongGe_array = infolinedata_initial.split(" ")  # 用空格将消息分割成字符串数组


    if len(infolinedata_initial) < 5:        #检测到读取结束
        break

    if len(KongGe_array) ==15:

        if KongGe_array[3] == '0929':  # 检测到是message_1  0x3A1
            signal_1 = KongGe_array[0]
            signal_2 = int(KongGe_array[6]) * 2
            try:
                axes[0,0].lines_1.remove(lines_1[0])
            except Exception:
                pass

            Rear_RS_EMIT_RS_RX_Distance.pop(0)
            Rear_RS_EMIT_RS_RX_Distance.append(signal_2)
            Rear_RS_EMIT_RS_RX_Time .pop(0)
            Rear_RS_EMIT_RS_RX_Time .append(signal_1)
            lines_1 = axes[0,0].plot(x, Rear_RS_EMIT_RS_RX_Distance)

    plt.pause(0.001)  # 暂停一秒
    plt.ioff()  # 关闭画图的窗口








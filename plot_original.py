import pandas as pd
import matplotlib.pyplot as plt

from tools import cut_week_to_days, chinese_font
from text_read import idc_correct, event_desc_correct



def plot_alarm_num_day(data):

    # 把一周的数据分割为每一天
    data_day_1, data_day_2, data_day_3, data_day_4, data_day_5, data_day_6, data_day_7 = cut_week_to_days(data)

    # 每一天的告警总数-y_1
    alarm_total_num_y_1 = [len(data_day_1['event_time']), len(data_day_2['event_time']), len(data_day_3['event_time']),
                           len(data_day_4['event_time']), len(data_day_5['event_time']), len(data_day_6['event_time']),
                           len(data_day_7['event_time'])]

    # 每一天的接手告警总数-y_2
    alarm_total_num_y_2 = [len(data_day_1.loc[data_day_1['event_handle_status'] == 1]),
                           len(data_day_2.loc[data_day_2['event_handle_status'] == 1]),
                           len(data_day_3.loc[data_day_3['event_handle_status'] == 1]),
                           len(data_day_4.loc[data_day_4['event_handle_status'] == 1]),
                           len(data_day_5.loc[data_day_5['event_handle_status'] == 1]),
                           len(data_day_6.loc[data_day_6['event_handle_status'] == 1]),
                           len(data_day_7.loc[data_day_7['event_handle_status'] == 1])]
    # 每一天-x
    alarm_total_num_x = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # 画图

    plt.bar(alarm_total_num_x, alarm_total_num_y_1, alpha=0.9, width=0.35, facecolor='lightskyblue', label='告警总数')

    plt.plot(alarm_total_num_x, alarm_total_num_y_1, alpha=0.9, color='lightskyblue')

    plt.bar(alarm_total_num_x, alarm_total_num_y_2, alpha=0.9, width=0.35, facecolor='yellowgreen', label='接手告警数量')

    plt.plot(alarm_total_num_x, alarm_total_num_y_2, alpha=0.9, color='yellowgreen')
    # 图片标题
    plt.title()
    # 图例
    plt.legend(fontsize=12)
    # 显示每个点的值
    for a, b in zip(alarm_total_num_x, alarm_total_num_y_1):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=11, font="Times New Roman")
    for a, b in zip(alarm_total_num_x, alarm_total_num_y_2):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=11, font="Times New Roman")
    # 保存图片，清晰度
    plt.rcParams['savefig.dpi'] = 300
    plt.savefig('alarm_num_day.png', bbox_inches='tight')
    plt.show()

    return




def plot_original_analysis(path, out_file_name):
    """
    主文件，运行上面所有的代码
    :param path:
    :param out_file_name:
    :return:
    """
    chinese_font()  # 正确显示中文字体
    # 完整数据
    data = pd.read_csv(path + out_file_name)  # 读取数据

    plot_alarm_num_day(data) 



    return

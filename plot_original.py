import pandas as pd
import matplotlib.pyplot as plt

from tools import cut_week_to_days, chinese_font
from text_read import idc_correct, event_desc_correct


def plot_each_level_handle_status(data):

    ax1 = plt.subplot(2, 2, 1)
    df = data.loc[data['event_level'] == 0]

    df['event_handle_status'].value_counts().plot(kind='pie', autopct='%.2f%%', explode=(0.1, 0.1),
                                                  colors=['yellowgreen', '#EB572A'], labels=["未接手", "接手"])
    plt.ylabel("")

    ax2 = plt.subplot(2, 2, 2)
    df = data.loc[data['event_level'] == 1]

    df['event_handle_status'].value_counts().plot(kind='pie', autopct='%.2f%%', explode=(0.1, 0.1),
                                                  colors=['yellowgreen', '#EB572A'], labels=["未接手", "接手"])
    plt.ylabel("")

    ax3 = plt.subplot(2, 2, 3)
    df = data.loc[data['event_level'] == 2]

    df['event_handle_status'].value_counts().plot(kind='pie', autopct='%.2f%%', explode=(0.1, 0.1),
                                                  colors=['yellowgreen', '#EB572A'], labels=["未接手", "接手"])
    plt.ylabel("")


    ax4 = plt.subplot(2, 2, 4)
    df = data.loc[data['event_level'] == 3]

    df['event_handle_status'].value_counts().plot(kind='pie', autopct='%.2f%%', explode=(0.1, 0.1),
                                                  colors=['yellowgreen', '#EB572A'], labels=["未接手", "接手"])
    plt.ylabel("")

    # 图片标题
    plt.suptitle()
    # 保存图片，清晰度
    plt.rcParams['savefig.dpi'] = 300
    plt.savefig('each_level_handle.png', bbox_inches='tight')
    plt.show()
    return



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
    # 告警总数的直方图
    plt.bar(alarm_total_num_x, alarm_total_num_y_1, alpha=0.9, width=0.35, facecolor='lightskyblue', label='告警总数')
    # 告警总数的点线图
    plt.plot(alarm_total_num_x, alarm_total_num_y_1, alpha=0.9, color='lightskyblue')
    # 接手告警总数的直方图
    plt.bar(alarm_total_num_x, alarm_total_num_y_2, alpha=0.9, width=0.35, facecolor='yellowgreen', label='接手告警数量')
    # 接手告警总数的点线图
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



def plot_idc_alarm(data):


    for i in range(len(data["event_handle_status"])):
        data["event_idc"][i] = idc_correct(data["event_idc"][i])
    idc_list = data['event_idc'].unique().astype(str).tolist()


    alarm_total_num = []
    for idc in idc_list:
        alarm_total_num.append(len(data['event_handle_status'].loc[data['event_idc'] == idc]))


    idc_handle = []
    for idc in idc_list:
        idc_handle.append(sum(data['event_handle_status'].loc[data['event_idc'] == idc]))

    # 把三个列表转换为Dataframe，方便后续处理（排序等）
    df_idc_list = pd.DataFrame(idc_list, columns=["idc"])
    df_alarm_total_num = pd.DataFrame(alarm_total_num, columns=["alarm_total_num"])
    df_idc_handle = pd.DataFrame(idc_handle, columns=["idc_handle"])
    result = pd.concat([df_idc_list, df_alarm_total_num, df_idc_handle], axis=1)
    result.sort_values(['idc_handle'], inplace=True, ascending=False)  # 排序

    # 画图

    plt.bar(result["idc"][:20], result["alarm_total_num"][:20], alpha=0.9, width=0.35, facecolor='lightskyblue',
            label='')

    plt.bar(result["idc"][:20], result["idc_handle"][:20], alpha=0.9, width=0.35, facecolor='yellowgreen',
            label='')
    # x轴坐标旋转60度
    plt.xticks(rotation=60)
    # 图片标题
    plt.title()
    # 图例
    plt.legend(fontsize=12)
    # 显示每个点的值
    for a, b in zip(result["idc"][:20], result["alarm_total_num"][:20]):
        plt.text(a, b + 5.15, '%.0f' % b, ha='center', va='bottom', fontsize=11, font="Times New Roman")
    for a, b in zip(result["idc"][:20], result["idc_handle"][:20]):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=11, font="Times New Roman")
    # 保存图片，清晰度
    plt.rcParams['savefig.dpi'] = 300
    plt.savefig('idc_alarm.png', bbox_inches='tight')
    plt.show()
    return



def plot_desc_alarm(data):


    for i in range(len(data["event_handle_status"])):
        data["event_desc"][i] = event_desc_correct(data["event_desc"][i])
    event_desc_list = data['event_desc'].unique().astype(str).tolist()

    alarm_total_num = []
    for event_desc in event_desc_list:
        alarm_total_num.append(len(data['event_handle_status'].loc[data['event_desc'] == event_desc]))


    event_desc_handle = []
    for event_desc in event_desc_list:
        event_desc_handle.append(sum(data['event_handle_status'].loc[data['event_desc'] == event_desc]))

    # 把三个列表转换为Dataframe，方便后续处理（排序等）
    df_event_desc_list = pd.DataFrame(event_desc_list, columns=["event_desc"])
    df_alarm_total_num = pd.DataFrame(alarm_total_num, columns=["alarm_total_num"])
    df_event_desc_handle = pd.DataFrame(event_desc_handle, columns=["event_desc_handle"])
    result = pd.concat([df_event_desc_list, df_alarm_total_num, df_event_desc_handle], axis=1)
    result["百分比"] = result['event_desc_handle'] / result['alarm_total_num']
    result.sort_values(['event_desc_handle'], inplace=True, ascending=False)  # 排序

    # 画图
    # 控制图片大小
    plt.figure(figsize=[10, 15])

    plt.bar(result["event_desc"][:20], result["alarm_total_num"][:20], alpha=0.9, width=0.35, facecolor='lightskyblue',
            label='')

    plt.bar(result["event_desc"][:20], result["event_desc_handle"][:20], alpha=0.9, width=0.35, facecolor='yellowgreen',
            label='')
    # x轴坐标旋转90度，字体大小10
    plt.xticks(rotation=90, size=10)
    # 图片标题
    plt.title()
    # 图例
    plt.legend(fontsize=12)
    # 显示每个点的值
    for a, b in zip(result["event_desc"][:20], result["alarm_total_num"][:20]):
        plt.text(a, b + 15.15, '%.0f' % b, ha='center', va='bottom', fontsize=11, font="Times New Roman")
    for a, b in zip(result["event_desc"][:20], result["event_desc_handle"][:20]):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=11, font="Times New Roman")
    # 保存图片，清晰度
    plt.rcParams['savefig.dpi'] = 300
    plt.savefig('event_desc.png', bbox_inches='tight')
    plt.show()
    return



def plot_sub_type_alarm(data):


    event_sub_type_list = data['event_sub_type'].unique().astype(str).tolist()


    alarm_total_num = []
    for event_sub_type in event_sub_type_list:
        alarm_total_num.append(len(data['event_handle_status'].loc[data['event_sub_type'] == event_sub_type]))


    event_sub_type_handle = []
    for event_sub_type in event_sub_type_list:
        event_sub_type_handle.append(sum(data['event_handle_status'].loc[data['event_sub_type'] == event_sub_type]))

    # 把三个列表转换为Dataframe，方便后续处理（排序等）
    df_event_sub_type_list = pd.DataFrame(event_sub_type_list, columns=["event_sub_type"])
    df_alarm_total_num = pd.DataFrame(alarm_total_num, columns=["alarm_total_num"])
    df_event_sub_type_handle = pd.DataFrame(event_sub_type_handle, columns=["event_sub_type_handle"])
    result = pd.concat([df_event_sub_type_list, df_alarm_total_num, df_event_sub_type_handle], axis=1)
    result["百分比"] = result['event_sub_type_handle'] / result['alarm_total_num']
    result.sort_values(['event_sub_type_handle'], inplace=True, ascending=False)  # 排序

    # 画图
    # 控制图片大小
    plt.figure(figsize=[10, 15])

    plt.bar(result["event_sub_type"][:20], result["alarm_total_num"][:20], alpha=0.9, width=0.35, facecolor='lightskyblue',
            label='告警总数')

    plt.bar(result["event_sub_type"][:20], result["event_sub_type_handle"][:20], alpha=0.9, width=0.35, facecolor='yellowgreen',
            label='接手告警数量')
    # x轴坐标旋转90度，字体大小10
    plt.xticks(rotation=60, size=10)
    # 图片标题
    plt.title()
    # 图例
    plt.legend(fontsize=12)
    # 显示每个点的值
    for a, b in zip(result["event_sub_type"][:20], result["alarm_total_num"][:20]):
        plt.text(a, b + 6.15, '%.0f' % b, ha='center', va='bottom', fontsize=11, font="Times New Roman")
    for a, b in zip(result["event_sub_type"][:20], result["event_sub_type_handle"][:20]):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=11, font="Times New Roman")
    # 保存图片，清晰度
    plt.rcParams['savefig.dpi'] = 300
    plt.savefig('sub_type.png', bbox_inches='tight')
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

    plot_each_level_handle_status(data) 
    plot_alarm_num_day(data) 
    plot_idc_alarm(data) 
    plot_desc_alarm(data) 
    plot_sub_type_alarm(data) 


    return

import pandas as pd
import matplotlib.pyplot as plt

from metrics import evaluation
from tools import cut_week_to_days, chinese_font


def plot_re_pre_day(data):
    """
    算法在本周中每一天的召回率和精确率
    :param data: 原始告警文件，增加了预测结果，去除了传输数据
    :return:
    """
    # 把一周的数据分割为每一天
    data_day_1, data_day_2, data_day_3, data_day_4, data_day_5, data_day_6, data_day_7 = cut_week_to_days(data)

    # 建立每一天数据的列表，day_list[0]是全部数据
    day_list = [data, data_day_1, data_day_2, data_day_3, data_day_4, data_day_5, data_day_6, data_day_7]

    # 为每一天的数据重设index
    for day in day_list:
        day.reset_index(inplace=True)

    # 生成每一天的召回率-y1和精确率-y2
    recall_list = []
    precision_list = []
    for day in day_list:
        recall, precision = evaluation(day['event_handle_status'], day['pre_handle_status'])
        recall_list.append(recall)
        precision_list.append(precision)
    recall_list = [i * 100 for i in recall_list]
    precision_list = [i * 100 for i in precision_list]

    # 每一天-x
    week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # 画图
    # 召回率的点线图
    plt.plot(week_days, recall_list[1:], color='orange', marker='o', label="Recall: 描述漏报情况")
    # 精确率的点线图
    plt.plot(week_days, precision_list[1:], color='dodgerblue', marker='^', label="Precision: 描述准确情况")
    # 召回率的均值
    plt.hlines(recall_list[0], 'Monday', 'Sunday', colors="orange", linestyles="dashed")
    # 精确率的均值
    plt.hlines(precision_list[0], 'Monday', 'Sunday', colors="dodgerblue", linestyles="dashed")
    # 图例
    plt.legend()
    # 标题
    plt.title('本周告警接手预测算法效果 \n 本周平均Recall: ' + str('%.2f%%' % recall_list[0]) + ' 本周平均Precision: ' + str('%.2f%%' % precision_list[0]))

    # 显示每个点的值
    for a, b in zip(week_days, recall_list[1:]):
        plt.text(a, b + 0.01, '%.2f%%' % b, ha='center', va='bottom', fontsize=11, font="Times New Roman")
    for a, b in zip(week_days, precision_list[1:]):
        plt.text(a, b + 0.01, '%.2f%%' % b, ha='center', va='bottom', fontsize=11, font="Times New Roman")
    plt.text('Sunday', recall_list[0] + 0.01, '%.2f%%' % recall_list[0], ha='center', va='bottom', fontsize=11,
             color="orange",font="Times New Roman")
    plt.text('Sunday', precision_list[0] + 0.01, '%.2f%%' % precision_list[0], ha='center', va='bottom', fontsize=11,
             color="dodgerblue",font="Times New Roman")
    # 网格
    plt.grid(alpha=0.3)
    # 保存图片，清晰度
    plt.rcParams['savefig.dpi'] = 300
    plt.savefig('/Users/yuao/PycharmProjects/smart-alarm-evaluation/Figures/algorithm_re_pre.png', bbox_inches='tight')
    plt.show()
    return


def plot_algorithm_analysis(path, out_file_name):
    chinese_font()  # 正确显示中文字体
    # 完整数据
    data = pd.read_csv(path + out_file_name)  # 读取数据
    plot_re_pre_day(data)
    return

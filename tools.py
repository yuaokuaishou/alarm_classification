import time
import datetime
import matplotlib.pyplot as plt


def chinese_font():
    """
    正确显示中文字体
    :return:
    """
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    return


def stamp_to_time(timestamp):
    if timestamp > 1000000000000:
        time_local = time.localtime(timestamp / 1000)  # 毫秒
    else:
        time_local = time.localtime(timestamp)  # 秒
    time_standard = time.strftime("%Y-%m-%d", time_local)
    return time_standard


def time_to_zero_stamp(time_):
    time__ = time_ + " 00:00:00"
    time_array = time.strptime(time__, "%Y-%m-%d %H:%M:%S")
    timestamp = time.mktime(time_array)
    return int(timestamp) * 1000


def cut_week_to_days(data):
    """
    把一周的数据切分为每天的数据
    :param data: 原始数据或者增加了结果的数据都可以
    :return: 每一天的Dataframe
    """
    # 所有的时间戳变为列表
    time_list = data['event_time'].tolist()

    # 找到最开始的时间戳，把时间定位到本周的第一天
    day_1_stamp = min(time_list)
    day_1_time = datetime.datetime.strptime(stamp_to_time(day_1_stamp), '%Y-%m-%d')

    # 从第一天的0点开始，每增加一天，就是第二天的0点（第一天的结束）；start:一天开始的时间，end:一天结束的时间
    day_1_start_stamp = time_to_zero_stamp((day_1_time).strftime('%Y-%m-%d'))
    day_1_end_stamp = time_to_zero_stamp((day_1_time + datetime.timedelta(days=1)).strftime('%Y-%m-%d'))
    day_2_end_stamp = time_to_zero_stamp((day_1_time + datetime.timedelta(days=2)).strftime('%Y-%m-%d'))
    day_3_end_stamp = time_to_zero_stamp((day_1_time + datetime.timedelta(days=3)).strftime('%Y-%m-%d'))
    day_4_end_stamp = time_to_zero_stamp((day_1_time + datetime.timedelta(days=4)).strftime('%Y-%m-%d'))
    day_5_end_stamp = time_to_zero_stamp((day_1_time + datetime.timedelta(days=5)).strftime('%Y-%m-%d'))
    day_6_end_stamp = time_to_zero_stamp((day_1_time + datetime.timedelta(days=6)).strftime('%Y-%m-%d'))
    day_7_end_stamp = time_to_zero_stamp((day_1_time + datetime.timedelta(days=7)).strftime('%Y-%m-%d'))

    # 把一周的数据分割为每一天
    data_day_1 = data.loc[(data['event_time'] >= day_1_start_stamp) & (data['event_time'] < day_1_end_stamp)]
    data_day_2 = data.loc[(data['event_time'] >= day_1_end_stamp) & (data['event_time'] < day_2_end_stamp)]
    data_day_3 = data.loc[(data['event_time'] >= day_2_end_stamp) & (data['event_time'] < day_3_end_stamp)]
    data_day_4 = data.loc[(data['event_time'] >= day_3_end_stamp) & (data['event_time'] < day_4_end_stamp)]
    data_day_5 = data.loc[(data['event_time'] >= day_4_end_stamp) & (data['event_time'] < day_5_end_stamp)]
    data_day_6 = data.loc[(data['event_time'] >= day_5_end_stamp) & (data['event_time'] < day_6_end_stamp)]
    data_day_7 = data.loc[(data['event_time'] >= day_6_end_stamp) & (data['event_time'] < day_7_end_stamp)]

    return data_day_1, data_day_2, data_day_3, data_day_4, data_day_5, data_day_6, data_day_7

def evaluation(label, pre_label):
    """
    评价整体精度的指标，输出分类的召回率和准确率
    :param label: 标签列表
    :param pre_label: 分类结果列表
    :return:
    """
    TT, TF, FT, FF = 0, 0, 0, 0
    for i in range(len(label)):
        if label[i] == 1:
            if pre_label[i] == 1:
                TT += 1
            else:
                TF += 1
        else:
            if pre_label[i] == 1:
                FT += 1
            else:
                FF += 1

    recall = TT / (TT + TF)
    precision = TT / (TT + FT)
    return recall, precision

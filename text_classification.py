import fasttext


def classifier(df, model_, threshold):
    """
    文本分类器
    输出分类结果
    :param text: 输入的告警文本
    :param model_: 训练好的模型
    :param threshold: 二分类判定概率阈值
    :return: 分类结果
    """
    pred_handle_status_ = []
    handle_probability_ = []
    model = fasttext.load_model(model_)  # 加载训练好的模型

    for text in df['text_new']:
        text = text.replace("\n", " ")  # 部分告警信息包换换行符"\n"
        cancel_probability = model.predict(text)[1][0]  # result = [label, probability]
        handle_probability = abs(1-cancel_probability)

        if handle_probability > threshold:
            handle_status = 1
        else:
            handle_status = 0

        handle_probability_.append(handle_probability)
        pred_handle_status_.append(handle_status)

    df['handle_status'] = pred_handle_status_
    df['handle_probability'] = handle_probability_
    label = df['label'].tolist()
    handle_status = df['handle_status'].tolist()
    print("alarm_num: ", sum(handle_status))
    return df, label, handle_status


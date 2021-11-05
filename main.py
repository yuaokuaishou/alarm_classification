from metrics import evaluation
from plot_algorithm import plot_algorithm_analysis
from plot_original import plot_original_analysis
from text_classification import classifier
from text_engineer import additional_rules
from text_out import out_file
from text_preprocess import preprocess
from text_read import pull
import warnings

warnings.filterwarnings('ignore')

threshold = 0.00011  # 分类器阈值。阈值越小，召回率越高，精度越低；阈值越大则相反。0.0011
model = "support_file/well_trained_model.bin"  # 选择模型
path = "/Users/yuao/Downloads/"
# file_name = "每周告警任务2021-10-18_2021-10-24.xlsx"
# out_file_name = "每周告警任务2021-10-18_2021-10-24_results.csv"

file_name_list = ["每周告警任务2021-09-27_2021-10-03.xlsx", "每周告警任务2021-10-04_2021-10-10.xlsx", "每周告警任务2021-10-11_2021-10-17.xlsx", "每周告警任务2021-10-18_2021-10-24.xlsx", "每周告警任务2021-10-25_2021-10-31.xlsx"]
out_file_name_list = ["每周告警任务2021-09-27_2021-10-03_results.csv", "每周告警任务2021-10-04_2021-10-10_results.csv", "每周告警任务2021-10-11_2021-10-17_results.csv", "每周告警任务2021-10-18_2021-10-24_results.csv", "每周告警任务2021-10-25_2021-10-31_results.csv"]

if __name__ == '__main__':
    i = 4
    file_name = file_name_list[i]
    out_file_name = out_file_name_list[i]

    # 文件读取，生成dataframe，有两列["label", "text"]
    alarm_file = pull(path, file_name)

    # 文本预处理
    inputs = alarm_file['text']  # 读取dataframe中的text，用于下一步的预处理
    alarm_file_new = preprocess(inputs, alarm_file)  # 预处理

    # 输出训练结果
    df, label, handle_status = classifier(alarm_file_new, model, threshold)  # 文本分类

    # 给原始文件加上预测结果
    file_out = out_file(df, path, file_name)
    file_out.to_csv(path + out_file_name, index=False)

    # 打印召回率和准确率
    recall, precision = evaluation(label, handle_status)
    print("recall: %.2f%%" % (recall * 100))
    print("precision: %.2f%%" % (precision * 100))

    label_engineer, handle_status_engineer = additional_rules(path, out_file_name)

    recall, precision = evaluation(label_engineer, handle_status_engineer)
    print("recall: %.2f%%" % (recall * 100))
    print("precision: %.2f%%" % (precision * 100))

    # # 画图-离线数据分析
    # plot_original_analysis(path, out_file_name)
    #
    # # 画图-分类算法指标
    # plot_algorithm_analysis(path, out_file_name)




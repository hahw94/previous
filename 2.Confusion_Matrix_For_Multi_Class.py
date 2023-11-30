from plot_definition import *

# 개별 시간대 및 데이터 유형별로 그래프 뽑기
save_path = '/home/seohyunwoo/paper_img/fog/result_img/'
datasets_info = "fix_1_30000_12"
data_type_list = ["train","test"]
predict_hour_list = [1,2,3]
label_list = ["0 ~ 0.2","0.2 ~ 0.5","0.5 ~ 1","1 ~ 2","2 ~ 5","5 ~\n(km)"]
file_info = "class"

for data_type in data_type_list:
    for predict_hour in predict_hour_list:
        process_each_def(data_type, predict_hour, label_list, save_path, datasets_info, file_info)
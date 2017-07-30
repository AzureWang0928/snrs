# -*- coding: utf-8 -*-
import simplejson as json

def store(path1,path2, data):
    train_num = int((len(data) * 0.9))
    with open(path1, 'a') as json_file:
        for i in range(train_num):
            json_file.write(json.dumps(data[i]))
            json_file.write("\n")
    with open(path2, 'a') as json_file:
        for i in range(train_num+1, len(data)):
            json_file.write(json.dumps(data[i]))
            json_file.write("\n")

def load(path):
    data_list = []
    with open(path) as json_file:
        for line in json_file:
            data_line = json.loads(line)
            data_list.append(data_line)
        store('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/unique_data/review_train0.9.json','G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/unique_data/review_test0.9.json', data_list)

load('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/unique_data/review.json')

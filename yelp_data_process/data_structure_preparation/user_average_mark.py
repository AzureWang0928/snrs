# -*- coding: utf-8 -*-
import simplejson as json

def store(path, data):
    with open(path, 'a') as json_file:
        for i in range(len(data)):
            json_file.write(json.dumps(data[i]))
            json_file.write("\n")

def load(path):
    new_data_list = []
    with open(path) as json_file:
        for line in json_file:
            sum = 0.0
            data_line = json.loads(line)
            for each_pair in data_line["stars"]:
                sum = sum + each_pair[1]
            average = sum / len(data_line["stars"])
            data_dict = {}
            data_dict["user_id"] = data_line["user_id"]
            data_dict["average_star"] = round(average, 2)
            new_data_list.append(data_dict)
        store('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/unique_data/average_score0.9.json',new_data_list)

load('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/unique_data/user_review_mark0.9.json')

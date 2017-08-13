# -*- coding: utf-8 -*-
import simplejson as json

def format(data):
    format_list = []
    user_review_mark = {}
    star_list = []
    for each_review in data:
        if each_review["user_id"] not in user_review_mark:
            # star_list = []
            user_review_mark[each_review["user_id"]] = []
            user_review_mark[each_review["user_id"]].append([each_review["business_id"], each_review["stars"]])
        else:
            # star_list.append([each_review["business_id"], each_review["stars"]])
            user_review_mark[each_review["user_id"]].append([each_review["business_id"], each_review["stars"]])
    for user_id in user_review_mark:
        format_dict = {}
        format_dict["user_id"] = user_id
        format_dict["stars"] = user_review_mark[user_id]
        format_list.append(format_dict)
    return format_list

def store(path, data):
    with open(path, 'a') as json_file:
        for i in range(len(data)):
            json_file.write(json.dumps(data[i]))
            json_file.write("\n")

def load(path):
    data_list = []
    with open(path) as json_file:
        for line in json_file:
            data_line = json.loads(line)
            data_list.append(data_line)
        new_data_list = format(data_list)
        store('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/unique_data/user_review_mark0.9.json',new_data_list)

load('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/unique_data/review_train0.9.json')
# load('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/unique_data/new_review_train.json')

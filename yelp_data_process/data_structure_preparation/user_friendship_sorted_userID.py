# -*- coding: utf-8 -*-
import simplejson as json

def clean(data):
    user_list = {}
    user_list["user_id"] = data["user_id"]
    user_list["friends"] = data["friends"]
    return user_list

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
            new_data_line = clean(data_line)
            data_list.append(new_data_line)
        data_list.sort(key=lambda x: x["user_id"])
        store('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/unique_data/user_friendship.json',data_list)
    return data_list

user_data = load('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/unique_data/user.json')

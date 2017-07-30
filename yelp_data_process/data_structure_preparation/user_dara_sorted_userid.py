# -*- coding: utf-8 -*-
import simplejson as json

def clean(data):
    user_list = {}
    user_list["user_id"] = data["user_id"]
    user_list["name"] = data["name"]
    user_list["friends"] = data["friends"]
    user_list["review_count"] = data["review_count"]
    user_list["fans"] = data["fans"]
    user_list["average_stars"] = data["average_stars"]
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
            data_list.append(data_line)
        data_list.sort(key=lambda x: x["user_id"])
        store('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/processed_user_sorted_userID.json',data_list)
    return data_list

user_data = load('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/1.0processed_user.json')

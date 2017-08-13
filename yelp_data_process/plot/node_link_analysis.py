# -*- coding: utf-8 -*-
import simplejson as json

def construct(data):
    data_list = []
    user_link_list = {}
    user_link_list["user_id"] = data["user_id"]
    user_link_list["link_number"] = len(data["friends"])
    data_list.append(user_link_list)
    return data_list

def store(path, data):
    with open(path, 'a') as json_file:
        json_file.write(json.dumps(data))
        json_file.write("\n")

def load(path):
    with open(path) as json_file:
        for line in json_file:
            data_line = json.loads(line)
            new_data_line = construct(data_line)
            store('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/unique_data/node_link_count.json', new_data_line)

load('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/unique_data/user_friendship.json')

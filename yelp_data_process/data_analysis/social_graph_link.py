# -*- coding: utf-8 -*-
import simplejson as json

def construct(data):
    data_list = []
    for i in range(len(data["friends"])):
        user_link_list = {}
        user_link_list["to_node"] = data["user_id"]
        user_link_list["from_node"] = data["friends"][i]
        data_list.append(user_link_list)
    return data_list

def store(path, data):
    with open(path, 'a') as json_file:
        for i in range(len(data)):
            json_file.write(json.dumps(data[i]))
            json_file.write("\n")

def load(path):
    with open(path) as json_file:
        for line in json_file:
            data_line = json.loads(line)
            new_data_line = construct(data_line)
            store('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/unique_data/social_graph_link.json', new_data_line)

load('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/unique_data/user_friendship.json')

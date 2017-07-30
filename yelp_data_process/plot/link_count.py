# -*- coding: utf-8 -*-
import simplejson as json

def format(data):
    user_link_list = []
    for each_data in data:
        array = [each_data, data[each_data]]
        user_link_list.append(array)
    return user_link_list

def construct(data):
    user_link_dict = {}
    for i in range(len(data)):
        if data[i]["link_number"] not in user_link_dict:
            user_link_dict[data[i]["link_number"]] = 1
        else:
            temp = user_link_dict[data[i]["link_number"]] + 1
            user_link_dict[data[i]["link_number"]] = temp
    user_link_dict
    return user_link_dict

def store(path, data):
    with open(path, 'a') as json_file:
         for i in range(len(data)):
            json_file.write(json.dumps(data[i][0]))
            json_file.write('\t')
            json_file.write(json.dumps(data[i][1]))
            json_file.write('\t')
            json_file.write('1')
            json_file.write("\n")

def load(path):
    with open(path) as json_file:
        data_list = []
        for line in json_file:
            data_line = json.loads(line)
            data_list.append(data_line[0])
        new_data_line = construct(data_list)
        format_data = format(new_data_line)
        store('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/unique_data/link_count_result.json', format_data)

load('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/unique_data/node_link_count.json')

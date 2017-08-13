# -*- coding: utf-8 -*-
import simplejson as json

def format(data):
    influnence_list = []
    for each_data in data:
        array = [each_data, data[each_data]]
        influnence_list.append(array)
    return influnence_list

def construct(data):
    influence_dict = {}
    for i in range(len(data)):
        if data[i] not in influence_dict:
            influence_dict[data[i]] = 1
        else:
            temp = influence_dict[data[i]] + 1
            influence_dict[data[i]] = temp
    influence_dict
    return influence_dict

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
            data_list.append(data_line["PR_valve"])
        new_data_line = construct(data_list)
        format_data = format(new_data_line)
        store('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/unique_data/influence_count_result.json', format_data)

load('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/unique_data/user_influence_analysis.json')

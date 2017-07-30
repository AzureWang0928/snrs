# -*- coding: utf-8 -*-
import simplejson as json

dict = {}
def format_map(data):
    if data["user_id"] not in dict:
        # print len(dict)
        dict[data["user_id"]] = len(dict)


def id_replace(path):
    with open(path) as json_file:
        data_list = []
        # for line in json_file:
        #     data = json.loads(line)
        #     if data["user_id"] not in dict:
        #         print "miss"
        #     else:
        #         data["user_id"] = dict[data["user_id"]]
        #         data_list.append(data)
        for line in json_file:
            data = json.loads(line)
            for i in range(len(data["friends"])):
                if data["friends"][i] not in dict:
                    print "miss"
                else:
                    data["friends"][i] = dict[data["friends"][i]]
            data_list.append(data)
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
            format_map(data_line)

load('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/processed_user_sorted_userID.json')
load('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/processed_review_sorted_date.json')
user_data = id_replace('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/processed_user_sorted_userID_unique.json')
store('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/processed_user_sorted_userID_unique2.json', user_data)
# review_data = id_replace('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/processed_review_sorted_date.json')
# store('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/processed_review_sorted_date_unique.json', review_data)
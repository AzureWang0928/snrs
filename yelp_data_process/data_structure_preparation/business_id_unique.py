<<<<<<< HEAD
# -*- coding: utf-8 -*-
import simplejson as json

dict = {}
def format_map(data):
    if data["business_id"] not in dict:
        # print len(dict)
        dict[data["business_id"]] = len(dict)

def id_replace(path):
    with open(path) as json_file:
        data_list = []
        for line in json_file:
            data = json.loads(line)
            if data["business_id"] not in dict:
                print "miss"
            else:
                data["business_id"] = dict[data["business_id"]]
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

load('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/2.0processed_business.json')
load('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/processed_review_sorted_date_unique.json')
business_data = id_replace('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/2.0processed_business.json')
store('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/processed_business_unique.json', business_data)
review_data = id_replace('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/processed_review_sorted_date_unique.json')
=======
# -*- coding: utf-8 -*-
import simplejson as json

dict = {}
def format_map(data):
    if data["business_id"] not in dict:
        # print len(dict)
        dict[data["business_id"]] = len(dict)

def id_replace(path):
    with open(path) as json_file:
        data_list = []
        for line in json_file:
            data = json.loads(line)
            if data["business_id"] not in dict:
                print "miss"
            else:
                data["business_id"] = dict[data["business_id"]]
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

load('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/2.0processed_business.json')
load('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/processed_review_sorted_date_unique.json')
business_data = id_replace('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/2.0processed_business.json')
store('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/processed_business_unique.json', business_data)
review_data = id_replace('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/processed_review_sorted_date_unique.json')
>>>>>>> 09db2f1c1a365de53ae0d37bf002b813910439fa
store('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/processed_review_sorted_date_unique2.json', review_data)
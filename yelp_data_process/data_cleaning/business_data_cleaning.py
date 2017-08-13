<<<<<<< HEAD
# -*- coding: utf-8 -*-
import simplejson as json

def clean(data):
    business_list = {}
    business_list["business_id"] = data["business_id"]
    business_list["review_count"] = data["review_count"]
    business_list["stars"] = data["stars"]
    business_list["neighborhoods"] = data["neighborhoods"]
    business_list["longitude"] = data["longitude"]
    business_list["latitude"] = data["latitude"]
    return business_list

def store(path, data):
    with open(path, 'a') as json_file:
        json_file.write(json.dumps(data))
        json_file.write("\n")

def load(path):
    data_list = []
    with open(path) as json_file:
        for line in json_file:
            data_line = json.loads(line)
            new_data_line = clean(data_line)
            store('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/processed_business.json',new_data_line)
    return data_list

business_data = load('G:/college/learning/Final_project/workspace/yelp_data_process/uncleaned_data/yelp_academic_dataset_business.json')
=======
# -*- coding: utf-8 -*-
import simplejson as json

def clean(data):
    business_list = {}
    business_list["business_id"] = data["business_id"]
    business_list["review_count"] = data["review_count"]
    business_list["stars"] = data["stars"]
    business_list["neighborhoods"] = data["neighborhoods"]
    business_list["longitude"] = data["longitude"]
    business_list["latitude"] = data["latitude"]
    return business_list

def store(path, data):
    with open(path, 'a') as json_file:
        json_file.write(json.dumps(data))
        json_file.write("\n")

def load(path):
    data_list = []
    with open(path) as json_file:
        for line in json_file:
            data_line = json.loads(line)
            new_data_line = clean(data_line)
            store('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/processed_business.json',new_data_line)
    return data_list

business_data = load('G:/college/learning/Final_project/workspace/yelp_data_process/uncleaned_data/yelp_academic_dataset_business.json')
>>>>>>> 09db2f1c1a365de53ae0d37bf002b813910439fa

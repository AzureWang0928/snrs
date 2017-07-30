# -*- coding: utf-8 -*-
import simplejson as json

# review_count


def clean(data):
    review_list = {}
    review_list["user_id"] = data["user_id"]
    review_list["business_id"] = data["business_id"]
    review_list["stars"] = data["stars"]
    review_list["date"] = data["date"]
    return review_list

def store(path, data):
    with open(path, 'a') as json_file:
        json_file.write(json.dumps(data))
        json_file.write("\n")
        # for i in range(len(data)):
        #     json_file.write(json.dumps(data[i]))
        #     json_file.write("\n")

def load(path):
    data_list = []
    with open(path) as json_file:
        for line in json_file:
            data_line = json.loads(line)
            new_data_line = clean(data_line)
            store('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/3.0processed_review.json',new_data_line)

load('G:/college/learning/Final_project/workspace/yelp_data_process/uncleaned_data/yelp_academic_dataset_review.json')

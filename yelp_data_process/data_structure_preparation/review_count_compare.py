# -*- coding: utf-8 -*-
import simplejson as json


def load(path):
    total_count = 0
    with open(path) as json_file:
        for line in json_file:
            data_line = json.loads(line)
            total_count = total_count + data_line["review_count"]
        print total_count

load('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/1.0processed_user.json')

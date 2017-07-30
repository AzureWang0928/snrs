# -*- coding: utf-8 -*-
from __future__ import division
import simplejson as json

#用户数量
user_num = -1
#活跃用户数量
active_user_num = -1
#商铺数量
business_num = -1
#评价数量
review_num = -1
#矩阵稀疏性
sparsity =0.0

def store_active_userid(path, data):
    with open(path, 'a') as json_file:
        json_file.write(json.dumps(data))
        json_file.write("\n")

def calculate_number(path):
    count = 0
    with open(path) as json_file:
        for line in json_file:
            data_line = json.loads(line)
            if data_line:
                count += 1
    return count

def user_analysis(path):
    count = 0
    sum = 0.0
    variance_sum = 0.0
    with open(path) as json_file:
        for line in json_file:
            user_list = json.loads(line)
            count += 1
            sum += float(user_list["stars"])
        average = sum/count
    json_file.close()

    with open(path) as json_file:
        for line in json_file:
            user_list = json.loads(line)
            star = float(user_list["stars"])
            variance_sum += (star - average)*(star - average)
        variance = variance_sum/count
    return count,average,variance

def calculate_sparsity():
    return review_num/(user_num*business_num)

# user_num = calculate_number('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/processed_user.json')
active_user_num,active_average_stars,active_variance = user_analysis('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/unique_data/new_review_train.json')
# business_num = calculate_number('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/processed_business.json')
# review_num = calculate_number('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/processed_review.json')
print(active_average_stars)
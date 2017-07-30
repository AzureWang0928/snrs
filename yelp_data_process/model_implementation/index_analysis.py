# -*- coding: utf-8 -*-
import numpy as np
import simplejson as json
from functools import reduce
import time


w1 = -58126.4
w2 = -13.4591
e = -110746

def rmse(predictions, targets):
    return np.sqrt(((predictions - targets) ** 2).mean())

def ame(predictions, targets):
    return (np.abs(predictions - targets)).mean()

def load(path1, path2, path3, path4, path5):
    real_mark_dict = {}
    with open(path1) as train_json_file:
        for line in train_json_file:
            train_data_line = json.loads(line)
            if train_data_line["user_id"] not in real_mark_dict:
                business_mark_dict = {}
            business_mark_dict[train_data_line["business_id"]] = train_data_line["stars"]
            real_mark_dict[train_data_line["user_id"]] = business_mark_dict
            # print (real_mark_dict)
    # print(time.time())
    influence_PR_dict = {}
    influence_item_dict = {}
    influence_friend_dict = {}
    with open(path2) as influence_json_file:
        for line in influence_json_file:
            influence_data_line = json.loads(line)
            influence_PR_dict[influence_data_line["user_id"]] = influence_data_line["PR_valve"]
            influence_item_dict[influence_data_line["user_id"]] = influence_data_line["item_plus"]
            friend_plus_dict = {}
            for i in range(len(influence_data_line["friend_plus"])):
                friend_plus_dict[influence_data_line["friend_plus"][i][0]] = influence_data_line["friend_plus"][i][1]
            influence_friend_dict[influence_data_line["user_id"]] = friend_plus_dict
            # print(influence_friend_dict)
    # print(time.time())

    user_sim_dict = {}
    with open(path3) as similarity_json_file:
        for line in similarity_json_file:
            similarity_data_line = json.loads(line)
            user_sim_dict[similarity_data_line["user_id"]] = similarity_data_line["similarity"]
            # print(user_sim_dict)

    average_score_dict = {}
    with open(path4) as average_score_json_file:
        count = 0
        for line in average_score_json_file:
            average_score_data_line = json.loads(line)
            while count != average_score_data_line["user_id"]:
                average_score_dict[count] = 3.75
                count = count + 1
            average_score_dict[average_score_data_line["user_id"]] = average_score_data_line["average_star"]
            count = count + 1
            # print(average_score_dict)
        average_score_dict[686554] = 3.75
        average_score_dict[686555] = 3.75
    # print(time.time())

    train_mark_dict = {}
    with open(path5) as train_json_file:
        for line in train_json_file:
            train_data_line = json.loads(line)
            if train_data_line["user_id"] not in train_mark_dict:
                business_mark_dict = {}
            business_mark_dict[train_data_line["business_id"]] = train_data_line["stars"]
            train_mark_dict[train_data_line["user_id"]] = business_mark_dict
            # print (real_mark_dict)
    # print(time.time())
    return real_mark_dict, influence_PR_dict, influence_item_dict, influence_friend_dict, user_sim_dict, average_score_dict, train_mark_dict

def format_list(real_mark_dict,user_sim_dict,average_score_dict,influence_PR_dict, influence_item_dict, influence_friend_dict, train_mark_dict):
    real_mark_list = []
    user_sim_list = []
    average_self_mark_list = []
    difference_mark_list = []
    influence_PR_list = []
    influence_friend_list = []
    influence_item_list = []

    for each_review in real_mark_dict:
        for business_id in list(real_mark_dict[each_review].keys()):
            each_sim_list = []
            sim_friend_mark_list = []
            sim_friend_average_mark_list = []
            each_influence_PR_list = []
            each_influence_friend_list = []
            each_influence_item_list = []
            if not user_sim_dict[each_review]:
                each_sim_list = [0]
                sim_friend_mark_list = [0]
                sim_friend_average_mark_list = [0]
                each_influence_PR_list = [0]
                each_influence_friend_list = [0]
                each_influence_item_list = [0]
            for each_sim_friend in user_sim_dict[each_review]:
                if int(list(each_sim_friend.keys())[0]) in average_score_dict:
                    each_sim_list.append(list(each_sim_friend.values())[0])
                    sim_friend_average_mark_list.append(average_score_dict[int(list(each_sim_friend.keys())[0])])
                    if business_id in train_mark_dict[int(list(each_sim_friend.keys())[0])]:
                        sim_friend_mark_list.append(train_mark_dict[int(list(each_sim_friend.keys())[0])][business_id])
                    else:
                        sim_friend_mark_list.append(average_score_dict[int(list(each_sim_friend.keys())[0])])

                    each_influence_PR_list.append(influence_PR_dict[each_review])#取得对应u的PR值影响力
                    each_influence_friend_list.append(influence_friend_dict[each_review][int(list(each_sim_friend.keys())[0])])
                    each_influence_item_list.append(influence_item_dict[each_review])#取得对应u的项目评价数目影响力
                    # print(each_influence_friend_list)
                    # print(each_influence_item_list)
                    # print()
            real_mark_list.append(real_mark_dict[each_review][business_id])
            average_self_mark_list.append(average_score_dict[each_review])
            difference_mark_list.append(np.array(sim_friend_mark_list) - np.array(sim_friend_average_mark_list))

            user_sim_list.append(each_sim_list)
            influence_PR_list.append(each_influence_PR_list)
            influence_friend_list.append(each_influence_friend_list)
            influence_item_list.append(each_influence_item_list)
            # print(difference_mark_list)
    # print(time.time())

    return real_mark_list, user_sim_list, average_self_mark_list, difference_mark_list, influence_PR_list, influence_friend_list, influence_item_list


# print (rmse(np.array([2,2,3]), np.array([0,2,6])))
# print (ame(np.array([2,2,3]), np.array([0,2,6])))
# print (  5 * np.array([2,2,3]))
time1  = time.time()
or_child = 'G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/unique_data/'
real_mark_dict, influence_PR_dict, influence_item_dict, influence_friend_dict, user_sim_dict, average_score_dict, train_mark_dict = load(or_child + '/new_review_train.json', or_child + '/user_influence_analysis.json', or_child + '/similarity.json', or_child + '/average_score.json', or_child + 'review.json')
real_mark_list, user_sim_list, average_self_mark_list, difference_mark_list, influence_PR_list, influence_friend_list, influence_item_list =  format_list(real_mark_dict, user_sim_dict, average_score_dict, influence_PR_dict, influence_item_dict, influence_friend_dict, train_mark_dict)

trSIM = np.array(user_sim_list)
trMeanSelf = np.array(average_self_mark_list)
trInfPR = np.array(influence_PR_list)
trInfFriend = np.array(influence_friend_list)
trInfItem = np.array(influence_item_list)
trDifMark = difference_mark_list
# create a y value which is approximately linear but with some random noise

trY = np.array(real_mark_list)

# DifMark = tf.placeholder(tf.float32)
# SIM = tf.placeholder(tf.float32)  # create symbolic variables
# MeanSelf = tf.placeholder(tf.float32)  # create symbolic variables
# InfPR = tf.placeholder(tf.float32)  # create symbolic variables
# InfFriend = tf.placeholder(tf.float32)  # create symbolic variables
# InfItem = tf.placeholder(tf.float32)  # create symbolic variables
#
# Y = tf.placeholder(tf.float32)

# CFSM = []
# for (difMark, sim, meanSelf, infPR, infFriend, infItem, y) in zip(trDifMark, trSIM, trMeanSelf, trInfPR, trInfFriend,trInfItem, trY):
#     difMark = np.array(difMark)
#     sim = np.array(sim)
#     infPR = np.array(infPR)
#     infFriend = np.array(infFriend)
#     infItem = np.array(infItem)
#     CFSM.append(meanSelf + (np.dot(sim, difMark)) / (np.dot(sim, 1) + 0.0000001))

CFSMIF = []
for (difMark, sim, meanSelf, infPR, infFriend, infItem, y) in zip(trDifMark, trSIM, trMeanSelf, trInfPR, trInfFriend,trInfItem, trY):
    difMark = np.array(difMark)
    sim = np.array(sim)
    infPR = np.array(infPR)
    infFriend = np.array(infFriend)
    infItem = np.array(infItem)
    UIF = e/686556 + ((1 - e) * ((w1 * infFriend)+ (w2 * infItem)) * infPR)
    CFSMIF.append(meanSelf + (np.dot((sim * difMark), UIF)) / (np.dot(sim, UIF) + 0.0000001))

# with open('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/unique_data/compare.json', 'a') as json_file:
#     for i in range(len(real_mark_list)):
#         json_file.write(json.dumps(real_mark_list[i]))
#         json_file.write(" ")
#         json_file.write(json.dumps(CFSMIF[i]))
#         json_file.write("\n")

print("RMES for Average",rmse(trY, np.array([3.745] * len(real_mark_list))))
print("AME for Average",ame(trY, np.array([3.745] * len(real_mark_list))))
print()

# print(rmse(trY, np.array(CFSM)))
# print(ame(trY, np.array(CFSM)))
# print()

print("RMES for CFSMIF",rmse(trY, np.array(CFSMIF)))
print("AME for CFSMIF",ame(trY, np.array(CFSMIF)))
time2 = time.time()

print()
m, s = divmod(time2-time1, 60)
h, m = divmod(m, 60)
print ("%02d:%02d:%02d" % (h, m, s))
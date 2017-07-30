# -*- coding: utf-8 -*-
import simplejson as json
import numpy as np
import tensorflow as tf
import time
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

def store(path, data):
    with open(path, 'a') as json_file:
        json_file.write(json.dumps(data))
        json_file.write("\n")

def load(path1, path2, path3, path4):
    real_mark_dict = {}
    with open(path1) as train_json_file:
        for line in train_json_file:
            train_data_line = json.loads(line)
            if train_data_line["user_id"] not in real_mark_dict:
                business_mark_dict = {}
            business_mark_dict[train_data_line["business_id"]] = train_data_line["stars"]
            real_mark_dict[train_data_line["user_id"]] = business_mark_dict
            # print (real_mark_dict)
    print(time.time())
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
    print(time.time())

    user_sim_dict = {}
    with open(path3) as similarity_json_file:
        for line in similarity_json_file:
            similarity_data_line = json.loads(line)
            user_sim_dict[similarity_data_line["user_id"]] = similarity_data_line["similarity"]
            # print(user_sim_dict)

    average_score_dict = {}
    with open(path4) as average_score_json_file:
        for line in average_score_json_file:
            average_score_data_line = json.loads(line)
            average_score_dict[average_score_data_line["user_id"]] = average_score_data_line["average_star"]
            # print(average_score_dict)
    print(time.time())

    return real_mark_dict, influence_PR_dict, influence_item_dict, influence_friend_dict, user_sim_dict, average_score_dict

def format_list(real_mark_dict,user_sim_dict,average_score_dict,influence_PR_dict, influence_item_dict, influence_friend_dict):
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
                    if business_id in real_mark_dict[int(list(each_sim_friend.keys())[0])]:
                        sim_friend_mark_list.append(real_mark_dict[int(list(each_sim_friend.keys())[0])][business_id])
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
    print(time.time())

    return real_mark_list, user_sim_list, average_self_mark_list, difference_mark_list, influence_PR_list, influence_friend_list, influence_item_list


def graidents(real_mark_list, user_sim_list, average_self_mark_list, difference_mark_list, influence_PR_list, influence_friend_list, influence_item_list):

    trSIM = np.array(user_sim_list)
    trMeanSelf = np.array(average_self_mark_list)
    trInfPR = np.array(influence_PR_list)
    trInfFriend = np.array(influence_friend_list)
    trInfItem = np.array(influence_item_list)
    trDifMark =difference_mark_list
    # create a y value which is approximately linear but with some random noise
    trY = np.array(real_mark_list)

    DifMark = tf.placeholder(tf.float32)
    SIM = tf.placeholder(tf.float32)  # create symbolic variables
    MeanSelf = tf.placeholder(tf.float32)  # create symbolic variables
    InfPR = tf.placeholder(tf.float32)  # create symbolic variables
    InfFriend = tf.placeholder(tf.float32)  # create symbolic variables
    InfItem = tf.placeholder(tf.float32)  # create symbolic variables

    Y = tf.placeholder(tf.float32)

    # def model(X, w, b):
    #     # linear regression is just X*w + b, so this model line is pretty simple
    #     return tf.multiply(X, w) + b

    def model(DifMark, SIM, MeanSelf, InfPR, InfFriend, InfItem, w1, w2, e, b):
        UIF = e/686556 + tf.multiply((1 - e), (tf.multiply(w1, InfFriend)+ tf.multiply(w2, InfItem)) * InfPR)
        return MeanSelf + (SIM * DifMark * UIF) / (SIM * UIF + 0.0000001)

    w1 = tf.Variable(0.0, name="weights1")
    w2 = tf.Variable(0.0, name="weights2")
    e = tf.Variable(0.0, name="init")
    # create a variable for biases
    b = tf.Variable(0.0, name="biases")
    y_model = model(DifMark, SIM, MeanSelf, InfPR, InfFriend, InfItem, w1, w2, e, b)

    cost = tf.square(Y - y_model)  # use square error for cost function

    # construct an optimizer to minimize cost and fit line to mydata
    train_op = tf.train.GradientDescentOptimizer(0.01).minimize(cost)

    # launch the graph in a session
    with tf.Session() as sess:
        # you need to initialize variables (in this case just variable w)
        init = tf.global_variables_initializer()
        sess.run(init)

        # train
        for i in range(1):
            # print(time.time())
            # print(sess.run(w1))  # it should be something around 2
            # print(sess.run(w2))  # it should be something around 2
            # print(sess.run(e))  # it should be something around 2
            # # print bias
            # print(sess.run(b))  # it should be something atound 2
            # print()
            for (difMark, sim, meanSelf, infPR, infFriend, infItem, y) in zip(trDifMark, trSIM, trMeanSelf, trInfPR, trInfFriend, trInfItem, trY):
                sess.run(train_op, feed_dict={DifMark: difMark, SIM: sim, MeanSelf: meanSelf, InfPR: infPR, InfFriend: infFriend, InfItem: infItem, Y: y})
                # print()
                # print weight
        print("w1: ",sess.run(w1))  # it should be something around 2
        print("w2: ",sess.run(w2))  # it should be something around 2
        print("e: ",sess.run(e))  # it should be something around 2
    return w1, w2, e

time1 = time.time()
or_child = 'G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/unique_data/'
real_mark_dict, influence_PR_dict, influence_item_dict, influence_friend_dict, user_sim_dict, average_score_dict = load(or_child + '/new_review_train.json', or_child + '/user_influence_analysis.json', or_child + '/similarity.json', or_child + '/average_score.json')
real_mark_list, user_sim_list, average_self_mark_list, difference_mark_list, influence_PR_list, influence_friend_list, influence_item_list =  format_list(real_mark_dict, user_sim_dict, average_score_dict, influence_PR_dict, influence_item_dict, influence_friend_dict)

w1, w2, e = graidents(real_mark_list, user_sim_list, average_self_mark_list, difference_mark_list, influence_PR_list, influence_friend_list, influence_item_list)
time2 = time.time()

print()
m, s = divmod(time2-time1, 60)
h, m = divmod(m, 60)
print ("Running time: %02d:%02d:%02d" % (h, m, s))
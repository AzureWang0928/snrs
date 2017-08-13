# -*- coding: utf-8 -*-
import simplejson as json
import numpy as np

def format(data):
    similarity_list = []
    for each_user in data:
        similarity_dict = {}
        similarity_dict["user_id"] = each_user
        similarity_dict["similarity"] = data[each_user]
        similarity_list.append(similarity_dict)
    return similarity_list

def store(path, data):
    with open(path, 'a') as json_file:
        for i in range(len(data)):
            json_file.write(json.dumps(data[i]))
            json_file.write("\n")

def load(path1, path2):
    friendship_data = []
    with open(path1) as friendship_json_file:
        for line in friendship_json_file:
            data_line = json.loads(line)
            friendship_data.append(data_line)
        # print len(friendship_data)

    mark_data = {}
    with open(path2) as mark_json_file:
        for line in mark_json_file:
            data_line = json.loads(line)
            business_mark = {}
            for data in data_line["stars"]:
                business_mark[data[0]] = data[1]
            mark_data[data_line["user_id"]] = business_mark

    similarity_dict = {}
    #取出某个用户所有好友
    for each_friendship in friendship_data:
        #如果好友集不为空
        user_similarity_list = []
        sim = 0
        if each_friendship["friends"]:
            #依次取出好友id
            for friend_id in  each_friendship["friends"]:
                user_similarity_dict = {}
                sim = 0
                #如果我自己和好友都有评价
                if mark_data.has_key(friend_id) & mark_data.has_key(each_friendship["user_id"]):
                    #计算评价商铺集合
                    friend_set = mark_data[friend_id].keys()
                    average_friend_mark = np.mean(mark_data[friend_id].values())
                    self_set = mark_data[each_friendship["user_id"]].keys()
                    average_self_mark = np.mean(mark_data[each_friendship["user_id"]].values())
                    # friend_set = set(map(lambda star: star[0],mark_data[friend_id]))
                    # self_set = set(map(lambda star: star[0],mark_data[each_friendship["user_id"]]))
                    #求共同评价商铺集合
                    and_business = set(friend_set) & set(self_set)
                    if and_business:
                        # print and_business
                        friend_mark_list = np.array(map(lambda key: mark_data[friend_id][key],list(and_business)))
                        self_mark_list = np.array(map(lambda key: mark_data[each_friendship["user_id"]][key],list(and_business)))
                        # print friend_mark_list
                        # print self_mark_list
                        # print average_friend_mark
                        # print average_self_mark
                        num = reduce(lambda a,b:a+b,map(lambda a, b: (a - average_friend_mark)*(b - average_self_mark), friend_mark_list, self_mark_list))
                        # print num
                        # num = float(self_mark_list.T * friend_mark_list)
                        denom = np.linalg.norm(self_mark_list - average_self_mark) * np.linalg.norm(friend_mark_list - average_friend_mark)
                        if denom != 0:
                            pcc = num / denom  # PCC
                            sim = 0.5 + 0.5 * pcc  # 归一化
                        # print round(sim, 4)
                user_similarity_dict[friend_id] = round(sim, 4)
                # print user_similarity_dict
                user_similarity_list.append(user_similarity_dict)
            # print user_similarity_list
        similarity_dict[each_friendship["user_id"]]  = user_similarity_list
        # print  similarity_dict
    similarity_list = format(similarity_dict)
    store('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/unique_data/similarity0.9.json', similarity_list)

load('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/unique_data/user_friendship.json', 'G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/unique_data/user_review_mark0.9.json')

<<<<<<< HEAD
# -*-coding:utf-8-*-

import math
import simplejson as json

# ----------------新增代码段END----------------------


class ItemBasedCF:
    def __init__(self, train_file):
        self.train_file = train_file
        self.readData()

    def readData(self):
        # 读取文件，并生成用户-物品的评分表和测试集
        self.train = dict()  # 用户-物品的评分表
        for line in open(self.train_file):
            train_data_line = json.loads(line)
            if train_data_line["user_id"] not in self.train:
                self.train[train_data_line["user_id"]] = {}
            self.train[train_data_line["user_id"]][train_data_line["business_id"]] = float(train_data_line["stars"])

    def ItemSimilarity(self):
        # 建立物品-物品的共现矩阵
        C = dict()  # 物品-物品的共现矩阵
        N = dict()  # 物品被多少个不同用户购买
        for user, items in self.train.items():
            for i in items.keys():
                N.setdefault(i, 0)
                N[i] += 1
                C.setdefault(i, {})
                for j in items.keys():
                    if i == j: continue
                    C[i].setdefault(j, 0)
                    C[i][j] += 1
        # 计算相似度矩阵
        self.W = dict()
        for i, related_items in C.items():
            self.W.setdefault(i, {})
            for j, cij in related_items.items():
                self.W[i][j] = cij / (math.sqrt(N[i] * N[j]))
        return self.W

    # 给用户user推荐，前K个相关用户
    def Recommend(self, user, K=3, N=10):
        rank = dict()
        action_item = self.train[user]  # 用户user产生过行为的item和评分
        for item, score in action_item.items():
            for j, wj in sorted(self.W[item].items(), key=lambda x: x[1], reverse=True)[0:K]:
                if j in action_item.keys():
                    continue
                rank.setdefault(j, 0)
                rank[j] += score * wj
        return dict(sorted(rank.items(), key=lambda x: x[1], reverse=True)[0:N])

# 声明一个ItemBased推荐的对象
Item = ItemBasedCF('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/unique_data/new_review_train.json')
Item.ItemSimilarity()
# recommedDic = Item.Recommend(15)
for k, v in recommedDic.iteritems():
=======
# -*-coding:utf-8-*-

import math
import simplejson as json

# ----------------新增代码段END----------------------


class ItemBasedCF:
    def __init__(self, train_file):
        self.train_file = train_file
        self.readData()

    def readData(self):
        # 读取文件，并生成用户-物品的评分表和测试集
        self.train = dict()  # 用户-物品的评分表
        for line in open(self.train_file):
            train_data_line = json.loads(line)
            if train_data_line["user_id"] not in self.train:
                self.train[train_data_line["user_id"]] = {}
            self.train[train_data_line["user_id"]][train_data_line["business_id"]] = float(train_data_line["stars"])

    def ItemSimilarity(self):
        # 建立物品-物品的共现矩阵
        C = dict()  # 物品-物品的共现矩阵
        N = dict()  # 物品被多少个不同用户购买
        for user, items in self.train.items():
            for i in items.keys():
                N.setdefault(i, 0)
                N[i] += 1
                C.setdefault(i, {})
                for j in items.keys():
                    if i == j: continue
                    C[i].setdefault(j, 0)
                    C[i][j] += 1
        # 计算相似度矩阵
        self.W = dict()
        for i, related_items in C.items():
            self.W.setdefault(i, {})
            for j, cij in related_items.items():
                self.W[i][j] = cij / (math.sqrt(N[i] * N[j]))
        return self.W

    # 给用户user推荐，前K个相关用户
    def Recommend(self, user, K=3, N=10):
        rank = dict()
        action_item = self.train[user]  # 用户user产生过行为的item和评分
        for item, score in action_item.items():
            for j, wj in sorted(self.W[item].items(), key=lambda x: x[1], reverse=True)[0:K]:
                if j in action_item.keys():
                    continue
                rank.setdefault(j, 0)
                rank[j] += score * wj
        return dict(sorted(rank.items(), key=lambda x: x[1], reverse=True)[0:N])

# 声明一个ItemBased推荐的对象
Item = ItemBasedCF('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/unique_data/new_review_train.json')
Item.ItemSimilarity()
# recommedDic = Item.Recommend(15)
for k, v in recommedDic.iteritems():
>>>>>>> 09db2f1c1a365de53ae0d37bf002b813910439fa
    print(k, "\t", v)
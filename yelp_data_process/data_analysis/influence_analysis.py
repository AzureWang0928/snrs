<<<<<<< HEAD
# -*- coding: utf-8 -*-
from pygraph.classes.digraph import digraph
import simplejson as json


class PRIterator:
    __doc__ = '''计算一张图中的PR值'''

    def __init__(self, dg):
        self.damping_factor = 0.85  # 阻尼系数,即α
        self.max_iterations = 100  # 最大迭代次数
        self.min_delta = 0.000001  # 确定迭代是否结束的参数,即ϵ
        self.graph = dg

        nodes = self.graph.nodes()
        graph_size = len(nodes)

        if graph_size == 0:
            return {}
        page_rank = dict.fromkeys(nodes, 1.0 / graph_size)  # 给每个节点赋予初始的PR值
        damping_value = (1.0 - self.damping_factor) / graph_size  # 公式中的(1−α)/N部分

        flag = False
        for i in range(self.max_iterations):
            change = 0
            for node in nodes:
                rank = 0
                for incident_page in self.graph.incidents(node):  # 遍历所有“入射”的页面
                    rank += self.damping_factor * (page_rank[incident_page] / len(self.graph.neighbors(incident_page)))
                rank += damping_value
                change += abs(page_rank[node] - rank)  # 绝对值
                page_rank[node] = rank

            # print("This is NO.%s iteration" % (i + 1))
            # print(page_rank)
            # print""

            if change < self.min_delta:
                flag = True
                break
        if flag:
            print("finished in %s iterations!" % node)
        else:
            print("finished out of 100 iterations!")
        return page_rank



def store(path, data):
    with open(path, 'a') as uif_json_file:
        for j in range(len(data)):
            uif_json_file.write(json.dumps(data[j]))
            uif_json_file.write("\n")

if __name__ == '__main__':
    #Declare the graph
    dg = digraph()
    #Declare the pagerank list
    PR_list = []
    #Declare the review count list and total review count
    review_count_list = []
    total_review_count = 0
    #Declare the friends plus list
    friend_plus_map = {}

    with open('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/unique_data/user.json') as node_json_file:
        for line in node_json_file:
            data_line = json.loads(line)
            user_node = data_line["user_id"]
            dg.add_node(user_node)

            review_count = data_line["review_count"]
            total_review_count = total_review_count + review_count
            review_count_list.append(review_count)
        print (1)
    with open('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/unique_data/user_friendship.json') as node_json_file:
        user_list = {}
        for line in node_json_file:
            data_line = json.loads(line)
            user_list[data_line["user_id"]] = data_line["friends"]

        for each_user in user_list:
            friend_plus_map[each_user] = []
            if user_list[each_user]:
                for friend_user in user_list[each_user]:
                    and_count = 0
                    or_count = 0

                    and_count = len(set(user_list[each_user]) & set(user_list[friend_user]))
                    or_count = len(set(user_list[each_user]) | set(user_list[friend_user]))
                    result = float(and_count) / or_count
                    friend_plus_map[each_user].append([friend_user, result])

    with open('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/unique_data/social_graph_link.json') as edge_json_file:
        for line in edge_json_file:
            data_line = json.loads(line)
            from_node = data_line["from_node"]
            to_node = data_line["to_node"]
            dg.add_edge((from_node, to_node))

    pr = PRIterator(dg)
    page_ranks = pr.page_rank()

    for i in range(len(page_ranks)):
        PR_dict = {}
        PR_dict["user_id"] = len(PR_list)
        PR_dict["PR_valve"] = page_ranks[i]
        PR_dict["item_plus"] = float(review_count_list[i])/total_review_count
        PR_dict["friend_plus"] = friend_plus_map[len(PR_list)]
        PR_list.append(PR_dict)
=======
# -*- coding: utf-8 -*-
from pygraph.classes.digraph import digraph
import simplejson as json


class PRIterator:
    __doc__ = '''计算一张图中的PR值'''

    def __init__(self, dg):
        self.damping_factor = 0.85  # 阻尼系数,即α
        self.max_iterations = 100  # 最大迭代次数
        self.min_delta = 0.000001  # 确定迭代是否结束的参数,即ϵ
        self.graph = dg

        nodes = self.graph.nodes()
        graph_size = len(nodes)

        if graph_size == 0:
            return {}
        page_rank = dict.fromkeys(nodes, 1.0 / graph_size)  # 给每个节点赋予初始的PR值
        damping_value = (1.0 - self.damping_factor) / graph_size  # 公式中的(1−α)/N部分

        flag = False
        for i in range(self.max_iterations):
            change = 0
            for node in nodes:
                rank = 0
                for incident_page in self.graph.incidents(node):  # 遍历所有“入射”的页面
                    rank += self.damping_factor * (page_rank[incident_page] / len(self.graph.neighbors(incident_page)))
                rank += damping_value
                change += abs(page_rank[node] - rank)  # 绝对值
                page_rank[node] = rank

            # print("This is NO.%s iteration" % (i + 1))
            # print(page_rank)
            # print""

            if change < self.min_delta:
                flag = True
                break
        if flag:
            print("finished in %s iterations!" % node)
        else:
            print("finished out of 100 iterations!")
        return page_rank



def store(path, data):
    with open(path, 'a') as uif_json_file:
        for j in range(len(data)):
            uif_json_file.write(json.dumps(data[j]))
            uif_json_file.write("\n")

if __name__ == '__main__':
    #Declare the graph
    dg = digraph()
    #Declare the pagerank list
    PR_list = []
    #Declare the review count list and total review count
    review_count_list = []
    total_review_count = 0
    #Declare the friends plus list
    friend_plus_map = {}

    with open('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/unique_data/user.json') as node_json_file:
        for line in node_json_file:
            data_line = json.loads(line)
            user_node = data_line["user_id"]
            dg.add_node(user_node)

            review_count = data_line["review_count"]
            total_review_count = total_review_count + review_count
            review_count_list.append(review_count)
        print (1)
    with open('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/unique_data/user_friendship.json') as node_json_file:
        user_list = {}
        for line in node_json_file:
            data_line = json.loads(line)
            user_list[data_line["user_id"]] = data_line["friends"]

        for each_user in user_list:
            friend_plus_map[each_user] = []
            if user_list[each_user]:
                for friend_user in user_list[each_user]:
                    and_count = 0
                    or_count = 0

                    and_count = len(set(user_list[each_user]) & set(user_list[friend_user]))
                    or_count = len(set(user_list[each_user]) | set(user_list[friend_user]))
                    result = float(and_count) / or_count
                    friend_plus_map[each_user].append([friend_user, result])

    with open('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/unique_data/social_graph_link.json') as edge_json_file:
        for line in edge_json_file:
            data_line = json.loads(line)
            from_node = data_line["from_node"]
            to_node = data_line["to_node"]
            dg.add_edge((from_node, to_node))

    pr = PRIterator(dg)
    page_ranks = pr.page_rank()

    for i in range(len(page_ranks)):
        PR_dict = {}
        PR_dict["user_id"] = len(PR_list)
        PR_dict["PR_valve"] = page_ranks[i]
        PR_dict["item_plus"] = float(review_count_list[i])/total_review_count
        PR_dict["friend_plus"] = friend_plus_map[len(PR_list)]
        PR_list.append(PR_dict)
>>>>>>> 09db2f1c1a365de53ae0d37bf002b813910439fa
    store('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/unique_data/user_influence_analysis.json',PR_list)
#!/usr/bin/python2.7
# _*_ coding: utf-8 _*_

from matplotlib import pyplot as plt
import KNN

matrix, labels = KNN.file2matrix('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/unique_data/link_count_result.json')


plt.figure(figsize=(8, 5), dpi=80)
axes = plt.subplot(111)

type_x = []
type_y = []

for i in range(len(labels)):
    type_x.append(matrix[i][0])
    type_y.append(matrix[i][1])

axes.semilogx()
axes.semilogy()
axes.scatter(type_x, type_y, s=80, marker='+', c='red')


# plt.scatter(matrix[:, 0], matrix[:, 1], s=20 * numpy.array(labels),
#             c=50 * numpy.array(labels), marker='o',
#             label='test')
plt.xlabel('Outdegree',fontsize=30)
plt.ylabel('Number of Nodes',fontsize=30)
axes.legend(('Outdegree',), loc=1, scatterpoints=1, fontsize=30)

plt.show()
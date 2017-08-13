<<<<<<< HEAD
#!/usr/bin/python2.7
# _*_ coding: utf-8 _*_

from matplotlib import pyplot as plt
import numpy as np
import KNN

matrix, labels = KNN.file2matrix('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/unique_data/influence_count_result.json')


plt.figure(figsize=(8, 5), dpi=80)
axes = plt.subplot(111)

type_x = []
type_y = []
type_x_normal = []

def MaxMinNormalization(x,Max,Min):
    x = (x - Min) / (Max - Min)
    return x

for i in range(len(labels)):
    type_x.append(matrix[i][0] * (10**7))
    type_y.append(matrix[i][1])

# for i in range(len(type_x)):
#     type_x_normal.append(MaxMinNormalization(type_x[i], np.max(type_x), np.min(type_x)))

axes.semilogx()
axes.semilogy()
axes.scatter(type_x, type_y, s=60, marker='x', c='red')


# plt.scatter(matrix[:, 0], matrix[:, 1], s=20 * numpy.array(labels),
#             c=50 * numpy.array(labels), marker='o',
#             label='test')
plt.xlabel('Influence',fontsize=30)
plt.ylabel('Number of Users',fontsize=30)
axes.legend(('Influence',), loc=1, scatterpoints=1, fontsize=30)

plt.show()
=======
#!/usr/bin/python2.7
# _*_ coding: utf-8 _*_

from matplotlib import pyplot as plt
import numpy as np
import KNN

matrix, labels = KNN.file2matrix('G:/college/learning/Final_project/workspace/yelp_data_process/cleaned_data/unique_data/influence_count_result.json')


plt.figure(figsize=(8, 5), dpi=80)
axes = plt.subplot(111)

type_x = []
type_y = []
type_x_normal = []

def MaxMinNormalization(x,Max,Min):
    x = (x - Min) / (Max - Min)
    return x

for i in range(len(labels)):
    type_x.append(matrix[i][0] * (10**7))
    type_y.append(matrix[i][1])

# for i in range(len(type_x)):
#     type_x_normal.append(MaxMinNormalization(type_x[i], np.max(type_x), np.min(type_x)))

axes.semilogx()
axes.semilogy()
axes.scatter(type_x, type_y, s=60, marker='x', c='red')


# plt.scatter(matrix[:, 0], matrix[:, 1], s=20 * numpy.array(labels),
#             c=50 * numpy.array(labels), marker='o',
#             label='test')
plt.xlabel('Influence',fontsize=30)
plt.ylabel('Number of Users',fontsize=30)
axes.legend(('Influence',), loc=1, scatterpoints=1, fontsize=30)

plt.show()
>>>>>>> 09db2f1c1a365de53ae0d37bf002b813910439fa

<<<<<<< HEAD
from sklearn import  linear_model


reg = linear_model.Ridge (alpha = .5)
reg.fit ([[0, 0], [0, 0], [1, 1]], [0, .1, 1])
reg.coef_
=======
from sklearn import  linear_model


reg = linear_model.Ridge (alpha = .5)
reg.fit ([[0, 0], [0, 0], [1, 1]], [0, .1, 1])
reg.coef_
>>>>>>> 09db2f1c1a365de53ae0d37bf002b813910439fa
reg.intercept_
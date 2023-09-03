import numpy as np
A = np.mat('[1 2;3 4]')
A
matrix([[1, 2],
        [3, 4]])
A.I
matrix([[-2. ,  1. ],
        [ 1.5, -0.5]])
b = np.mat('[5 6]')
b
matrix([[5, 6]])
b.T
matrix([[5],
        [6]])
A*b.T
matrix([[17],
        [39]])

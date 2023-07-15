import math
import numpy as np
import math



@staticmethod
def load_dataset(filename = 'data1.csv'):
    A = np.loadtxt(filename,dtype = str, delimiter=",")
    X = A[1:,1:]
    X = X.T
    Y = A[1:,0]

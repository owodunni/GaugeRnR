#!/usr/bin/env python3
import numpy as np

# y_ijk = u + pi + oj +(PO)ij+eijk 
# measurments: [o1:[p1:[m1, m2, m3],p2:[m1,m2,m3]],
#               o2:[p1:[m1, m2, m3],p2:[m1,m2,m3]]


class Distribution:
    def __init__(self, number, mean, sigma):
        self.number = number
        self.mean = mean
        self.sigma = sigma
    
    def batch(self):
        return(np.random.normal(self.mean, self.sigma, self.number))

class Settings:
    def __init__(self, operators, parts, measurments):
        self.operators = operators
        self.parts = parts
        self.measurments = measurments
        self.size = [operators.number, parts.number, measurments.number]

class Generator:
    def __init__(self, settings):
        self.settings = settings
        self.data = np.empty(settings.size, dtype=float)

        operators = self.settings.operators.batch()
        print("operators:")
        print(operators)
        parts = self.settings.parts.batch()
        print("parts:")
        print(parts)

        for i in range(0, len(operators)):
            for j in range(0, len(parts)):
                self.data[i,j,:]  = \
                    operators[i] + \
                    parts[j] +\
                    self.settings.measurments.batch()
                




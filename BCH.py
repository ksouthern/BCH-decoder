import math
class BCH(object):
    def __init__(self, n, k, d):
        self.n = n
        self.k = k
        self.d = d
        self.m = math.log(n + 1, 2)
        self.t = math.floor((d+1)/2)


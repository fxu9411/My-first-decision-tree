import pandas as pd
import collections
import math


# Initial Function: Read data
def read_data(id):
    return pd.read_csv(id)


# Algo: Choose the most important feature
def entropy(dist):
    value = 0
    total = 0

    for i, j in dist.iteritems():
        total += j

    for i,j in dist.iteritems():
        if j != 0:
            prob = j / total
            value += (prob * math.log(prob, 2))
        else:
            value += 0
    return value * -1

def choose_feature_split(data):
    pass


# Test:

data = read_data("occupancy_A.csv")

columns = list(data)

for i in columns:
    data.sort_values(by=i, ascending=True)
    print(data)
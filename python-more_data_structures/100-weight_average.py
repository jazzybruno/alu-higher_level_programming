#!/usr/bin/python3
def weight_average(my_list=[]):
    total_weight = sum(weight for _, weight in my_list)
    if not my_list or total_weight == 0:
        return 0
    return sum(score * weight for score, weight in my_list) / total_weight

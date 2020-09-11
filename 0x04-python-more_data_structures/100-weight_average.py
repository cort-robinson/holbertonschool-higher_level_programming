#!/usr/bin/python3
def weight_average(my_list=[]):
    total_weight = sum(list(i[1] for i in my_list))
    sum_total = sum(i[0] * i[1] for i in my_list)
    return sum_total / total_weight

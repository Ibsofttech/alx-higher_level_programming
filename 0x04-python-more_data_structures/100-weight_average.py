#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        sum = 0
        weight = 0
        for num1, num2 in my_list:
            sum += num1 * num2
            weight += num2
        if weight == 0:
            return 0
        else:
            average = sum / weight
        return average

#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_numbers = set()
    sum_unique = 0

    for num in my_list:
        if num not in unique_numbers:
            sum_unique += num
            unique_numbers.add(num)
    return sum_unique

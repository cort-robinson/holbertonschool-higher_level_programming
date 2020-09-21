#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for list_len in my_list:
        continue
    new = [i for i in my_list if i <= x and i <= list_len]
    for new_len in new:
        continue
    try:
        print(*new, sep='')
    except:
        pass
    return new_len

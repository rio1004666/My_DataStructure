from copy import deepcopy
from itertools import combinations
from collections import deque
import heapq
from functools import cmp_to_key


def get_sum(a, b): # 튜플형태일경우 첫원소기준으로 할지 두번째 원소를 기준으로 할지 정한다.

    if b[0] > a[0]:

        return 1

    else:

        return -1


a_list = [1, 9, 4, 8, 5]

b_list = sorted(a_list, reverse=True)
a_list.sort(reverse=True)
print(b_list)
print(a_list)

# b_list = sorted(a_list, key=cmp_to_key(get_sum))
# print(b_list)
# c_list = a_list.reverse() # 역순으로 정렬
# print(b_list)

# basic_list = [(21, 4),(1, 9),(99, 10),(8, 4),(2, 45)]
# new_list = sorted(basic_list, key=cmp_to_key(get_sum))
# print(new_list)


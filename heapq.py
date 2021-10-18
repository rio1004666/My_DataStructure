import collections
import heapq

"""
이진트리 기반의 최소 힙 자료구조를 사용할 수 있다. 
만약 자료구조를 정렬된 상태로 유지할 필요가 있을 경우 
계속해서 정렬을 하는 것 보다는, heapify하는 것이 효율적이다.
"""
# import heapq
# heap = []
# heapq.heappush(heap, 4)
# heapq.heappush(heap, 6)
# print(heap)
#
#
# # 우선순위큐를 활용한 다익스트라 알고리즘
#
#
# def solution(n, s, a, b, fares):
#     graph = collections.defaultdict(list)
#     graph2 = [[] for _ in range(n + 1)]
#     for src, dst, cost in fares:
#         graph[src] += [(dst, cost)]
#         graph[dst] += [(src, cost)]
#     for src, dst, cost in fares:
#         graph2[src].append((dst, cost))
#         graph2[dst].append((src, cost))
#     print(graph)
#     print(graph2)
#
#
# fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
# solution(6, 4, 6, 2, fares)

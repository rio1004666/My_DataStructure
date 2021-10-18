
# 파이썬의 강력한 리스트 기능 특정인덱스에 접근해서
# pop할수있음
import collections
from typing import List, Deque


class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
def isPalindrome(head : ListNode) -> bool:
    q: List = []
    if not head: # 맨처음 노드가 없다면 그냥 팰린드롬이라고 판정
        return True
    node = head
    while node is not None: # node를 빼서 빌때까지 계속뺀다,
        q.append(node.val) # 연결리스트 노드에 있는 값만 빼서 리스트에 넣는다.
        node - node.next # 그다음 노드를 가리키는 노드를 다시 가리킨다.
    # 팰린드롬 판별

    while len(q) > 1:
        if q.pop(0) != q.pop(): # 하지만 성능 저하다
            return False
    return True

def isPalindrome(head: ListNode) -> bool:
    q: Deque = collections.deque() # 데크를 활용하여 첫원소 pop시간복잡도를 1로한다.
    if not head:
        return True

    node = head
    while node is not None:
        q.append(node.val)
        node = node.next
    while len(q) > 1:
        if q.popleft() != q.pop():
            return False
    return True
def isPalindrome2(head: ListNode) -> bool:
    rev = None
    fast,slow = head,head
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow,rev, slow.next

    if fast:
        slow = slow.next
    while rev and slow and rev.val == slow.val:
        rev, slow = rev.next, slow.next
    return not rev

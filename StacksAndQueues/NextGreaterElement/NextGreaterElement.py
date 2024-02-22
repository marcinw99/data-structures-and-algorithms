from collections import deque
from typing import List


def next_greater_element_brute(nums1: List[int], nums2: List[int]) -> List[int]:
    answer = [-1] * len(nums1)

    for i in range(len(nums1)):
        temp = deque(nums2)
        while temp and temp[0] != nums1[i]:
            temp.popleft()
        if temp and len(temp) > 2:
            answer[i] = temp[1]

    return answer


def next_greater_element_hashmap_stack(nums1: List[int], nums2: List[int]) -> List[int]:
    hashmap = {}

    stack = []
    for num in nums2:
        while stack and stack[-1] < num:
            popped = stack.pop()
            hashmap[popped] = num
        stack.append(num)

    answer = [-1] * len(nums1)
    for i in range(len(nums1)):
        answer[i] = hashmap[nums1[i]] if nums1[i] in hashmap else -1

    return answer


def next_greater_element_hashmap_stack_cleaner(nums1: List[int], nums2: List[int]) -> List[int]:
    hashmap = {}

    stack = []
    for num in nums2:
        while stack and stack[-1] < num:
            popped = stack.pop()
            hashmap[popped] = num
        stack.append(num)

    while stack:
        hashmap[stack.pop()] = -1

    answer = [-1] * len(nums1)
    for i in range(len(nums1)):
        answer[i] = hashmap[nums1[i]]

    return answer


print(next_greater_element_hashmap_stack_cleaner([4, 1, 2], [1, 3, 4, 2]))  # -1, 3, -1
print(next_greater_element_hashmap_stack_cleaner([4, 1, 2], [1, 3, 4, 2, 5, 11, 0]))  # 5, 3, 5
print(next_greater_element_hashmap_stack_cleaner([2, 4], [1, 2, 3, 4]))  # 3, -1

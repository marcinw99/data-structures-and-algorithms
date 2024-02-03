from collections import defaultdict
from typing import List


def numberOfSubarrays(nums: List[int], k: int) -> int:
    counts = defaultdict(int)
    counts[0] = 1
    ans = curr = 0

    for num in nums:
        curr += num % 2
        print(curr, counts[curr - k])
        ans += counts[curr - k]
        counts[curr] += 1

    return ans


print(numberOfSubarrays([1, 1, 2, 1, 1], 3))

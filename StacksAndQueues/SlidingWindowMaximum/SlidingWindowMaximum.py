def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
    answer = [0] * (len(nums) - 2)
    window = [0] * k

    for i in range(k):
        window[i] = nums[i]

    answer[0] = max(window)

    for i in range(len(nums) - 3):
        window.remove(nums[i])
        window.append(nums[i + 3])
        answer[i + 1] = max(window)

    return answer


print(sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3))  # [3, 3, 5, 5, 6, 7]

# real challenge is to do this in O(n)

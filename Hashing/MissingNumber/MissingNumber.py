# copy-paste żeby zrozumieć jak to kurwa działa
def missingNumber(nums):
    missing = len(nums)
    for i, num in enumerate(nums):
        print(missing, i, num)
        operation = i ^ num
        missing ^= operation
    return missing


print(missingNumber([3, 0, 1]))
# print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))

def sort(nums , a):
    for x in nums:
        if x == a:
            return True
    return False
nums = [5, 3, 8, 6, 7, 2]
print(sort(nums , 18))

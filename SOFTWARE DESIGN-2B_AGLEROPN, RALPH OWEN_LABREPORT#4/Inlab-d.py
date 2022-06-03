def maxmin(nums,a):
    if a == 1:
        return nums[0],nums[0]
    else:
        b, c = maxmin(nums, a - 1)
        return nums[a - 1] if (nums[a - 1] > b) else b, \
               nums[a - 1] if (nums[a - 1] < c) else c

nums=[1 ,2 ,3 , 4, 5 ,6 ,7, 8, 9, 10]
m,a=maxmin(nums, 9)
print(m,a)

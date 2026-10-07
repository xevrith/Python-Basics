# #### FIND 33: 

def has_33(nums):
    if 3 in nums:
        if nums[nums.index(3) + 1] == 3 or nums[nums.index(3) - 1] == 3:
            print(True)
        else:
            print(False)
    else:
        print(False)




has_33([1, 3, 3])
has_33([1, 3, 1, 3])
has_33([5,6,7,8])
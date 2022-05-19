def threeSumClosest(nums, target):
    nums.sort()
    prev_diff = 10000
    for i in range(len(nums)):
        a = i
        b = i+1
        c = len(nums)-1
        while b<c:
            threeSum = nums[a]+nums[b]+nums[c]
            print(nums[a],nums[b],nums[c])
            cur_diff = abs(threeSum-target)
            print(threeSum, cur_diff, prev_diff)
            if cur_diff<prev_diff:
                prev_diff = cur_diff
                res = threeSum
                print(res)
            if target>threeSum:
                b+=1
            if target<threeSum:
                c-=1
            if target==threeSum:
                return res



    return res




nums = [1,2,5,10,11]
target = 12
print(threeSumClosest(nums, target))
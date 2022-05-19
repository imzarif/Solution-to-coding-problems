def houseRobber(nums):
    rob1, rob2 = 0,0
    for n in nums:
        temp = max(rob1+n,rob2)
        rob1=rob2
        rob2=temp
    return rob2
nums = [6,3,10,8,2,10,3,5,10,5,3]
print(houseRobber(nums))
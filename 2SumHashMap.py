def twoSum(nums, target):
    hash_map = {}
    for i in range(len(nums)):
        to_find = target-nums[i]
        if to_find not in hash_map:
            hash_map[nums[i]] = i
            print(hash_map[nums[i]])
        else:
            return hash_map[to_find],i
nums = [3,3]
target = 6
print(twoSum(nums,target))
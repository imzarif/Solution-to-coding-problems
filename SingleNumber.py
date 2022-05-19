def singleNumber(nums):
    hash_map = {}
    for i in nums:
        if i in hash_map:
            hash_map[i] = 2
        else:
            hash_map[i] = 1

    hash_map_keys = list(hash_map.keys())
    hash_map_vals = list(hash_map.values())
    return hash_map_keys[hash_map_vals.index(min(hash_map_vals))]

nums = [4,1,2,1,2]
print(singleNumber(nums))
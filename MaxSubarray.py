def MaxSubarray(nums):
    prefix = 0
    result =[]
    i=0
    j=0
    while j<len(nums):
        if i==j:
            prefix=nums[i]
        else:
            prefix += nums[j]
        result.append(prefix)
        if prefix<0:
            j+=1
            i=j
            #prefix=0
            continue
        if prefix>=0:
            j+=1
    print(result)
    return max(result)

nums = [-1]
print(MaxSubarray(nums))
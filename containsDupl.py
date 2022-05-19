def ContainsDup(nums):
    hashset = set()
    for n in nums:
        if n in hashset:
            return True
        else:
            hashset.add(n)
    return False


    #nums.sort()
    #i,j = 0,1
    #while j<len(nums):
     #   if nums[i]==nums[j]:
      #      return True
       # i+=1
        #j+=1
    #return False

nums = [1,2,3,4]
print(ContainsDup(nums))











































































































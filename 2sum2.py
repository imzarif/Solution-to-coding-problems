def twosumtwo(numbers, target):
    i=0
    j=len(numbers)-1
    while i<j:
        if numbers[i] +numbers[j]>target:
            j-=1
        if numbers[i] + numbers[j]<target:
            i+=1
        if numbers[i]+numbers[j]==target:
            return i+1, j+1


  #  hashmap = {}
   # for i in range(len(numbers)):
    #    to_find = target - numbers[i]
     #   if to_find in hashmap:
      #      return hashmap[to_find]+1, i+1
       # else:
        #    hashmap[numbers[i]] = i

numbers = [2,3,4]
target = 6
print(twosumtwo(numbers, target))

def firstUniqChar(s):
    freq = [0]*26
    for i in s:
        freq[ord(i)-ord("a")]+=1
    for i in s:
        if freq[ord(i)-ord("a")]==1:
            return s.index(i)
    return -1

s = "loveleetcode"
print(firstUniqChar(s))


    #count = {}
    #keys=[]
    #values=[]
    #for i in s:
    #   if i not in count:
     #       count[i]=1
     #   else:
      #      count[i]+=1
   # key_list = list(count.keys())
    #value_list = list(count.values())
   # min_value = min(value_list)
   # index_of_min_value = value_list.index(min_value)
    #min_key = key_list[index_of_min_value]
    #first_uniqe = s.index(min_key)

 #   if min_value==1:
  #      return first_uniqe
   # else:
    #    return -1



   # cs = ""
   # check = set()
   # for i in range(0,len(s)):
   #     for j in range(i+1,len(s)):
   #         if s[i]==s[j]:
   #             check.add(s[i])
    #            break
    #for i in range(len(s)):
    #    if s[i] not in check:
     #       cs+=s[i]
    #if cs=="":
    #    return -1
    #return s.index(cs[0])

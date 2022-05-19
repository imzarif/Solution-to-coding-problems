def LenLastWord(s):
    count = 0
    space_count = 0
    for i in range(len(s)-1,-1,-1):
        if s[i]!=" ":
            count+=1
            space_count=1


        else:
            if space_count==1 and count!=0:
                return count
            space_count = 1
    return count

s = "a"
print(LenLastWord(s))
def reverseString(s):
    i = 0
    j = len(s)-1
    while i<j:
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
        i+=1
        j-=1
    return s

s = ["H","a","n","n","a","h"]
print(reverseString(s))

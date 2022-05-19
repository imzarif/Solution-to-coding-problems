def isPalindrome(s):
    s1 = ""
    s2 = ""
    count = 0
    while count<len(s):
        if (ord(s[count])>=48 and ord(s[count])<=57) or (ord(s[count])>=65 and ord(s[count])<=122):
            if ord(s[count])<=90 or ord(s[count])>=97:
                s1 += s[count].lower()
        count+=1
    print(s1)
    anti_count = len(s1)-1
    while anti_count>=0:
        s2 += s1[anti_count]
        anti_count-=1
    print(s2)
    if s1==s2:
        return True
    else:
        return False

s = "A man, a plan, a canal: Panama"
print(isPalindrome("0P"))


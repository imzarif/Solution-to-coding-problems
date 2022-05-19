def LPS(s):
    def palchekcer(ss):
        l=0
        r=len(ss)-1
        while l<r:
            if ss[l]==ss[r]:
                l+=1
                r-=1
            else:
                return False
        return True

    def palcheckertwo(ss): #more efficient
        if ss==ss[::-1]:
            return True
        else:
            return False
    palLength = []
    l=0
    r=len(s)-1
    max, min = 0,0
    while l<len(s):
        while l<r:
            if s[l]==s[r]:
                b = palcheckertwo(s[l:r+1])
                if b==True:
                    if max-min<r-l:
                        max, min = r, l
                        break
            r-=1
        l+=1
        r=len(s)-1
        if max-min>r-l:
            break

    return s[min:max+1]





s = "caccbbccd"
print(LPS(s))

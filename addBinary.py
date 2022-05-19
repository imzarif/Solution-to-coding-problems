def addBinary(s1,s2):
    result = ""
    carry = 0
    if len(s1)>len(s2):
        s2 = "0" * (len(s1) - len(s2)) + s2
    elif len(s2)>len(s1):
        s1= "0" * (len(s2) - len(s1)) + s1

    for i in range(len(s1)-1, -1, -1):
        if s1[i]=="1" and s2[i]=="1":
            if carry == "1":
                result = "1"+result
            else:
                result = "0"+result
            carry = "1"

        elif s1[i]=="0" and s2[i]=="0":
            if carry == "1":
                result = "1" + result
            else:
                result = "0" + result
            carry = "0"
        else:
            if carry == "1":
                result = "0" + result
                carry = "1"

            else:
                result = "1"+result
                carry = "0"
        if i==0 and carry=="1":
           result = carry+result


    return result


s1 = "1010"
s2 = "1011"
print(addBinary(s1,s2))

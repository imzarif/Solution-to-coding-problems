def PlusOne(digits):
    #if digits[len(digits)-1]<9:
     #   digits[len(digits)-1]+=1
      #  return digits
    #else:
        for n in range(len(digits)-1,-1,-1):
            if digits[n]==9:
                digits[n]=0
                if n==0:
                    digits.append(digits[n])
                    digits[n]=1
                    return digits
            else:
                digits[n]+=1
                return digits




print(PlusOne([9,9]))
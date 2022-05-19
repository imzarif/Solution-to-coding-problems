def leterCombination(digits):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    output = []
    list_of_strings = []
    for d in digits:
        first_part = (int(d)-2)*3
        if int(d)==8 or int(d)==9:
            first_part+=1
        second_part = first_part+3
        if int(d)==7 or int(d)==9:
            second_part+=1
        list_of_strings.append(alphabets[first_part:second_part])

    string_count = 0
    i=0
    j=0
    t_str = ""
    if len(list_of_strings)>=1:
        for i in list_of_strings[0]:
            if len(list_of_strings)>=2:
                for j in list_of_strings[1]:
                    if len(list_of_strings)>=3:
                        for k in list_of_strings[2]:
                            if len(list_of_strings)==4:
                                for l in list_of_strings[3]:
                                    output.append(i+j+k+l)
                            else:
                                output.append(i+j+k)
                    else:
                        output.append(i+j)
            else:
                output.append(i)



    return output

print(leterCombination(""))

def numberPlate(plate):
    plate = plate+"#"
    seperator = "-"
    p = 0
    counter = 0
    sub_counter = 0
    while p<len(plate):
        if plate[p]==seperator:
            counter+=1
        if counter==0 and 32<=ord(plate[p])<=41:
            return "Invalid"

        if counter==1:
            p+=1
            while plate[p]!=seperator:
                p+=1
                sub_counter+=1
            if sub_counter!=2:
                return "Invalid"
            counter+=1
        if counter==2:
            p+=1
            sub_counter=0
            while plate[p] != "#":
                p += 1
                sub_counter += 1
            if sub_counter != 4:
                return "Invalid"
        p+=1

    return "Valid"


s = "Kha-23-6789"

print(numberPlate(s))















































































































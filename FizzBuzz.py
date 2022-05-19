def fizzBuzz(n):
    i=1
    answer = []
    while i<=n:
        if i%3==0 and i%5==0:
            answer.append("FizzBuzz")
            i+=1
            continue
        elif i%3==0:
            answer.append("Fizz")
            i+=1
            continue
        elif i%5==0:
            answer.append("Buzz")
            i+=1
            continue
        else:
            answer.append(str(i))
            i+=1

    return answer

print(fizzBuzz(15))
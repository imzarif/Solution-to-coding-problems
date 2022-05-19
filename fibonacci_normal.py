def fib(n):
    count = 1
    p=0
    if n==0:
        return 0
    for i in range(1,n):
        temp = count
        count += p
        p=temp
    return count



print(fib(9))

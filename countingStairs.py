def countingStairs(n):
    num = 0
    memo = {}
    def recurse(num):
        if num in memo:
            return memo[num]
        if num==n:
            return 1
        if num>n:
            return 0
        if num<n:
            result = recurse(num+1)+recurse(num+2)
            memo[num] = result
            return result
    result = recurse(num)
    return result
print(countingStairs(20))
def climbingStairs(n):
    s = 0
    sol_sub = {}
    def recurse(s):
        if s in sol_sub:
            return sol_sub[s]
        if s==n:
            return 1
        if s>n:
            return 0
        result = recurse(s+1) + recurse(s+2)
        sol_sub[s] = result
        return result
    print(recurse(s))


n = 2
climbingStairs(n)
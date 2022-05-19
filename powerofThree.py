def powerofThree(n):
    answer = 1
    while answer<=n:
        if answer==n:
            return True
        answer = 3 * answer

    return False

print(powerofThree(1))
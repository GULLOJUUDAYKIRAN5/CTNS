def rec(n):
    if n==0:
        return
    else:
        print(n)
        rec(n-1)
rec(5)

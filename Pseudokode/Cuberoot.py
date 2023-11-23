def find_cube_root(X):
    ans = 0
    while ans ** 3 < abs(X):
        ans += 1
    if ans ** 3 == abs(X):
        print(X, "is not a perfect cube")
        ans = None
    else:
        if X < 0:
            ans = -ans
    return ans
def FindRoot(x,epsilon):
    r = x
    while abs(x-r*r) > epsilon:
        r = (r + x/r)/2
    return r
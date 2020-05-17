def binary_search(x, v):
    e = -1
    d = len(v)
    while e < d - 1:
        m = (e + d) // 2
        if v[m] < x:
            e = m
        else:
            d = m
    return d
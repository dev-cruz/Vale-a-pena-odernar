def selection(array):
    v = array.copy()
    r = []
    while len(v) > 0:
        m = min(v)
        r.append(m)
        v.remove(m)
    return r
def quicksort(v):
    if len(v) <= 1: return v

    pivot = v[0]
    equals = [x for x in v if x == pivot]
    less = [x for x in v if x < pivot]
    bigger = [x for x in v if x > pivot]
    return quicksort(less) + equals + quicksort(bigger)
def sum_tail(a, accumulator=0):
    if a == 0:
        return accumulator
    return sum_tail(a - 1, accumulator + a)
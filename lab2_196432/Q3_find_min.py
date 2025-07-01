def find_min(list):
    if len(list) == 0:
        return None
    min_val = list[0]
    for i in range(1, len(list)):
        if list[i] < min_val:
            min_val = list[i]
    return min_val
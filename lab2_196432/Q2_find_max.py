def find_max(list):
    if len(list) == 0:
        return None
    max_val = list[0]
    for i in range(1, len(list)):
        if list[i] > max_val:
            max_val = list[i]
    return max_val
def rotate_list(lst, a):
    a = a % len(lst) 
    return lst[-a:] + lst[:-a]
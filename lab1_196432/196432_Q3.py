def countdown_head(a):
    if a < 0:
        return
    print(a)
    countdown_head(a - 1)

def endless_counter(value=float('inf')):
    idx = 0
    while idx <= value:
        print(idx, end=', ' if idx != value else '.')
        idx += 1


endless_counter(100)

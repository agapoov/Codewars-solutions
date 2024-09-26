def last_digit(n1, n2):
    if n1 and n2 == 0:
        return 1
    i = 1
    lst = []
    while True:
        num = (n1**i) % 10
        if num in lst:
            break
        else:
            lst.append(num)
            i += 1

    cycle_len = len(lst)
    index = (n2-1) % cycle_len

    return lst[index]

lister = [18, 110, 32, 14, 80, 83, 22, 64, 69, 11]

#lister = [random.randint(1, 1_000_000) for x in range(5000)]


def bubblesort(lst):
    is_sorted = False
    n = 1
    while is_sorted is False:
        is_sorted = True
        for i in range(len(lst) - n):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                is_sorted = False
        n += 1
    return lst


print(bubblesort(lister))

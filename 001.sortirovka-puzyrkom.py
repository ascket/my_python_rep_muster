# На массивах до 1000 элементов работает довольно быстро, а на маленьких массивах до 5 элементов очень быстро (быстрее некоторых сложных алгоритмов)

lister = [18, 29, 24, 31, 23, 96, 17, 74, 37, 37]


def sorter_puz(l):
    count = 1
    while count < len(l):
        for x in range(len(l) - count):
            if l[x] > l[x + 1]:
                l[x], l[x + 1] = l[x + 1], l[x]
        count += 1

    return l


print(sorter_puz(lister))

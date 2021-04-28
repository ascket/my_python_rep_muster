lister = [15, 29, 40, 20, 40, 47, 65, 33, 27, 59]


def linear_search(lst, item):
    find_list = []
    count = 0
    while count < len(lst):
        if lst[count] == item:
            find_list.append(count)
        count += 1
    if find_list:
        return find_list
    return -1


#print(line_search(lister, 59))

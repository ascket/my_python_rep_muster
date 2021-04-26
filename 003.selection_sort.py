# Finds the smallest value in an array


def smallestIndex(item):
    smallest_index = 0
    smallest = item[0]
    for x in range(1, len(item)):
        if item[x] < smallest:
            smallest_index = x
            smallest = item[x]
    return smallest_index


def sorter(item):
    newLister = []
    for x in range(len(item)):
        smallest_index = smallestIndex(item)
        newLister.append(item.pop(smallest_index))
    return newLister


lister = [34, 1, 4, 3, 2, 5, -6, 77, 4, 0]
print(sorter(lister))


# Binary search


def binary_search(item, number):
    low = 0
    high = len(item) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = item[mid]
        if guess == number:
            return mid
        if guess < number:
            low = mid + 1
        else:
            high = mid - 1
    return None

def binar_search(item, number):
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


lister = [1, 1, 2, 3, 5, 6, 7, 8, 67, 555]
print(binar_search(lister, 67))

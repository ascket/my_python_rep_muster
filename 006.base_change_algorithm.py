def base10(number, base):
    if base < 2:
        raise ValueError("Base must be >= 2")
    if number < 0:
        raise ValueError("Number must be positive integer")
    if number == 0:
        return [0]
    digits = []
    while number > 0:
        #mod = number % base
        #number = number // base
        number, mod = divmod(number, base)
        digits.insert(0, mod)
    return digits


def encodic(digits, digits_base):
    if max(digits) >= len(digits_base):
        raise ValueError("Base has not enough symbols")
    return "".join([digits_base[x] for x in digits])
    # encoder = ""
    # for x in digits:
    #     encoder += digits_base[x]
    # return encoder


def rebase_from10(number, base):
    digits_map = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if base < 2 or base > 36:
        raise ValueError("Base must be >= 2 and <= 36")
    sign = -1 if number < 0 else 1
    number *= sign
    digits = base10(number, base)
    encoding = encodic(digits, digits_map)
    if sign == -1:
        encoding = "-" + encoding
    return encoding


e = rebase_from10(10, 2)
print(e)
print(0b1010)

def tri_area(base, height):
    return (base * height) / 2


# -------------------------------------------------------------------------------------
def grade_percentage(user_score, pass_score):
    s = ''
    if int(user_score[:-1]) < int(pass_score[:-1]):
        s += 'FAILED'
    else:
        s += 'PASSED'
    return 'You' + ' ' + s + ' ' + 'the Exam'


# -------------------------------------------------------------------------------------
def XO(txt):
    xs = 0
    os = 0
    for i in range(0, len(txt)):
        if txt[i] == 'x' or txt[i] == 'X':
            xs += 1
        elif txt[i] == 'o' or txt[i] == 'O':
            os += 1
    return xs == os


# REFACTORED
def x_o(txt):
    os = txt.count('o') + txt.count('O')
    xs = txt.count('x') + txt.count('X')
    return os == xs


# -------------------------------------------------------------------------------------

def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact


# -------------------------------------------------------------------------------------


def unique_sort(lst):
    bucket = []
    for element in lst:
        if element not in bucket:
            bucket.append(element)
    return sorted(bucket)


# print(unique_sort([1, 2, 4, 3]))
# print(unique_sort([1, 4, 4, 4, 4, 4, 3, 2, 1, 2]))
# -------------------------------------------------------------------------------------


def setify(lst):
    new_set = set(lst)
    unique_lst = list(new_set)
    return sorted(unique_lst)


# -------------------------------------------------------------------------------------


def reverse(arg):
    if arg is True and isinstance(arg, bool):
        return False
    elif arg is False and isinstance(arg, bool):
        return True
    else:
        return "boolean expected"


# print(reverse(True))
# print(reverse(False))
# print(reverse(0))
# print(reverse(None))
# -------------------------------------------------------------------------------------

def average(lst):
    bucket = 0
    for num in lst:
        bucket += num
    total = bucket / len(lst)
    return int(total)


# print(average([1, 2, 3]))
# print(average([34, 65, 12]))
# print(average([13, 13, 13]))
# print(average([5, 2, 3, 4, 1]))
# -------------------------------------------------------------------------------------


def counterpartCharCode(char):
    swapped = char.swapcase()
    return ord(swapped)


# -------------------------------------------------------------------------------------


import math
import datetime


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

def next_in_line(lst, num):
    if len(lst) >=1:
        lst.append(num)
        lst.pop(0)
        return lst
    else:
        return "No list has been selected"


# print(next_in_line([5, 6, 7, 8, 9], 1))
# print(next_in_line([7, 6, 3, 23, 17], 10))

# -------------------------------------------------------------------------------------


def to_degree(radian):
    return math.ceil(radian * (180/math.pi))


# -------------------------------------------------------------------------------------


def profit_margin(cost_price, sales_price):
    percentage = 100 - ((cost_price / sales_price) * 100)
    rounded = round(percentage, 1)
    return str(rounded) + "%"


# print(profit_margin(50, 50))
# print(profit_margin(28, 39))
# print(profit_margin(33, 84))
# -------------------------------------------------------------------------------------

def name_shuffle(txt):
    lst = txt.split()
    return lst[1] + " " + lst[0]

# -------------------------------------------------------------------------------------


def time_for_milk_and_cookies(date):
    return date.day == 24 and date.month == 12


# -------------------------------------------------------------------------------------


def length(txt):
    if txt == "":
        return 0
    else:
        return 1 + length(txt[1:])


# -------------------------------------------------------------------------------------


def alphabet_soup(txt):
    lst = [letter for letter in txt]
    return ''.join(sorted(lst))


# -------------------------------------------------------------------------------------


def binary(decimal):
    binary_str = bin(decimal)
    return binary_str[2:]


# -------------------------------------------------------------------------------------


def triangle(n):
    return (n * (n + 1)) / 2


# -------------------------------------------------------------------------------------
# correct_signs("3 < 7 < 11") ➞ True
# correct_signs("13 > 44 > 33 > 1") ➞ False
# correct_signs("1 < 2 < 6 < 9 > 3") ➞ True


def correct_signs(txt):
    return eval(txt)


# -------------------------------------------------------------------------------------


def abcmath(a, b, c):
    for i in range(0, b+1):
        a += a
    return a % c == 0


# -------------------------------------------------------------------------------------


def count_ones(num):
    num_str = bin(num)
    counter = 0
    for char in num_str:
        if char == '1':
            counter += 1
    return counter


# -------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------

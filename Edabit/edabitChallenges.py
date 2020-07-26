import math
import datetime
import string


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


def is_vowel_sandwich(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if len(s) != 3:
        return False
    else:
        if s[1] in vowels and s[0] not in vowels and s[2] not in vowels:
            return True
        else:
            return False


# print(is_vowel_sandwich("cat"))  # ➞ True
# print(is_vowel_sandwich("ear"))  # ➞ False
# print(is_vowel_sandwich("bake"))  # ➞ False
# print(is_vowel_sandwich("try"))  # ➞ False
# -------------------------------------------------------------------------------------


def how_many_times(msg):
    bucket = 0
    letters = string.ascii_lowercase
    for character in msg:
        for i in range(0, len(letters)):
            if character == letters[i]:
                bucket += (i + 1)
    return bucket


# -------------------------------------------------------------------------------------


def halve_count(a, b):
    count = 0
    while (a/2) > b:
        a /= 2
        count += 1
    return count


# -------------------------------------------------------------------------------------


def equal(a, b, c):
    count = 0
    if a == b or a == c:
        count += 2
        if b == c:
            count += 1
    elif b == c:
        count += 2
    return count


# -------------------------------------------------------------------------------------


def count_vowels(txt):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for letter in txt:
        if letter in vowels:
            count += 1
    return count


# -------------------------------------------------------------------------------------


def index_of_caps(word):
    bucket = []
    for i in range(0, len(word)):
        if word[i].isupper():
            bucket.append(i)
    return bucket


# -------------------------------------------------------------------------------------


# import math

def cone_volume(h, r):
    volume = (math.pi * r**2 * h)/3
    return round(volume, 2)


# -------------------------------------------------------------------------------------


def alphanumeric_restriction(s):
    return s.isnumeric() or s.isalpha()


# -------------------------------------------------------------------------------------


def letter_counter(lst, letter):
    count = 0
    for partial_list in lst:
        for character in partial_list:
            if letter == character:
                count += 1
    return count


# -------------------------------------------------------------------------------------


def doubled_pay(n):
    total_pennies = 0
    base_pay = 1
    for i in range(1, n+1):
        if i == 1:
            total_pennies += 1
        if i > 1:
            base_pay *= 2
            total_pennies += base_pay
    return total_pennies


# print(doubled_pay(1))
# print(doubled_pay(2))
# print(doubled_pay(3))
# print(doubled_pay(4))
# print(doubled_pay(5))
# -------------------------------------------------------------------------------------


def filter_list(lst):
    bucket = []
    for element in lst:
        if isinstance(element, int):
            bucket.append(element)
    return bucket


# -------------------------------------------------------------------------------------


def get_student_names(students):
    value_lst = students.values()
    return sorted(value_lst)


# -------------------------------------------------------------------------------------


def is_symmetrical(num):
    str_num = str(num)
    reversed_num = reversed(str_num)
    return str_num == reversed_num


# -------------------------------------------------------------------------------------


# str,int=int,str #de-drunk
def int_to_str(num):
    return str(num)


def str_to_int(num):
    return int(num)


# -------------------------------------------------------------------------------------
# Write a function that removes any non-letters from a string, returning a well-known film title.


def letters_only(txt):
    bucket = []
    for letter in txt:
        if letter.isalpha():
            bucket.append(letter)
    return ''.join(bucket)


# -------------------------------------------------------------------------------------

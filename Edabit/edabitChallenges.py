def tri_area(base, height):
    return (base * height)/2


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
    for i in range(1, num+1):
        fact = fact * i
    return fact

# -------------------------------------------------------------------------------------


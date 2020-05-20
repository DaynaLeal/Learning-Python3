# into to booleans
# note that True and False must be capital
# these are called type bool
# you can check type by using type()
my_baby_bool = "true"
print(type(my_baby_bool))  # returns <class 'str'>

my_baby_bool_two = True
print(type(my_baby_bool_two))  # returns <class 'bool'>
# ------------------------------------------------------------------------------

# intro to conditionals
if True:
    "code"

# example to lock dave out of your computer (he sometimes uses angelas login


def dave_check(user_name):
    if user_name == "Dave":
        return "Get off my computer Dave!"
    if user_name == "angela_catlady_87":
        return "I know it is you Dave! Go away!"


# Enter a user name here, make sure to make it a string
user = "angela_catlady_87"

print(dave_check(user))
# ------------------------------------------------------------------------------


def greater_than(x, y):
    if x > y:
        return x
    if x < y:
        return y
    if x == y:
        return "These numbers are the same"


# determine if student has enough credits to graduate


def graduation_reqs(credits):
    if credits >= 120:
        return "You have enough credits to graduate!"


print(graduation_reqs(120))
# ------------------------------------------------------------------------------

# update to the graduation_reqs() function to add logical operator "and"
# also can use "or" or "not"


def graduation_reqs(gpa, credits):
    if credits >= 120 and gpa >= 2.0:
        return "You meet the requirements to graduate!"


# ------------------------------------------------------------------------------

# or operator to update, if one of requirements is met, then mail is sent


def graduation_mailer(gpa, credits):
    if gpa >= 2.0 or credits >= 120:
        return True


# ------------------------------------------------------------------------------

# not operator (must go at front of condition) on the grad req function again

def grad_reqs(gpa, credits):
    if (gpa >= 2.0) and (credits >= 120):
        return "You meet the requirements to graduate!"
    if(gpa >= 2.0) and (not credits >= 120):
        return "You do not have enough credits to graduate."
    if(not gpa >= 2.0) and (credits >= 120):
        return "Your GPA is not high enough to graduate."
    if (not gpa >= 2.0) and (not credits >= 120):
        return "You do not meet either requirement to graduate!"


# ------------------------------------------------------------------------------

# else statement very similar
def grad_req(gpa, credits):
    if (gpa >= 2.0) and (credits >= 120):
        return "You meet the requirements to graduate!"
    if (gpa >= 2.0) and not (credits >= 120):
        return "You do not have enough credits to graduate."
    if not (gpa >= 2.0) and (credits >= 120):
        return "Your GPA is not high enough to graduate."
    else:
        return "You do not meet the GPA or the credit requirement for graduation."


# ------------------------------------------------------------------------------
# else if == "elif"
def grade_converter(gpa):
    if gpa >= 4.0:
        grade = "A"
    elif gpa >= 3.0:
        grade = "B"
    elif gpa >= 2.0:
        grade = "C"
    elif gpa >= 1.0:
        grade = "D"
    else:
        grade = "F"
    return grade


# ------------------------------------------------------------------------------
# Try and Except statements

# try:
#     # some statement
# except ErrorName:
#     # some statement

def divides(a, b):
    try:
        result = a / b
        print(result)
    except ZeroDivisionError:
        print("Can't divide by zero!")

# another example


def raises_value_error():
    raise ValueError


try:
    raises_value_error()
except ValueError:
    print("You raised a ValueError!")

# ------------------------------------------------------------------------------
# REVIEW


def applicant_selector(gpa, ps_score, ec_count):
    if gpa >= 3.0 and ps_score >= 90 and ec_count >= 3:
        return "This applicant should be accepted."
    elif gpa >= 3.0 and ps_score >= 90 and not ec_count >= 3:
        return "This applicant should be given an in-person interview."
    else:
        return "This applicant should be rejected."

train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1


def f_to_c(f_temp):
    c_temp = (f_temp - 32)*(5/9)
    return c_temp


f100_in_celsius = f_to_c(100)


def c_to_f(c_temp):
    f_temp = (c_temp*(9/5)) + 32
    return f_temp


c0_in_fahrenheit = c_to_f(0)


def get_force(mass, acceleration):
    return mass*acceleration


train_force = get_force(train_mass, train_acceleration)

print(train_force)
print("The GE train supplies " + str(train_force) + " Newtoms of force.")


def get_energy(mass, c=(3*10**8)):
    return mass*(c**2)


bomb_energy = get_energy(bomb_mass)

print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")


def get_work(mass, acceleration, distance):
    return get_force(mass, acceleration) * distance


train_work = get_work(train_mass, train_acceleration, train_distance)

print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")

# -------------------------------------------------------------------------------------------
# FUNCTION CODE CHALLENGES

# Write a function named tenth_power() that has one parameter named num.
# The function should return num raised to the 10th power.
# Write your tenth_power function here:


def tenth_power(num):
    return num**10


# Uncomment these function calls to test your tenth_power function:
print(tenth_power(1))
# 1 to the 10th power is 1
print(tenth_power(0))
# 0 to the 10th power is 0
print(tenth_power(2))
# 2 to the 10th power is 1024
# --------------------------------------------------------------------------

# Write a function named square_root() that has one parameter named num.
# Use exponents (**) to return the square root of num.
# Write your square_root function here:


def square_root(num):
    return num**(1/2)


# Uncomment these function calls to test your square_root function:
print(square_root(16))
# should print 4
print(square_root(100))
# should print 10
# --------------------------------------------------------------------------

# Create a function called win_percentage() that takes two parameters named wins and losses.
# This function should return out the total percentage of games won by a team based on these two numbers.
# Write your win_percentage function here:


def win_percentage(wins, losses):
    percentage = 100*(wins/(wins+losses))
    return percentage


# Uncomment these function calls to test your win_percentage function:
print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100
# --------------------------------------------------------------------------

# Write a function named average() that has two parameters named num1 and num2.
# The function should return the average of these two numbers.
# Write your average function here:


def average(num1, num2):
    return (num1+num2)/2


# Uncomment these function calls to test your average function:
print(average(1, 100))
# The average of 1 and 100 is 50.5
print(average(1, -1))
# The average of 1 and -1 is 0
# --------------------------------------------------------------------------

# Write a function named remainder() that has two parameters named num1 and num2.
# The function should return the remainder of twice num1 divided by half of num2.
# Write your remainder function here:


def remainder(num1, num2):
    return (num1*2)%(num2/2)


# Uncomment these function calls to test your remainder function:
print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0
# ---------------------------------------------------------------------------------------------------------------

# ADVANCED PYTHON FUNCTIONS
# Write a function named first_three_multiples() that has one parameter named num.
# This function should print the first three multiples of num. Then, it should return the third multiple.
# Write your first_three_multiples function here


def first_three_multiples(num):
    print(num*1)
    print(num*2)
    print(num*3)
    return num*3


# Uncomment these function calls to test your first_three_multiples function:
first_three_multiples(10)
# should print 10, 20, 30, and return 30
first_three_multiples(0)
# should print 0, 0, 0, and return 0
# --------------------------------------------------------------------------

# Create a function called tip() that has two parameters named total and percentage.
# This function should return the amount you should tip given a total and the percentage you want to tip.
# Write your tip function here:


def tip(total, percentage):
    return total*(percentage*.01)


# Uncomment these function calls to test your tip function:
print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0
# --------------------------------------------------------------------------

# Write a function named introduction() that has two parameters named first_name and last_name.
# The function should return the last_name, followed by a comma, a space, first_name another space,
# and finally last_name.
# Write your introduction function here:


def introduction(first_name, last_name):
    return last_name + ", " + first_name + " " + last_name


# Uncomment these function calls to test your introduction function:
print(introduction("James", "Bond"))
# should print Bond, James Bond
print(introduction("Maya", "Angelou"))
# should print Angelou, Maya Angelou
# --------------------------------------------------------------------------

# Some say that every one year of a human’s life is equivalent to seven years of a dog’s life.
# Write a function named dog_years() that has two parameters named name and age.
# The function should compute the age in dog years and return the following string:
# "{name}, you are {age} years old in dog years"
# Write your dog_years function here:


def dog_years(name, age):
    return name + ", you are " + str(age * 7) + " years old in dog years"


# Uncomment these function calls to test your dog_years function:
print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"
print(dog_years("Dayna", 27))
# --------------------------------------------------------------------------

# Create a function named lots_of_math(). This function should have four parameters named a, b, c, and d.
# The function should print 3 lines and return 1 value.
# First, print the sum of a and b.
# Second, print d subtracted from c.
# Third, print the first number printed, multiplied by the second number printed.
# Finally, return the third number printed mod a.
# Write your lots_of_math function here:


def lots_of_math(a, b, c, d):
    added = (a+b)
    print(added)
    subtracted = (c-d)
    print(subtracted)
    multiplied = added*subtracted
    print(multiplied)
    return multiplied % a


# Uncomment these function calls to test your lots_of_math function:
print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0

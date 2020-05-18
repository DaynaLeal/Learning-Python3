# functions must start with 'def' have the colon, and indented code following colon
def greet_customer():
    print("Welcome to Engrossing Grocers.")
    print("Our special is mandarin oranges.")
    print("Have fun shopping!")


greet_customer()


# --------------------------------------------------------------
# you can still pass in parameters
def mult_two_add_three(number):
    print(number * 2 + 3)


mult_two_add_three(5)


# --------------------------------------------------------------
# you can use multiple parameters separated by commas (positional)
def mult_x_add_y(number, x, y):
    print(number*x + y)


mult_x_add_y(1, 3, 1)


# --------------------------------------------------------------
# in addition to positional arguments, you can make keyword arguments that specify which argument
# is to be matched with which parameter
mult_x_add_y(number=5, x=2, y=3)


# --------------------------------------------------------------
# we can also define the parameters this way when declaring a function to provide default values
# if you assign a default value with keyword first, then you cannot add a positional parameter second
# BUT you can assign a positional parameter first and a keyword parameter second
def hello_function(name="dayna"):
    print("Hello, " + name)


hello_function()  # prints hello dayna
hello_function("Marty")  # prints hello Marty


def create_spreadsheet(title, row_count=1000):
    print("Creating a spreadsheet called "+title + " with " + str(row_count) + " rows")


create_spreadsheet("Downloads")


# --------------------------------------------------------------
# Return
def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age


my_age = calculate_age(2049, 1993)
dads_age = calculate_age(2049, 1953)

print("I am " + str(my_age) + " years old and my dad is " + str(dads_age))


# --------------------------------------------------------------
# Multiple Return values can be separated with commas
def get_boundaries(target, margin):
    low_limit = target - margin
    high_limit = margin + target
    return low_limit, high_limit


low, high = get_boundaries(100, 20)  # this sets the two returned values to their own variables


# --------------------------------------------------------------
# Scope works the same as in other languages within and outside functions


# --------------------------------------------------------------
# Review
# multiplying a string creates multiples of that string


# A module is a collection of Python declarations intended broadly to be used as a tool.
# Modules are also often referred to as “libraries” or “packages” —
# a package is really a directory that holds a collection of modules.

# SYNTAX:
# from module_name import object_name
# Import datetime from datetime below:
from datetime import datetime

current_time = datetime.now()
print(current_time)

# -------------------------------------------------------------------------------------------

# Import random below:
import random

# Create random_list below:
random_list = [random.randint(1, 101) for i in range(101)]
# print(random_list)

# Create randomer_number below:
randomer_number = random.choice(random_list)


# Print randomer_number below:
print(randomer_number)

# -------------------------------------------------------------------------------------------

# import codecademylib3_seaborn
from matplotlib import pyplot as plt
# import random

# Add your code below:

numbers_a = range(1, 13)
numbers_b = random.sample(range(1000), 12)

plt.plot(numbers_a, numbers_b)

plt.show()

# -------------------------------------------------------------------------------------------

# Import Decimal below:
from decimal import Decimal

# Fix the floating point math below:
two_decimal_points = Decimal('0.2') + Decimal('0.69')
print(two_decimal_points)

four_decimal_points = Decimal('0.53') * Decimal('0.65')
print(four_decimal_points)

# -------------------------------------------------------------------------------------------
# how to import from another file
# from file named library


def always_three():
    return 3


# from different file
# Import library below:
from library import always_three

# Call your function below:
print(always_three())


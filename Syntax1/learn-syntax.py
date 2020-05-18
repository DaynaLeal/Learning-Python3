# lesson 1
my_name = "Dayna"
print("Hello, " + my_name + "!")  # instead of console.log() or system.out.println()

# -------------------------------------------------------------------------
# lesson 2 taught about commenting out with a hash
# like this

# -------------------------------------------------------------------------
# lesson 3 taught about print()
print("Hello world (in python)")

# -------------------------------------------------------------------------
# lesson 4 taught about how both single and double quotes are used interchangably like js
print("They're going home.")
print('He said "Hello"')

# -------------------------------------------------------------------------
# lesson 5 teaches about variable structure
# no characters other than underscore
# numbers cannot be at beginning
the_language = "Python"
print(the_language)
# now the_language can also be updated
the_language = "Python 3"
print(the_language)

# -------------------------------------------------------------------------
# lesson 6 discusses error types (uncomment to see)
# this is a SyntaxError (mismatch quote)
# print('This message has mismatched quote marks!")
# and this is a NameError (doesnt recognize undeclared variable name)
# print(Abracadabra)

# -------------------------------------------------------------------------
# lesson 7 is about numbers
an_int = 5  # integers are whole numbers
a_float = 5.5  # float values are decimal numbers
# not type cast like Java, more like js so the variable is assigned type based on what value is declared

# -------------------------------------------------------------------------
# lesson 8: Calculations
print(15 / 4)  # this converts integers to float answer

# -------------------------------------------------------------------------
# lesson 9: Using Variables as numbers
quilt_width = 8
quilt_length = 12
print(quilt_width * quilt_length)
quilt_length = 8  # change quilt length and recalculate
print(quilt_width * quilt_length)

# -------------------------------------------------------------------------
# lesson 10: Exponents using **
# Calculation of squares for quilts:
# 6x6 quilt
print(6**2)
# 7x7 quilt
print(7**2)
# 8x8 quilt
print(8**2)
# How many squares for 6 people to have 6 quilts each that are 6x6?
print(6**4)

# -------------------------------------------------------------------------
# lesson 11: Modulo/Modulus/%
my_team = 27 % 4
print(my_team)


# -------------------------------------------------------------------------
# lesson 12: concatenation
string1 = "The wind, "
string2 = "which had hitherto carried us along with amazing rapidity, "
string3 = "sank at sunset to a light breeze; "
string4 = "the soft air just ruffled the water and "
string5 = "caused a pleasant motion among the trees as we approached the shore, "
string6 = "from which it wafted the most delightful scent of flowers and hay."
# Define message below:
message = string1 + string2 + string3 + string4 + string5 + string6
print(message)
# also note that str() parses a number to a string

# -------------------------------------------------------------------------
# lesson 13: plus equals
# plus equals can also be used for string concatenation to update the end of a string variable
concat1 = "this is a python string"
print(concat1)
concat1 += "!"
print(concat1)

# -------------------------------------------------------------------------
# lesson 14: multi-line strings
# using three ''' or """ to enclose a super long string also allows you not to focus on
to_you = '''Stranger, if you passing meet me and desire to speak to me, 
why should you not speak to me?
And why should I not speak to you?'''
print(to_you)

# -------------------------------------------------------------------------
# lesson 15: short review
my_age = 27
half_my_age = (my_age / 2)
greeting = "Hello there"
name = "Dayna"
greeting_with_name = greeting + ", " + name

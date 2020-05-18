# first we need 3 products with descriptions and prices
lovely_loveseat_description = '''Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.'''
lovely_loveseat_price = 254.00

stylish_settee_description = '''Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.'''
stylish_settee_price = 180.50

luxurious_lamp_description = '''Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.'''
luxurious_lamp_price = 52.15

# now we need a sales tax variable
sales_tax = 0.088

# we have our first customer
customer_one_total = 0
customer_one_itemization = ""

# customer 1 is making a purchase of the lovely loveseat
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description

# customer 1 also wants the lamp
customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description

# now calculate sales tax
customer_one_tax = (customer_one_total * sales_tax)
customer_one_total += customer_one_tax

# now print receipt
print("Customer One Items:")
print(customer_one_itemization)
print("Customer One Total:")
print(customer_one_total)

# testing input()
goal_for_today = input("What is your goal for today?")
print(goal_for_today)

def ground_shipping(weight):
    if weight <= 2:
        cost = 1.50 * weight
    elif 2 < weight <= 6:  #note how you can simplify a chain comparison
        cost = 3.00 * weight
    elif 6 < weight <= 10:
        cost = 4.00 * weight
    else:
        cost = 4.75 * weight
    return cost + 20


print(ground_shipping(8.4))

premium_ground = 125


def drone_shipping(weight):
    if weight <= 2:
        cost = 4.50 * weight
    elif 2 < weight <= 6:
        cost = 9.00 * weight
    elif 6 < weight <= 10:
        cost = 12.00 * weight
    else:
        cost = 14.25 * weight
    return cost


print(drone_shipping(1.5))


def cheapest_option(weight):
    if ground_shipping(weight) < premium_ground and ground_shipping(weight) < drone_shipping(weight):
        print("The cheapest shipping method is ground shipping.")
        print("The cost of ground shipping will be $" + str(ground_shipping(weight)))
    elif drone_shipping(weight) < premium_ground and drone_shipping(weight) < ground_shipping(weight):
        print("The cheapest shipping method is drone shipping.")
        print("The cost of drone shipping will be $" + str(drone_shipping(weight)))
    else:
        print("The cheapest shipping method is premium ground shipping.")
        print("The cost of premium ground shipping will be $" + str(premium_ground))


print(cheapest_option(4.8))
print(cheapest_option(41.5))



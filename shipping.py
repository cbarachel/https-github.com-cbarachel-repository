# Determines the shipping cost based on the ship_to_state.
# When testing, change the ship_to_state to various state abreviations
# to verify your code works for all conditions.
# prompt user to enter a state to ship to
ship_to_state = input(
    "Enter a state to ship to, e.g. TX, NM, OK, NY, AK, HI, etc.: ")

# convert user input to uppercase
ship_to_state = ship_to_state.upper()

# set the default shipping cost to 12.5
shipping_cost = 12.5

# determine the shipping cost based on the state
if ship_to_state == "TX" or ship_to_state == "NM" or ship_to_state == "OK":
    shipping_cost = 0
elif ship_to_state == "NY":
    shipping_cost = 7
elif ship_to_state == "AK":
    shipping_cost = 15.75
elif ship_to_state == "HI":
    shipping_cost = 20

# print the output
print("Shipping to {} costs {}.".format(ship_to_state, shipping_cost))

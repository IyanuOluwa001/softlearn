import keyword
#import numpy as np

# CODE 1
# print("Attempting to brew...")
# my_value= 5
# his_value=5
# our_outcome = my_value+his_value
# print (our_outcome)

# CODE 2 - Syntax
# if my_value > 5:
#     print("x is greater than 5")
#     print("That's a big number!")

# # Check if a word is a keyword
# print(keyword.iskeyword("if"))      # True
# print(keyword.iskeyword("hello"))   # False
# print(keyword.iskeyword("for"))     # True
# print(keyword.iskeyword("my_var"))  # False

# CODE 3 - Calculate the total price including tax
# price = 25.00
# tax_rate = 0.08
# total = price + (price * tax_rate)  # Add 8% tax

# # Print the result
# print(f"Total price: ₦{total}")

# print(missing_ingredient) # This variable does not exist!

#Lesson 7
# CODE 4 - ARITHMETIC OPERATORS
# available_milk = 12.0
# milk_per_serving = 1.5      # 1.5 cups
# scoops_per_serving = 3      # 3 scoops
# total_guests = 2

# # Multiply to calculate the total ingredients needed
# total_milk_needed = milk_per_serving * total_guests      # 3.0 cups
# total_scoops_needed = scoops_per_serving * total_guests  # 6 scoops

# # Subtract to find the remaining inventory
# remaining_milk = available_milk - total_milk_needed                # 9.0 cups left
# print (remaining_milk)

# CODE 5 - COMPARISM OPERATORS
# milk_ounces = 12
# cereal_scoops = 4
# bowl_capacity = 5

# # Check if current assets meet minimum requirements
# has_enough_milk = milk_ounces >= 8             # 12 >= 8 is True
# has_enough_cereal = cereal_scoops >= 3          # 4 >= 3 is True
# fits_in_bowl = cereal_scoops <= bowl_capacity  # 4 <= 5 is True

# #LOGICAL OPERATORS
# milk_ounces = 12
# cereal_scoops = 4
# bowl_capacity = 5

# # Using 'and' to ensure ALL requirements are met
# ready_to_serve = (milk_ounces >= 8) and (cereal_scoops >= 3) and (bowl_capacity >= cereal_scoops)
# # ready_to_serve is True because all individual expressions are True
# print (ready_to_serve)

# # Using 'or' to check alternate options
# can_use_alternate_bowl = (bowl_capacity >= 10) or (cereal_scoops <= 3)
# # evaluates to False because bowl_capacity is 5 (5 >= 10 is False) and cereal_scoops is 4 (4 <= 3 is False)

# #PARENTHESIS
# cereal_scoops = 3
# milk_ounces = 12

# # Parentheses force the addition to occur first
# average_volume = (cereal_scoops + milk_ounces) / 4
# # (3 + 12) / 4 -> 15 / 4 -> 3.75

# Lesson 8
# CODE 6 - TYPE CONVERSION
# banana_count = "2"      # text string
# milk_cups = "1.5"       # text string
# milk_cups = float("1.5")
# banana_orderno = int(banana_count)

# # Convert the text variables into numeric variables
# banana_number = int(banana_count)   # Becomes the integer 2
# milk_number = float(milk_cups)      # Becomes the float 1.5

# # Perform mathematical addition on the numbers
# total = banana_number + milk_number  # 2 + 1.5 = 3.5

# Lesson 9
# CODE 7 - Conditional Statement
# selected_drink = "Green Tea"
# default_temp = 100
# if selected_drink == "Green Tea":
#     default_temp = 80

# print(default_temp)

# CODE 8
# selected_drink = "Green Tea"

# if selected_drink == "Green Tea":
#     target_temp = 80
# elif selected_drink == "Coffee":
#     target_temp = 90

# CODE 9
# selected_drink = "Coffee"
# target_temp = 100

# if selected_drink == "Green Tea":
#     target_temp = 80
# elif selected_drink == "Coffee":
#     target_temp = 90

# print(target_temp)

# CODE 10
# selected_drink = "Hot Cocoa"
# target_temp = 0

# if selected_drink == "Green Tea":
#     target_temp = 80
# elif selected_drink == "Coffee":
#     target_temp = 90
# else:
#     target_temp = 100
# print (target_temp)

# CODE 11
# selected_drink = "Black Tea"
# target_temp = 100

# if selected_drink == "Green Tea":
#     target_temp = 80
#     print("This line will be skipped!")

# print(target_temp)

#Lesson 10
# CODE 12
# for count in range(3):
#     print("Grind " + str(count))

# CODE 13
# # 1. First, define what 'grind_pepper' actually does
# def grind_pepper():
#     print("*Crack* Pepper added!")

# # range(5) counts from 0 to 4 (exactly 5 steps)
# for twist_number in range(5):
#     print("Grinding twist number " + str(twist_number + 1))
#     grind_pepper()

# CODE 14
# pepper_weight = 0.0  #(starting state)

# # Repeat as long as our sensor weight is less than our target of 2.0 grams
# while pepper_weight < 2.0:
#     grind_pepper()
#     pepper_weight = read_scale_sensor() # Update the loop variable!
   
# weight = 0.0
# while weight < 1.5:
#     weight = weight + 0.5
#     print("Current weight: " + str(weight))

# CODE 15
# The common cleanup methods:
# order = "  latte  "

# cleaned = order.strip()        # Removes whitespace from both ends -> "latte"
# loud = order.upper()           # Converts to uppercase -> "  LATTE  "
# quiet = order.lower()          # Converts to lowercase -> "  latte  "
# proper = order.strip().title() # Chains methods to strip and capitalize -> "Latte"

# # Replace words inside a string
# message = "Your coffee is ready"
# new_message = message.replace("coffee", "latte") # -> "Your latte is ready"

# CODE 16
# customer_name = "  alIce   "

# # Clean the string and save the output back into a variable
# cleaned_name = customer_name.strip()
# proper_name = cleaned_name.capitalize()

# print("[" + proper_name + "]")

# CODE 17
# order = "  espresso  "
# print(order.strip().upper())
# CODE 18
# name = "Alice"
# drink = "latte"
# price = 4.50

# # The f-string automatically formats the variables inside the string
# receipt = f"Order for {name}: {drink} — ₦{price:.2f}"
# print ("-")
# print (receipt)

# CODE 19 
# customer = "Bob"
# total = 12.0
# print ("-")
# print(f"Thank you, {customer}! Total: ₦{total:.2f}")

# CODE 20
# raw_order_list = "latte,espresso,mocha"
# menu_display = ""

# # 1. Split the comma-separated string into a List
# items = raw_order_list.split(",")
# print ("-")
# print (raw_order_list)

# # 2. Join the List using a newline character (\n) as the separator
# menu_display = "\n".join(items)
# print ("-")
# print (menu_display)

# CODE 21
# sentence = "latte and espresso"
# words = sentence.split(" and ")
# print ("-")
# print(words)
# rejoined = "-".join(words)
# print(rejoined)

# name_field = "  jOHn  "
# email_field = " JOHN@Company.com  "

# clean_name = name_field.strip().capitalize
# email_field = email_field.strip().lower



# CODE 22 - Creating and calling a function
# 1. Defining the routine (This does not run the code!)
# def brew_coffee():
#     print()
#     print("Grinding espresso beans...")
#     print("Brewing hot coffee into the cup...")
#     print("Coffee is ready!")

# # 2. Calling the routine (This executes the nested lines)
# brew_coffee()

# CODE 23
# def greet_barista():
#     print()
#     print("Hello, barista!")

# greet_barista()

# CODE 24
# "customer_name" is a placeholder parameter
# def print_cup_label(customer_name):
#     print("--------------------")
#     print("Order: Hot Latte")
#     print("Name: " + customer_name)
#     print("--------------------")

# # Pass real string values (arguments) into the function
# print_cup_label("Alice")
# print_cup_label("Bob")

# Lesson 12
# CODE 25
# def order_drink(drink, size):
#     print("Dispensing " + size + " " + drink)

# order_drink("espresso", "large")

# CODE 26
# Definition
# def calculate_price(count, cost):
#     total = count * cost
#     return total  # Send the calculated float back

# # Call and save the returned value in a variable
# #customer_receipt = calculate_price(cups_ordered, price_per_cup)
# customer_receipt = calculate_price(2, 1.2)
# print("$" + str(customer_receipt))

# CODE 27
# def add_tax(subtotal):
#     # Note: we can't assign variable inside return in python
#     # return final_total = subtotal * 1.08
#     final_total = subtotal * 1.08
#     return final_total

# final_total = add_tax(10)
# print(final_total)

# CODE 28
# This is an optimized version of code 27
# def add_tax(subtotal):
#     return subtotal * 1.08

# final_total = add_tax(10)
# print(final_total)

# CODE 29
# def make_custom_drink(base_drink, milk_type, sugar_packets):
#     # Assemble the descriptive string step-by-step
#     description = f"{base_drink} with {milk_type} milk"
    
#     if sugar_packets > 0:
#         description = description + f" and {sugar_packets} sugar packets"
        
#     return description

# # Generate distinct order strings
# order1 = make_custom_drink("Latte", "almond", 2)
# order2 = make_custom_drink("Cappuccino", "whole", 0)

# print(order1) # "Latte with almond milk and 2 sugar packets"
# print(order2) # "Cappuccino with whole milk"

# CODE 30
# A function with 5 distinct parameters
# def record_kiosk_order(name, drink, size, milk, sugar_packets):
#     print(f"Kiosk Receipt for {name}:")
#     print(f"  Item: {size} {drink}")
#     print(f"  Milk: {milk}")
#     print(f"  Sugar: {sugar_packets} packets")

# #Note: Enusure to provide the parameters the way it is written in the function definition
# tocker=record_kiosk_order("kola", "chocolate", "large", "evaporated", "natural")
# print(tocker)

# CODE 31
# def mix_liquid(drink, quantity):
#     print ("This is a "+ quantity+ " " + drink)

# mix_liquid ("yoghurt", "large")

#CODE 32
# def print_receipt(item, cost):
#     print(item + ": ₦" + str(cost))

# Run it in order
#print_receipt("Espresso", 4.50)

#CODE 33
#Ordering arguments by name - keyword arguments
# def brew_cup(drink, size, temperature):
#     print(f"Brewing a {temperature} {size} {drink}...")

# #Call using explicit names. The order of these lines does not matter!
# #type 1
# kocker=brew_cup(temperature="iced", drink="cappuccino", size="medium")
# print(kocker)
# #type 2
# brew_cup(temperature="iced", drink="cappuccino", size="medium")

#CODE 34
# def cup_label(name, drink):
#     print(name+ " ordered "+ drink)

# cup_label(drink="espresso", name="Manuel")

#CODE 35
# Required parameters come first; default parameters are placed at the end
# def process_order(name, drink, size="medium", milk="whole"):
#     print(f"Order for {name}: {size} {drink} with {milk} milk.")
# process_order("Iyanu", "Cola")

#CODE 36
# Required fields are declared first, optional default fields are placed last
# def process_order(name, drink, size="medium"):
#     print(f"{name} wants a {size} {drink}")

# # Now we can safely omit the optional size argument
# process_order("Alice", "Latte") # Uses the default "medium"
# process_order("Bob", "Espresso", "large") # Overrides the default

#CODE 37
#We can overwrite default parameters
# def sprinkle_sugar(packets=1):
#     print("Adding " + str(packets) + " sugar packets.")

# sprinkle_sugar()
# sprinkle_sugar(3)

#CODE 38
# def brew_custom_cup(drink, size, temperature, milk="whole", sugar=0):
#     print(f"Making a {temperature} {size} {drink} with {milk} milk")

# #Correct: Positional arguments first, then keywords to override defualts
# brew_custom_cup("Latte", "large", "hot", milk="almond", sugar=1)

#CODE 39
# def label(name, drink, size="medium"):
#     print(name + " wants a " + size + " " + drink)

# # Attempt to place a positional argument AFTER a keyword argument
# #label(name="Alice", "espresso")
# #to solve the error, write it this way:
# label(name="Alice", drink="espresso")

#CODE 40
# def toppings(*args):
#     print(args)
# toppings("chocolate", "sprinkles", "whipped cream")

# #CODE 41
# def make_coffee(*toppings):
#     print ("Coffee with:")

#     for topping in toppings:
#         print(f"-{topping}")

# make_coffee("chocolate", "sprinkles", "whipped cream")

# CODE 42
# def add_numbers(a: int, b: int) -> int:
#     return a + b

# print (add_numbers(1,2))

# CODE 43
# Need to install numpy for this code to work   
# def try_numpy():
#     prices = np.array([1200, 3500, 800, 2500])
#     discounted = prices * 0.9
#     return discounted

# print(try_numpy())


# # Code snippet for panda
# import pandas as pd

# df = pd.read_csv("sales.csv")
# print(df.head())

# # Code snippet for Scikit-learn
# from sklearn.linear_model import LogisticRegression

# model = LogisticRegression()
# model.fit(X_train, y_train)
# predictions = model.predict(X_test)

# # Code snippet for PyTouch
# import torch
# import torch.nn as nn

# model = nn.Linear(10, 1)

# CODE 44 - Local variables
# def make_latte():
#     # These are local variables (napkin notes)
#     coffee_grams = 18
#     milk_ounces = 8
    
#     print(f"Brewing with {coffee_grams}g of coffee and {milk_ounces}oz of milk.")

# make_latte()

# # This will CRASH the program! Comment it out for the program to run normally
# print(coffee_grams)

# CODE 45 - Commiting a value to global variable
# def steam_milk():
#     temp = 65
#     print(f"Milk steamed to {temp} degrees.")
#     return temp  # Hand the value back before the napkin is destroyed!

# # Capture the returned value in a global variable
# final_temp = steam_milk()
# print(f"The final temperature was {final_temp}")

# CODE 46
# Global variable (written on the public whiteboard)
# menu_price = 4.50

# def serve_customer(name):
#     # We can read the global variable naturally
#     print(f"Charging {name} ₦{menu_price:.2f} for their latte.")

# serve_customer("Alice")

# CODE 47 - Reading global variables
# menu_price = 4.50  # Global

# def update_price(new_price):
#     menu_price = new_price  # This accidentally creates a LOCAL variable!
#     print(f"Local function variable set to: ₦{menu_price:.2f}")

# update_price(5.00)
# print(f"Global whiteboard price is: ₦{menu_price:.2f}")

# CODE 48
# shop_name = "Espresso Cart"
# def print_shop():
#     print("Welcome to " + shop_name)

# print_shop()

# CODE 49-How to use global
# menu_price = 4.50  # Global

# def update_price(new_price):
#     global menu_price  # Link this function to the global whiteboard variable
#     menu_price = new_price  # This now updates the global whiteboard!
#     print(f"Whiteboard price updated to ₦{menu_price:.2f}")

# update_price(5.00)
# print(f"Current menu price is now: ₦{menu_price:.2f}") # Output: 5.00

# CODE 50 - A wrong way to access global variable
# total_sales = 0.0

# def record_sale(amount):
#     total_sales = total_sales + amount
#     print(f"Sale recorded: ₦{amount:.2f}")

# record_sale(4.50)

# CODE 51 - Access global variable the right way
# total_sales = 0.0  # Global

# def record_sale(amount):
#     global total_sales  # Explicitly link to the global variable
#     total_sales = total_sales + amount
#     print(f"Sale recorded: ₦{amount:.2f}")

# record_sale(4.50)
# print(f"Register total sales: ₦{total_sales:.2f}")

# CODE 52 - another use of global
# count = 0
# def increment():
#     global count
#     count = count + 1
#     print(count)

# increment()
# increment()

# CODE 53 - Local and Global
# global_sales= 0

# def make_drink():
#     local_count = 0  # Born fresh on every function call
#     global global_sales
    
#     local_count = local_count + 1
#     global_sales = global_sales + 1
#     print(f"Local: {local_count}, Global: {global_sales}")

# make_drink()
# make_drink()
# make_drink()
# #Local will remain 1, because it resets everytime the program finish running.

# CODE 54 - Defining and using nonlocal variable
# def run_coffee_cart():
#     # Outer parent function's local variable
#     current_order = "Espresso"
    
#     def change_order(new_drink):
#         nonlocal current_order  # Link to the parent function's variable
#         current_order = new_drink
#         print(f"Order updated to: {current_order}")
        
#     change_order("Latte")
#     print(f"Final cart order: {current_order}")

# run_coffee_cart()

# CODE 55 - Another trial
def outer():
    x = "original"
    def inner():
        nonlocal x
        x = "modified"
    inner()
    print(x)

outer()
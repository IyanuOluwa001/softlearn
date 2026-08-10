import keyword

# CODE 1
print("Attempting to brew...")
my_value= 5
his_value=5
our_outcome = my_value+his_value
print (our_outcome)

# CODE 2 - Syntax
if my_value > 5:
    print("x is greater than 5")
    print("That's a big number!")

# Check if a word is a keyword
print(keyword.iskeyword("if"))      # True
print(keyword.iskeyword("hello"))   # False
print(keyword.iskeyword("for"))     # True
print(keyword.iskeyword("my_var"))  # False

# CODE 3 - Calculate the total price including tax
price = 25.00
tax_rate = 0.08
total = price + (price * tax_rate)  # Add 8% tax

# Print the result
print(f"Total price: ₦{total}")

# print(missing_ingredient) # This variable does not exist!

#Lesson 7
# CODE 4 - ARITHMETIC OPERATORS
available_milk = 12.0
milk_per_serving = 1.5      # 1.5 cups
scoops_per_serving = 3      # 3 scoops
total_guests = 2

# Multiply to calculate the total ingredients needed
total_milk_needed = milk_per_serving * total_guests      # 3.0 cups
total_scoops_needed = scoops_per_serving * total_guests  # 6 scoops

# Subtract to find the remaining inventory
remaining_milk = available_milk - total_milk_needed                # 9.0 cups left
print (remaining_milk)

# CODE 5 - COMPARISM OPERATORS
milk_ounces = 12
cereal_scoops = 4
bowl_capacity = 5

# Check if current assets meet minimum requirements
has_enough_milk = milk_ounces >= 8             # 12 >= 8 is True
has_enough_cereal = cereal_scoops >= 3          # 4 >= 3 is True
fits_in_bowl = cereal_scoops <= bowl_capacity  # 4 <= 5 is True

#LOGICAL OPERATORS
milk_ounces = 12
cereal_scoops = 4
bowl_capacity = 5

# Using 'and' to ensure ALL requirements are met
ready_to_serve = (milk_ounces >= 8) and (cereal_scoops >= 3) and (bowl_capacity >= cereal_scoops)
# ready_to_serve is True because all individual expressions are True
print (ready_to_serve)

# Using 'or' to check alternate options
can_use_alternate_bowl = (bowl_capacity >= 10) or (cereal_scoops <= 3)
# evaluates to False because bowl_capacity is 5 (5 >= 10 is False) and cereal_scoops is 4 (4 <= 3 is False)

#PARENTHESIS
cereal_scoops = 3
milk_ounces = 12

# Parentheses force the addition to occur first
average_volume = (cereal_scoops + milk_ounces) / 4
# (3 + 12) / 4 -> 15 / 4 -> 3.75

# Lesson 8
# CODE 6 - TYPE CONVERSION
banana_count = "2"      # text string
milk_cups = "1.5"       # text string
milk_cups = float("1.5")
banana_orderno = int(banana_count)

# Convert the text variables into numeric variables
banana_number = int(banana_count)   # Becomes the integer 2
milk_number = float(milk_cups)      # Becomes the float 1.5

# Perform mathematical addition on the numbers
total = banana_number + milk_number  # 2 + 1.5 = 3.5

# Lesson 9
# CODE 7 - Conditional Statement
selected_drink = "Green Tea"
default_temp = 100
if selected_drink == "Green Tea":
    default_temp = 80

print(default_temp)

# CODE 8
selected_drink = "Green Tea"

if selected_drink == "Green Tea":
    target_temp = 80
elif selected_drink == "Coffee":
    target_temp = 90

# CODE 9
selected_drink = "Coffee"
target_temp = 100

if selected_drink == "Green Tea":
    target_temp = 80
elif selected_drink == "Coffee":
    target_temp = 90

print(target_temp)

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
for count in range(3):
    print("Grind " + str(count))

# CODE 13
# 1. First, define what 'grind_pepper' actually does
def grind_pepper():
    print("*Crack* Pepper added!")

# range(5) counts from 0 to 4 (exactly 5 steps)
for twist_number in range(5):
    print("Grinding twist number " + str(twist_number + 1))
    grind_pepper()

# CODE 14
# pepper_weight = 0.0  #(starting state)

# # Repeat as long as our sensor weight is less than our target of 2.0 grams
# while pepper_weight < 2.0:
#     grind_pepper()
#     pepper_weight = read_scale_sensor() # Update the loop variable!
   
weight = 0.0
while weight < 1.5:
    weight = weight + 0.5
    print("Current weight: " + str(weight))

# CODE 15
# The common cleanup methods:
order = "  latte  "

cleaned = order.strip()        # Removes whitespace from both ends -> "latte"
loud = order.upper()           # Converts to uppercase -> "  LATTE  "
quiet = order.lower()          # Converts to lowercase -> "  latte  "
proper = order.strip().title() # Chains methods to strip and capitalize -> "Latte"

# Replace words inside a string
message = "Your coffee is ready"
new_message = message.replace("coffee", "latte") # -> "Your latte is ready"

# CODE 16
customer_name = "  alIce   "

# Clean the string and save the output back into a variable
cleaned_name = customer_name.strip()
proper_name = cleaned_name.capitalize()

print("[" + proper_name + "]")

order = "  espresso  "
print(order.strip().upper())

# CODE 17
order = "  espresso  "
print(order.strip().upper())

# CODE 18
name = "Alice"
drink = "latte"
price = 4.50

# The f-string automatically formats the variables inside the string
receipt = f"Order for {name}: {drink} — ₦{price:.2f}"
print ("-")
print (receipt)

# CODE 19 
customer = "Bob"
total = 12.0
print ("-")
print(f"Thank you, {customer}! Total: ₦{total:.2f}")

# CODE 20
raw_order_list = "latte,espresso,mocha"
menu_display = ""

# 1. Split the comma-separated string into a List
items = raw_order_list.split(",")
print ("-")
print (raw_order_list)

# 2. Join the List using a newline character (\n) as the separator
menu_display = "\n".join(items)
print ("-")
print (menu_display)

# CODE 21
sentence = "latte and espresso"
words = sentence.split(" and ")
print ("-")
print(words)
rejoined = "-".join(words)
print(rejoined)

name_field = "  jOHn  "
email_field = " JOHN@Company.com  "

clean_name = name_field.strip().capitalize
email_field = email_field.strip().lower



# CODE 22 - Creating and calling a function
# 1. Defining the routine (This does not run the code!)
def brew_coffee():
    print()
    print("Grinding espresso beans...")
    print("Brewing hot coffee into the cup...")
    print("Coffee is ready!")

# 2. Calling the routine (This executes the nested lines)
brew_coffee()

# CODE 23
def greet_barista():
    print()
    print("Hello, barista!")

greet_barista()
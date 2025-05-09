import pyinputplus as pyip

# Define product prices
bread_prices = {"wheat": 1.00, "white": 0.80, "sourdough": 1.20}
protein_prices = {"chicken": 2.50, "turkey": 2.50, "ham": 2.00, "tofu": 1.50}
cheese_prices = {"cheddar": 0.50, "Swiss": 0.60, "mozzarella": 0.50}
condiment_prices = {"mayo": 0.20, "mustard": 0.20, "lettuce": 0.30, "tomato": 0.30}

# Pick Your Bread Choice
bread_choice = pyip.inputMenu(
    ["wheat", "white", "sourdough"], prompt="Please choose type of bread: \n"
)
print("User bread choice:", bread_choice)

# Pick Your Protein Choice
protein_choice = pyip.inputMenu(
    ["chicken", "turkey", "ham", "tofu"], prompt="Please choose type of protein: \n"
)
print("User protein choice:", protein_choice)

# Cheese?
wants_cheese = pyip.inputYesNo("Would you like cheese on your sandwich? ")
if wants_cheese == "yes":
    cheese_type = pyip.inputMenu(
        ["cheddar", "Swiss", "mozzarella"], prompt="Please choose type of cheese: \n"
    )
    print("User cheese choice:", cheese_type)

# Pick Your Condiments Choice
wants_lettuce = pyip.inputYesNo("Would you like lettuce on your sandwich? ")
if wants_lettuce == "yes":
    print("User lettuce choice:", wants_lettuce)

wants_tomato = pyip.inputYesNo("Would you like tomato on your sandwich? ")
if wants_tomato == "yes":
    print("User tomato choice:", wants_tomato)

wants_mustard = pyip.inputYesNo("Would you like mustard on your sandwich? ")
if wants_mustard == "yes":
    print("User mustard choice:", wants_mustard)

wants_mayo = pyip.inputYesNo("Would you like mayo on your sandwich? ")
if wants_mayo == "yes":
    print("User mayo choice:", wants_mayo)

num_sandwiches = pyip.inputInt("How many sandwiches would you like? ", min=1)
print("Number of sandwiches:", num_sandwiches)

# Calculate total cost

total_cost = 0
total_cost += bread_prices[bread_choice]
total_cost += protein_prices[protein_choice]
if wants_cheese == "yes":
    total_cost += cheese_prices[cheese_type]
if wants_lettuce == "yes":
    total_cost += condiment_prices["lettuce"]
if wants_tomato == "yes":
    total_cost += condiment_prices["tomato"]
if wants_mustard == "yes":
    total_cost += condiment_prices["mustard"]
if wants_mayo == "yes":
    total_cost += condiment_prices["mayo"]

# Multiply by number of sandwiches
total_cost *= num_sandwiches

# Print the total cost
print("Total cost: ${:.2f}".format(total_cost))

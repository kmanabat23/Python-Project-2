from scipy.stats import randint
import numpy as np

# A dictionary of car makes and models with price range on what Kelly Blue Books has them approx. costing at the moment based on market
cars = {
    'Toyota Camry': {'price_range': (20000, 30000)},
    'Honda Civic': {'price_range': (15000, 25000)},
    'Ford Mustang': {'price_range': (25000, 40000)},
    'Chevrolet Corvette': {'price_range': (50000, 80000)},
    'BMW M3': {'price_range': (60000, 90000)},
    'Mercedes-Benz S-Class': {'price_range': (90000, 150000)},
    'Audi A4': {'price_range': (30000, 45000)},
    'Subaru Impreza': {'price_range': (20000, 30000)},
    'Nissan Altima': {'price_range': (25000, 35000)},
    'Tesla Model 3': {'price_range': (40000, 55000)},
    'Mazda CX-5': {'price_range': (25000, 35000)},
    'Hyundai Sonata': {'price_range': (20000, 30000)},
    'Kia Forte': {'price_range': (15000, 25000)},
    'Volkswagen Golf': {'price_range': (20000, 30000)},
    'Porsche 911': {'price_range': (90000, 150000)}
}

# Ask the user to input a minimum and maximum price range for car comparison
min_price = int(input("Enter the minimum price range: "))
max_price = int(input("Enter the maximum price range: "))

# Initialize an empty list to store the cars that fall within the user's price range
cars_within_price_range = []

# Loop through each car in the dictionary and generate a random price within its price range
for car, info in cars.items():
    price_range = info['price_range']
    random_price = randint.rvs(price_range[0], price_range[1]) #randit.rsv funtion is what generates an estimate cost if what a certain make & model may cost you based on market for your budget needs
    info['price'] = random_price
    
    # Check if the generated price falls within the user's specified range
    if random_price >= min_price and random_price <= max_price:
        cars_within_price_range.append(car)

# If no cars fall within the user's price range, print a message and exit the program
if not cars_within_price_range:
    print("Sorry, no cars found within the specified price range.")
    exit()

# Sort the cars based on their generated prices
sorted_cars = sorted(cars_within_price_range, key=lambda x: cars[x]['price'])

# Print the list of cars that fall within the user's price range, sorted by price
print("Cars within price range:")
for car in sorted_cars:
    price = cars[car]['price']
    print("- {} (${:,})".format(car, price))

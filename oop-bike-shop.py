# Here's OOP basic using Bike Shop as a Use Case
# Implemented CRUD operations using OOP: Create, Read, Update, Delete
# Author: Pizofreude

# In this OOP project, we're going to create a bike store. For this code, we've created a base class Bike, which has common attributes like brand, model, and price.
# Then, we've created two subclasses, RoadBike and MountainBike, which inherit from Bike and add specific attributes like frame size and suspension type.

# Each class has a display_info method to print out the bike's information.

# We've also created instances of these classes to represent actual bikes in our store.

# Finally, we extended this project further by adding methods for CRUD operations like creating, reading, updating, and deleting bike objects
#  from our dealership's inventory.

class Bike:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: ${self.price:.2f}")


class RoadBike(Bike):
    def __init__(self, brand, model, price, frame_size):
        super().__init__(brand, model, price)
        self.frame_size = frame_size

    def display_info(self):
        super().display_info()
        print(f"Frame Size: {self.frame_size} inches")


class MountainBike(Bike):
    def __init__(self, brand, model, price, suspension_type):
        super().__init__(brand, model, price)
        self.suspension_type = suspension_type

    def display_info(self):
        super().display_info()
        print(f"Suspension Type: {self.suspension_type}")


# Let's create some bike objects:
bike1 = RoadBike("Trek", "Domane SL 6", 2499.99, 52)
bike2 = RoadBike("Giant", "Defy Advanced Pro 2", 2999.99, 56)
bike3 = MountainBike("Specialized", "Stumpjumper ST", 1999.99, "Front Suspension")
bike4 = MountainBike("Santa Cruz", "Tallboy", 3499.99, "Full Suspension")

# Display bike information:
bike1.display_info()
print("\n")
bike3.display_info()


# We'll implement basic CRUD operations: creating, reading, updating, and deleting bike objects.
class BikeShop:
    def __init__(self):
        self.inventory = []

    def add_bike(self, bike):
        self.inventory.append(bike)

    def find_bike_by_model(self, model):
        for bike in self.inventory:
            if bike.model == model:
                return bike
        return None

    def update_bike_price(self, model, new_price):
        bike = self.find_bike_by_model(model)
        if bike:
            bike.price = new_price
            print(f"Price for {bike.brand} {bike.model} updated to ${new_price:.2f}")
        else:
            print(f"Bike with model {model} not found")

    def sell_bike(self, model):
        bike = self.find_bike_by_model(model)
        if bike:
            self.inventory.remove(bike)
            print(f"Sold: {bike.brand} {bike.model}")
        else:
            print(f"Bike with model {model} not found")

# Let's create a bike shop and add some bikes to its inventory:
bike_shop = BikeShop()
bike_shop.add_bike(bike1)
bike_shop.add_bike(bike2)
bike_shop.add_bike(bike3)
bike_shop.add_bike(bike4)

# Let's perform some operations:
print("Inventory:")
for bike in bike_shop.inventory:
    bike.display_info()

print("\nSelling a bike:")
bike_shop.sell_bike("Domane SL 6")

print("\nUpdated Inventory:")
for bike in bike_shop.inventory:
    bike.display_info()

# Let's update the price of a bike:
bike_shop.update_bike_price("Defy Advanced Pro 2", 3999.99)


# In this code, we've created a `BikeShop` class that has a list called `inventory` to keep track of the bikes in stock. We've added methods to:

# 1. `add_bike`: Add a bike to the inventory.
# 2. `find_bike_by_model`: Find a bike by its model.
# 3. `update_bike_price`: Update the price of a bike by providing its model.
# 4. `sell_bike`: Remove a bike from the inventory when it's sold.

# We've created a `BikeShop` instance and added our bike objects to its inventory. Then, we've demonstrated selling a bike and updating prices.
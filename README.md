# Bike Dealership Python Project

This Python project simulates a roadbike and MTB dealership management system using Object-Oriented Programming (OOP). It allows you to create, read, update, and delete bike objects in a virtual inventory.

## Table of Contents

- [Bike Dealership Python Project](#bike-dealership-python-project)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Getting Started](#getting-started)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)

## Introduction

In this project, we've created two classes, `RoadBike` and `MountainBike`, that inherit from a base class `Bike`. Each class represents a specific type of bike and includes attributes like brand, model, price, and additional details (frame size or suspension type).

A `BikeShop` class manages the inventory of bikes and provides methods for performing CRUD operations:

- `add_bike`: Add a bike to the inventory.
- `find_bike_by_model`: Find a bike by its model.
- `update_bike_price`: Update the price of a bike.
- `sell_bike`: Remove a bike from the inventory when it's sold.

## Getting Started

To get started with this project, follow these steps:

1. Clone this repository to your local machine:

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:

   ```bash
   cd bike-dealership-python
   ```

3. Run the Python script:

   ```bash
   python bike_dealership.py
   ```

## Usage

You can use this project to:

- Add new bikes to the inventory.
- Display information about bikes.
- Update bike prices.
- Sell bikes and remove them from the inventory.

Here's an example of how to use the code:

```python
# Create a BikeShop instance
bike_shop = BikeShop()

# Add bikes to the inventory
bike_shop.add_bike(bike1)
bike_shop.add_bike(bike2)
bike_shop.add_bike(bike3)
bike_shop.add_bike(bike4)

# Display inventory
for bike in bike_shop.inventory:
    bike.display_info()

# Perform operations like selling a bike or updating prices
bike_shop.sell_bike("Domane SL 6")
bike_shop.update_bike_price("Tallboy", 3199.99)
```

## Contributing

Contributions are welcome! If you have ideas for improvements or new features, please submit an issue or a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
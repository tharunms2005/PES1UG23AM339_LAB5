"""
Inventory System Module
This module provides basic functionality for managing stock items 
in an inventory. It supports adding, removing, saving, loading, 
and viewing items with quantities. All functions include proper 
validation, safe file handling, and PEP8-compliant naming.
"""

import json
from datetime import datetime


stock_data = {}


def add_item(item, qty=0, logs=None):
    """Add a specified quantity of an item to the inventory."""
    if logs is None:
        logs = []
    if not isinstance(item, str) or not isinstance(qty, int):
        print("Invalid input types.")
        return
    if qty < 0:
        print("Quantity cannot be negative.")
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """Remove a specified quantity of an item from the inventory."""
    if not isinstance(item, str) or not isinstance(qty, int):
        print("Invalid input types.")
        return
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Item '{item}' not found in inventory.")


def get_qty(item):
    """Return the current quantity of a specific item."""
    return stock_data.get(item, 0)


def load_data(file_name="inventory.json"):
    """Load inventory data from a JSON file and return it as a dictionary."""
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Could not load data; starting with an empty inventory.")
        return {}


def save_data(file_name="inventory.json"):
    """Save the current inventory data to a JSON file."""
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(stock_data, file, indent=2)
    print("Inventory data saved successfully.")


def print_data():
    """Print all items and their quantities in a formatted report."""
    print("\nInventory Report:")
    if not stock_data:
        print("No items in inventory.")
        return
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """Return a list of items with quantity below a given threshold."""
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """Main execution function demonstrating inventory operations."""
    add_item("apple", 10, logs=[])
    add_item("banana", 2, logs=[])
    remove_item("apple", 3)
    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")
    save_data()  # Save the updated stock_data
    print_data()


if __name__ == "__main__":
    main()

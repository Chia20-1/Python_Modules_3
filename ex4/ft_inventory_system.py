#!/usr/bin/env python3


import sys


"""
1. Split my input with colons -> str.split(:)
2. Specify how many time I split. (Error - invalid parameter:).
3. if {item} in {data structure} to find duplicates
4. int() to check of dictionary [key: value] pair.
"""


def parse_input() -> dict[str, int]:
    inventory: dict[str, int] = {}
    for arg in sys.argv[1:]:
        try:
            key, value = arg.split(":", 1)
        except ValueError:
            print(f"Error - invalid parameter '{arg}'")
            continue
        if key in inventory:
            print(f"Redundant item '{key}' - discarding")
            continue
        try:
            inventory[key] = int(value)
        except ValueError as e:
            print(f"Quantity error for '{key}':", e)
    return inventory


def find_extremes(inventory: dict[str, int]) -> tuple[str, int, str, int]:
    first = True
    for key in inventory:
        value = inventory[key]
        if first:
            max_key = min_key = key
            max_value = min_value = value
            first = False
            continue
        if value > max_value:
            max_value = value
            max_key = key
        if value < min_value:
            min_value = value
            min_key = key
    return max_key, max_value, min_key, min_value


def ft_inventory_system() -> None:
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = parse_input()
    print("Got inventory:", inventory)
    print("Item list: [", end="")
    first = True
    for key in inventory:
        if not first:
            print(", ", end="")
        print(f"'{key}'", end="")
        first = False
    print("]")
    size = len(inventory)
    total = sum(inventory.values())
    if size == 0 or total == 0:
        print("No items in inventory.")
        return
    if size == 1:
        print(f"Total quantity of {size} item: {total}")
    else:
        print(f"Total quantity of the {size} items: {total}")
    for key in inventory:
        value = inventory[key]
        percentage = round((value / total * 100), 1)
        print(f"Item {key} represents {percentage}%")
    max_key, max_value, min_key, min_value = find_extremes(inventory)
    print(f"Item most abundant: {max_key} with quanity {max_value}")
    print(f"Item least abundant: {min_key} with quanity {min_value}")
    inventory.update({"magic_item": 1})
    print("Updated inventory:", inventory)


if __name__ == "__main__":
    ft_inventory_system()

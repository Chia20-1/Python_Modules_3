#!/usr/bin/env python3


import math


input_prompt: str = ("Enter new coordinates as"
                     " floats in format 'x,y,z': ")


# Create 3 containers to store the numeric string
# Putchar accordingly and move to the next upon seeing ","
# To check if there is more tokens, keep track of the comma count


def get_player_pos() -> tuple[float, float, float]:
    token1: str = ""
    token2: str = ""
    token3: str = ""
    comma_count: int = 0
    input_str = input(input_prompt)
    for char in input_str:
        if char == ",":
            comma_count += 1
            if comma_count > 2:
                print("Invalid syntax")
                return None
            continue
        elif char == " ":
            continue
        if comma_count == 0:
            token1 += char
        elif comma_count == 1:
            token2 += char
        elif comma_count == 2:
            token3 += char
    if comma_count != 2:
        print("Invalid syntax")
        return None
    x: float = float(token1)
    y: float = float(token2)
    z: float = float(token3)
    return (x, y, z)


def ft_coordinate_system() -> None:
    print("=== Game Coordinate System ===")
    print("\nGet a first set of coordinates")
    while True:
        try:
            start_point = get_player_pos()
            start_x: float = round(start_point[0], 1)
            start_y: float = round(start_point[1], 1)
            start_z: float = round(start_point[2], 1)
            sum = (start_x) ** 2 + (start_y) ** 2 + (start_z) ** 2
            distance = round(math.sqrt(sum), 4)
            print("Got a first tuple:", start_point)
            print(f"It includes: X={start_x}, "
                  f"Y={start_y}, Z={start_z}")
            print("Distance to center: ", distance)
            break
        except ValueError as e:
            print("Error on parameter", e)
        except TypeError:
            pass
    print("\nGet a second set of coordinates")
    while True:
        try:
            end_point = get_player_pos()
            end_x: float = round(end_point[0], 1)
            end_y: float = round(end_point[1], 1)
            end_z: float = round(end_point[2], 1)
            diff_x = (end_x - start_x) ** 2
            diff_y = (end_y - start_y) ** 2
            diff_z = (end_z - start_z) ** 2
            sum = diff_x + diff_y + diff_z
            distance = round(math.sqrt(sum), 4)
            print("Distance between the 2 sets of "
                  "coordinates: ", distance)
            break
        except ValueError as e:
            print("Error on parameter", e)
        except TypeError:
            pass


if __name__ == "__main__":
    ft_coordinate_system()

#!/usr/bin/env python3


input_prompt: str = ("Enter new coordinates as"
                     " floats in format 'x,y,z':")


# Create 3 containers to store the numeric string
# Putchar accordingly and move to the next upon seeing ","
# To check if there is more tokens, keep track of the comma count


def get_player_pos() -> tuple[int, int, int]:
    token1: str = ""
    token2: str = ""
    token3: str = ""
    comma_count: int = 0
    input_str = input(input_prompt)
    for char in input_str:
        if char == ","
            comma_count += 1
            continue
        elif char == " "
            continue
        if comma_count == 0
            token1 += char
        elif comma_count == 1
            token2 += char
        elif comma_count == 2
            token3 += char
        else
            print("Invalid syntax")
            break
    else:
        if comma_count != 2
            print("Invalid syntax")
            continue
        try:
            x: int = int(token1)
            y: int = int(token2)
            z: int = int(token3)
        except ValueError as e:
            print("Error on parameter", e)


get_player_pos()
    
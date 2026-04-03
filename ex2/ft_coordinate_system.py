#!/usr/bin/env python3


input_prompt: str = ("Enter new coordinates as"
                     " floats in format 'x,y,z':")


# Logic is created 3 containers to store the numeric string
# Put the char accordingly and stop upon seeing ","
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
        
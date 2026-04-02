#!/usr/bin/env python3


import sys


def ft_command_quest() -> None:
    length: int = len(sys.argv)
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    if (length == 1):
        print("No arguments provided!")
    else:
        print(f"Arguments received: {length - 1}")
    for i in range(1, length):
        print(f"Argument {i}: {sys.argv[i]}")
        i += 1
    print(f"Total arguments: {length}\n")


# def ft_command_quest() -> None:
#     args = sys.argv[1:]
#     for i, arg in enumerate(args, start=1):
#         print(f"Argument {i}: {arg}")


if __name__ == "__main__":
    ft_command_quest()

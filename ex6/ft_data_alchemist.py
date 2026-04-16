#!/usr/bin/env python3


import random


# [expression for item in iterable]
def ft_data_alchemist() -> None:
    players: list[str] = ['Alice', 'bob', 'Charlie', 'dylan',
                          'Emma', 'Gregory', 'john', 'kevin', 'Liam']
    all_caps: list[str] = [name.capitalize() for name in players]
    caps_only: list[str] = [name for name in players if name[0].isupper()]
    scores: dict[str, int] = {
        name: random.randint(0, 1000) for name in all_caps
        }
    average_score: float = sum(scores.values()) / len(scores)
    high_score = {
        name: scores[name]
        for name in scores
        if scores[name] > average_score
    }
    print("=== Game Data Alchemist ===\n")
    print("Initial list of players:", players)
    print("New list with all names capitalized:", all_caps)
    print("New list of capitalized names only:", caps_only)
    print()
    print("Score dict:", scores)
    print("Score average is", round(average_score, 2))
    print("High scores:", high_score)


if __name__ == "__main__":
    ft_data_alchemist()

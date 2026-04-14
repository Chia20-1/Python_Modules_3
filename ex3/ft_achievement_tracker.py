#!/usr/bin/env python3


import random


"""
Create a list of achievements
For each player:
    Create a set that stores their achievements. This will be empty at first
    Decide how many achievements we want to have
    While the set has fewer achievements than our target:
        Choose a random achievement from the list and add it to the set.
        // Think: Why is a set good for this?

Choosing a random achievement:
    Choose a random number from 0 to (list size)
    Use that number as an index into the list
"""


achievements: list[str] = ["Crafting Genius", "Strategist",
                           "World Savior", "Speed Runner",
                           "Survivor", "Master Explorer",
                           "Treasure Hunter", "Unstoppable",
                           "First Steps", "Collector Supreme",
                           "Untouchable", "Sharp Mind",
                           "Boss Slayer"]


master_list: set[str] = set(achievements)


def fill_set(count: int, target: set[str]) -> set[str]:
    while len(target) < count:
        target.add(achievements[random.randint(0, len(achievements) - 1)])
    return target


#   names: list = ["alice", "bob", "charlie", "dylan
#   player: dict = {}
#   for name in names:
#   player = {name: set()}


def gen_player_achievements() -> None:
    print("=== Achievement Tracker System ===\n")
    alice: set[str] = set()
    bob: set[str] = set()
    charlie: set[str] = set()
    dylan: set[str] = set()
    common: set[str] = set()
    alice = fill_set(6, alice)
    bob = fill_set(7, bob)
    charlie = fill_set(9, charlie)
    dylan = fill_set(5, dylan)
    print("Player Alice: ", alice)
    print("Player Bob: ", bob)
    print("Player Charlie: ", charlie)
    print("Player Dylan: ", dylan)
    print()
    print("All distinct achievements: ", achievements)
    print()
    common = alice.intersection(bob, charlie, dylan)
    print()
    print("Common achievements: ", common)
    print()
    print("Only Alice has:", alice.difference(bob, charlie, dylan))
    print("Only Bob has:", bob.difference(alice, charlie, dylan))
    print("Only Charlie has:", charlie.difference(alice, bob, dylan))
    print("Only Dylan has:", dylan.difference(alice, bob, charlie))
    print()
    print("Alice is missing:", master_list.difference(alice))
    print("Bob is missing:", master_list.difference(bob))
    print("Charlie is missing:", master_list.difference(charlie))
    print("Dylan is missing:", master_list.difference(dylan))


if __name__ == "__main__":
    gen_player_achievements()

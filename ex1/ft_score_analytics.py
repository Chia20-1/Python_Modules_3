#!/usr/bin/env python3


import sys


def display_score_analytics(scores: list[int]) -> None:
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")
    print()


def parse_scores(argv: list[str], length: int) -> list[int]:
    scores: list[int] = []
    for arg in sys.argv[1:]:
        try:
            value = int(arg)
            scores = scores + [value]
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    return scores


def ft_score_analytics() -> None:
    length: int = len(sys.argv)
    error_message: str = ("No scores provided. Usage: python3"
                          "ft_score_analytics.py <score1> <score2> ...\n")
    print("=== Player Score Analytics ===")
    if length == 1:
        print(error_message)
        return
    scores: list[int] = parse_scores(sys.argv, length)
    if len(scores) == 0:
        print(error_message)
        return
    display_score_analytics(scores)


if __name__ == "__main__":
    ft_score_analytics()

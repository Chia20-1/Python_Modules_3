#!/usr/bin/env python3


import random
import typing


player_list: list[str] = ["alice", "bob", "charlie", "dylan"]


action_list: list[str] = ["eat", "sleep", "use", "grab",
                          "climb", "run", "move", "swim", "release"]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        player = player_list[random.randrange(len(player_list))]
        action = action_list[random.randrange(len(action_list))]
        yield (player, action)


def consume_event(
                 events: list[tuple[str, str]]
                 ) -> typing.Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        index = random.randrange(len(events))
        yield events.pop(index)


def ft_data_stream() -> None:
    event_stream = gen_event()
    print("=== Game Data Stream Processor ===")
    for i in range(1000):
        print(f"Event {i}: Player did action {next(event_stream)}")
    ten_events: list[tuple[str, str]] = []
    for _ in range(10):
        ten_events.append(next(event_stream))
    print("Built list of 10 events: ", ten_events)
    for event in consume_event(ten_events):
        print("Got even from list:", event)
        print("Events in list:", ten_events)


if __name__ == "__main__":
    ft_data_stream()

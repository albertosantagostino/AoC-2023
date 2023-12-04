#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from copy import deepcopy
from functools import reduce

from common.meta_utils import get_puzzle_input


def parse_input(puzzle_input):
    games = {}

    for line in puzzle_input:
        game_id = int(line.split(':')[0].split()[1])
        xx = [el.strip().split(',') for el in line.split(':')[1].split(';')]
        game_turns = []
        for el in xx:
            current_turn = {}
            for entry in el:
                number, color = entry.strip().split()
                current_turn[color] = int(number)
            game_turns.append(current_turn)
        games[game_id] = game_turns

    return games


def part1(puzzle_input):
    games = parse_input(puzzle_input)
    available_cubes = {'red': 12, 'green': 13, 'blue': 14}
    result = 0

    for kk, vv in games.items():
        valid_game = True
        for game_turn in vv:
            for color, number in game_turn.items():
                if (number > available_cubes[color]):
                    valid_game = False
                    break
        if valid_game:
            result += kk

    return result


def part2(puzzle_input):
    games = parse_input(puzzle_input)
    result = 0

    for vv in games.values():
        min_cubes = {'red': 0, 'green': 0, 'blue': 0}
        for game_turn in vv:
            for color, number in game_turn.items():
                if (number > min_cubes[color]):
                    min_cubes[color] = number
        result += reduce(lambda v1, v2: v1 * v2, list(min_cubes.values()))

    return result


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(filename=__file__)
    print(f"Part 1 solution: {part1(deepcopy(puzzle_input))}")
    print(f"Part 2 solution: {part2(deepcopy(puzzle_input))}")

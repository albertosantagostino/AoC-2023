#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from copy import deepcopy

from common.meta_utils import get_puzzle_input

DIGITS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def part1(puzzle_input):
    puzzle_input = [[ch for ch in line if ch.isdigit()] for line in puzzle_input]
    puzzle_input = [[int(ch) for idx, ch in enumerate(line) if (idx == 0 or idx == len(line) - 1)]
                    for line in puzzle_input]
    result = 0

    for line in filter(None, puzzle_input):
        try:
            result += line[0] * 10 + line[1]
        except IndexError:
            result += line[0] * 10 + line[0]

    return result


def part2(puzzle_input):
    replaced_puzzle_input = []

    for line in puzzle_input:
        for idx, kk in enumerate(DIGITS):
            line = line.replace(kk, kk[0] + str(idx + 1) + kk[-1])
        replaced_puzzle_input.append(line)

    return part1(replaced_puzzle_input)


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(filename=__file__)
    print(f"Part 1 solution: {part1(deepcopy(puzzle_input))}")
    print(f"Part 2 solution: {part2(deepcopy(puzzle_input))}")

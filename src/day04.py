#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ipdb

from copy import deepcopy

from common.meta_utils import get_puzzle_input


def parse_input(puzzle_input):
    cards = {}
    for card in puzzle_input:
        card_id, numbers_win, numbers_card = [entry.strip() for entry in card.replace(':', '|').split('|')]
        cards[int(card_id.split()[1])] = {
            'numbers_win': [int(num) for num in numbers_win.split()],
            'numbers_card': [int(num) for num in numbers_card.split()],
            'amount': 1
        }
    return cards


def part1(puzzle_input):
    cards = parse_input(puzzle_input)
    score = 0
    for card in cards.values():
        numbers_common = list(set(card['numbers_win']) & set(card['numbers_card']))
        score += int(2**(len(numbers_common) - 1))

    return score


def part2(puzzle_input):
    cards = parse_input(puzzle_input)

    for kk in [*cards.keys()]:
        card = cards[kk]
        numbers_common = list(set(card['numbers_win']) & set(card['numbers_card']))

        for ii in range(kk, kk + len(numbers_common)):
            try:
                cards[ii + 1]['amount'] += card['amount']
            except KeyError:
                pass

    return sum([vv['amount'] for vv in cards.values()])


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(filename=__file__)
    print(f"Part 1 solution: {part1(deepcopy(puzzle_input))}")
    print(f"Part 2 solution: {part2(deepcopy(puzzle_input))}")

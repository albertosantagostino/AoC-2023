#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from copy import deepcopy
from collections import Counter, OrderedDict
from functools import cmp_to_key

from common.meta_utils import get_puzzle_input


def evaluate_hands(hand, consider_jacks):
    frequency = dict(Counter(ch[0] for ch in hand))
    if consider_jacks:
        frequency_sorted = sorted(frequency, key=frequency.get)
        try:
            frequency_sorted.remove('J')
        except ValueError:
            pass
        try:
            hand = hand.replace('J', frequency_sorted[-1])
        except IndexError:
            pass
        frequency = dict(Counter(ch[0] for ch in hand))

    if len(frequency) == 1:
        return 6
    elif len(frequency) == 5:
        return 0
    elif len(frequency) == 3 and 3 not in frequency.values():
        return 2
    elif len(frequency) == 4:
        return 1
    elif len(frequency) == 2:
        if 1 in frequency.values():
            return 5
        else:
            return 4
    else:
        return 3


def compare_hands(hand1, hand2, consider_jacks):
    card_strength = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    if not consider_jacks:
        card_strength.pop(0)

    val1, val2 = evaluate_hands(hand1, consider_jacks), evaluate_hands(hand2, consider_jacks)
    if val1 == val2:
        for card1, card2 in zip(hand1, hand2):
            if card1 != card2:
                return card_strength.index(card1) - card_strength.index(card2)

    return val1 - val2


def solve(puzzle_input, consider_jacks=False):
    hands_bids = {xx.split()[0]: int(xx.split()[1]) for xx in puzzle_input}

    # Sort hands (from weakest to strongest)
    sorted_keys = sorted([*hands_bids.keys()],
                         key=cmp_to_key(lambda val1, val2: compare_hands(val1, val2, consider_jacks)))
    sx = OrderedDict((kk, hands_bids[kk]) for kk in sorted_keys)

    res = 0
    for idx, vv in enumerate(sx.values()):
        res += (idx+1) * vv

    return res


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(filename=__file__)
    print(f"Part 1 solution: {solve(deepcopy(puzzle_input))}")
    print(f"Part 2 solution: {solve(deepcopy(puzzle_input), consider_jacks=True)}")

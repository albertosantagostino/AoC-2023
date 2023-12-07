#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ipdb

from copy import deepcopy

from common.meta_utils import get_puzzle_input


def parse_input(puzzle_input):
    puzzle_input = [el for el in puzzle_input if el]
    seeds = [int(el) for el in puzzle_input[0].split()[1:]]

    almanac = {}
    curr_key = None
    for ii in range(1, len(puzzle_input)):
        #ipdb.set_trace()
        if 'map' in puzzle_input[ii]:
            curr_key = puzzle_input[ii].split()[0]
            almanac[curr_key] = []
        else:
            almanac[curr_key].append(tuple(int(el) for el in puzzle_input[ii].split()))

    return seeds, almanac


def run_lookup(initial_value, lookup_key, almanac):

    for destination_start, source_start, range_lenght in almanac[lookup_key]:
        if initial_value >= source_start and initial_value <= source_start + range_lenght:
            return initial_value + destination_start - source_start
    return initial_value


def part1(seeds, almanac):

    locations = []
    for seed in seeds:
        aa = run_lookup(seed, 'seed-to-soil', almanac)
        bb = run_lookup(aa, 'soil-to-fertilizer', almanac)
        cc = run_lookup(bb, 'fertilizer-to-water', almanac)
        dd = run_lookup(cc, 'water-to-light', almanac)
        ee = run_lookup(dd, 'light-to-temperature', almanac)
        ff = run_lookup(ee, 'temperature-to-humidity', almanac)
        res = run_lookup(ff, 'humidity-to-location', almanac)
        locations.append(res)

    return min(locations)


def part2(seeds, almanac):

    seeds


if __name__ == "__main__":
    puzzle_input = [
        'seeds: 79 14 55 13', '', 'seed-to-soil map:', '50 98 2', '52 50 48', '', 'soil-to-fertilizer map:', '0 15 37',
        '37 52 2', '39 0 15', '', 'fertilizer-to-water map:', '49 53 8', '0 11 42', '42 0 7', '57 7 4', '',
        'water-to-light map:', '88 18 7', '18 25 70', '', 'light-to-temperature map:', '45 77 23', '81 45 19',
        '68 64 13', '', 'temperature-to-humidity map:', '0 69 1', '1 0 69', '', 'humidity-to-location map:', '60 56 37',
        '56 93 4'
    ]
    #puzzle_input = get_puzzle_input(filename=__file__)
    seeds, almanac = parse_input(puzzle_input)
    print(f"Part 1 solution: {part1(seeds, almanac)}")
    print(f"Part 2 solution: {part2(seeds, almanac)}")

# Advent of Code 2023 🎄

<div align="center">

| Day                                        | 1   | 2   | 📃                        | ⏲️   | | Day                                        | 1   | 2   | 📃                        | ⏲️   |
| ------------------------------------------ | :-: | :-: | :-----------------------: | :--: |-| -------------------------------------------| :-: | :-: | :-----------------------: | :--: |
| [01](https://adventofcode.com/2023/day/1)  | ⭐  | ⭐  | [day01.py](src/day01.py)  | 🟢🟢 | | [14](https://adventofcode.com/2023/day/14) |     |     |                           |      |
| [02](https://adventofcode.com/2023/day/2)  | ⭐  | ⭐  | [day02.py](src/day02.py)  | 🟢🟢 | | [15](https://adventofcode.com/2023/day/15) |     |     |                           |      |
| [03](https://adventofcode.com/2023/day/3)  |     |     |                           |      | | [16](https://adventofcode.com/2023/day/16) |     |     |                           |      |
| [04](https://adventofcode.com/2023/day/4)  | ⭐  | ⭐  | [day04.py](src/day04.py)  | 🟢🟢 | | [17](https://adventofcode.com/2023/day/17) |     |     |                           |      |
| [05](https://adventofcode.com/2023/day/5)  | ⭐  |     | [day05.py](src/day05.py)  | 🟢   | | [18](https://adventofcode.com/2023/day/18) |     |     |                           |      |
| [06](https://adventofcode.com/2023/day/6)  | ⭐  | ⭐  | [day06.py](src/day06.py)  | 🟡🟡 | | [19](https://adventofcode.com/2023/day/19) |     |     |                           |      |
| [07](https://adventofcode.com/2023/day/7)  | ⭐  | ⭐  | [day07.py](src/day07.py)  | 🟢🟢 | | [20](https://adventofcode.com/2023/day/20) |     |     |                           |      |
| [08](https://adventofcode.com/2023/day/8)  |     |     |                           |      | | [21](https://adventofcode.com/2023/day/21) |     |     |                           |      |
| [09](https://adventofcode.com/2023/day/9)  |     |     |                           |      | | [22](https://adventofcode.com/2023/day/22) |     |     |                           |      |
| [10](https://adventofcode.com/2023/day/10) |     |     |                           |      | | [23](https://adventofcode.com/2023/day/23) |     |     |                           |      |
| [11](https://adventofcode.com/2023/day/11) |     |     |                           |      | | [24](https://adventofcode.com/2023/day/24) |     |     |                           |      |
| [12](https://adventofcode.com/2023/day/12) |     |     |                           |      | | [25](https://adventofcode.com/2023/day/25) |     |     |                           |      |
| [13](https://adventofcode.com/2023/day/13) |     |     |                           |      | |                                            |     |     |                           |      |

<sub>🟢 < 1 day | 🟡 1÷7 days | 🟠 = 7+ days</sub>

</div>

## 🎵 On the Nth day of Christmas, my true love sent to me 🎶

1. A [meme](https://knowyourmeme.com/memes/trebuchets) from 2015
2. A tavern game from a DnD setting
3. -
4. An elf with scratchcards addiction
5. -
6. A race condition pun?
7. Yet another elf addicted to gambling

*Only added when both parts are completed*

## Suggested Christmas songs 🔔

- [I Want a Hippopotamus for Christmas](https://www.youtube.com/watch?v=57vrqCENNPc)
- [Merry Merry](https://www.youtube.com/watch?v=Mo41lMhxR5Q)

## How to run

`Python 3.9` and `poetry` required. From the root folder:

````bash
# Prepare virtualenv (will be placed at .venv/). Only needed the first time
poetry install
# Activate the virtualenv
source .venv/bin/activate
# Run the solution
python3.9 src/day__.py
````

The script `src/day00_template.py` is a template  
Scripts are configured to automatically download puzzle inputs

### Setup (automatic puzzle input download)

To get and set your credentials: login into [AoC](https://adventofcode.com/), open the Web Developer Tools (`CTRL+SHIFT+I`). Go to the `Storage` tab (or `Application/Storage` in Chrome) and copy the value of your `session` cookie into the `aoc_cookie` entry of `config.json`

**Security note**: do not commit the `config.json` file as it contains your personal cookie. Run `git update-index --assume-unchanged config.json` to prevent git from tracking the file

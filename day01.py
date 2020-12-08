import itertools
import math

def return_list() -> list:
    filepath = r'AOC2020/day01input.txt'
    with open(filepath, 'r') as file:
        return [int(line) for line in file]

def find_sum(num_list: list, multiples: int) -> int:
    return [(math.prod(combos)) for combos in itertools.combinations(num_list, multiples) if sum(combos) == 2020][0]

def main():
    num_list = return_list()
    print("DAY 01: the two numbers multiplied are:", find_sum(num_list, 2))
    print("DAY 01: the three numbers multiplied are:", find_sum(num_list, 3))

if __name__ == '__main__':
    main()

import math
def get_input() -> list:
    with open(r'AOC2020/day03input.txt', 'r') as file:
        file_list = file.read().splitlines()
        return [[char for char in line] for line in file_list]

def tree_count(forest:list, x_traj:int, y_traj:int):
    tree_count = 0
    x_len = len(forest[0])
    y_len = len(forest)
    for cur_x, cur_y in zip(range(0, y_len * x_traj, x_traj), range(0, y_len, y_traj)):
        new_x = cur_x % x_len
        if forest[cur_y][new_x] == '#':
            tree_count += 1
    return tree_count

def main():
    # Part 1
    print(f"\nDay 03: part one, tree count is {tree_count(get_input(), 3, 1)}")
    # Part 2
    traj_list = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    tree_multiple = [tree_count(get_input(), traj[0], traj[1]) for traj in traj_list]
    print(f"DAY 03: part two, tree multipied is {math.prod(tree_multiple)}")

if __name__ == '__main__':
    main()

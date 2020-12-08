def get_input() -> list:
    with open(r'AOC2020/day06input.txt', 'r') as file:
        file_list = file.read().split("\n\n")
    return file_list

def part_one(ans_list:list):
    for loc, ans in enumerate(ans_list):
        ans_list[loc] = set(ans.replace("\n", ""))
    ans_cnt = sum([len(grp) for grp in ans_list])
    return ans_cnt

def part_two(ans_list:list):
    ans_list = [loc.split('\n') for loc in ans_list]
    return sum([help_two(loc) for loc in ans_list])

def help_two(loc):
    for i, ans in enumerate(loc):
        loc[i] = set(ans)
    compare = loc[0]
    for ans in loc:
        compare = compare & ans
    return len(compare)

def main():
    print(f'\nDAY 06: count of answers by group is {part_one(get_input())}')
    print(f'DAY 06: count of unique answers by group is {part_two(get_input())}')

if __name__ == '__main__':
    main()

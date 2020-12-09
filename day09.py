import itertools as it
def get_input() -> list:
    with open(r'AOC2020/day09input.txt', 'r') as file:
        file_list = file.read().splitlines()
        file_list = [int(to_num) for to_num in file_list]
    return file_list

def part_one(code_list, slice_size):
    for chunk in range(len(code_list) - slice_size):
        ind = False
        check_num = code_list[chunk + slice_size]
        for combos in it.combinations(code_list[chunk:chunk + slice_size], 2):
            if sum(combos) == check_num:
                ind = True
                break
        if not ind:
            return check_num

def part_two(code_list:list, bad_num:int):
    for i in range(len(code_list)):
        for j in range(i, len(code_list)):
            if sum(code_list[i:j+1]) == bad_num:
                return min(code_list[i:j+1]) + max(code_list[i:j+1])

def main():
    bad_num = part_one(get_input(), 25)
    print(f'\nDAY 09 Part 1:  {bad_num}')
    print(f'DAY 09 Part 2:  {part_two(get_input(), bad_num)}')

if __name__ == '__main__':
    main()

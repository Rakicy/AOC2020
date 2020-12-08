def parse_line(line:str) -> list:
    dash_loc = line.find('-')
    space_loc = line.find(' ')
    colon_loc = line.find(':')
    low = int(line[:dash_loc])
    high = int(line[dash_loc + 1:space_loc])
    letter = line[colon_loc - 1: colon_loc]
    password = line[colon_loc + 2:]
    return low, high, letter, password


def is_valid_part_one(low:int, high:int, letter:str, password:str) -> bool:
    letter_count = password.count(letter)
    if low <= letter_count <= high:
        return True
    return False

def is_valid_part_two(low:int, high:int, letter:str, password:str) -> bool:
    first_pos = letter == password[low - 1]
    second_pos = letter == password[high - 1]
    return first_pos ^ second_pos

def main():
    # part 1 test case
    corr_count = 0
    test_case = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']
    for line in test_case:
        low, high, letter, password = parse_line(line)
        if is_valid_part_one(low, high, letter, password):
            corr_count += 1
    print(f'\nDAY 02: The test case for part 1 has {corr_count} passwords correct.')
    # part 1 full list
    corr_count = 0
    with open(r'AOC2020/day02input.txt', 'r') as file:
        for line in file:
            low, high, letter, password = parse_line(line)
            if is_valid_part_one(low, high, letter, password):
                corr_count += 1
    print(f'DAY 02: The full list for part 1 has {corr_count} passwords correct.')
    #part 2 test case
    corr_count = 0
    for line in test_case:
        low, high, letter, password = parse_line(line)
        if is_valid_part_two(low, high, letter, password):
            corr_count += 1
    print(f'DAY 02: The test case for part 2 has {corr_count} passwords correct.')
    # part 2 full list
    corr_count = 0
    with open(r'AOC2020/day02input.txt', 'r') as file:
        for line in file:
            low, high, letter, password = parse_line(line)
            if is_valid_part_two(low, high, letter, password):
                corr_count += 1
    print(f'DAY 02: The full list for part 2 has {corr_count} passwords correct.')
            
    
if __name__ == '__main__':
    main()

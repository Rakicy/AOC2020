import pandas as pd
import numpy as np

def get_input() -> list:
    with open(r'AOC2020/day04input.txt', 'r') as file:
        file_list = file.read().split('\n\n')
    id_list = [line.replace('\n', ' ').split(' ') for line in file_list]
    return id_list

def create_df_row(id:list) -> dict:
    item_id = {'byr':np.NaN, 'iyr':np.NaN, 'eyr':np.NaN, 'hgt':np.NaN, 'hgt_type':"", 'hcl':np.NaN, 'ecl':np.NaN, 'pid':np.NaN, 'cid':""}
    for id_part in id:
        descrip = id_part[:3]
        value = id_part[4:]
        if descrip == 'hgt' and (value[-2:] == 'cm' or value[-2:] == 'in'):
            item_id['hgt_type'] = value[-2:]
            value = value[:-2]
        if descrip in ['byr', 'iyr', 'eyr', 'hgt']:
            value = int(value)
        item_id[descrip] = value
    return item_id

def create_df(id_list:list):
    col_list = ['byr', 'iyr', 'eyr', 'hgt', 'hgt_type', 'hcl', 'ecl', 'pid', 'cid']
    df = pd.DataFrame(columns=col_list)
    data_list = []
    for id in id_list:
        data_list.append(create_df_row(id))
    df = df.append(data_list, ignore_index = True)
    return df

def part_one(df_id):
    valid_ids = df_id.dropna(axis = 0)
    return valid_ids, len(valid_ids.index)

def part_two(valid_ids):
    valid_data_count = 0
    eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    #filter data
    valid_data = valid_ids[(valid_ids.byr >= 1920) & (valid_ids.byr <= 2002) & (valid_ids.iyr >= 2010) & (valid_ids.iyr <= 2020) & (valid_ids.eyr >= 2020) & (valid_ids.eyr <= 2030) & (valid_ids.ecl.isin(eye_colors)) & (valid_ids.pid.str.len() == 9) & (valid_ids.hgt_type.isin(['cm', 'in'])) & (((valid_ids.hgt_type == 'cm') & (valid_ids.hgt >=  150) & (valid_ids.hgt <= 193)) | ((valid_ids.hgt_type == 'in') & (valid_ids.hgt >=  59) & (valid_ids.hgt <= 76))) & (valid_ids.hcl.str.count('^#(?:[0-9a-fA-F]{1,2}){6}$'))]

    valid_data_count = len(valid_data.index)
    return valid_data_count

def main():
    df_id = create_df(get_input())
    # Part 1
    valid_ids, valid_id_count = part_one(df_id)
    print(f"\nDAY 04: The number of valid IDs is: {valid_id_count}")
    # Part 2
    print(f"DAY 04: The number of valid IDs with valid data is {part_two(valid_ids)}")

if __name__ == '__main__':
    main()

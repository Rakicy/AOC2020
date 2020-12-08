import numpy as np

def get_input() -> list:
    with open(r'AOC2020/day05input.txt', 'r') as file:
        file_list = file.read().splitlines()
    return file_list

def fill_list(seat_list:list):
    plane_seats = np.zeros((8, 128), np.int)
    for seat in seat_list:
        y_dir, x_dir = seat[:7], seat[-3:]
        x_loc, y_loc = find_x_axis(x_dir), find_y_axis(y_dir)
        plane_seats[x_loc][y_loc] = y_loc * 8 + x_loc
    return plane_seats
         
def find_x_axis(x_dir:str) -> int:
    x_axis = [0, 7]
    for dir in x_dir:
        change_amt = round((x_axis[1] - x_axis[0])/2)
        if dir == 'R':
            x_axis[0] += change_amt
        else:
            x_axis[1] -= change_amt
    if x_dir[-1] == 'R':
        return x_axis[1]
    else:
        return x_axis[0]
            
def find_y_axis(y_dir:str) -> int:
    y_axis = [0, 127]
    for dir in y_dir:
        change_amt = round((y_axis[1] - y_axis[0])/2)
        if dir == 'B':
            y_axis[0] += change_amt
        else:
            y_axis[1] -= change_amt
    if y_dir[-1] == 'B':
        return y_axis[1]
    else:
        return y_axis[0]

def part_one(plane_seats):
    return plane_seats.max()

def part_two(plane_seats):
    id_list = plane_seats.flatten()
    sorted_id = np.sort(id_list)
    for i, seat_id in enumerate(sorted_id):
        if i != len(sorted_id) - 1:
            if sorted_id[i + 1] - sorted_id[i] == 2:
                return sorted_id[i] + 1
        
def main():
    seat_filled_list = fill_list(get_input())
    print(f'\nDAY 05: The maximum seat ID is: {part_one(seat_filled_list)}')
    print(f'DAY 05: My seat ID is: {part_two(seat_filled_list)}')

if __name__ == '__main__':
    main()

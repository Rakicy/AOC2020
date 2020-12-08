def get_input() -> list:
    with open(r'AOC2020/day08input.txt', 'r') as file:
        file_list = file.read().splitlines()
        for ind, ins in enumerate(file_list):
            file_list[ind] = [ins[:3], int(ins[4:])]
    return file_list

def part_one(inst_list:list):
    accum = 0
    cur_ins = 0
    seen = {}
    while True:
        if cur_ins in seen:
            return accum
        ins = inst_list[cur_ins][0]
        if ins == "nop":
            seen[cur_ins] = True
            cur_ins += 1
        elif ins == "acc":
            seen[cur_ins] = True
            accum += inst_list[cur_ins][1]
            cur_ins += 1
        elif ins == "jmp":
            seen[cur_ins] = True
            cur_ins += inst_list[cur_ins][1]
            
        

def part_two(inst_list:list):
    accum = 0
    cur_ins = 0
    seen = {}
    for change in range(len(inst_list)):
        new_inst_list = get_input() #recreating data is visibly faster than copy.deepcopy(inst_list)
        if new_inst_list[change][0] == "jmp":
            new_inst_list[change][0] = "nop"
        elif new_inst_list[change][0] == "nop":
            new_inst_list[change][0] = "jmp"
        accum = 0
        cur_ins = 0
        seen = {}
        while True:
            ins = new_inst_list[cur_ins][0]
            if ins == "nop":
                seen[cur_ins] = True
                cur_ins += 1
            elif ins == "acc":
                seen[cur_ins] = True
                accum += new_inst_list[cur_ins][1]
                cur_ins += 1
            elif ins == "jmp":
                seen[cur_ins] = True
                cur_ins += new_inst_list[cur_ins][1]
            if cur_ins in seen:
                break
            if cur_ins == len(new_inst_list) - 1:
                if new_inst_list[cur_ins][0] == 'acc':
                     accum += new_inst_list[cur_ins][1]
                return accum

def main():
    print(f'\nDAY 08 Part 1:  {part_one(get_input())}')
    print(f'DAY 08 Part 2:  {part_two(get_input())}')

if __name__ == '__main__':
    main()

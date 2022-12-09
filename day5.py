import copy
# Function process a move from the list. Fifo parameter its to set rearrangement mode has fifo or lifo.
# For part one we need lifo instead we use fifo on part two
def move_crate(origin,destiny,moves, fifo):
    aux_list = []
    
    for i in range(moves):
        aux_list.append(origin.pop())
    
    if fifo:
        aux_list.reverse()

    destiny.extend(aux_list)

crates = {'1': [], '2': [], '3': [], '4': [], '5': [], '6': [],
    '7': [], '8': [], '9': []
}


# Read starting crate position
with open('input_day5bis.txt', 'r') as f:
    while True:
        line = f.readline().strip()
        
        if not line:
            break
        
        line = line.replace(' ', '').replace('[', '').replace(']','')

        for i in range(0,9):
            if line[i] != '.':
                crates[str(i+1)].append(line[i])
    
    f.close()
        

for item in crates.values():
    item.reverse()

# We create a copy from the crates order read from file
crates_parte_two = copy.deepcopy(crates)

# Read the list of moves crates
with open('input_day5.txt', 'r') as f:
    while True:
        line = f.readline().strip()

        if not line:
            break

        line_a = copy.deepcopy(line.split(' '))
        line_b = copy.deepcopy(line.split(' '))
        # move_crate(crates[line_a[3]], crates[line_a[5]], int(line_a[1]), False)
        move_crate(crates_parte_two[line_b[3]], crates_parte_two[line_b[5]], int(line_b[1]), True)

print('--- PART ONE ---')
for crate in crates.values():
    print(crate[-1])

print('--- PART TWO ---')
for crate in crates_parte_two.values():
    print(crate[-1])

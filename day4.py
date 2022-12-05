### PART ONE ###
with open('input_day4.txt','r') as f:  
    result = 0

    while True:
        line = f.readline().strip()

        if not line:
            break
        
        section = line.split(',')
        first_assignments = [int(i) for i in section[0].split('-')]
        second_assignments = [int(i) for i in section[1].split('-')]
        
        if first_assignments[0] >= second_assignments[0] and first_assignments[1] <= second_assignments[1]:
            result += 1
        elif second_assignments[0] >= first_assignments[0] and second_assignments[1] <= first_assignments[1]:
            result += 1
        
    f.close()

print('--- PART ONE ---')
print(result)

### PART TWO ###
with open('input_day4.txt','r') as f:    
    result = 0

    while True:
        line = f.readline().strip()

        if not line:
            break
        
        section = line.split(',')
        first_assignments = [int(i) for i in section[0].split('-')]
        second_assignments = [int(i) for i in section[1].split('-')]
        
        if len(set(range(first_assignments[0],first_assignments[1]+1)) & set(range(second_assignments[0],second_assignments[1]+1))) != 0:
            result += 1

    f.close()

print('--- PART TWO ---')
print(result)
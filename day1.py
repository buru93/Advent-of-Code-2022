### PART ONE ###
with open('input_day1.txt','r') as f:
    content = f.readline()
    calories = 0
    calories_max = 0
    
    while True:
        line = f.readline()
        
        if not line:
            break
        
        if line == '\n':
            if calories_max < calories:
                calories_max = calories
            calories = 0
        else:
            calories += int(line.strip())
    f.close()

print(calories_max)

### PART TWO ###
with open('input_day1.txt','r') as f:
    content = f.readline()
    calories = 0
    calories_list = []
    
    while True:
        line = f.readline()
        
        if not line:
            break
        
        if line == '\n':
            calories_list.append(calories)
            calories = 0
        else:
            calories += int(line.strip())
    f.close()


calories_list.sort(reverse=True)

print(sum(calories_list[0:3]))
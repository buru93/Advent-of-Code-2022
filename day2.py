# A X - Rock --> 1 point 
# B Y - Paper --> 2 point
# C Z - Scissors --> 3 point
# Rock > Scissors > Paper > Rock

### PART ONE ###
posible_results = { 'AX': 4, 'AY': 8, 'AZ': 3, 'BX': 1, 'BY': 5, 'BZ': 9, 'CX': 7, 'CY': 2, 'CZ':  6 }

with open('input_day2.txt','r') as f:
    
    result = 0
    
    while True:
        # line = ''.join(f.readline().split(' '))
        line = f.readline().strip()
        
        
        if not line:
            break
        
        # if line == '\n':
        #     print('------')
        # else:
        #     print(line.strip())
        result  += posible_results[''.join(line.split(' '))]
    
    f.close()

print('--- PART ONE ---')
print(result)

### PART TWO ###
# Now for in this case the second letter indicate us the result we should get(X = loss, Y = draw, Z = win)
posible_results_b = { 'AX': 3, 'AY': 4, 'AZ': 8, 'BX': 1, 'BY': 5, 'BZ': 9, 'CX': 2, 'CY': 6, 'CZ': 7 }

with open('input_day2.txt','r') as f:
    
    result_b = 0
    
    while True:
        # line = ''.join(f.readline().split(' '))
        line = f.readline().strip()
        
        
        if not line:
            break
        
        # if line == '\n':
        #     print('------')
        # else:
        #     print(line.strip())
        result_b  += posible_results_b[''.join(line.split(' '))]
        
    f.close()

print('--- PART TWO ---')
print(result_b)
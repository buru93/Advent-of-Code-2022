### PART ONE ###
import string

letters_value  = dict([(index, x) for x, index in enumerate(string.ascii_letters, start=1)])

with open('input_day3.txt','r') as f:    
    result = 0

    while True:
        line = f.readline().strip()

        if not line:
            break
        
        split1 = line[0:int(len(line)/2)]
        split2 = line[int(len(line)/2):]
              
        for letter in split1:
            if letter in split2:
                result += letters_value[letter]
                break

    f.close()

print('--- PART ONE ---')
print(result)

### PART TWO ###
import string

letters_value  = dict([(index, x) for x, index in enumerate(string.ascii_letters, start=1)])

with open('input_day3.txt','r') as f:
    result = 0
    number_of_lines = 0
    lines = []
    
    while True:
        line = f.readline().strip()
        
        if not line:
            break
        
        lines.append(line)
        number_of_lines += 1
        
        if number_of_lines == 3:
            
            for item in lines[0]:
                if item in lines[1]:
                    if item in lines[2]:
                        result += letters_value[item]
                        break
            number_of_lines = 0
            lines = []
        
                
        # split1 = line[0:int(len(line)/2)]
        # split2 = line[int(len(line)/2):]
              
        # for letter in split1:
        #     if letter in split2:
        #         result += letters_value[letter]
        #         break

    f.close()

print('--- PART TWO ---')
print(result)
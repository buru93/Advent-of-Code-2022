with open('input_day6.txt','r') as f:
    content = f.read()

starter_packet = 0
marker_packet = 4
starter_message = 0
marker_message = 14

# Loop to get the first packet-marker
while True:
    if len(set(content[starter_packet:marker_packet])) == 4:
        first_packet = marker_packet
        break
    
    starter_packet += 1
    marker_packet += 1

while True:
    if len(set(content[starter_message:marker_message])) == 14:
        first_message = marker_message
        break
    
    starter_message += 1
    marker_message += 1

print(f"PART ONE - Marker equal to {first_packet}")
print(f"PART TWO - Marker equal to {first_message}")
dial = 50
count = 0
lines = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']

for line in lines:
    direction = line[0]
    distance = int(line[1:])


    passes = (distance - 1) // 100

    if direction == "R":
        if (dial + distance) % 100 < dial:
             passes += 1
        

    elif direction == "L":
        if dial - distance < 0:
            passes += 1
            remaining_distance = distance - dial
            passes += (remaining_distance - 1) // 100
            
    count += passes

    if direction == "L":
        new_dial = dial - distance
    else:
        new_dial = dial + distance
    dial = new_dial % 100
    
print(count)

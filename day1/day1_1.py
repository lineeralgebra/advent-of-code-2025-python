dial = 50
count = 0

lines = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']

for line in lines:
    direction = line[0]
    distance = int(line[1:])

    if direction == "L":
        new_dial = dial - distance
    else:
        new_dial = dial + distance
    dial = new_dial % 100

    if dial == 0:
        count += 1

print(count)

def solve(instructions):
    dial = 50
    count = 0

    for instruction in instructions:
        direction = instruction[0] # L or R
        distance = int(instruction[1:]) # and its the distance like 12 or 01

        if direction == "L":
            dial -= distance
        else:
            dial += distance

        dial = dial % 100
        
        print(f"{instruction} → Kadran: {dial}")

        if dial == 0:
            count += 1

    return count 

test_input = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

instructions_list = test_input.strip().split('\n')
final_count = solve(instructions_list) # Pass the list, not the single string.

print(final_count)

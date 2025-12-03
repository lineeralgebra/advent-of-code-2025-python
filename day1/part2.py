def solve_part2_correct(instructions):
    dial = 50
    count = 0

    for instruction in instructions:
        direction = instruction[0]
        distance = int(instruction[1:])
        step = -1 if direction == "L" else 1

        for _ in range(distance):
            dial = (dial + step) % 100
            if dial == 0:
                count += 1

    return count


instructions_list = [
   
]

final_count = solve_part2_correct(instructions_list)
print("Part 2 password:", final_count)

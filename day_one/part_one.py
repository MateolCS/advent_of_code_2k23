
def part_one(path):
    calibration_sum = 0
    f = open(path, "r")
    lines = f.readlines()

    for line in lines:
        first_number = None
        second_number = None
        for char in line:
            if char.isdigit():
                if first_number is None:
                    first_number = char
                else:
                    second_number = char

        if second_number is None:
            calibration_sum += int(first_number + first_number)
        else:
            calibration_sum += int(first_number + second_number)
    return calibration_sum

print(part_one("input"))




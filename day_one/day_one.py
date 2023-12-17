

def task_one(path):
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

#print(task_one("input"))

def task_two(path):
    f = open(path, "r")
    lines = f.readlines()
    calibration_sum = 0
    for line in lines:
        numbers = []
        for i in range(len(line)):
            if line[i].isdigit():
                numbers.append(line[i])
            if line[i] == "o" and line[i:i+3] == "one":
                numbers.append("1")
            if line[i] == "t" and line[i:i+3] == "two":
                numbers.append("2")
            if line[i] == "t" and line[i:i+5] == "three":
                numbers.append("3")
            if line[i] == "f" and line[i:i+4] == "four":
                numbers.append("4")
            if line[i] == "f" and line[i:i+4] == "five":
                numbers.append("5")
            if line[i] == "s" and line[i:i+3] == "six":
                numbers.append("6")
            if line[i] == "s" and line[i:i+5] == "seven":
                numbers.append("7")
            if line[i] == "e" and line[i:i+5] == "eight":
                numbers.append("8")
            if line[i] == "n" and line[i:i+4] == "nine":
                numbers.append("9")
            if line[i] == "z" and line[i:i+4] == "zero":
                numbers.append("0")
        current_number = numbers[0] + numbers[-1]
        calibration_sum += int(current_number)
    return calibration_sum




print(task_two("input"))


import os
import re
import itertools

here = os.path.dirname(__file__)
input_path = os.path.join(here, "day7input.txt")

with open(input_path, "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]


def op_permutations(ops, slots):
    return list(itertools.product(ops, repeat=slots))

# PART A
def isValidPermPartA(target : int, perm_list : list, number_list : list):
    result = int(number_list[0])
    for idx, perm in enumerate(perm_list):
        if perm == "*":
            result *= int(number_list[idx + 1])
        else:
            result += int(number_list[idx + 1])

    if int(target) == int(result):
        return True, result
    return False, result

def calibrationResultPartA(lines : list) -> int:
    sum = 0
    valid = False
    for line in lines:
        target, numbers = line.split(":")
        number_list = numbers.split()
        for perm in op_permutations(["+", "*"], len(number_list) - 1 ):
            perm_list = list(perm)
            valid, result = isValidPermPartA(target, perm_list, number_list)
            if valid == True:
                sum += result
                valid = False
                break

    return sum


#PART B
def isValidPermPartB(target : int, perm_list : list, number_list : list):
    result = int(number_list[0])
    for idx, perm in enumerate(perm_list):
        if perm == "*":
            result *= int(number_list[idx + 1])
        elif perm == "||":
            result = int(''.join(str(result).split() + number_list[idx + 1].split()))
        else:
            result += int(number_list[idx + 1])

    if int(target) == int(result):
        return True, result
    return False, result


def calibrationResultPartB(lines : list) -> int:
    sum = 0
    valid = False
    for line in lines:
        target, numbers = line.split(":")
        number_list = numbers.split()
        for perm in op_permutations(["+", "*", "||"], len(number_list) - 1 ):
            perm_list = list(perm)
            valid, result = isValidPermPartB(target, perm_list, number_list)
            if valid == True:
                sum += result
                valid = False
                break

    return sum

if __name__ == "__main__":
    print(f"PART A: {calibrationResultPartA(lines)}")
    print(f"PART B: {calibrationResultPartB(lines)}")
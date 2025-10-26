from ordered_set import OrderedSet
import os

here = os.path.dirname(__file__)
input_path = os.path.join(here, "day2input.txt")

perfect_sets = []

def is_safe(input_list: list) -> bool:
    input_list = [int(x) for x in input_list if x.strip()]
    seen = list(OrderedSet(input_list))

    if len(seen) != len(input_list):
        return False
    if seen != list(sorted(input_list)) and seen != list(reversed(sorted(input_list))):
        return False
    for idx, val in enumerate(seen):
        if ( (idx + 1) <= ( int(len(seen) - 1) )):
            diff = abs(int(seen[idx]) - int(seen[idx + 1]))
            if (diff > 3) or (diff < 1):
                return False

    return True

def is_safe_dampened(input_list: list) -> bool:

    if is_safe(input_list):
        return True

    for i in range(len(input_list)):
        test_list = input_list[:i] + input_list[i+1:]
        if is_safe(test_list):
            return True
    return False


with open(input_path, "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]

perfect_sets = [line.split() for line in lines if is_safe(line.split())]
perfect_sets_damp = [line.split() for line in lines if is_safe_dampened(line.split())]


if __name__ == "__main__":
    print (f"PART A: {len(perfect_sets)}\n")
    print (f"PART B: {len(perfect_sets_damp)}\n")



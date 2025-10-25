import os

here = os.path.dirname(__file__)
input_path = os.path.join(here, "day1input.txt")

with open(input_path, "r", encoding="utf-8") as f:
    part_a_lines = [line for line in f if line.strip()]

first_col = []
second_col = []
for line in part_a_lines:
    parts = line.strip().split()
    if len(parts) >= 2:
        first_col.append(parts[0])
        second_col.append(parts[1])
    else:
        first_col.append(parts[0] if parts else None)
        second_col.append(None)


def compare_lists(list1, list2) -> list[int]:
    return [abs(int(list1[idx]) - int(list2[idx])) for idx, list1[idx] in enumerate(list1) if idx < len(list2)]

def sum_list(input_list) -> int:
    return sum(int(x) for x in input_list if x is not None)

def similarity(list1, list2) -> int:
    left_numbers = [ int(list1[idx]) for idx, list1[idx] in enumerate(list1) if idx < len(list2) and list1[idx] in list2]
    sum = int(0)
    for idx, left_numbers[idx] in enumerate(left_numbers):
        left_val = left_numbers[idx]
        frequency = 0
        for idx2, list2[idx2] in enumerate(list2):
            if int(left_val) == int(list2[idx2]):
                frequency += 1

        sum += int(left_val) * frequency

    return sum
if __name__ == "__main__":

    unsorted_first_col = first_col.copy()
    unsorted_second_col = second_col.copy()

    # Part A
    (first_col).sort()
    (second_col).sort()
    distances = compare_lists(first_col, second_col)
    print(f"PART A: {sum_list(distances)}")


    # Part B
    similarity_score = similarity(unsorted_first_col, unsorted_second_col)
    print(f"PART B: {similarity_score}")



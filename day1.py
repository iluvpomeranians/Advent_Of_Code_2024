# ...existing code...
import os

here = os.path.dirname(__file__)
input_path = os.path.join(here, "day1input.txt")

with open(input_path, "r", encoding="utf-8") as f:
    lines = [line for line in f if line.strip()]

first_col = []
second_col = []
for line in lines:
    parts = line.strip().split()
    if len(parts) >= 2:
        first_col.append(parts[0])
        second_col.append(parts[1])
    else:
        first_col.append(parts[0] if parts else None)
        second_col.append(None)

(first_col).sort()
(second_col).sort()

def compare_lists(list1, list2) -> list[int]:
    return [abs(int(list1[idx]) - int(list2[idx])) for idx, list1[idx] in enumerate(list1) if idx < len(list2)]

def sum_list(input_list) -> int:
    return sum(int(x) for x in input_list if x is not None)

if __name__ == "__main__":
    # print(first_col)
    # print(second_col)
    distances = compare_lists(first_col, second_col)
    print(sum_list(distances))

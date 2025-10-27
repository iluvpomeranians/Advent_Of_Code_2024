import math
import os
import re

here = os.path.dirname(__file__)
input_path = os.path.join(here, "day5input.txt")

with open(input_path, "r", encoding="utf-8") as f:
    instructions = [line.strip() for line in f if line.strip()]

rules, updates, incorrect_updates = [], [], []

for line in instructions:
    (rules if "|" in line else updates).append(line.strip())

rules_dict = {}
for rule in rules:
            match = re.search(r"(\d+)\|(\d+)", rule)
            if match:
                x, y = match.groups()
                rules_dict.setdefault(x, []).append(y)

def analyze_updates():

    valid = False
    total = 0

    for update in updates:
        valid = False
        values = update.split(",")
        for i,val in enumerate(values):
            follow_list = rules_dict.get(f"{val}")
            if follow_list is not None:
                for follow_val in follow_list:
                    if follow_val not in values[:i]:
                        valid = True
                    else:
                        valid = False
                        break

            if valid == False:
                incorrect_updates.append(values)
                break

        if valid == True:
            total += int(values[math.floor(len(values)/2)])

    return total

def update_correction(incorrect_updates) -> int:
    valid = False
    total = 0
    idx = 0

    while idx < len(incorrect_updates):

        update_list = incorrect_updates[idx]
        valid = False
        for i,val in enumerate(update_list):
            follow_list = rules_dict.get(f"{val}")
            if follow_list is not None:
                for follow_val in follow_list:
                    if follow_val not in update_list[:i]:
                        valid = True
                    else:
                        valid = False
                        newlist = update_list.copy()
                        j = update_list.index(follow_val)
                        newlist.insert(i+1, newlist.pop(j))
                        incorrect_updates[idx] = newlist
                        break

            if valid == False:
                break

        if valid == True:
            total += int(update_list[math.floor(len(update_list)/2)])

            idx += 1

    return total


def update_correction_v2(incorrect_updates) -> int:
    total = 0
    idx = 0

    while idx < len(incorrect_updates):
        update_list = incorrect_updates[idx]
        print(f"Processing {update_list} @ {idx}")

        valid = True

        for i, val in enumerate(update_list):
            follow_list = rules_dict.get(val)
            if follow_list:
                for follow_val in follow_list:
                    # If this follow_val appears *before* val, it's out of order
                    if follow_val in update_list[:i]:
                        # Rearrange and retry
                        newlist = update_list.copy()
                        j = update_list.index(follow_val)
                        newlist.insert(i + 1, newlist.pop(j))
                        incorrect_updates[idx] = newlist

                        print(f"Reprocessing same index {idx} with new order: {newlist}")
                        valid = False
                        break

                if not valid:
                    break  # break out of inner loop to retry this update

        if valid:
            # If update is now valid, count its middle value
            total += int(update_list[len(update_list) // 2])
            idx += 1  # only move to next update if current one is valid

    print(f"Total: {total}")
    return total



if __name__ == "__main__":
    print(f"PART A: {analyze_updates()}\n")
    print(f"PART B: {update_correction(incorrect_updates)}\n")

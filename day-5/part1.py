# This is a problem from the 2024 Advent of Code calendar.
# Part 1 of Day 5

rules = {}
updates = []
correct_updates = []

# The goal of this function is to populate the two lists for this exercise
def input_lines():
    with open("input.txt",'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            if "|" in line:
                elements = line.split("|")
                if int(elements[0])not in rules:
                    rules[int(elements[0])] = []
                
                if int(elements[1]) not in rules:
                    rules[int(elements[1])] = []
                
                rules[int(elements[0])].append(int(elements[1]))
            else:
                updates.append([int(x) for x in line.split(",")])

def check_rules():
    for update in updates:
        correct = True
        for i in range(len(update)-1):
            if update[i+1] not in rules[update[i]]:
                correct = False
                break
            
        if correct:
            correct_updates.append(update)

def sum_correct_midpoints():
    sum = 0
    for update in correct_updates:
        sum += update[len(update)//2]

    print(sum)

def main():
    input_lines()
    check_rules()
    sum_correct_midpoints()

main()
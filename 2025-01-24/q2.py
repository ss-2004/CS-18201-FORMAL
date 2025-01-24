# 2. Design a Python program to verify simple Boolean expressions using truth tables.
#  Input a Boolean expression (e.g., (A and B) or (not A)), and generate the truth table for all
# possible values of the variables.
#  Compare the result against a user-provided expected truth table to verify its correctness.

import itertools

def generate_truth_table(expression, variables):
    truth_table = []
    for values in itertools.product([False, True], repeat=len(variables)):
        env = dict(zip(variables, values))
        result = eval(expression, {}, env)
        truth_table.append((values, result))
    return truth_table

def print_truth_table(truth_table, variables):
    header = variables + ["Result"]
    print("\t".join(header))
    for row in truth_table:
        values, result = row
        print("\t".join(map(str, values)) + "\t" + str(result))

def verify_truth_table(expression, variables, expected_truth_table):
    generated_truth_table = generate_truth_table(expression, variables)
    return generated_truth_table == expected_truth_table

expression = input("Enter a Boolean expression (e.g., (A and B) or (not A)): ")
variables = input("Enter the variables in the expression separated by spaces (e.g., A B): ").split()

truth_table = generate_truth_table(expression, variables)
print("Generated Truth Table:")
print_truth_table(truth_table, variables)

expected_truth_table = []
print("Enter the expected truth table (e.g., for A B Result):")
for _ in range(2 ** len(variables)):
    row = input().split()
    values = tuple(map(lambda x: x == 'True', row[:-1]))
    result = row[-1] == 'True'
    expected_truth_table.append((values, result))

is_correct = verify_truth_table(expression, variables, expected_truth_table)
if is_correct:
    print("The generated truth table matches the expected truth table.")
else:
    print("The generated truth table does not match the expected truth table.")

def arithmetic_arranger():
    problems = []
    for i in range(5):
        problem = input(f"Enter problem {i+1}: ")
        if problem == "":
            break
        problems.append(problem)

    # Check that there are no more than 5 problems
    if len(problems) > 5:
        return "Error: Too many problems."

    # Create empty lists for each line of the arranged problems
    first_line = []
    second_line = []
    dash_line = []
    result_line = []

    # Loop through each problem and split into operands and operator
    for problem in problems:
        parts = problem.split()

        # Check that each operand is a number
        if not parts[0].isnumeric() or not parts[2].isnumeric():
            return "Error: Numbers must only contain digits."

        # Check that the operator is valid
        if parts[1] != "+" and parts[1] != "-":
            return "Error: Operator must be '+' or '-'."

        # Convert operands to integers
        num1 = int(parts[0])
        num2 = int(parts[2])

        # Check that operands are no more than 4 digits long
        if num1 > 9999 or num2 > 9999:
            return "Error: Numbers cannot be more than four digits."

        # Determine the width of the problem
        width = max(len(parts[0]), len(parts[2])) + 2

        # Add operands and operator to the lines
        first_line.append(str(num1).rjust(width))
        second_line.append(parts[1] + str(num2).rjust(width - 1))
        dash_line.append("-" * width)

        # Calculate the result
        if parts[1] == "+":
            result = num1 + num2
        else:
            result = num1 - num2

        result_line.append(str(result).rjust(width))

    # Join the lines together with spaces and return the formatted problem
    arranged_problems = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(dash_line) + "\n" + "    ".join(result_line)

    return arranged_problems


print(arithmetic_arranger())


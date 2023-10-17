def arithmetic_arranger(problems, solve=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = ""
    second_line = ""
    dash_line = ""
    result_line = ""

    for problem in problems:
        parts = problem.split()

        if parts[1] not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        if not parts[0].isdigit() or not parts[2].isdigit():
            return "Error: Numbers must only contain digits."

        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(parts[0]), len(parts[2])) + 2

        first_line += str(parts[0]).rjust(width) + "    "
        second_line += parts[1] + str(parts[2]).rjust(width - 1) + "    "
        dash_line += "-" * width + "    "

        if solve:
            if parts[1] == "+":
                result = int(parts[0]) + int(parts[2])
            else:
                result = int(parts[0]) - int(parts[2])

            result_line += str(result).rjust(width) + "    "

    arranged_problems = first_line.rstrip() + "\n" + second_line.rstrip() + "\n" + dash_line.rstrip()

    if solve:
        arranged_problems += "\n" + result_line.rstrip()

    return arranged_problems

problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
print(arithmetic_arranger(problems))




print(arithmetic_arranger(problems, solve=True))

 


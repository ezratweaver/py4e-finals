def arithmetic_arranger(user_problems, show_results):
    separated_problems = []
    for problem in user_problems:
        split_problem = problem.split()
        separated_problems.append(split_problem)
    if len(separated_problems) > 5:
        return print('Error: Too Many Problems')

    for problem in separated_problems:
        if not problem[0].isdigit() or not problem[2].isdigit():
            return print('Error: Numbers must only contain digits.')

    firstline = ""
    secondline = ""
    thirdline = ""
    fourthline = ""
    for problem in separated_problems:
        num1 = int(problem[0])
        num2 = int(problem[2])
        operator = problem[1]

        if operator not in ['+', '-']:
            return print("Error: Operator must be '+' or '-'.")

        max_len = max(len(problem[0]), len(problem[2]))
        firstline += f"{num1:>{max_len+2}}    "
        secondline += f"{operator} {num2:>{max_len}}    "
        thirdline += "-"*(max_len+2) + "    "
        if show_results:
            if operator == '+':
                result = num1 + num2
            else:
                result = num1 - num2
            fourthline += f"{result:>{max_len+2}}    "

    arranged_problems = (
    firstline.rstrip() + "\n" + secondline.rstrip() + "\n" + thirdline.rstrip())

    if fourthline:
        arranged_problems += "\n" + fourthline.rstrip()
    return arranged_problems

print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
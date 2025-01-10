def arithmetic_arranger(problems, display_answers=False):
    # Error: Too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    # Splitting the input into components
    first_operands = []
    second_operands = []
    operators = []
    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            continue
        operand1, operator, operand2 = parts

        # Error: Operator must be '+' or '-'
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        # Error: Numbers must only contain digits
        if not (operand1.isdigit() and operand2.isdigit()):
            return "Error: Numbers must only contain digits."

        # Error: Numbers cannot be more than four digits
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        first_operands.append(operand1)
        second_operands.append(operand2)
        operators.append(operator)

    # Preparing for vertical formatting
    line1, line2, line3, line4 = "", "", "", ""
    for i in range(len(problems)):
        operand1 = first_operands[i]
        operand2 = second_operands[i]
        operator = operators[i]

        # Determine spacing and width for alignment
        max_length = max(len(operand1), len(operand2))
        width = max_length + 2

        top = operand1.rjust(width)
        bottom = operator + " " + operand2.rjust(max_length)
        line = "-" * width
        answer = ""
        if display_answers:
            if operator == "+":
                answer = str(int(operand1) + int(operand2)).rjust(width)
            elif operator == "-":
                answer = str(int(operand1) - int(operand2)).rjust(width)

        # Building the final lines
        if i > 0:
            line1 += "    "
            line2 += "    "
            line3 += "    "
            line4 += "    "
        line1 += top
        line2 += bottom
        line3 += line
        if display_answers:
            line4 += answer

    arranged_problems = line1 + "\n" + line2 + "\n" + line3
    if display_answers:
        arranged_problems += "\n" + line4

    return arranged_problems

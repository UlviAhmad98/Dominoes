def what_to_do(instructions):
    if instructions.startswith("Simon says"):
        instruction_1 = instructions[11:]
        return f"I {instruction_1}"
    elif instructions.endswith("Simon says"):
        instruction_2 = instructions[0:(instructions.index("S") - 1)]
        return f"I {instruction_2}"
    else:
        return "I won't do it!"


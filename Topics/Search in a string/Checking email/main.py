def check_email(string):
    space = " "
    incorrect = "@."
    email = "@"
    email_1 = ".@"
    dot = "."
    if (space not in string) and (email_1 not in string) and (incorrect not in string) and (string[-1] != ".") and (email in string) and (dot in string) and ((string.index("@") + 1) < string.rindex(".")):
        return "True"
    else:
        return "False"

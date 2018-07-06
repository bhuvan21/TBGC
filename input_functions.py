def safe_string_input(prompt, denied=None, accepted=None):
    if accepted == None:
        return input(prompt)
    else:
        while True:
            inp = input(prompt)
            if inp in accepted:
                return inp
            else:
                print(denied)

def safe_int_input(prompt, denied=None, accepted_range=None):
    while True:
        try:
            inp = int(input(prompt))
            if accepted_range == None:
                return inp
            else:
                if inp in accepted_range:
                    return inp
                else:
                    print(denied)
        except ValueError:
            print(denied)

def safe_input(itype, prompt, denied=None, accepted=None):
    if itype == str:
        return safe_string_input(prompt, denied, accepted)
    elif itype == int:
        return safe_int_input(prompt, denied, accepted)

def numbered_choice(prompt, choice_names, choices, input_func=safe_input, output_func=print, other_commands=False):
    if other_commands:
        other_commands = ["i", "I"]
    else:
        other_commands = []

    output_func(prompt)
    for n, choice in enumerate(choice_names):
        output_func(f"{n+1}. {choice}")
    inp = input_func(str, "", "That's not an option.", [str(x) for x in range(1, len(choice_names)+1)]+other_commands)
    try:
        return choices[int(inp)-1]
    except ValueError:
        return inp

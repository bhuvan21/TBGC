def safe_string_input(prompt, denied, accepted = None):
    if accepted == None:
        return input(prompt)
    else:
        while True:
            inp = input(prompt)
            return inp if inp in accepted else print(denied)

def safe_int_input(prompt, denied, accepted_range = None):
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

def safe_input(type, prompt, denied, accepted = None):
    if type == str:
        return safe_string_input(prompt, denied, accepted)
    elif type == int:
        return safe_int_input(prompt, denied, accepted)
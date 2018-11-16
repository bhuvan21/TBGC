# offers a numbered choice, accepting only numbers within the correct range of the choices as input
def numbered_choice(options, prompt, reprompt=None):
    reprompt = prompt if reprompt is None else reprompt
    print(prompt)
    cycles = 0
    
    while True:
        if cycles > 0:
            print(reprompt)
        for n, option in enumerate(options):
            print("{}. {}".format(n+1, option))
        inp = input()
        try:
            if 0 < int(inp) <= len(options):
                return int(inp) - 1
        except ValueError:
            pass    
        cycles += 1
        
def t_ornamentate(s):
    o = ""
    o += " "*6 + "_"*len(s) + " "*6 + "\n"
    o += "="*5 + "(" + s + ")" + "="*5 + "\n"
    o += " "*6 + "‾"*len(s) + " "*6
    return o

def s_ornamentate(s):
    o = ""
    o += "---" + s + "---"
    return o

def decorate(l):
    if l.level == 0:
        return t_ornamentate(l.name)
    elif l.level == 1:
        return s_ornamentate(l.name)
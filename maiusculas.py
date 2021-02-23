import string

def maiusculas(a_string):
    maiusculas = ""
    for c in a_string:
        if c in string.ascii_uppercase:
            maiusculas = maiusculas + c
    return maiusculas
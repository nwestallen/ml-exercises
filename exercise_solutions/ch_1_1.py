def check_if_symmetric(s: str):
    l = len(s)
    if l < 2:
        return True
    else:
        i = 0
        while i < l//2 + 1:
            if s[i] != s[l-i-1]:
                return False
            i += 1
        return True

def convert_to_numbers(s: str):
    return [0 if i == ' ' else ord(i) - 96 for i in s]

def convert_to_letters(l: list):
    alpha = ' abcdefghijklmnopqrstuvwxyz'
    return ''.join([alpha[n] for n in l])

def get_intersection(a1: list, a2: list):
    result = []
    for i in a1:
        if not i in result and i in a2:
            result.append(i)
    return result

def get_union(a1: list, a2: list):
    result = []
    for i in a1:
        if not i in result:
            result.append(i)
    for j in a2:
        if not j in result:
            result.append(j)
    return result

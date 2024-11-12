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

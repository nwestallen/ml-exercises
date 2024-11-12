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
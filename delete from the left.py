def min_moves_to_equal_strings(s, t):
    i = len(s) - 1
    j = len(t) - 1
 
    while i >= 0 and j >= 0:
        if s[i] == t[j]:
            i -= 1
            j -= 1
        else:
            break
 
    return i + j + 2

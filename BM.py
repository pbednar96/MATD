def bad_char_rule(pattern):
    len_pattern = len(pattern)
    bchr = [-1] * 256

    for i in range(len_pattern):
        bchr[ord(pattern[i])] = i
    #print(bchr)
    return bchr

def BM_search(pattern, txt):
    len_pattern = len(pattern)
    len_txt = len(txt)

    BCHT = bad_char_rule(pattern)

    s = 0
    while s <= len_txt - len_pattern:
        j = len_pattern - 1

        while j >= 0 and pattern[j] == txt[s + j]:
            j -= 1

        if j < 0:
            print(f"Found pattern at index {s}")
            if s + len_pattern < len_txt:
                s += len_pattern - BCHT[ord(txt[s + len_pattern])]
            else:
                s += 1
        else:
            s += max(1, j - BCHT[ord(txt[s + j])])

if __name__ == '__main__':
    BM_search(str("ahoooOj").lower(), str("sdSD2da ahooooj dsda hahoooooojahah ++ahooooj").lower())
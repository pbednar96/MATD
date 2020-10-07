def bad_match_table(pattern):
    len_pattern = len(pattern)
    bmt = [len_pattern] * 256

    # length - index - 1
    for i in range(len_pattern - 1):
        bmt[ord(pattern[i])] = len_pattern - i - 1

    return bmt


def BMH_search(pattern, txt):
    len_pattern = len(pattern)
    len_txt = len(txt)

    BMT = bad_match_table(pattern)

    pos = len_pattern - 1
    while pos < len_txt:
        j = len_pattern - 1
        i = pos
        while j >= 0 and txt[i] == pattern[j]:
            j -= 1
            i -= 1
        if j == -1:
            print(f"Found pattern at index {i + 1}")
        pos += BMT[ord(txt[pos])]


if __name__ == '__main__':
    BMH_search(str("ahoooOj").lower(), str("sdSD2da ahooooj dsda hahoooooojahah ++ahooooj").lower())

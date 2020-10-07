
def brute_force(pattern, txt):
    len_pattern = len(pattern)
    len_txt = len(txt)

    for i in range(len_txt - len_pattern + 1):
        tmp = 0

        while (tmp < len_pattern):
            if (txt[i + tmp] != pattern[tmp]):
                break
            tmp += 1

        if (tmp == len_pattern):
            print("Pattern found at index ", i)

if __name__ == '__main__':
    brute_force(str("ahoooOj").lower(), str("sdSD2da ahooooj dsda hahoooooojahah ++ahooooj").lower())
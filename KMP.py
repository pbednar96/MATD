def KMP_search(pattern, txt):
    len_pattern = len(pattern)
    len_txt = len(txt)

    pre_lst = compute_prefix_function(pattern)
    j = 0

    for i in range(len_txt):
        while j > 0 and txt[i] != pattern[j]:
            j = pre_lst[j - 1]
        if txt[i] == pattern[j]:
            j += 1
        if j == len_pattern:
            print("Found pattern at index " + str(i - j))
            j = pre_lst[j - 1]



def compute_prefix_function(pattern):
    pre = [0] * len(pattern)
    i, j = 1, 0

    while i < len(pattern):
        if pattern[i] == pattern[j]:
            j += 1
            pre[i] = j
            i += 1
        elif j != 0:
            j = pre[j - 1]
        else:
            pre[i] = 0
            i += 1
    # print(pre)
    return pre


if __name__ == '__main__':
    KMP_search(str("ahoahOj").lower(), str("sdSD2da ahoahoj dsda hahoooooojahah ++ahoahoj").lower())

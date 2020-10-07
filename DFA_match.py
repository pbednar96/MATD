import argparse
import string


def next_state(pattern, len_pattern, lst_chars, state, j):
    if state < len_pattern:
        if j == lst_chars.index(pattern[state]):
            return state + 1

    i = 0

    for k in range(state, 0, -1):
        if lst_chars.index(pattern[k - 1]) == j:
            while i < k - 1:
                if pattern[i] != pattern[state - k + 1 + i]:
                    break
                i += 1
            if i == k - 1:
                return k
    return 0


def DFA_match(pattern, txt):
    len_pattern = len(pattern)
    len_txt = len(txt)
    # take only lower case char to reduce matrix size
    lst_chars = list(string.ascii_lowercase)

    # add special characters that weren't in the set
    lst_others_char = list(txt)
    for item in list(set(lst_others_char) - set(lst_chars)):
        lst_chars.append(item)

    # create matrix of zeros and calculated path -- matrix[len_pattern +1 , count_char]
    matrix_path = [[0 for col in range(len(lst_chars))] for row in range(len_pattern + 1)]

    for state in range(len_pattern + 1):
        for j in range(len(lst_chars)):
            matrix_path[state][j] = next_state(pattern, len_pattern, lst_chars, state, j)

    # search phase
    state = 0
    for i in range(len_txt):
        state = matrix_path[state][lst_chars.index(txt[i])]
        if state == len_pattern:
            print(f"Found pattern at index {format(i - len_pattern + 1)} index")


if __name__ == '__main__':
    # DFA_match(str("ahoooOj").lower(), str("sdSD2da ahooooj dsda hahoooooojahah ++ahooooj").lower())
    parser = argparse.ArgumentParser(description="Find String")
    parser.add_argument("pattern", type=str, default="well", help="Pattern to search")
    parser.add_argument("text_for_search", type=str,
                        default="Hi, the script works well. So we will continue tomorrow, well.",
                        help="Text for search pattern")
    args = parser.parse_args()
    DFA_match(args.pattern.lower(), args.text_for_search.lower())
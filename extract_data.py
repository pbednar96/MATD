import re
import glob

#selected dataset - Reuters newsletter

START_TEXT = "<TEXT>"
END_TEXT = "</TEXT>"

START_TITLE = "<TITLE>"
END_TITLE = "</TITLE>"

START_BODY = "<BODY>"
END_BODY = "</BODY>"


def extract_text(string):
    list_texts = []
    find_all_text = re.findall(f'{START_TEXT}(.*?){END_TEXT}', string)
    for item in find_all_text:
        title = re.findall(f'{START_TITLE}(.*?){END_TITLE}', item)
        body = re.findall(f'{START_BODY}(.*?){END_BODY}', item)
        list_texts.append([title, body])
    return list_texts


def load_file(filename):
    with open(filename, "r", encoding="utf8", errors='ignore') as txt_file:
        txt = txt_file.read().replace("\n", " ")
    return txt


def get_all_files_in_directory(directory, FNE):
    # directory - directory with files
    # FNE - file name extension
    return glob.glob(f"{directory}*{FNE}")


if __name__ == '__main__':
    files_to_load = get_all_files_in_directory("datasets/", ".sgm")
    list_of_texts = []
    for filename in files_to_load:
        print(filename)
        raw_string = load_file(filename)
        result_of_file = extract_text(raw_string)
        list_of_texts += result_of_file

    with open("output.txt", "w") as file:
        file.write(str(list_of_texts))

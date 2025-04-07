import os
import json


# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as file:
        data = json.load(file)
    if field in data.keys():
        vystup = data[field]
    else:
        vystup = None
    return vystup

def linear_search(prohledavana_sekvence, hledane_cislo):
    mezi_seznam = []
    for idx, cislo in enumerate(prohledavana_sekvence):
        if cislo == hledane_cislo:
            mezi_seznam.append(idx)
        else:
            pass
    dictionary_vystup = {"positions":mezi_seznam, "count":len(mezi_seznam)}
    return dictionary_vystup

def pattern_search(prohledavana_sekvence, hledany_vzor):
    mnozina_vystup = set()
    for idx in range(0,len(prohledavana_sekvence) - len(hledany_vzor) + 1):
        pattern_similarity = 0
        for idx_pattern, pattern_element in enumerate(hledany_vzor):
            if prohledavana_sekvence[idx + idx_pattern] == pattern_element:
                pattern_similarity += 1
            else:
                break
        if pattern_similarity == len(hledany_vzor):
            mnozina_vystup.add(idx + len(mnozina_vystup)//2 - 1)
        else:
            pass
    return mnozina_vystup


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(read_data("sequential.json", "unordered_numbers"))
    found_numbers = linear_search(sequential_data, 0)
    print(found_numbers)
if __name__ == '__main__':
    main()
    print(pattern_search(read_data("sequential.json", "dna_sequence"), "ATA"))



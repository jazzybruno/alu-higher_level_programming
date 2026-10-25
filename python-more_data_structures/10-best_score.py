#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best = None
    for key, value in a_dictionary.items():
        if best is None or value > a_dictionary[best]:
            best = key
    return best

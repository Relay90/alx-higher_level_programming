#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    max_value = max(a_dictionary.values())
    best_keys = [
            key for key, value in a_dictionary.items() if value == max_value
            ]
    return best_keys[0] if best_keys else None

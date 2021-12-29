# Small file with functions so main.py is only flask related.

from json import load
from typing import List

with open("output_words.json") as f:
    words = load(f)

# Every letter in the alphabet mapped to a prime number.
alphabet = {
    "a": 2,
    "b": 3,
    "c": 5,
    "d": 7,
    "e": 11,
    "f": 13,
    "g": 17,
    "h": 19,
    "i": 23,
    "j": 29,
    "k": 31,
    "l": 37,
    "m": 41,
    "n": 43,
    "o": 47,
    "p": 53,
    "q": 59,
    "r": 61,
    "s": 67,
    "t": 71,
    "u": 73,
    "v": 79,
    "w": 83,
    "x": 89,
    "y": 97,
    "z": 101,
}

scores = {
    "a": 1,
    "b": 3,
    "c": 3,
    "d": 2,
    "e": 1,
    "f": 4,
    "g": 2,
    "h": 4,
    "i": 1,
    "j": 8,
    "k": 5,
    "l": 1,
    "m": 3,
    "n": 1,
    "o": 1,
    "p": 3,
    "q": 10,
    "r": 1,
    "s": 1,
    "t": 1,
    "u": 1,
    "v": 4,
    "w": 4,
    "x": 8,
    "y": 4,
    "z": 10,
}


def get_hash(word):
    hash = 1
    for char in word:
        hash *= alphabet[char.lower()]

    return hash


def find_words(tiles: list, matches: set = set()):

    # Ooo fancy walrus operator.
    if (hash := str(get_hash(tiles))) in words:
        matches.update(set(words.get(hash)))

    for i in range(len(tiles) - 1):
        #           Hacky way to query all elements in a list except one item...
        find_words(
            list(
                # I would like to reverse this so it removes the correct letters in order
                reversed(tiles[:i] + tiles[i + 1 :])
            ),
            matches=matches,
        )

    return matches


def get_score(word):
    score = 0
    for char in word:
        score += scores[char.lower()]

    return score
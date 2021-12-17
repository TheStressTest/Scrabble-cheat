# Small file with functions so main.py is only flask related.

from json import load

with open("output_words.json") as f:
    words = load(f)

with open("definitions.json") as f:
    definitions = load(f)

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


def get_hash(word):
    hash = 1
    for char in word:
        hash *= alphabet[char.lower()]

    return hash


def get_definition(word):
    return definitions[word]


def find_words(tiles: list, matches=[]):
    # Ooo fancy walrus operator.
    if (hash := str(get_hash(tiles))) in words:
        matches += words.get(hash)

    while tiles:

        print(tiles)
        # recursion
        find_words(tiles, matches=matches)

    return matches


if __name__ == "__main__":
    print(find_words(list("EELGRASS")))
    print(find_words(list("FRANKLIN"), matches=[]))
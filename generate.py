# small script used to generate the 'hash' of every word

#                   PROBLEM
#   So, you may be wondering how this works.
# Well let me start by explaining why we map
# each number to a prime number and not a number
# if we map A: 2, B: 3, C: 3, etc, then this
# combination of letters (EJ) returns 50 because
# 5 x 10 = 50, however, the problem here is
# that "YB" also returns 50 because 25 x 2 is
# ALSO 50. Here is where the problem arises.
#
#                   SOLUTION
#
#   So, we can solve this by mapping each number to a prime
# number because primes have only two factors, 1 and
# themselves, because we don't map any letter to 1 we
# don't have to worry about that. Because each prime
# only have 2 factors (We can ignore 1) we know that
# When you multiply 2 prime numbers together, the new
# number only has 2 factors, (The two primes)
# (Again 1 is also a factor but we don't have to worry about it)
# So if we test the combination of letters: NO, we get
# 41 x 43 or 1,763. The only other way to get 1,763
# besides (1 x 1,763) IS 43 x 41 because those are
# the two factors. So the only other way to get 1,763
# using our alphabet is On, which is infact an anagram of
# "No".

from sys import argv
from collections import defaultdict
import json


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


if __name__ == "__main__":
    file_name = argv[1]
    file_name_output = argv[2]

    with open(file_name, "r") as f:
        lines = json.load(f)
        hashes = defaultdict(list)
        for line in lines:
            hashes[get_hash(list(line.rstrip()))].append(line)

    with open(file_name_output, "w") as f:
        json.dump(hashes, f, indent=4)
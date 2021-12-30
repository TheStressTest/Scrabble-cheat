# Scrabble word finder 🔍
 
# How it works
Now you may be wondering, "How does this actually work?"<br/>
Well, it all starts with prime numbers.
## Prime numbers
Wikepedia defines [prime numbers](https://en.wikipedia.org/wiki/Prime_number) as
> a natural number greater than 1 that is not a product of two smaller natural numbers.

For example, 5 is a prime number because the only two factors of 5 are 1 and itself.

## Commutative property
The commutative property states that a ⋅ b = b ⋅ a

## Putting it all together
Using this information we know that if we multiply 2 or more prime numbers together,
 - The only factors of the product will be the original primes, 1, and itself
 - The product won't be a prime number
 - It doesn't matter which order we multiply the primes by, as long as we use the same primes, the product will be the same number.

So using this logic, we can create a "hash" for a word by assigning each letter to a prime number
| Letter | Number |
| ------| ------- |
| A | 2 |
| B | 3 |
| C | 5 |
| D | 7 |
| E | 11 |
| F | 13 |
| G | 17 |
| H | 19 |
| I | 23 |
| J | 29 |
| K | 31 |
| L | 37 |
| M | 41 |
| N | 43 |
| O | 47 |
| P | 53 |
| Q | 59 |
| R | 61 |
| S | 67 |
| T | 71 |
| U | 73 |
| V | 79 |
| W | 83 |
| X | 89 |
| Y | 97 |
| Z | 101 |

## Usage

Let's take the word "Hi". <br/>
H and I are assigned to 19 and 23, respectively.<br/>
To get the "hash" of these characters, we multiply the values together: 19 ⋅ 23 is 437. <br/>
We know that the only way to get a product of 437 using our alphabet is 19 (H) and 23 (I) because
 - The factors of 437 are 1, 437, 19 (H), and 23 (I). [See](https://www.factors-of.com/_437_)
 - 1 and 437 are both *not* prime numbers, thus they are not in our dictionary.
 - [The commutative property](#commutative-property) states that we could also get this product with 23 (I) and 19 (H), but that's the whole idea.

## Code
We start by pre-computing the hashes of all the words in the dictinoary in [this](/generate.py) python script.<br/>
Then, we can get the "hash" of any word and quickly see what other words in the scrabble dictionary share the same letters. Using the power of JSON!

# Notes
 - I am aware that you have to attach a word to another word in scrabble. However, this project was made to demonstrate word anagram finding. I might add this feature in the future.
 - The simplest (but slow) way to do this would be to go through every word in the scrabble dictionary (~200,000) and sort their characters in numerical order, and then compare that new word to all the characters in your rack (sorted by numerical order).
 
## Installation:
 * Running this project is as easy as `docker build -t scrabble . && docker run -p 8080:8080 scrabble`
[Dont have docker?](https://www.docker.com/get-started) 🐳
 * If it's not that easy
    - Install [docker](https://www.docker.com/get-started)
    - Download this repository (There should be a green button at the top right corner.)
    - Extract the contents of the downloaded zip file.
    - Open a terminal (method is different per platform)
    - Run `docker build -t scrabble . && docker run -p 8080:8080 scrabble` in the newly opened terminal and hope for the best.
    - In a browser go to http://localhost:8080
    - Enjoy
# Credits
 - I did NOT make the scrabble pieces (Trust me I am not that good at CSS). Credit goes to [James Holmes](https://codepen.io/32bitkid/pen/NPEgbx)
 - Pallets, for making [flask](https://github.com/pallets/flask) (The http library I use)

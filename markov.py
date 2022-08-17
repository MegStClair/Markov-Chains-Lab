"""Generate Markov text from text files."""

from random import choice
import sys

n = int(sys.argv[2])

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open(file_path).read()
    
    return contents


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    words = text_string.split()

    chains = {}

    for index in range(len(words)- n):
        key = tuple(words[index:index + n])
        value = words[index + n]

        if key not in chains:
            chains[key] = [value]
        else:
            chains[key].append(value)


        #    key = tuple(words[index:index+n])
        #    value = words[i + n]

    # for i in range(len(words)-2):
    #     key = (words[i], words[i + 1])
    #     value = words[i + 2]

    #     if key not in chains:
    #         chains[key] = [value]
    #     else:
    #         chains[key].append(value)

    return chains


def make_text(chains):
    """Return text from chains."""

    upper_keys = []
    for key in chains:
        if key[0][0].isupper():
            upper_keys.append(key)
    current_key = choice(upper_keys)
    words = [current_key[i] for i in range(n)]   

    while current_key in chains:
        next_word = choice(chains[current_key])
        words.append(next_word)
        current_key = current_key[1:] + (next_word,)


    return ' '.join(words)


input_path = sys.argv[1]
# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)

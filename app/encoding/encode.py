import tensorflow as tf
import numpy as np

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET_SIZE = len(ALPHABET)

CHAR_TO_INT = {char: i for i, char in enumerate(ALPHABET)}
INT_TO_CHAR = {i: char for i, char in enumerate(ALPHABET)}

def encode_word(word: str) -> tf.Tensor:
    if len(word) != 5:
        raise ValueError("Word must be 5 letters long for Wordle encoding.")

    encoded_letters = []
    for char in word.lower():
        if char not in CHAR_TO_INT:
            raise ValueError(f"Character '{char}' not in alphabet.")
        one_hot = tf.one_hot(CHAR_TO_INT[char], depth=ALPHABET_SIZE, dtype=tf.float32)
        encoded_letters.append(one_hot)

    return tf.concat(encoded_letters, axis=0)


# encoded_apple = encode_word("apple")
# print(f"Encoded 'apple' shape: {encoded_apple.shape}") # Should be (130,)
# print(f"Encoded 'apple': {encoded_apple}") # full tensor

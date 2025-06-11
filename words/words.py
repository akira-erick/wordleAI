import os

file_path = os.path.join(os.path.dirname(__file__), 'output_words.txt')

def get_words():
    with open(file_path, 'r') as file:
        words = file.read().splitlines()

    return words

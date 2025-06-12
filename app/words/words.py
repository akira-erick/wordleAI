import os

file_path = os.path.join(os.path.dirname(__file__), 'output_words.txt')
with open(file_path, 'r') as file:
    words = file.read().splitlines()

def get_words():
    return words

#print(get_words()) 
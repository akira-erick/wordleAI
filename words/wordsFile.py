import unicodedata
import re
from pathlib import Path

ROMAN_REGEX = re.compile(
    r"^M{0,4}(CM|CD|D?C{0,3})"
    r"(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
)

def normalize_word(word):
    word = unicodedata.normalize('NFD', word)
    word = ''.join(c for c in word if unicodedata.category(c) != 'Mn')

    word = re.sub(r'[^a-zA-Z]+$', '', word)

    return word

def is_roman_word(word):
    return bool(ROMAN_REGEX.fullmatch(word.upper()))

def is_valid(word):
    if '-' in word:
        return False
    if not word.isalpha():
        return False
    if len(word) != 5:
        return False
    
    if is_roman_word(word):
        return False
    
    if word[0].isupper() and not word.isupper():
        return False
    return True

def process_file(path):
    valid_words = set()
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            word = line.strip()
            word = normalize_word(word)
            if is_valid(word):
                valid_words.add(word.upper())
    return valid_words

# files taken from:
# br-sem-acentos.txt - https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt
# Lista-de-Palavras.txt - http://200.17.137.109:8081/novobsi/Members/cicerog/disciplinas/introducao-a-programacao/arquivos-2015-2/algoritmos/Lista-de-Palavras.txt/view
# pt_BR.txt - https://cgit.freedesktop.org/libreoffice/dictionaries/plain/pt_BR/pt_BR.dic

file_paths = ["br-sem-acentos.txt", "Lista-de-Palavras.txt", "pt_BR.txt"]

words = set()

for file_path in file_paths:
    words.update(process_file(file_path))

with open('output_words.txt', 'w', encoding='utf-8') as out_file:
    for word in sorted(words):
        out_file.write(word + '\n')
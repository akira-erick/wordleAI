import pandas as pd

from words import get_words

words = get_words()

all_letters = "".join(words)

letter_counts = pd.Series(list(all_letters)).value_counts()

total_letters = len(all_letters)
letter_percentages = (letter_counts / total_letters) * 100

#print(letter_percentages.sort_index(), "\n")

word_df = pd.DataFrame([list(word) for word in words])

word_df.columns = [f"pos_{i+1}" for i in range(5)]

#print(word_df, "\n")

position_percentages = {}
for col in word_df.columns:
    letter_counts_at_pos = word_df[col].value_counts()
    total_letters_at_pos = len(word_df[col])
    percentages = (letter_counts_at_pos / total_letters_at_pos) * 100
    position_percentages[col] = percentages

position_percentages_df = pd.DataFrame(position_percentages).fillna(0)

#print(position_percentages_df.sort_index(), "\n")

def get_letter_percentages():
    return letter_percentages.sort_index()

def get_position_percentages():
    return position_percentages_df.sort_index()
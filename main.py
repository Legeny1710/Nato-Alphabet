import pandas as pd


nato_alphabet_dataframe = pd.read_csv("nato_phonetic_alphabet.csv")


nato_alphabet_dict = {str(row.letter):str(row.code) for (index, row) in nato_alphabet_dataframe.iterrows()}


user_input = input("Enter the word: ")

user_input_list = [letter for letter in user_input]

convert_to_nato = []

for i in user_input_list:
    for (letter, word) in nato_alphabet_dict.items():
        if i.upper() == letter:
            convert_to_nato.append(word)

print(convert_to_nato)
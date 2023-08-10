import pandas as pd


nato_alphabet_dataframe = pd.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_dict = {str(row.letter):str(row.code) for (index, row) in nato_alphabet_dataframe.iterrows()}

user_input = input("Enter the word: ")

try:
    output_list = [nato_alphabet_dict[letter] for letter in user_input.upper()]
except KeyError:
    print("Sorry, only letters in the alphabet")
else:
    print(output_list)
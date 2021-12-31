import pandas
# This program takes a name and prints a list of NATO phonetic alphabetic for each letter of the name

data = pandas.read_csv("nato_phonetic_alphabet.csv")

NATO_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}

name = input("Please, type a name: ").upper()

for letter in name:
    print(NATO_alphabet[letter], end = "  ")
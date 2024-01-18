"""
projekt_1.py: první projekt do Engeto online Python akademie
author: Martin Burian
email: martajs4@seznam.cz
discord: Burdangello
"""
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''

]


dash = "-" * 40





# Display available text parts
print("We have the following parts of text:")
for i, part in enumerate(TEXTS, start=1):
    print(f"{i}. Part {i}")

# Get user input for the part to analyze
while True:
    try:
        selected_part = int(input("Enter a number between 1 and "
                                  f"{len(TEXTS)} to select a part: "))
        if 1 <= selected_part <= len(TEXTS):
            break
        else:
            print("Invalid input. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Analyze the selected text part
text_part = TEXTS[selected_part - 1]

# Analyze the selected text part
words = text_part.split()

total_words = len(words)
titlecase_words = sum(1 for word in words if word.istitle())
uppercase_words = sum(1 for word in words if word.isupper())
lowercase_words = sum(1 for word in words if word.islower())
numeric_strings = sum(1 for word in words if word.isnumeric())
sum_of_numbers = sum(int(word) for word in words if word.isnumeric())

histogram = {}
for word in words:
    length = len(word)
    histogram[length] = histogram.get(length, 0) + 1

# Display analysis results
print(f"\nAnalysis for Part {selected_part}:\n")
print(f"There are {total_words} words in the selected text part.")
print(f"There are {titlecase_words} titlecase words.")
print(f"There are {uppercase_words} uppercase words.")
print(f"There are {lowercase_words} lowercase words.")
print(f"There are {numeric_strings} numeric strings.")
print(f"The sum of all the numbers {sum_of_numbers}")

# Display histogram
print("\n----------------------------------------")
print("LEN|  OCCURRENCES  |NR.")
print("----------------------------------------")
for length, occurrences in sorted(histogram.items()):
    print(f"{length:2}|{'*' * occurrences:>{12}}|{occurrences}")

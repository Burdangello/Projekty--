"""
projekt_1.py: První projekt do Engeto online Python akademie.
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

titlecase_words = list()
uppercase_words = list()
lowercase_words = list()
numeric_strings = list()
sum = 0
dash = "-" * 40

username_password = {
    
    "bob" : "123",
    "ann" : "pass123",
    "mike" : "password",
    "liz" : "pass123",
}

username = input("Insert your username: ")
password = input("Insert your password: ")

if username_password.get(username) == password:
    print(dash)
    print(f"Welcome to the app, {username}")
    print(f"We have {len(TEXTS)} texts to be analyzed.") 
    print(dash)
    choice = (input(f"Enter a number btw. 1 and {len(TEXTS)} to select: "))
    if choice.isnumeric():
        if 1 <= int(choice) <= len(TEXTS):
            text_part = (TEXTS[int(choice) - 1])
            words = text_part.split()
            for word in words:
                if word.istitle():
                    titlecase_words.append(word)
                elif word.isupper():
                    uppercase_words.append(word)
                elif word.islower():
                    lowercase_words.append(word)
                elif word.isnumeric():
                    numeric_strings.append(word)
                    sum += int(word)
            else:    
                pass
        else:
            print(f"Please, choose number between 1 and {len(TEXTS)}. terminating the program!")
    else:
        print("Entered input isn't number, terminating the program!")
else:
    print(f"Unregistered user, terminating the program...")

print(dash)
print(f"There are {len(words)} words in the selected text.")
print(f"There are {len(titlecase_words)} titlecase word.")
print(f"There are {len(uppercase_words)} uppercase words.")
print(f"There are {len(lowercase_words)} lowercase words.")
print(f"There are {len(numeric_strings)} numeric strings.")
print(f"The sum of all the numbers {sum}.") 
print(dash)


words = text_part.split()
sequence_count = {}

for word in words:
    seq_len = len(word)
    sequence_count[seq_len] = sequence_count.get(seq_len, 0) + 1

table_str = "LEN|  OCCURRENCES  |NR.\n" + "-" * 40 + "\n"
for seq_len in range(1, 12):
    count = sequence_count.get(seq_len, 0)
    table_str += f"{seq_len:2}|{'*' * count: <13}|{count: <2}\n"
print(table_str)



"""
projekt_1.py: první projekt do Engeto Online Python Akademie
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

text1 = TEXTS[0].split()
text2 = TEXTS[1].split()
text3 = TEXTS[2].split()

i = list()
u = list()
l = list()
n = list()
s = 0
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
    print(dash)
    print("We have 3 texts to be analyzed.")
    print(dash)
    choice = (input("Enter a number btw. 1 and 3 to select: "))
    print(dash)
    if choice.isnumeric():
        if choice == "1":    
            print(f"There are {len(text1)} words in the selected text.")
            for word in text1:
                if word.istitle():
                    i.append(word)
                elif word.isupper():
                    u.append(word)
                elif word.islower():
                    l.append(word)
                elif word.isnumeric():
                    n.append(word)
                    s+= int(word)
                else:    
                    pass
            print(f"There are {len(u)} titlecase word.")
            print(f"There are {len(i)} uppercase words.")
            print(f"There are {len(l)} lowercase words.")
            print(f"There are {len(n)} numeric strings.")
            print(f"The sum of all the numbers {s}")        
            print(dash)
        elif choice == "2":    
            print(f"There are {len(text2)} words in the selected text.")
            for word in text2:
    
               if word.istitle():
                   i.append(word)
        
               elif word.isupper():
                   u.append(word)
    
               elif word.islower():
                   l.append(word)
    
               elif word.isnumeric():
                   n.append(word)
                   s+= int(word)
               else:    
                   pass
            print(f"There are {len(u)} titlecase word.")
            print(f"There are {len(i)} uppercase words.")
            print(f"There are {len(l)} lowercase words.")
            print(f"There are {len(n)} numeric strings.")
            print(f"The sum of all the numbers {s}")        
            print(dash)
        elif choice == "3":    
            print(f"There are {len(text3)} words in the selected text.")
            for word in text3:
                if word.istitle():
                    i.append(word)
                elif word.isupper():
                    u.append(word)
                elif word.islower():
                    l.append(word)
                elif word.isnumeric():
                    n.append(word)
                    s+= int(word)
            else:    
                pass
            print(f"There are {len(u)} titlecase word.")
            print(f"There are {len(i)} uppercase words.")
            print(f"There are {len(l)} lowercase words.")
            print(f"There are {len(n)} numeric strings.")
            print(f"The sum of all the numbers {s}")        
            print(dash)
        else:
            print("Please, pick number 1, 2 or 3. terminating the program!")
    else:
       print("Entered input isn't number, terminating the program!")
else:
    print(f"unregistered user, terminating the program...")
    
# Coment    
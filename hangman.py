def changeWrd(word, letter, w):
    for i in range(len(word)):
      if word[i] == letter:
         w[i] = letter
    return w

def getWrd(w):
    word = ""
    for i in range(len(w)):
        word = word + w[i] + ' '
    return word

def getGuessed(guessed):
    lets = ""
    for i in range(len(guessed)):
        lets = lets + guessed[i] +", "
    return lets

def hangman(strikes):

#I know I could do this more efficiently with an array



    if strikes == 1:
        print(" -------|")
        print(" |      |")
        print("        |")
        print("        |")
        print("        |")
        print("        |")
        print("        |")

    elif strikes == 2:
        print(" -------|")
        print(" |      |")
        print(" O      |")
        print("        |")
        print("        |")
        print("        |")
        print("        |") 

    elif strikes == 3:
        print(" -------|")
        print(" |      |")
        print(" O      |")
        print(" |      |")
        print("        |")
        print("        |")
        print("        |") 

    elif strikes == 4:
        print(" -------|")
        print(" |      |")
        print(" O      |")
        print(" |      |")
        print("\|/     |")
        print("        |")
        print("        |") 

    elif strikes == 5:
        print(" -------|")
        print(" |      |")
        print(" O      |")
        print(" |      |")
        print("\|/     |")
        print(" |      |")
        print("        |")

    elif strikes == 6:
        print(" -------|")
        print(" |      |")
        print(" O      |")
        print(" |      |")
        print("\|/     |")
        print(" |      |")
        print("/ \     |") 

    else:
        print(" -------|")
        print("        |")
        print("        |")
        print("        |")
        print("        |")
        print("        |")
        print("        |") 

    return "_________" + "\n"

word = input("input word: ")

word = word.lower()

w = ['_']*len(word)

if ' ' in word:
    w = changeWrd(word, ' ', w)

strikes = 0
guessed = []

print(hangman(strikes))
print(getWrd(w))

while (strikes < 6) and ('_' in getWrd(w)):

    letter = input("guess a letter: ")

    if letter in word:
        w = changeWrd(word, letter, w)
        print("correct")

    else:
        strikes = strikes + 1
        strike = 6 - strikes
        print("wrong")
        print(str(strike) + " strikes remain")
    
    guessed.append(letter)

    print(hangman(strikes))

    print(getWrd(w))

    if len(guessed) >= 1:
        print("letters guessed: " + getGuessed(guessed))

if strikes == 6:
    print("you lost")

else:
    print("you won!")
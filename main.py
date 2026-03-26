import Words

KnownWords = []

def HideWord(Word):
    HideWord = []

    for index in Word:
        if index == " ":
            HideWord.append(" ")
        else:
            HideWord.append("_")

    return ' '.join(HideWord)

def CheckLetter(Letter, Word):
    NewWord = []
    Correct = False

    for index in Word:
        if index == " ":
            NewWord.append(" ")
        elif index == Letter and not KnownWords[Letter]:
            NewWord.append(Letter)
            KnownWords.append(Letter)
            Correct = True
        elif KnownWords[Letter]:
            continue
        else:
            NewWord.append("_")

    return Correct, ' '.join(NewWord)

def Start():
    print("Hangman time")
    RandomWord = Words.RNGWord()
    HiddenWord = HideWord(str(RandomWord))

    print(f"The word is {HiddenWord}")

    Lives = 5
    
    while Lives > 0:
        Letter = input("Input a letter: ")
        Correct, NewWord = CheckLetter(Letter, RandomWord)

        if not Correct:
            Lives -= 1
            print("Nope!")
            print(f"Lives left: {str(Lives)}")
        else:
            print("Nice Job!")

        HiddenWord = NewWord
        print(NewWord)


Start()
import Words

KnownWords = {}

def HideWord(Word):
    HideWord = []

    for index in Word:
        if index == " ":
            HideWord.append(" ")
        else:
            HideWord.append("_")

    return ''.join(HideWord)

def CheckLetter(Letter, Word):
    NewWord = []
    Correct = False

    for value in KnownWords.values():
        if value == Letter:
            return False, 0
    
    KnownWords[str(len(KnownWords))] = Letter

    for index in Word:
        print(index)
        if index == " ":
            NewWord.append(" ")
        elif index == Letter:
            NewWord.append(Letter)
            Correct = True
        else:
            if index not in KnownWords.values():
                NewWord.append("_")
            else:
                NewWord.append(index)

    return Correct, ''.join(NewWord)

def Start():
    print("Hangman time")
    RandomWord = Words.RNGWord()
    HiddenWord = HideWord(str(RandomWord))

    print(f"The word is {HiddenWord}")

    Lives = 5
    Won = False
    
    while Lives > 0:
        Letter = input("Input a letter: ")
        Correct, NewWord = CheckLetter(Letter, RandomWord)

        if not Correct:
            Lives -= 1
            print("Nope!")
            print(f"Lives left: {str(Lives)}")
        else:
            print("Nice Job!")
        
        if NewWord: 
            HiddenWord = NewWord

        if HiddenWord == RandomWord:
            Won = True
            break

        print(HiddenWord)

    if Won:
        print("Amazing JOb!!!!! You WON!!!!!!!!!!")
    else:
        print("You Stuck!!!")

Start()
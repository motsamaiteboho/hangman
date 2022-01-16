secreteword = "message"
letterguessed = ""

guesscount = 6
while guesscount >= 0:
    guess  = input("Enter the letter: ")
    if guess in secreteword:
        print("The guessed letter is " + guess)
        letterguessed += guess
        guesscount -=1
    else:
        guesscount -= 1

wrongguesses = 0
for letter in secreteword:
    if letter in letterguessed:
        print(letter, end= "")
    else:
        print("_", end= "")
        wrongguesses +=1

if  wrongguesses == 0:
    print("\nCongradulations, you have won and the secrete word is " + secreteword)
else:
    print("Ooops, you have lost and the secrete word is " + secreteword)
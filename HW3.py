import tkinter as tk
import random

window = tk.Tk()

maxNo = 99
score = 0
totalscore = 0
guess = 0

def buttonClick():
    global guess
    global score
    global totalscore
    try:
        guess = int(guessBox.get())
        if 1 <= guess <= maxNo:
            result = random.randint(0, maxNo + 1)
            if guess == result:
                score += 10
                totalscore += 10
            elif guess % 10 == result % 10 or guess // 10 == result // 10:
                score += 5
                totalscore += 5
            elif guess % 10 == result // 10 or guess // 10 == result % 10: 
                score += 2
                totalscore += 2
        else:
            result = "Entry not valid"
    except:
        result = "Entry not valid"
    guessnumberLabel.config(text="Your guess number = " + str(guess).zfill(2))
    resultLabel.config(text="Random number = " + str(result).zfill(2))
    scoreLabel.config(text="Score = " + str(score))
    scoreallLabel.config(text="TotalScore = " + str(totalscore))
    guessBox.delete(0, tk.END)

guessLabel = tk.Label(window, text="Enter a number from 01 to " + str(maxNo).zfill(2))
guessBox = tk.Entry(window)
guessnumberLabel = tk.Label(window, text="Your guess number = " + str(guess))
resultLabel = tk.Label(window, text="Random number = ")
scoreLabel = tk.Label(window, text="Score = " + str(score))
scoreallLabel = tk.Label(window, text="TotalScore = " + str(totalscore))
button = tk.Button(window, text="guess", command=buttonClick)

guessLabel.pack()
guessBox.pack()
guessnumberLabel.pack()
resultLabel.pack()
scoreLabel.pack()
scoreallLabel.pack()
button.pack()

window.mainloop()


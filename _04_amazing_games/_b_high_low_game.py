from tkinter import messagebox, simpledialog, Tk
import sys
import random

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # 1. Change this line to give you a random number between 1 - 100.
    r = random.randint(1, 100)

    # 2. Print out the random variable that you made in step #1
    print(r)
    # 3. Code a for loop to run steps 4-10, 10 times
    for q in range(10):
        # 4. Ask the user for a guess using a pop-up window, and save their response
        e = simpledialog.askinteger(title=None, prompt="What is the number?")
        # 5. If the guess is correct
        if e == r:
            # 6. Win. Use 'sys.exit(0)' to end the program
            messagebox.showinfo(title=None, message="Correct!")
            sys.exit(0)
        # 7. if the guess is high
            # 8. Tell them it's too high
        if e < r:
            messagebox.showinfo(title=None, message="high")
        # 9. Else if the guess is low
            # 10. Tell them it's too low
        if e > r:
            messagebox.showinfo(title=None, message="low")
    #11. Outside of the loop, tell the user they lost
    messagebox.showinfo(title=None, message="you lost")
    window.mainloop()

from tkinter import messagebox, simpledialog, Tk
import random

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Make a variable equal to a positive number less than 4 using random.randInt(0, 3)
    fdddd = random.randint(0, 6)
    # 2. Print your variable to the console
    print(fdddd)
    # 3. Get the user to enter something that they think is awesome
    simpledialog.askstring(title=None, prompt="What is the awesome thing?")
    # 4. If your variable is  0
        # -- tell the user whatever they entered is awesome!
    if fdddd == 0:
        messagebox.showinfo(title=None, message="That's awesome!")
    # 5. If your variable is  1
        # -- tell the user whatever they entered is ok.
    if fdddd == 1:
        messagebox.showinfo(title=None, message="That's ok!")
    # 6. If your variable is  2
        # -- tell the user whatever they entered is boring.
    if fdddd == 2:
        messagebox.showinfo(title=None, message="That's boring.")
    # 7. If your variable is  3
        # -- invent your own message to give to the user (be nice).
    if fdddd == 3:
        messagebox.showinfo(title=None, message="That's bad.")
    if fdddd == 4:
        messagebox.showinfo(title=None, message="That's cool.")
    if fdddd == 5:
        messagebox.showinfo(title=None, message="That's worth.")
    if fdddd == 6:
        messagebox.showinfo(title=None, message="That's weird.")
    # Run the window's .mainloop() method
    window.mainloop()

from tkinter import messagebox, simpledialog, Tk
d = 0
# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if d == 0:
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Ask the user if they know how to write code.
    code = simpledialog.askstring(title=None, prompt="Did you know hows to write code?")
    # 2. If they say "yes", tell them they will rule the world in a message box pop-up.
    if code == "yes":
        answer = messagebox.showinfo(title=None, message="You will rule the world.")
    # 3. Otherwise, tell them to sign up for classes at The League in an error box pop-up.
    else:
        answer = messagebox.showinfo(title=None, message="Sign up for classes.")
    # Run the window's .mainloop() method
window.mainloop()

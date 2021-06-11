import tkinter as tk 

window = tk.Tk()

label = tk.Button(
    text="Hello, Tkinter",
    foreground="white",  # Set the text color to white
    background="green",  # Set the background color to black
    width=30, 
    height=10
)
label.pack()

window.mainloop()
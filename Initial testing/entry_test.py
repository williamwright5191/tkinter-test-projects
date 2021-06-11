import tkinter as tk


window = tk.Tk()

label = tk.Label(text="Name")

entry = tk.Entry()

label.pack()
entry.pack()

entry.insert(0, "Will")
name = entry.get()
print(name)

window.mainloop()


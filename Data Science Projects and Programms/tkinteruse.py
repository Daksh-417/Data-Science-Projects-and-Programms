import tkinter as tk

def add():
    result.set(float(num1.get()) + float(num2.get()))

root = tk.Tk()
root.title("Simple GUI Calculator")

tk.Label(root, text="Enter number 1").pack()
num1 = tk.Entry(root)
num1.pack()

tk.Label(root, text="Enter number 2").pack()
num2 = tk.Entry(root)
num2.pack()

tk.Button(root, text="Add", command=add).pack()

result = tk.StringVar()
tk.Label(root, textvariable=result).pack()

root.mainloop()

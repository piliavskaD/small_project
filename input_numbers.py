import tkinter as tk

def f(x): #That expression for exaples
    return x * x + 2  #You can put various expression


def ppl():
    input_text = t.get()

    num = int(input_text) if input_text else 0

    res = f(num)

    l2.delete("1.0", tk.END)

    l2.insert(tk.END, res)

    print("click")
    return

def deleta_text():

    l2.delete("1.0", tk.END)
    return

root = tk.Tk()
root.geometry("300x200")
root.title("My program")
l = tk.Label(root, text="Enter text", width=25)
l.pack()

t = tk.Entry(root, width=10)
t.pack()

b1 = tk.Button(root, text="START", command=ppl)
b1.pack()

b2 = tk.Button(root, text="END", command=deleta_text)
b2.pack()

l2 = tk.Text(root,)
l2.pack()

root.mainloop()
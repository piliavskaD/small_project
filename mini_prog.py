import tkinter as tk
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

def ppl():
    x_data = entry_x.get().split()
    y_data = entry_y.get().split()

    lst_x = [float(x) for x in x_data]
    lst_y = [float(y) for y in y_data]

    if len(lst_y) != len(lst_x):
        print("X and Y must have the same length")
        return
    
    ax.plot(lst_x, lst_y, marker="o")
    ax.set_title("Your graphic")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()
    


root = tk.Tk()
root.geometry("500x300")
root.resizable(width=False, height=False)

b = tk.Button(root, text="START", width=20, height=2, bg="green", command=ppl)
b.pack(pady=20)

L_x = tk.Label(root, text="Enter x throught space(' ')", width=30)
entry_x = tk.Entry(root, width=50)
L_x.pack()
entry_x.pack(pady=10)

L_y = tk.Label(root, text="Enter y throught space(' ')", width=30)
entry_y = tk.Entry(root, width=50)
L_y.pack()
entry_y.pack(pady=10)

root.mainloop()
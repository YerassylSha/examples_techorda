import tkinter as tk

def do_close():
    window.destroy()

window = tk.Tk()
window.geometry("450x450")
window.title("Chart_aexample")

btnClose = tk.Button(window, text="Close", font = ('Helvetica', 10, 'bold'), command=do_close)
btnClose.place(x=330, y=400, width=90, height=30)

window.mainloop()

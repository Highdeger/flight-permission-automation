import tkinter as tk
from hashlib import md5

i = 1
last_hash = ''
the_h = 4

def toggler(event):
    global last_hash
    global the_h
    text = t1.get(1.0, tk.END)[0:-1]
    new_hash = str(md5(text.encode()).digest())
    if new_hash != last_hash:
        last_hash = new_hash
        for x in range(len(text)):
            print(x, '->', text[x])
        t1.edit_modified(False)

        if text.count('\n') >= 4:
            the_h = text.count('\n') + 1
            t1.configure(height=the_h)

root = tk.Tk()
root.geometry('600x400+200+200')

f = tk.Frame(root)

t1 = tk.Text(f)
t1.configure(height=the_h)
t1.bind('<<Modified>>', toggler)
t1.pack(side='top')

e1 = tk.Entry(f, text='Hello World!')
e1.pack(side='top')

f.pack()
root.mainloop()

import tkinter as tk

HEIGHT = 100
WIDTH = 250

root = tk.Tk()

root.title('PasswordGen')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='gray')#Pode se utilizar o valor hexadecimal da cor
frame.place(relx=0.1, rely=0.1, relwidt=0.8, relheight=0.8)

button = tk.Button(frame, text='OK!', bg='white', fg='black')
button.pack(side='bottom')

label = tk.Label(frame, text='Digite a informação de login', bg='gray',height=1, width=30)
label.pack()

entry = tk.Entry(frame, bg='white')
entry.pack()
root.mainloop()

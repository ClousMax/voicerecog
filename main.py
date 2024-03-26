from tkinter import *
from tkinter import ttk
def finish():
    root.destroy()
    print("Закрыто приложение") 
def click():
    print("Hello")

root = Tk()     # создаем корневой объект - окно
root.title("Приложения для текста")     # устанавливаем заголовок окна
root.geometry("500x500+550+200")    # устанавливаем размеры окна и смещяем
root.minsize(300,300) 

label = Label(text="Распознавание речи") # создаем текстовую метку
label.pack()    # размещаем метку в окне

btn = ttk.Button(text="Click", command=click)
btn.pack()

frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10])
name_label = ttk.Label(frame,text="Первый фрейм")
name_label.pack(anchor=W)

name_frame=ttk.Entry(frame)
name_frame.pack(anchor=W)

frame.pack(anchor=W,side=LEFT, padx=5,pady=5)
root.protocol("WM_DELETE_WINDOW", finish)
root.mainloop()
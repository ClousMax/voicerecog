from tkinter import *
from tkinter import ttk
import speech_recognition as sr
import pyttsx3 
import voiceRecog #Из Файла
#перевод
from googletrans import Translator, constants
from pprint import pprint



translator = Translator()
def finish():
    root.destroy()
    print("Закрыто приложение") 

def click():
    print("Hello")
    text = voiceRecog.main()
    editor1.insert(END,text)

def translate():
    textToTranslate = editor1.get('1.0' ,END)
    result = translator.translate(textToTranslate, src='ru', dest='en')
    editor2.replace('1.0',END,result.text) #Результат в виде списка с данными, из него нужен только тект

root = Tk()     # создаем корневой объект - окно
root.title("Приложения для текста")     # устанавливаем заголовок окна
root.geometry("500x500+550+200")    # устанавливаем размеры окна и смещяем
root.minsize(300,300) 

label = Label(text="Распознавание речи") # создаем текстовую метку
label.pack()    # размещаем метку в окне

btn = ttk.Button(text="Записать", command=click)
btn.pack()

btn = ttk.Button(text="Перевод",command=translate)
btn.pack()

editor1 = Text(wrap='word',width=30) #Первый текст
editor1.pack(side=LEFT)

editor2 = Text(wrap='word',width=30) #Второй Текст
editor2.pack(side=LEFT)

root.protocol("WM_DELETE_WINDOW", finish)
root.mainloop()
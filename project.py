#Импорт библиотек
from tkinter import *
from tkinter import messagebox
from random import *
from time import *

#переменные которые будут использоваться
pc_score = 0
user_score = 0
pc_figur = ""
user_figur = ""

def stone(): #функция камня 
    global user_figur
    Kbut["bg"] = "green"
    Nbut["bg"] = "white"
    Bbut["bg"] = "white"
    user_figur = "Камень"
    PCbut["state"] = "normal"

def scissors(): #функция ножниц
    global user_figur
    Kbut["bg"] = "white"
    Nbut["bg"] = "green"
    Bbut["bg"] = "white"
    user_figur = "Ножницы"
    PCbut["state"] = "normal"

def paper(): #функция бумаги 
    global user_figur
    Kbut["bg"] = "white"
    Nbut["bg"] = "white"
    Bbut["bg"] = "green"
    user_figur = "Бумага"
    PCbut["state"] = "normal"

def go(): #функция самого принципа игры 
    global pc_figur,user_figur,user_score,pc_score
    t4["text"] = "Выбор бота - "
    for i in range(30):
        ran = randint(1, 4)
        if ran == 1:                                                 
            pc_figur = "Камень"                        #рандомный выбор фигуры ПК 
        if ran == 2:
            pc_figur = "Ножницы"
        if ran == 3:
            pc_figur = "Бумага"

        t4["text"] = "Выбор бота - " + pc_figur
        t4.update()
        sleep(0.1)

    if pc_figur == user_figur:
        messagebox.showinfo("result", "Ничья")

    else:
        if pc_figur == "Камень" and user_figur == "Ножницы":
            pc_score += 1
            messagebox.showinfo("resuit", "Бот победил")

        if pc_figur == "Камень" and user_figur == "Бумага":
            user_score += 1
            messagebox.showinfo("result", "Пользователь победил")

        if pc_figur == "Ножницы" and user_figur == "Бумага":                  #элементы победы или проигрыша
            pc_score += 1                                                     #то есть здесь расписано какая фигура бьёт ту или иную
            messagebox.showinfo("resuit", "Бот победил")                      #например камень ножницы или ножницы бьёт бумагу   

        if pc_figur == "Ножницы" and user_figur == "Камень":
            user_score += 1
            messagebox.showinfo("result", "Пользователь победил")

        if pc_figur == "Бумага" and user_figur == "Камень":
            pc_score += 1
            messagebox.showinfo("resuit", "Бот победил")

        if pc_figur == "Бумага" and user_figur == "Ножницы":
            user_score += 1
            messagebox.showinfo("result", "Пользователь победил")

        t5["text"] = "Пользователь - " + str(user_score)      #вывод очков игрока
        t6["text"] = "Бот - " + str(pc_score)              #вывод очков ПК 

    PCbut["state"]  = "disabled"

#ниже расписана работа самого окна приложения, а так положение и стиль кнопок и текста. 
root = Tk()
#root.geometry("500x500+200+200")
root.title("Камень,Ножницы,Бумага")
root.resizable(True, False)

t1 = Label(root, text = "Камень,Ножницы,Бумага", fg = "black")
t1.grid(row = 0 , column = 1)
t2 = Label(root, text = "Выбор Пользователя", fg = "green")
t2.grid(row = 1, column = 1 )

Kbut = Button(root, text = "Камень", command = stone)
Kbut.grid(row = 2, column = 0)
Nbut = Button(root, text = "Ножницы", command = scissors)
Nbut.grid(row = 2, column = 1)
Bbut = Button(root, text = "Бумага", command = paper)
Bbut.grid(row = 2, column = 2)

t3 = Label(root, text = "Выбор Бота", fg = "blue")
t3.grid(row = 3, column = 1)

PCbut = Button(root, text= "Сгенерировать", command = go)
PCbut["state"] = "disabled"
PCbut.grid(row = 4, column = 1)

t4 = Label(root, text = "Выбор Бота - 0", fg = "red" )
t4.grid(row = 6, column = 1)

t5 = Label(root, text = "Пользователь - 0", fg = "green" )
t5.grid(row = 7, column = 0)

t6 = Label(root, text = "Бот - 0", fg = "blue" )
t6.grid(row = 7, column = 1)

root.mainloop()   #зациклить программу 

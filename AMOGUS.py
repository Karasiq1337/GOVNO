from tkinter import *
from tkinter import ttk, messagebox
import csv

mdm = ['0'] * 14
md = []
mcom = ['New']
mcom1 = ['']
mcom2 = ['']

def users():
    roota = Toplevel(root)
    roota.title("Пользователь")
    roota.geometry("650x450+300+200")
    roota.resizable(None, None)
    roota.wm_attributes("-topmost, 1")
    roota.mainloop()


def admin():
    global md,mcom,mcom1,mcom2

def click_button1():
    global md,mcom,mcom1,mcom2
    mdm[0] = login.get()
    mdm[1] = parol.get()
    if combo_box.current() != 0:
        del md[combo_box.current()-1]
    md.append(mdm)
    mcom = ['New']
    mcom1 = ['']
    mcom2 = ['']
    i = 1
    for row in md:
        mcom.append(str(i))
        mcom1.append(row[0])
        mcom2.append(row[1])
        i += 1
        combo_box["value"] = mcom
        btn2['state'] = NORMAL

def click_button2():
    btn2['state'] = DISABLED
    with open("data.csv", "w", newline='', encoding="utf8") as file:
        writer = csv.writer(file)
        writer.writerow(md)

def click_button3():
    if btn2['state'] == NORMAL:
        messagebox.showinfo("", "Данные не были сохранены")
        return
    roota.destroy()
    btn16['state'] = NORMAL

def click_button4():
    global md
    if btn4['fg'] == '#000000':
        btn4['fg'] = '#00ff00'
        mdm[2] = '1'
    else:
        btn4['fg'] = '#000000'
        mdm[2] = '0'

def click_button5():
    global mdm
    if btn5['fg'] == '#000000':
        btn5['fg'] = '#00ff00'
        mdm[3] = '1'
    else:
        btn5['fg'] = '#000000'
        mdm[3] = '0'

def click_button6():
    global mdm
    if btn6['fg'] == '#000000':
        btn6['fg'] = '#00ff00'
        mdm[4] = '1'
    else:
        btn6['fg'] = '#000000'
        mdm[4] = '0'

def click_button7():
    global mdm
    if btn7['bg'] == '#F0F0F0':
        btn7['bg'] = '#00ff00'
        mdm[5] = '1'
    else:
        btn7['bg'] = '#F0F0F0'
        mdm[5] = '0'

def fun1(event):
    global mdm
    nm = []
    entry1.delete(0, END)
    entry2.delete(0, END)
    i = combo_box.current()
    entry1.insert(END, mcom1[i])
    entry2.insert(END, mcom2[i])
    nm = md[i - 1]
    mdm = nm
    if nm[2] == '1':
        btn4['fg'] = '#00ff00'
    else:
        btn4['fg'] = '#000000'
    if nm[3] == '1':
        btn5['fg'] = '#00ff00'
    else:
        btn5['fg'] = '#000000'
    if nm[4] == '1':
        btn6['fg'] = '#00ff00'
    else:
        btn6['fg'] = '#000000'
    if nm[5] == '1':
        btn7['bg'] = '#00ff00'
    else:
        btn7['bg'] = '#F0F0F0'

roota = Toplevel()
roota.title("Администратор")
roota.geometry("650x450+300+200")
roota.resizable(None, None)
roota.wm_attributes("-topmost", 1)

login = StringVar()
parol = StringVar()

Label1 = Label(roota, text="Администратор", font="14")
Label1.pack()
Label2 = Label(roota, text="Логин:", font="12")
Label2.place(x=240, y=50)
Label3 = Label(roota, text="Пароль:", font="12")
Label3.place(x=450, y=50)
Label4 = Label(roota, text="Порядковый номер:", font="12")
Label4.place(x=10, y=50)

combo_box = ttk.Combobox(roota, values=mcom, font="11", width=15)
combo_box.current(0)
combo_box.bind("«ComboboxSelected»", fun1)
combo_box.place(x=10, y=80)

entry1 = Entry(roota, textvariable=login, font="12", width=15)
entry1.place(x=240, y=80)
entry2 = Entry(roota, textvariable=parol, font="12", width=15)
entry2.place(x=450, y=80)

Label5 = Label(roota, text="Файл1", font="10")
Label5.place(x=240, y=120)
Label6 = Label(roota, text="Файл2", font="10")
Label6.place(x=390, y=120)
Label7 = Label(roota, text="Файл3", font="10")
Label7.place(x=540, y=120)

btn1 = Button(roota, text="Добавить пользователя", padx="10", pady="8", font="10", command=click_button1)
btn1.place(x=10, y=360)
btn2 = Button(roota, text="Сохранить", padx="10", pady="8", font="10", command=click_button2)
btn2.place(x=293, y=360)
btn3 = Button(roota, text="Главное меню", padx="10", pady="8", font="10", command=click_button3)
btn3.place(x=450, y=360)
btn4 = Button(roota, text="Все права", padx="3", pady="3", font="8", width=8, command=click_button4)
btn4.place(x=240, y=148)
btn5 = Button(roota, text="Запрет", padx="3", pady="3", font="8", width=8, command=click_button5)
btn5.place(x=240, y=197)
btn6 = Button(roota, text="Чтение", padx="3", pady="3", font="8", width=8,
command=click_button6)
btn6.place(x=240, y=250)
btn7 = Button(roota, text="Запись", padx="3", pady="3", font="8", width=8,
command=click_button7)
btn7.place(x=240, y=300)

roota.mainloop()

with open("data.csv", "r", encoding="utf8") as file:
    reader = csv.reader(file)
    i = 1
for row in reader:
    md.append(row)
    mcom.append(str(i))
    mcom1.append(row[0])
    mcom2.append(row[1])
    i += 1


def click_button16():
    if Login.get() == 'Admin':
        if Parol.get() == 'Admin':
            btn16['state'] = DISABLED
            admin()
    else:
        messagebox.showinfo("", "Неправильно введены логин или пароль")
    for i in range(len(mcom1)-1):
        if Login.get() == mcom1[i + 1]:
            if Parol.get() == mcom2[i + 1]:
                btn16['state'] = DISABLED
                users()
        else:
            messagebox.showinfo("", "Неправильно введены логин или пароль")

def click_button17():
    root.destroy()

root = Toplevel()
root.title("Главное окно")
root.geometry("650x450+300+200")
root.resizable(None, None)

Login = StringVar()
Parol = StringVar()

Label1 = Label(root, text="Программа моделирования управления доступом", font="14")
Label1.pack()
Label2 = Label(root, text="Введите логин:", font="14")
Label2.place(x=130, y=100)
Label3 = Label(root, text="Введите пароль:", font="14")
Label3.place(x=130, y=150)
Entry1 = Entry(root, textvariable=Login, font="14")
Entry1.place(x=300, y=100)
Entry2 = Entry(root, textvariable=Parol, font="14", show="*")
Entry2.place(x=300, y=150)

btn16 = Button(root, text="Вход", padx="10", pady="8", font="14", command=click_button16)
btn16.place(x=200, y=360)

btn17 = Button(root, text="Выход", padx="10", pady="8", font="14", command=click_button17)
btn17.place(x=350, y=360)

root.mainloop()
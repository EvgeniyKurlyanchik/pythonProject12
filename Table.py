from tkinter import *
from tkinter import ttk

root=Tk()
root.geometry('700x200')
root.title("Table")

# Данные для таблицы создаем
students= [("John", 25 ,"johnsmit@mail.ru"),("Hohn", 21 ,"hohnsmit@mail.ru")]

#созданием столбцы
columns=("name", "age", "email")
tree = ttk.Treeview(columns=columns, show="headings")
tree.pack(fill=BOTH, expand=1)

# определим заголовки
tree.heading("name", text="Имя")
tree.heading("age", text="Возраст")
tree.heading("email", text="Почта")
for student in students:
    tree.insert("",END, values=student)
root.mainloop()
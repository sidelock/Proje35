from tkinter import *
import os
from shutil import copyfile
import sqlite3
from tkinter import ttk
#import tkinter as tk
from tkinter import filedialog

Profile = {1:""}

def register1():
    global register1_screen
    register1_screen = Toplevel(main1_screen)
    register1_screen['background'] = '#FF0000'
    register1_screen.title("Kayıt Ekranı")
    register1_screen.geometry("600x600")

    global username1
    global password1
    global username1_entry
    global password1_entry
    username1 = StringVar()
    password1 = StringVar()

    Label(register1_screen, text="Lütfen Kullanıcı Adı ve Şifre Belirleyiniz").pack()
    Label(register1_screen, text="").pack()
    username1_lable = Label(register1_screen, text="Kullanıcı Adı * ")
    username1_lable.pack()
    username1_entry = Entry(register1_screen, textvariable=username1)
    username1_entry.pack()
    password1_lable = Label(register1_screen, text="Şifre * ")
    password1_lable.pack()
    password1_entry = Entry(register1_screen, textvariable=password1, show='*')
    password1_entry.pack()
    Label(register1_screen, text="").pack()
    Button(register1_screen, text="Kayıt Ol", width=10, height=1, bg="yellow", command=register1_user).pack()


def login1():
    global login1_screen
    login1_screen = Toplevel(main1_screen)
    login1_screen.title("Giriş Ekranı")
    login1_screen.geometry("600x600")
    Label(login1_screen, text="Lütfen Bilgilerinizi Giriniz.").pack()
    Label(login1_screen, text="").pack()

    global username1_verify
    global password1_verify

    username1_verify = StringVar()
    password1_verify = StringVar()

    global username1_login_entry
    global password1_login_entry

    Label(login1_screen, text="Kullanıcı Adı * ").pack()
    username1_login_entry = Entry(login1_screen, textvariable=username1_verify)
    username1_login_entry.pack()
    Label(login1_screen, text="").pack()
    Label(login1_screen, text="Şifre * ").pack()
    password1_login_entry = Entry(login1_screen, textvariable=password1_verify, show='*')
    password1_login_entry.pack()
    Label(login1_screen, text="").pack()
    Button(login1_screen, text="Giriş Yap", width=10,bg="turquoise", height=1, command=login1_verify).pack()

def register1_user():
    username1_info = username1.get()
    password1_info = password1.get()

    file1 = open(username1_info, "w")
    file1.write(username1_info + "\n")
    file1.write(password1_info)
    file1.close()

    username1_entry.delete(0, END)
    password1_entry.delete(0, END)

    Label(register1_screen, text="Kayıt Başarılı", fg="green", font=("calibri", 11)).pack()



def login1_verify():
    username1 = username1_verify.get()
    password1 = password1_verify.get()
    username1_login_entry.delete(0, END)
    password1_login_entry.delete(0, END)

    list1_of_files = os.listdir()
    if username1 in list1_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login1_sucess()

        else:
            password1_not_recognised()

    else:
        user1_not_found()




def login1_sucess():
    global login1_success_screen
    login1_success_screen = Toplevel(login1_screen)
    login1_success_screen.title("Giriş Başarılı")
    login1_success_screen.geometry("300x300")
    Label(login1_success_screen, text="Giriş Başarılı").pack()
    Button(login1_success_screen, text="Tamam", bg="turquoise" , command= Y_screen).pack()




def password1_not_recognised():
    global password1_not_recog_screen
    password1_not_recog_screen = Toplevel(login1_screen)
    password1_not_recog_screen.title("Hata")
    password1_not_recog_screen.geometry("300x300")
    Label(password1_not_recog_screen, text="Şifre Hatalı ").pack()
    Button(password1_not_recog_screen, text="Tamam", bg="red", command=delete1_password_not_recognised).pack()




def user1_not_found():
    global user1_not_found_screen
    user1_not_found_screen = Toplevel(login1_screen)
    user1_not_found_screen.title("Hata")
    user1_not_found_screen.geometry("300x300")
    Label(user1_not_found_screen, text="Kullanıcı Bulunamadı").pack()
    Button(user1_not_found_screen, text="Tamam", bg="red", command=delete1_user_not_found_screen).pack()




def delete1_login_success():
    login1_success_screen.destroy()


def delete1_password_not_recognised():
    password1_not_recog_screen.destroy()


def delete1_user_not_found_screen():
    user1_not_found_screen.destroy()


def main1_account_screen():
    global main1_screen
    main1_screen = Tk()
    main1_screen.geometry("600x600")
    main1_screen.title("Yönetici Paneli Giriş Ekranı")
    Label(text="Yönetim Ekranı Lütfen Giriş Yapınız", bg="brown", width="300",fg="white", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Giriş Yap", height="2",bg="turquoise", width="30", command=login1).pack()
    Label(text="").pack()


    main1_screen.mainloop()

def Y_screen():
    global  yscreen
    login1_success_screen.destroy()
    login1_screen.destroy()
    yscreen = Tk()
    yscreen.geometry("600x600")
    yscreen.title("Yönetici Seçim Paneli")


    Label(yscreen, text="Lütfen Seçim Yapınız.").pack()

    Button(yscreen , text="Öğretmen İşlemleri", height="5", width="50",bg="lightblue" , command= Ogretmen_Is).pack()

    Button(yscreen, text="Öğretmen Arama İşlemleri", height="5", width="50", bg="lightblue",command=Ogret_Search).pack()

    Button(yscreen , text="Öğrenci İşlemleri", height="5", width="50",bg="lightblue", command= Ogrenci_İs).pack()

    Button(yscreen, text="Öğrenci Arama İşlemleri", height="5", width="50", bg="lightblue", command=Ogr_Search).pack()

    Button(yscreen , text="Ders İşlemleri", height="5", width="50",bg="lightblue", command= ders_is).pack()

    Button(yscreen , text="Sınıf İşlemleri", height="5", width="50",bg="lightblue",command= snfis).pack()


    yscreen.mainloop()

#########################ÖĞRETMEN İŞLEMLERİ###################

def Ogretmen_Is():
    global root
    yscreen.destroy()
    root = Tk()
    root.title("Öğretmen İşlemleri")
    root.geometry("600x600")

    def add_customer():
        name = entryName.get()
        phone = entryPhone.get()
        more = entryMore.get()

        # Create connection
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        # Insert data
        cur.execute('''INSERT INTO customers (`name` , `phone`, `moreinfo`) VALUES (?,?,?)''', (name, phone, more))
        # commit connection
        conn.commit()
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        select = cur.execute("SELECT*FROM customers order by id desc")
        select = list(select)
        tree.insert('', END, values=select[0])
        # Photo profile
        filename = entryPhoto.get()
        ext = filename.split(".")
        id = select[0][0]

        conn.close()

    def delete_customer():
        idSelect = tree.item(tree.selection())['values'][0]
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        delete = cur.execute("delete from customers where id = {}".format(idSelect))
        conn.commit()
        conn.close()
        tree.delete(tree.selection())

    def sortByName():
        # clear the treeview
        for i in tree.get_children():
            tree.delete(i)
        # create connection
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        select = cur.execute("select*from customers order by `name` asc")
        conn.commit()
        for row in select:
            tree.insert('', END, values=row)
        conn.close()

    def SearchByName(event):
        for i in tree.get_children():
            tree.delete(i)

        name = entrySearchByName.get()

        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        select = cur.execute("SELECT*FROM customers where `name` = (?) ", (name,))
        conn.commit()
        select = list(select)
        for row in select:
            tree.insert('', END, values=row)

        conn.close()

    def SearchByPhone(event):
        for i in tree.get_children():
            tree.delete(i)

        phone = entrySearchByPhone.get()

        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        select = cur.execute("SELECT*FROM customers where `phone` = (?) ", (phone,))
        conn.commit()
        select = list(select)
        for row in select:
            tree.insert('', END, values=row)
        conn.close()

    def treeActionSelect(event):
        # load image

        idSelect = tree.item(tree.selection())['values'][0]
        nameSelect = tree.item(tree.selection())['values'][1]
        phoneSelect = tree.item(tree.selection())['values'][2]
        moreInfoSelect = tree.item(tree.selection())['values'][3]

        lid = Label(root, text="ID : " + str(idSelect))
        lid.place(x=110, y=350, width=50)
        lname = Label(root, text=" Ad Soyad : " + nameSelect)
        lname.place(x=110, y=380, width=150)
        lphone = Label(root, text="Telefon : " + str(phoneSelect))
        lphone.place(x=110, y=410, width=150)
        Tmore = Text(root)
        Tmore.place(x=260, y=360, width=280, height=100)
        Tmore.insert(END, "BRANŞ : " + moreInfoSelect)

    # Add Title
    lblTitle = Label(root, text="")
    lblTitle.place(x=0, y=0, width=250)

    # Label & Entry name
    lblName = Label(root, text="Adınız Soyadınız:",fg="white",bg="gray")
    lblName.place(x=5, y=50, width=155)
    entryName = Entry(root)
    entryName.place(x=170, y=50, width=380)

    # Label & Entry Phone
    lblPhone = Label(root, text="Telefon Numaranız:",fg="white",bg="gray")
    lblPhone.place(x=5, y=80, width=155)
    entryPhone = Entry(root)
    entryPhone.place(x=170, y=80, width=380)

    # Label & Entry Photo
    lblPhoto = Label(root, text="Email:",fg="white",bg="gray")
    lblPhoto.place(x=5, y=110, width=155)
    entryPhoto = Entry(root)
    entryPhoto.place(x=170, y=110, width=300)

    # More Info
    lblMore = Label(root, text="Branş:",fg="white",bg="gray")
    lblMore.place(x=5, y=140, width=155)
    entryMore = Entry(root)
    entryMore.place(x=170, y=140, width=380)

    # Command Button
    bAdd = Button(root, text="Kullanıcı Ekle", fg="black",bg="lightblue" ,command=add_customer)
    bAdd.place(x=5, y=170, width=155)

    bDelete = Button(root, text="Seçimi SİL", fg="black",bg="lightblue", command=delete_customer)
    bDelete.place(x=5, y=205, width=155)

    bSort = Button(root, text="Geri Dön", fg="black",bg="lightblue",command=Y_screen)
    bSort.place(x=5, y=275, width=155)

    bExit = Button(root, text="Programdan Çık", fg="black",bg="lightblue")
    bExit.place(x=5, y=310, width=155)

    # Load Image
    # Add Treeview
    tree = ttk.Treeview(root, columns=(1, 2, 3), height=5, show="headings")
    tree.place(x=170, y=170, width=400, height=175)
    tree.bind("<<TreeviewSelect>>", treeActionSelect)
    # Add scrollbar
    vsb = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
    vsb.place(x=530, y=200, height=175)
    tree.configure(yscrollcommand=vsb.set)

    # Add headings
    tree.heading(1, text="ID")
    tree.heading(2, text="İsim Soyisim")
    tree.heading(3, text="Telefon")
    # Define column width
    tree.column(1, width=50)
    tree.column(2, width=100)
    tree.column(3, width=100)
    # Display data in treeview object
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    select = cur.execute("select*from customers")
    for row in select:
        tree.insert('', END, values=row)
    root.mainloop()


def Ogrenci_İs():
    global ogrs
    yscreen.destroy()
    ogrs = Tk()
    ogrs.title("Öğrenci İşlemleri")
    ogrs.geometry("900x650")

    uygulama = Frame(ogrs)
    uygulama.grid()

    chek1 = Checkbutton(uygulama, text="Online Eğitime Katılıyor", onvalue=1, offvalue=0, height=5, width=20)
    chek1.grid(row=0, column=1, padx=550, pady=30)

    chek2 = Checkbutton(uygulama, text="Online Eğitime Katılmıyor", onvalue=1, offvalue=0, height=5, width=20)
    chek2.grid(row=1, column=1, padx=600)

    def add_customer():
        name = entryName.get()
        phone = entryPhone.get()
        more = entryMore.get()

        # Create connection
        conn = sqlite3.connect('database1.db')
        cur = conn.cursor()
        # Insert data
        cur.execute('''INSERT INTO customers (`name` , `phone`, `moreinfo`) VALUES (?,?,?)''', (name, phone, more))
        # commit connection
        conn.commit()
        conn = sqlite3.connect('database1.db')
        cur = conn.cursor()
        select = cur.execute("SELECT*FROM customers order by id desc")
        select = list(select)
        tree.insert('', END, values=select[0])
        # Photo profile
        filename = entryPhoto.get()
        ext = filename.split(".")
        id = select[0][0]

        conn.close()

    def delete_customer():
        idSelect = tree.item(tree.selection())['values'][0]
        conn = sqlite3.connect("database1.db")
        cur = conn.cursor()
        delete = cur.execute("delete from customers where id = {}".format(idSelect))
        conn.commit()
        conn.close()
        tree.delete(tree.selection())

    def sortByName():
        # clear the treeview
        for i in tree.get_children():
            tree.delete(i)
        # create connection
        conn = sqlite3.connect("database1.db")
        cur = conn.cursor()
        select = cur.execute("select*from customers order by `name` asc")
        conn.commit()
        for row in select:
            tree.insert('', END, values=row)
        conn.close()

    def SearchByName(event):
        for i in tree.get_children():
            tree.delete(i)

        name = entrySearchByName.get()

        conn = sqlite3.connect('database1.db')
        cur = conn.cursor()
        select = cur.execute("SELECT*FROM customers where `name` = (?) ", (name,))
        conn.commit()
        select = list(select)
        for row in select:
            tree.insert('', END, values=row)

        conn.close()

    def SearchByPhone(event):
        for i in tree.get_children():
            tree.delete(i)

        phone = entrySearchByPhone.get()

        conn = sqlite3.connect('database1.db')
        cur = conn.cursor()
        select = cur.execute("SELECT*FROM customers where `phone` = (?) ", (phone,))
        conn.commit()
        select = list(select)
        for row in select:
            tree.insert('', END, values=row)
        conn.close()

    def treeActionSelect(event):
        # load image

        idSelect = tree.item(tree.selection())['values'][0]
        nameSelect = tree.item(tree.selection())['values'][1]
        phoneSelect = tree.item(tree.selection())['values'][2]
        moreInfoSelect = tree.item(tree.selection())['values'][3]

        lid = Label(ogrs, text="ID : " + str(idSelect))
        lid.place(x=110, y=350, width=50)
        lname = Label(ogrs, text=" Ad Soyad : " + nameSelect)
        lname.place(x=110, y=380, width=150)
        lphone = Label(ogrs, text="Telefon : " + str(phoneSelect))
        lphone.place(x=110, y=410, width=150)
        Tmore = Text(ogrs)
        Tmore.place(x=260, y=360, width=280, height=100)
        Tmore.insert(END, "E Mail: " + moreInfoSelect)

    # Add Title
    lblTitle = Label(ogrs, text="")
    lblTitle.place(x=0, y=0, width=250)

    # Label & Entry name
    lblName = Label(ogrs, text="Adınız Soyadınız:",fg="white",bg="gray")
    lblName.place(x=5, y=50, width=155)
    entryName = Entry(ogrs)
    entryName.place(x=170, y=50, width=380)

    # Label & Entry Phone
    lblPhone = Label(ogrs, text="Veli Telefon Numarası:",fg="white",bg="gray")
    lblPhone.place(x=5, y=80, width=155)
    entryPhone = Entry(ogrs)
    entryPhone.place(x=170, y=80, width=380)

    # Label & Entry Photo
    lblPhoto = Label(ogrs, text="Sınıfınız:",fg="white",bg="gray")
    lblPhoto.place(x=5, y=110, width=155)
    entryPhoto = Entry(ogrs)
    entryPhoto.place(x=170, y=110, width=300)

    # More Info
    lblMore = Label(ogrs, text="E mail:",fg="white",bg="gray")
    lblMore.place(x=5, y=140, width=155)
    entryMore = Entry(ogrs)
    entryMore.place(x=170, y=140, width=380)

    # Command Button
    bAdd = Button(ogrs, text="Kullanıcı Ekle",fg="black",bg="lightblue", command=add_customer)
    bAdd.place(x=5, y=170, width=155)

    bDelete = Button(ogrs, text="Seçimi SİL", fg="black",bg="lightblue", command=delete_customer)
    bDelete.place(x=5, y=205, width=155)

    bSort = Button(ogrs, text="Geri Dön", fg="black",bg="lightblue",command=Y_screen)
    bSort.place(x=5, y=275, width=155)

    bExit = Button(ogrs, text="Programdan Çık", fg="black",bg="lightblue")
    bExit.place(x=5, y=310, width=155)

    # Load Image
    # Add Treeview
    tree = ttk.Treeview(ogrs, columns=(1, 2, 3), height=5, show="headings")
    tree.place(x=170, y=170, width=400, height=175)
    tree.bind("<<TreeviewSelect>>", treeActionSelect)
    # Add scrollbar
    vsb = ttk.Scrollbar(ogrs, orient="vertical", command=tree.yview)
    vsb.place(x=530, y=200, height=175)
    tree.configure(yscrollcommand=vsb.set)

    # Add headings
    tree.heading(1, text="ID")
    tree.heading(2, text="İsim Soyisim")
    tree.heading(3, text="Telefon")
    # Define column width
    tree.column(1, width=50)
    tree.column(2, width=100)
    tree.column(3, width=100)
    # Display data in treeview object
    conn = sqlite3.connect('database1.db')
    cur = conn.cursor()
    select = cur.execute("select*from customers")
    for row in select:
        tree.insert('', END, values=row)
    ogrs.mainloop()

def Ogr_Search():
    global src
    yscreen.destroy()
    src = Tk()
    src.title("Öğrenci Arama İşlemleri")
    src.geometry("600x600")

    def add_customer():

        name = entryName.get()
        phone = entryPhone.get()
        more = entryMore.get()

        # Create connection
        conn = sqlite3.connect('database1.db')
        cur = conn.cursor()
        # Insert data
        cur.execute("INSERT INTO customers (`name` , `phone`, `moreinfo`) VALUES (?,?,?)", (name, phone, more))
        # commit connection
        conn.commit()
        conn = sqlite3.connect('database1.db')
        cur = conn.cursor()
        select = cur.execute("SELECT*FROM customers order by id desc")
        select = list(select)
        tree.insert('', END, values=select[0])

        conn.close()

    def delete_customer():
        idSelect = tree.item(tree.selection())['values'][0]
        conn = sqlite3.connect("database1.db")
        cur = conn.cursor()
        delete = cur.execute("delete from customers where id = {}".format(idSelect))
        conn.commit()
        conn.close()
        tree.delete(tree.selection())

    def sortByName():
        # clear the treeview
        for i in tree.get_children():
            tree.delete(i)
        # create connection
        conn = sqlite3.connect("database1.db")
        cur = conn.cursor()
        select = cur.execute("select*from customers order by `name` asc")
        conn.commit()
        for row in select:
            tree.insert('', END, values=row)
        conn.close()

    def SearchByName(event):
        for i in tree.get_children():
            tree.delete(i)

        name = entrySearchByName.get()

        conn = sqlite3.connect('database1.db')
        cur = conn.cursor()
        select = cur.execute("SELECT*FROM customers where `name` = (?) ", (name,))
        conn.commit()
        select = list(select)
        for row in select:
            tree.insert('', END, values=row)

        conn.close()

    def SearchByPhone(event):
        for i in tree.get_children():
            tree.delete(i)

        phone = entrySearchByPhone.get()

        conn = sqlite3.connect('database1.db')
        cur = conn.cursor()
        select = cur.execute("SELECT*FROM customers where `phone` = (?) ", (phone,))
        conn.commit()
        select = list(select)
        for row in select:
            tree.insert('', END, values=row)
        conn.close()

    def treeActionSelect(event):
        # load image

        idSelect = tree.item(tree.selection())['values'][0]
        nameSelect = tree.item(tree.selection())['values'][1]
        phoneSelect = tree.item(tree.selection())['values'][2]
        moreInfoSelect = tree.item(tree.selection())['values'][3]


        lid = Label(src, text="ID : " + str(idSelect))
        lid.place(x=110, y=350, width=50)
        lname = Label(src, text=" Ad Soyad : " + nameSelect)
        lname.place(x=110, y=380, width=150)
        lphone = Label(src, text="Telefon : " + str(phoneSelect))
        lphone.place(x=110, y=410, width=150)
        Tmore = Text(src)
        Tmore.place(x=260, y=360, width=280, height=100)
        Tmore.insert(END, "E mail : " + moreInfoSelect)


    # Add Title
    lblTitle = Label(src, text="Öğrenci Arama", font=("Arial", 21), bg="lightblue", fg="black")
    lblTitle.place(x=0, y=0, width=600)

    # Search area
    lbSearchByName = Label(src, text="Öğrenci İsmi :", bg="black", fg="yellow")
    lbSearchByName.place(x=100, y=60, width=120)
    entrySearchByName = Entry(src)
    entrySearchByName.bind("<Return>", SearchByName)
    entrySearchByName.place(x=300, y=60, width=120)

    lbSearchByPhone = Label(src, text="Öğrenci Veli Telefon :", bg="black", fg="yellow")
    lbSearchByPhone.place(x=100, y=90, width=120)
    entrySearchByPhone = Entry(src)
    entrySearchByPhone.bind("<Return>", SearchByPhone)
    entrySearchByPhone.place(x=300, y=90, width=120)


    bDelete = Button(src, text="Seçimi Sil", fg="black",bg="lightblue", command=delete_customer)
    bDelete.place(x=5, y=205, width=155)

    bSort = Button(src, text="Geri Dön", fg="black",bg="lightblue", command=Y_screen)
    bSort.place(x=5, y=275, width=155)

    bExit = Button(src, text="Programdan Çık",fg="black",bg="lightblue")
    bExit.place(x=5, y=310, width=155)

    # Add Treeview
    tree = ttk.Treeview(src, columns=(1, 2, 3), height=5, show="headings")
    tree.place(x=170, y=170, width=400, height=175)
    tree.bind("<<TreeviewSelect>>", treeActionSelect)
    # Add scrollbar
    vsb = ttk.Scrollbar(src, orient="vertical", command=tree.yview)
    vsb.place(x=530, y=200, height=175)
    tree.configure(yscrollcommand=vsb.set)

    # Add headings
    tree.heading(1, text="ID")
    tree.heading(2, text="İsim Soyisim")
    tree.heading(3, text="Telefon")
    # Define column width
    tree.column(1, width=50)
    tree.column(2, width=100)
    tree.column(3, width=100)
    # Display data in treeview object
    conn = sqlite3.connect('database1.db')
    cur = conn.cursor()
    select = cur.execute("select*from customers")
    for row in select:
        tree.insert('', END, values=row)

    src.mainloop()

def Ogret_Search():
    global src1
    yscreen.destroy()
    src1 = Tk()
    src1.title("Öğretmen Arama İşlemleri")
    src1.geometry("600x600")

    def add_customer():

        name = entryName.get()
        phone = entryPhone.get()
        more = entryMore.get()

        # Create connection
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        # Insert data
        cur.execute("INSERT INTO customers (`name` , `phone`, `moreinfo`) VALUES (?,?,?)", (name, phone, more))
        # commit connection
        conn.commit()
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        select = cur.execute("SELECT*FROM customers order by id desc")
        select = list(select)
        tree.insert('', END, values=select[0])

        conn.close()

    def delete_customer():
        idSelect = tree.item(tree.selection())['values'][0]
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        delete = cur.execute("delete from customers where id = {}".format(idSelect))
        conn.commit()
        conn.close()
        tree.delete(tree.selection())

    def sortByName():
        # clear the treeview
        for i in tree.get_children():
            tree.delete(i)
        # create connection
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        select = cur.execute("select*from customers order by `name` asc")
        conn.commit()
        for row in select:
            tree.insert('', END, values=row)
        conn.close()

    def SearchByName(event):
        for i in tree.get_children():
            tree.delete(i)

        name = entrySearchByName.get()

        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        select = cur.execute("SELECT*FROM customers where `name` = (?) ", (name,))
        conn.commit()
        select = list(select)
        for row in select:
            tree.insert('', END, values=row)

        conn.close()

    def SearchByPhone(event):
        for i in tree.get_children():
            tree.delete(i)

        phone = entrySearchByPhone.get()

        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        select = cur.execute("SELECT*FROM customers where `phone` = (?) ", (phone,))
        conn.commit()
        select = list(select)
        for row in select:
            tree.insert('', END, values=row)
        conn.close()

    def treeActionSelect(event):
        # load image

        idSelect = tree.item(tree.selection())['values'][0]
        nameSelect = tree.item(tree.selection())['values'][1]
        phoneSelect = tree.item(tree.selection())['values'][2]
        moreInfoSelect = tree.item(tree.selection())['values'][3]


        lid = Label(src1, text="ID : " + str(idSelect))
        lid.place(x=110, y=350, width=50)
        lname = Label(src1, text=" Ad Soyad : " + nameSelect)
        lname.place(x=110, y=380, width=150)
        lphone = Label(src1, text="Telefon : " + str(phoneSelect))
        lphone.place(x=110, y=410, width=150)
        Tmore = Text(src1)
        Tmore.place(x=260, y=360, width=280, height=100)
        Tmore.insert(END, "Branş : " + moreInfoSelect)


    # Add Title
    lblTitle = Label(src1, text="Öğretmen Arama", font=("Arial", 21), bg="lightblue", fg="black")
    lblTitle.place(x=0, y=0, width=600)

    # Search area
    lbSearchByName = Label(src1, text="Öğretmen İsmi :", bg="black", fg="yellow")
    lbSearchByName.place(x=100, y=60, width=120)
    entrySearchByName = Entry(src1)
    entrySearchByName.bind("<Return>", SearchByName)
    entrySearchByName.place(x=300, y=60, width=120)

    lbSearchByPhone = Label(src1, text="Öğretmen Telefon :", bg="black", fg="yellow")
    lbSearchByPhone.place(x=100, y=90, width=120)
    entrySearchByPhone = Entry(src1)
    entrySearchByPhone.bind("<Return>", SearchByPhone)
    entrySearchByPhone.place(x=300, y=90, width=120)


    bDelete = Button(src1, text="Seçimi Sil", fg="black",bg="lightblue", command=delete_customer)
    bDelete.place(x=5, y=205, width=155)

    bSort = Button(src1, text="Geri Dön", fg="black",bg="lightblue", command=Y_screen)
    bSort.place(x=5, y=275, width=155)

    bExit = Button(src1, text="Programdan Çık",fg="black",bg="lightblue")
    bExit.place(x=5, y=310, width=155)

    # Add Treeview
    tree = ttk.Treeview(src1, columns=(1, 2, 3), height=5, show="headings")
    tree.place(x=170, y=170, width=400, height=175)
    tree.bind("<<TreeviewSelect>>", treeActionSelect)
    # Add scrollbar
    vsb = ttk.Scrollbar(src1, orient="vertical", command=tree.yview)
    vsb.place(x=530, y=200, height=175)
    tree.configure(yscrollcommand=vsb.set)

    # Add headings
    tree.heading(1, text="ID")
    tree.heading(2, text="İsim Soyisim")
    tree.heading(3, text="Telefon")
    # Define column width
    tree.column(1, width=50)
    tree.column(2, width=100)
    tree.column(3, width=100)
    # Display data in treeview object
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    select = cur.execute("select*from customers")
    for row in select:
        tree.insert('', END, values=row)

    src1.mainloop()



def ders_is():
    global drs
    yscreen.destroy()
    drs = Tk()
    drs.title("Ders İşlemleri")
    drs.geometry("600x600")

    def add_customer():
        name = entryName.get()
        phone = entryPhone.get()
        more = entryMore.get()


        # Create connection
        conn = sqlite3.connect('database2.db')
        cur = conn.cursor()
        # Insert data
        cur.execute('''INSERT INTO customers (`name` , `phone`, `moreinfo`) VALUES (?,?,?)''', (name, phone, more))
        # commit connection
        conn.commit()
        conn = sqlite3.connect('database2.db')
        cur = conn.cursor()
        select = cur.execute("SELECT*FROM customers order by id desc")
        select = list(select)
        tree.insert('', END, values=select[0])
        # Photo profile
        filename = entryPhoto.get()
        ext = filename.split(".")
        id = select[0][0]

        conn.close()

    def delete_customer():
        idSelect = tree.item(tree.selection())['values'][0]
        conn = sqlite3.connect("database2.db")
        cur = conn.cursor()
        delete = cur.execute("delete from customers where id = {}".format(idSelect))
        conn.commit()
        conn.close()
        tree.delete(tree.selection())

    def sortByName():
        # clear the treeview
        for i in tree.get_children():
            tree.delete(i)
        # create connection
        conn = sqlite3.connect("database2.db")
        cur = conn.cursor()
        select = cur.execute("select*from customers order by `name` asc")
        conn.commit()
        for row in select:
            tree.insert('', END, values=row)
        conn.close()

    def SearchByName(event):
        for i in tree.get_children():
            tree.delete(i)

        name = entrySearchByName.get()

        conn = sqlite3.connect('database2.db')
        cur = conn.cursor()
        select = cur.execute("SELECT*FROM customers where `name` = (?) ", (name,))
        conn.commit()
        select = list(select)
        for row in select:
            tree.insert('', END, values=row)

        conn.close()

    def SearchByPhone(event):
        for i in tree.get_children():
            tree.delete(i)

        phone = entrySearchByPhone.get()

        conn = sqlite3.connect('database2.db')
        cur = conn.cursor()
        select = cur.execute("SELECT*FROM customers where `phone` = (?) ", (phone,))
        conn.commit()
        select = list(select)
        for row in select:
            tree.insert('', END, values=row)
        conn.close()

    def treeActionSelect(event):
        # load image

        idSelect = tree.item(tree.selection())['values'][0]
        nameSelect = tree.item(tree.selection())['values'][1]
        phoneSelect = tree.item(tree.selection())['values'][2]
        moreInfoSelect = tree.item(tree.selection())['values'][3]

        lid = Label(drs, text="ID : " + str(idSelect))
        lid.place(x=110, y=350, width=50)
        lname = Label(drs, text=" Ders Adı : " + nameSelect)
        lname.place(x=110, y=380, width=150)
        lphone = Label(drs, text="Derslik Kapasitesi : " + str(phoneSelect))
        lphone.place(x=110, y=410, width=150)
        Tmore = Text(drs)
        Tmore.place(x=260, y=360, width=280, height=100)
        Tmore.insert(END, "Öğretmen : " + moreInfoSelect)

    # Add Title
    lblTitle = Label(drs, text="")
    lblTitle.place(x=0, y=0, width=250)

    # Label & Entry name
    lblName = Label(drs, text="Ders Adı:",fg="white",bg="gray")
    lblName.place(x=5, y=50, width=155)
    entryName = Entry(drs)
    entryName.place(x=170, y=50, width=380)

    # Label & Entry Phone
    lblPhone = Label(drs, text="Derslik Kapasitesi :", fg="white", bg="gray")
    lblPhone.place(x=5, y=80, width=155)
    entryPhone = Entry(drs)
    entryPhone.place(x=170, y=80, width=380)

    # Label & Entry Photo
    lblPhoto = Label(drs, text="Sınıf:", fg="white", bg="gray")
    lblPhoto.place(x=5, y=110, width=155)
    entryPhoto = Entry(drs)
    entryPhoto.place(x=170, y=110, width=300)

    # More Info
    lblMore = Label(drs, text="Öğretmen:", fg="white", bg="gray")
    lblMore.place(x=5, y=140, width=155)
    entryMore = Entry(drs)
    entryMore.place(x=170, y=140, width=380)

    # Command Button
    bAdd = Button(drs, text="Ders Ekle", fg="black",bg="lightblue", command=add_customer)
    bAdd.place(x=5, y=170, width=155)

    bDelete = Button(drs, text="Seçimi SİL", fg="black",bg="lightblue", command=delete_customer)
    bDelete.place(x=5, y=205, width=155)

    bSort = Button(drs, text="Geri Dön", fg="black",bg="lightblue",command=Y_screen)
    bSort.place(x=5, y=275, width=155)

    bExit = Button(drs, text="Programdan Çık", fg="black",bg="lightblue")
    bExit.place(x=5, y=310, width=155)

    # Load Image
    # Add Treeview
    tree = ttk.Treeview(drs, columns=(1, 2, 3), height=5, show="headings")
    tree.place(x=170, y=170, width=400, height=175)
    tree.bind("<<TreeviewSelect>>", treeActionSelect)
    # Add scrollbar
    vsb = ttk.Scrollbar(drs, orient="vertical", command=tree.yview)
    vsb.place(x=530, y=200, height=175)
    tree.configure(yscrollcommand=vsb.set)

    # Add headings
    tree.heading(1, text="ID")
    tree.heading(2, text="Ders Adı")
    tree.heading(3, text="Derslik Kapasitesi")
    # Define column width
    tree.column(1, width=50)
    tree.column(2, width=100)
    tree.column(3, width=100)
    # Display data in treeview object
    conn = sqlite3.connect('database2.db')
    cur = conn.cursor()
    select = cur.execute("select*from customers")
    for row in select:
        tree.insert('', END, values=row)
    drs.mainloop()

def snfis():
    global snf
    yscreen.destroy()
    snf = Tk()
    snf.title("Sınıf İşlemleri")
    snf.geometry("600x600")

    def add_customer():
        name = entryName.get()
        phone = entryPhone.get()
        more = entryMore.get()

        # Create connection
        conn = sqlite3.connect('database3.db')
        cur = conn.cursor()
        # Insert data
        cur.execute('''INSERT INTO customers (`name` , `phone`, `moreinfo`) VALUES (?,?,?)''', (name, phone, more))
        # commit connection
        conn.commit()
        conn = sqlite3.connect('database3.db')
        cur = conn.cursor()
        select = cur.execute("SELECT*FROM customers order by id desc")
        select = list(select)
        tree.insert('', END, values=select[0])
        # Photo profile
        filename = entryPhoto.get()
        ext = filename.split(".")
        id = select[0][0]

        conn.close()

    def delete_customer():
        idSelect = tree.item(tree.selection())['values'][0]
        conn = sqlite3.connect("database3.db")
        cur = conn.cursor()
        delete = cur.execute("delete from customers where id = {}".format(idSelect))
        conn.commit()
        conn.close()
        tree.delete(tree.selection())

    def sortByName():
        # clear the treeview
        for i in tree.get_children():
            tree.delete(i)
        # create connection
        conn = sqlite3.connect("database3.db")
        cur = conn.cursor()
        select = cur.execute("select*from customers order by `name` asc")
        conn.commit()
        for row in select:
            tree.insert('', END, values=row)
        conn.close()

    def SearchByName(event):
        for i in tree.get_children():
            tree.delete(i)

        name = entrySearchByName.get()

        conn = sqlite3.connect('database3.db')
        cur = conn.cursor()
        select = cur.execute("SELECT*FROM customers where `name` = (?) ", (name,))
        conn.commit()
        select = list(select)
        for row in select:
            tree.insert('', END, values=row)

        conn.close()

    def SearchByPhone(event):
        for i in tree.get_children():
            tree.delete(i)

        phone = entrySearchByPhone.get()

        conn = sqlite3.connect('database3.db')
        cur = conn.cursor()
        select = cur.execute("SELECT*FROM customers where `phone` = (?) ", (phone,))
        conn.commit()
        select = list(select)
        for row in select:
            tree.insert('', END, values=row)
        conn.close()

    def treeActionSelect(event):
        # load image

        idSelect = tree.item(tree.selection())['values'][0]
        nameSelect = tree.item(tree.selection())['values'][1]
        phoneSelect = tree.item(tree.selection())['values'][2]
        moreInfoSelect = tree.item(tree.selection())['values'][3]

        lid = Label(snf, text="ID : " + str(idSelect))
        lid.place(x=110, y=350, width=50)
        lname = Label(snf, text=" Sınıf İsmi : " + nameSelect)
        lname.place(x=110, y=380, width=150)
        lphone = Label(snf, text="Sınıf Kapasitesi : " + str(phoneSelect))
        lphone.place(x=110, y=410, width=150)
        Tmore = Text(snf)
        Tmore.place(x=260, y=360, width=280, height=100)
        Tmore.insert(END, "Sınıf Düzeyi : " + moreInfoSelect)

    # Add Title
    lblTitle = Label(snf, text="")
    lblTitle.place(x=0, y=0, width=250)

    # Label & Entry name
    lblName = Label(snf, text="Sınıf İsmi:",fg="white",bg="gray")
    lblName.place(x=5, y=50, width=155)
    entryName = Entry(snf)
    entryName.place(x=170, y=50, width=380)

    # Label & Entry Phone
    lblPhone = Label(snf, text="Sınıf Kapasitesi:",fg="white",bg="gray")
    lblPhone.place(x=5, y=80, width=155)
    entryPhone = Entry(snf)
    entryPhone.place(x=170, y=80, width=380)

    # Label & Entry Photo
    lblPhoto = Label(snf, text="Sınıf Öğretmeni:", fg="white", bg="gray")
    lblPhoto.place(x=5, y=110, width=155)
    entryPhoto = Entry(snf)
    entryPhoto.place(x=170, y=110, width=300)

    # More Info
    lblMore = Label(snf, text="Sınıf Düzeyi:", fg="white", bg="gray")
    lblMore.place(x=5, y=140, width=155)
    entryMore = Entry(snf)
    entryMore.place(x=170, y=140, width=380)

    # Command Button
    bAdd = Button(snf, text="Sınıf Ekle", fg="black",bg="lightblue", command=add_customer)
    bAdd.place(x=5, y=170, width=155)

    bDelete = Button(snf, text="Seçimi SİL", fg="black",bg="lightblue", command=delete_customer)
    bDelete.place(x=5, y=205, width=155)

    bSort = Button(snf, text="Geri Dön", fg="black",bg="lightblue",command=Y_screen)
    bSort.place(x=5, y=275, width=155)

    bExit = Button(snf, text="Programdan Çık", fg="black",bg="lightblue")
    bExit.place(x=5, y=310, width=155)

    # Load Image
    # Add Treeview
    tree = ttk.Treeview(snf, columns=(1, 2, 3), height=5, show="headings")
    tree.place(x=170, y=170, width=400, height=175)
    tree.bind("<<TreeviewSelect>>", treeActionSelect)
    # Add scrollbar
    vsb = ttk.Scrollbar(snf, orient="vertical", command=tree.yview)
    vsb.place(x=530, y=200, height=175)
    tree.configure(yscrollcommand=vsb.set)

    # Add headings
    tree.heading(1, text="ID")
    tree.heading(2, text="Sınıf İsmi")
    tree.heading(3, text="Sınıf Kapasitesi")
    # Define column width
    tree.column(1, width=50)
    tree.column(2, width=100)
    tree.column(3, width=100)
    # Display data in treeview object
    conn = sqlite3.connect('database3.db')
    cur = conn.cursor()
    select = cur.execute("select*from customers")
    for row in select:
        tree.insert('', END, values=row)
    snf.mainloop()



main1_account_screen()







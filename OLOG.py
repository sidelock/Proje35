from tkinter import *
import os
from shutil import copyfile
import sqlite3
from tkinter import ttk
#import tkinter as tk
from tkinter import filedialog

Profile = {1:""}

def register2():
    global register2_screen
    register2_screen = Toplevel(main2_screen)
    register2_screen.title("Kayıt Ekranı")
    #register2_screen.geometry("600x600")
    register2_screen["bg"] = "#1e1e1e"
    w, h = register2_screen.winfo_screenwidth(), register2_screen.winfo_screenheight()
    register2_screen.geometry("%dx%d+0+0" % (w, h))
    global username2
    global password2
    global username2_entry
    global password2_entry
    username2 = StringVar()
    password2 = StringVar()


    Label(register2_screen,text="Lütfen Kullanıcı Adı ve Parola belirleyiniz.",bg="#222222", fg="#ffffff", height="3", font=("Calibri", 15, "bold")).pack(fill="both")

    username2_lable = Label(register2_screen, text="Kullanıcı Adı:", bg="#1e1e1e", fg="#ffffff", font=("Calibri", 14))
    username2_lable.pack(pady=1)
    username2_entry = Entry(register2_screen, textvariable=username2)
    username2_entry.pack(ipady=5,ipadx=15, pady=6)
    password2_lable = Label(register2_screen, text="Parola:", bg="#1e1e1e", fg="#ffffff", font=("Calibri", 14))
    password2_lable.pack(pady=1)
    password2_entry = Entry(register2_screen, textvariable=password2, show='*')
    password2_entry.pack(ipady=5,ipadx=15, pady=8)

    Button(register2_screen, text="Kayıt Ol", width=20, height=2, bg="#B3ECED", fg="#333333", command=register2_user).pack()

def login2():
    global login2_screen
    login2_screen = Toplevel(main2_screen)
    login2_screen.title("Giriş Ekranı")
    #.geometry("600x600")
    login2_screen["bg"] = "#1e1e1e"
    w, h = login2_screen.winfo_screenwidth(), login2_screen.winfo_screenheight()
    login2_screen.geometry("%dx%d+0+0" % (w, h))

    Label(login2_screen,text="Lütfen Kullanıcı Adı ve Parolanızı giriniz.", bg="#222222", fg="#ffffff", height="3", font=("Calibri", 15, "bold")).pack(fill="both")


    global username2_verify
    global password2_verify

    username2_verify = StringVar()
    password2_verify = StringVar()

    global username2_login_entry
    global password2_login_entry

    Label(login2_screen, text="Kullanıcı Adı:", bg="#1e1e1e", fg="#ffffff", font=("Calibri", 14)).pack()
    username2_login_entry = Entry(login2_screen, textvariable=username2_verify)
    username2_login_entry.pack(ipady=5,ipadx=15, pady=6)
    Label(login2_screen, text="Parola:", bg="#1e1e1e", fg="#ffffff", font=("Calibri", 14)).pack()
    password2_login_entry = Entry(login2_screen, textvariable=password2_verify, show='*')
    password2_login_entry.pack(ipady=5,ipadx=15, pady=8)
    Button(login2_screen, text="Giriş Yap",width=20, height=2, bg="#B3ECED", fg="#333333", command=login2_verify).pack()

def register2_user():
    username2_info = username2.get()
    password2_info = password2.get()

    file2 = open(username2_info, "w")
    file2.write(username2_info + "\n")
    file2.write(password2_info)
    file2.close()

    username2_entry.delete(0, END)
    password2_entry.delete(0, END)

    Label(register2_screen, text="Kayıt Başarılı", bg="#1e1e1e", fg="#B3ECED", font=("Calibri", 14)).pack()

def login2_verify():
    username2 = username2_verify.get()
    password2 = password2_verify.get()
    username2_login_entry.delete(0, END)
    password2_login_entry.delete(0, END)

    list2_of_files = os.listdir()
    if username2 in list2_of_files:
        file2 = open(username2, "r")
        verify = file2.read().splitlines()
        if password2 in verify:
            login2_sucess()

        else:
            password2_not_recognised()

    else:
        user2_not_found()

def login2_sucess():
    global login2_success_screen
    login2_success_screen = Toplevel(login2_screen)
    login2_success_screen.title("Giriş Başarılı")
    login2_success_screen.geometry("300x150")
    login2_success_screen["bg"] = "#1e1e1e"
    Label(login2_success_screen, text="Giriş Başarılı", bg="#1e1e1e", fg="#ffffff", height="3", font=("Calibri", 15, "bold")).pack(fill="both",pady=5)
    Button(login2_success_screen, text="Tamam", width=20, height=2, bg="#B3ECED", fg="#333333", command=O_screen).pack()

def password2_not_recognised():
    global password2_not_recog_screen
    password2_not_recog_screen = Toplevel(login2_screen)
    password2_not_recog_screen.title("Hata")
    password2_not_recog_screen.geometry("300x150")
    password2_not_recog_screen["bg"] = "#1e1e1e"
    Label(password2_not_recog_screen, text="Parola Hatalı",bg="#1e1e1e", fg="#ffffff", height="3", font=("Calibri", 15, "bold")).pack(fill="both",pady=5)
    Button(password2_not_recog_screen, text="Tamam",  height="2", width=20, bg="#ffffff", fg="#333333", command=delete2_password_not_recognised).pack()

def user2_not_found():
    global user2_not_found_screen
    user2_not_found_screen = Toplevel(login2_screen)
    user2_not_found_screen.title("Hata")
    user2_not_found_screen.geometry("300x150")
    user2_not_found_screen["bg"] = "#1e1e1e"
    Label(user2_not_found_screen, text="Kullanıcı Bulunamadı",bg="#1e1e1e", fg="#ffffff", height="3", font=("Calibri", 15, "bold")).pack(fill="both",pady=5)
    Button(user2_not_found_screen, text="Tamam",bg="#B00020", fg="#ffffff",height="2", width=20, command=delete2_user_not_found_screen).pack()

def delete2_login_success():
    login2_success_screen.destroy()

def delete2_password_not_recognised():
    password2_not_recog_screen.destroy()

def delete2_user_not_found_screen():
    user2_not_found_screen.destroy()

# ******************************** Başlangıç Ekranı **********************************
def main2_account_screen():
    global main2_screen
    main2_screen = Tk()
    #main2_screen.geometry("600x600")
    w, h = main2_screen.winfo_screenwidth(), main2_screen.winfo_screenheight()
    main2_screen.geometry("%dx%d+0+0" % (w, h))
    main2_screen.title("Öğretmen Paneli Seçim Ekranı")
    main2_screen["bg"]="#1e1e1e"
    Label(text="Öğretmen Ekranı Lütfen Seçim Yapınız", bg="#222222", fg="#ffffff", width="300", height="3", font=("Calibri", 15,"bold")).pack()
    Button(text="Giriş Yap",bg="#B3ECED",fg="#333333",  height="3", width="40",font=("Calibri", 15), command=login2).pack(pady=15)
    Button(text="Kayıt Ol",bg="#B3ECED", fg="#333333", height="3", width="40",font=("Calibri", 15), command=register2).pack(pady=10)
    main2_screen.mainloop()


# ******************************** Öğretmen Seçim Paneli **********************************
def O_screen():
    global  oscreen
    login2_success_screen.destroy()
    login2_screen.destroy()
    oscreen = Tk()
    oscreen["bg"] = "#1e1e1e"
    w, h = oscreen.winfo_screenwidth(), oscreen.winfo_screenheight()
    oscreen.geometry("%dx%d+0+0" % (w, h))
    oscreen.title("Öğretmen Seçim Paneli")
    Label(oscreen, text="Lütfen Seçim Yapınız.",  bg="#222222", fg="#ffffff", height="3", font=("Calibri", 15,"bold")).pack(fill="both")
    Button(oscreen , text="Öğrenci İşlemleri", bg="#B3ECED", fg="#333333", height="4", width="50",font=("Calibri", 16,"bold"), command= Ogrenci_İs).pack(pady=10)
    Button(oscreen, text="Öğrenci Arama İşlemleri", bg="#B3ECED",fg="#333333", height="4", width="50",font=("Calibri", 16,"bold"), command=Ogr_Search2).pack(pady=10)
    Button(oscreen , text="Ders İşlemleri", bg="#B3ECED",fg="#333333", height="4", width="50",font=("Calibri", 16,"bold"), command= ders_is2).pack(pady=10)
    Button(oscreen , text="Sınıf İşlemleri", bg="#B3ECED",fg="#333333", height="4", width="50",font=("Calibri", 16,"bold"),command= snfis2).pack(pady=10)
    oscreen.mainloop()


# ******************************** Öğrenci İşlemleri **********************************
def Ogrenci_İs():
    global ogrs2
    oscreen.destroy()
    ogrs2 = Tk()
    ogrs2.title("Öğrenci İşlemleri")
    ogrs2["bg"] = "#1e1e1e"
    w, h = ogrs2.winfo_screenwidth(), ogrs2.winfo_screenheight()
    ogrs2.geometry("%dx%d+0+0" % (w, h))

    # uygulama = Frame(ogrs2)
    # uygulama.grid()

    chek1 = Checkbutton(ogrs2, text="Online Eğitime Katılıyor", onvalue=1, offvalue=0)
    chek1.grid(row=5, column=1)
    #
    chek2 = Checkbutton(ogrs2, text="Online Eğitime Katılmıyor", onvalue=1, offvalue=0)
    chek2.grid(row=6, column=1)

    # ******************************** Öğrenci İşlemleri Kayıt Ekleme **********************************
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

    # ******************************** Öğrenci İşlemleri Kayıt Silme **********************************
    def delete_customer():
        idSelect = tree.item(tree.selection())['values'][0]
        conn = sqlite3.connect("database1.db")
        cur = conn.cursor()
        delete = cur.execute("delete from customers where id = {}".format(idSelect))
        conn.commit()
        conn.close()
        tree.delete(tree.selection())

    # ******************************** Öğrenci İşlemleri Kayıt Sıralama **********************************
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

    # ******************************** Öğrenci İşlemleri Kayıt Arama **********************************
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

    # ******************************** Öğrenci İşlemleri Kayıt Listeleme **********************************
    def treeActionSelect(event):

        idSelect = tree.item(tree.selection())['values'][0]
        nameSelect = tree.item(tree.selection())['values'][1]
        phoneSelect = tree.item(tree.selection())['values'][2]
        moreInfoSelect = tree.item(tree.selection())['values'][3]

        lid = Label(ogrs2, text="ID : " + str(idSelect))
        #lid.place(x=110, y=350, width=50)
        lname = Label(ogrs2, text=" Ad Soyad: " + str(nameSelect))
        #lname.place(x=110, y=380, width=150)
        lphone = Label(ogrs2, text="Telefon : " + str(phoneSelect))
        lemail = Label(ogrs2, text="E-Posta : " + str(moreInfoSelect))
        #lphone.place(x=110, y=410, width=150)
        Tmore = Text(ogrs2)
        #Tmore.place(x=260, y=360, width=280, height=100)
        Tmore.insert(END, "E Mail: " + str(moreInfoSelect))

    # Entry Alanları
    entryName = Entry(ogrs2, width=30)
    entryName.grid(row=1, column=1, padx=5, pady=2)
    entryPhone = Entry(ogrs2, width=30)
    entryPhone.grid(row=2, column=1, padx=5, pady=2)
    entryPhoto = Entry(ogrs2, width=30)
    entryPhoto.grid(row=3, column=1, padx=5, pady=2)
    entryMore = Entry(ogrs2, width=30)
    entryMore.grid(row=4, column=1, padx=5, pady=2)

    # Label Alanları
    lblTitle = Label(ogrs2, text="Bilgi Girişi:", bg="#1e1e1e", fg="#ffffff", height="3", font=("Calibri", 15, "bold"))
    lblTitle.grid(row=0, column=0, columnspan=4, pady=(10, 0))
    lblName = Label(ogrs2, text="Adınız Soyadınız:", bg="#1e1e1e", fg="#ffffff", font=("Calibri", 13, "bold"))
    lblName.grid(row=1, column=0, padx=5, pady=5, sticky=E)
    lblPhone = Label(ogrs2, text="Veli Telefon Numarası:", bg="#1e1e1e", fg="#ffffff",  font=("Calibri", 13, "bold"))
    lblPhone.grid(row=2, column=0,padx=5, pady=5, sticky=E)
    lblClass = Label(ogrs2, text="Sınıfınız:",bg="#1e1e1e", fg="#ffffff", font=("Calibri", 13, "bold"))
    lblClass.grid(row=3, column=0,padx=5, pady=5, sticky=E)
    lblEmail = Label(ogrs2, text="E mail:",bg="#1e1e1e", fg="#ffffff", font=("Calibri", 13, "bold"))
    lblEmail.grid(row=4, column=0,padx=5, pady=5, sticky=E)


    # Kaydet
    bAdd = Button(ogrs2, text="Kullanıcı Ekle",width=30, bg="#B3ECED", fg="#333333", command=add_customer)
    bAdd.grid(row=7, column=1, pady=(15,3),padx=5)

    # Sil
    bDelete = Button(ogrs2, text="Seçimi SİL",width=30, bg="#B3ECED",fg="#333333", command=delete_customer)
    bDelete.grid(row=8, column=1, pady=2,padx=5)

    # Sırala
    bSort = Button(ogrs2, text="Geri Dön",width=30, bg="#B3ECED",fg="#333333", command=O_screen)
    bSort.grid(row=9, column=1, pady=3,padx=5)

    # Programı Kapat
    bExit = Button(ogrs2, text="Programdan Çık",width=30, bg="#B3ECED", fg="#333333", command=exit_program)
    bExit.grid(row=10, column=1, pady=3, padx=5)






    # Add Treeview
    tree = ttk.Treeview(ogrs2, columns=(1, 2, 3, 4, 5), show="headings")
    #tree.place(x=170, y=170, width=400, height=175)
    tree.grid(row=1, rowspan=10, column=3, padx=5)
    tree.bind("<<TreeviewSelect>>", treeActionSelect)
    # Add scrollbar
    vsb = ttk.Scrollbar(ogrs2, orient="vertical", command=tree.yview)
    #vsb.place(x=530, y=200, height=175)
    vsb.grid(row=1, rowspan=10, column=4)
    tree.configure(yscrollcommand=vsb.set)

    # Add headings
    tree.heading(1, text="Id")
    tree.heading(2, text="Ad Soyad")
    tree.heading(3, text="Telefon")
    tree.heading(4, text="Sınıf")
    tree.heading(4, text="E-Posta")
    # Define column width
    tree.column(1, width=50)
    tree.column(2, width=100)
    tree.column(3, width=80)
    tree.column(4, width=80)
    tree.column(5, width=80)
    # Display data in treeview object
    conn = sqlite3.connect('database1.db')
    cur = conn.cursor()
    select = cur.execute("select*from customers")
    for row in select:
        tree.insert('', END, values=row)
    ogrs2.mainloop()

def exit_program():
    ogrs2.destroy()
    sys.exit()

def Ogr_Search2():
    global src3
    oscreen.destroy()
    src3 = Tk()
    src3.title("Öğrenci Arama İşlemleri")
    #src3.geometry("600x600")
    src3["bg"] = "#1e1e1e"
    w, h = src3.winfo_screenwidth(), src3.winfo_screenheight()
    src3.geometry("%dx%d+0+0" % (w, h))


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


        lid = Label(src3, text="ID : " + str(idSelect))
        lid.place(x=110, y=350, width=50)
        lname = Label(src3, text=" Ad Soyad : " + nameSelect)
        lname.place(x=110, y=380, width=150)
        lphone = Label(src3, text="Telefon : " + str(phoneSelect))
        lphone.place(x=110, y=410, width=150)
        Tmore = Text(src3)
        Tmore.place(x=260, y=360, width=280, height=100)
        Tmore.insert(END, "E mail : " + moreInfoSelect)


    # Add Title
    lblTitle = Label(src3, text="Öğrenci Arama", font=("Arial", 21), bg="#222222", fg="#ffffff")
    lblTitle.place(x=0, y=0, width=600)

    # Search area
    lbSearchByName = Label(src3, text="Öğrenci İsmi :", bg="#222222", fg="#ffffff")
    lbSearchByName.place(x=100, y=60, width=120)
    entrySearchByName = Entry(src3)
    entrySearchByName.bind("<Return>", SearchByName)
    entrySearchByName.place(x=300, y=60, width=120)

    lbSearchByPhone = Label(src3, text="Öğrenci Veli Telefon :", bg="#222222", fg="#ffffff")
    lbSearchByPhone.place(x=100, y=90, width=120)
    entrySearchByPhone = Entry(src3)
    entrySearchByPhone.bind("<Return>", SearchByPhone)
    entrySearchByPhone.place(x=300, y=90, width=120)


    bDelete = Button(src3, text="Seçimi Sil", bg="#B3ECED",fg="#333333", command=delete_customer)
    bDelete.place(x=5, y=205, width=155)

    bSort = Button(src3, text="Geri Dön", bg="#B3ECED",fg="#333333", command=O_screen)
    bSort.place(x=5, y=275, width=155)

    bExit = Button(src3, text="Programdan Çık",bg="#B3ECED",fg="#333333")
    bExit.place(x=5, y=310, width=155)

    # Add Treeview
    tree = ttk.Treeview(src3, columns=(1, 2, 3), height=5, show="headings")
    tree.place(x=170, y=170, width=400, height=175)
    tree.bind("<<TreeviewSelect>>", treeActionSelect)
    # Add scrollbar
    vsb = ttk.Scrollbar(src3, orient="vertical", command=tree.yview)
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

    src3.mainloop()

def ders_is2():
    global drs2
    oscreen.destroy()
    drs2= Tk()
    drs2.title("Ders İşlemleri")
    #drs2.geometry("600x600")
    drs2["bg"] = "#1e1e1e"
    w, h = drs2.winfo_screenwidth(), drs2.winfo_screenheight()
    drs2.geometry("%dx%d+0+0" % (w, h))

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

        lid = Label(drs2, text="ID : " + str(idSelect))
        lid.place(x=110, y=350, width=50)
        lname = Label(drs2, text=" Ders Adı : " + nameSelect)
        lname.place(x=110, y=380, width=150)
        lphone = Label(drs2, text="Derslik Kapasitesi : " + str(phoneSelect))
        lphone.place(x=110, y=410, width=150)
        Tmore = Text(drs2)
        Tmore.place(x=260, y=360, width=280, height=100)
        Tmore.insert(END, "Öğretmen : " + moreInfoSelect)

    # Add Title
    lblTitle = Label(drs2, text="")
    lblTitle.place(x=0, y=0, width=250)


    # Command Button

    bDelete = Button(drs2, text="Seçimi SİL",  bg="#B3ECED",fg="#333333", command=delete_customer)
    bDelete.place(x=5, y=205, width=155)

    bSort = Button(drs2, text="Geri Dön", bg="#B3ECED",fg="#333333", command=O_screen)
    bSort.place(x=5, y=275, width=155)

    bExit = Button(drs2, text="Programdan Çık", bg="#B3ECED",fg="#333333")
    bExit.place(x=5, y=310, width=155)

    # Load Image
    # Add Treeview
    tree = ttk.Treeview(drs2, columns=(1, 2, 3), height=5, show="headings")
    tree.place(x=170, y=170, width=400, height=175)
    tree.bind("<<TreeviewSelect>>", treeActionSelect)
    # Add scrollbar
    vsb = ttk.Scrollbar(drs2, orient="vertical", command=tree.yview)
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
    drs2.mainloop()

def snfis2():
    global snf2
    oscreen.destroy()
    snf2 = Tk()
    snf2.title("Sınıf İşlemleri")
    snf2["bg"] = "#1e1e1e"
    w, h = snf2.winfo_screenwidth(), snf2.winfo_screenheight()
    snf2.geometry("%dx%d+0+0" % (w, h))

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

        lid = Label(snf2, text="ID : " + str(idSelect))
        lid.place(x=110, y=350, width=50)
        lname = Label(snf2, text=" Sınıf İsmi : " + nameSelect)
        lname.place(x=110, y=380, width=150)
        lphone = Label(snf2, text="Sınıf Kapasitesi : " + str(phoneSelect))
        lphone.place(x=110, y=410, width=150)
        Tmore = Text(snf2)
        Tmore.place(x=260, y=360, width=280, height=100)
        Tmore.insert(END, "Sınıf Düzeyi : " + moreInfoSelect)

    # Add Title
    # Command Button


    bDelete = Button(snf2, text="Seçimi SİL", bg="#B3ECED",fg="#333333", command=delete_customer)
    bDelete.place(x=5, y=205, width=155)

    bSort = Button(snf2, text="Geri Dön", bg="#B3ECED",fg="#333333", command=O_screen)
    bSort.place(x=5, y=275, width=155)

    bExit = Button(snf2, text="Programdan Çık", bg="#B3ECED",fg="#333333")
    bExit.place(x=5, y=310, width=155)



    # Load Image
    # Add Treeview
    tree = ttk.Treeview(snf2, columns=(1, 2, 3), height=5, show="headings")
    tree.place(x=170, y=170, width=400, height=175)
    tree.bind("<<TreeviewSelect>>", treeActionSelect)
    # Add scrollbar
    vsb = ttk.Scrollbar(snf2, orient="vertical", command=tree.yview)
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
    snf2.mainloop()


main2_account_screen()

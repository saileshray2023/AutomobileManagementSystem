# ================ Library importing ===============================

from tkinter import *
from tkinter import ttk
import programfunctions as pf
from tkinter import messagebox
import time
import tkinter as tk
import random
import tempfile
import os
import sqlite3

# ====================== Field Listeners=================================
reset = 0

def PnoListener(a,b,c):
    a=pnovar.get()
    global restchk
    restchk=1
    for i in a:
        if i.isalpha() or i.isspace():
            pnovar.set('')
            restchk=0
            messagebox.showinfo("Warning","Mobile No. doesn't contain alphabets or spaces")

def PnoFieldListener(a,b,c):
    a=epnovar.get()
    for i in a:
        if i.isalpha() or i.isspace():
            epnovar.set('')
            messagebox.showinfo("Warning","Mobile No. doesn't contain alphabets or spaces")
            
def quantityFieldlistener(a, b, c):
    global quantityVar
    global costVar
    global rateVar
    global reset
    a=quantityVar.get()
    for i in a:
        if i.isalpha() or i.isspace():
            quantityVar.set(0)
            messagebox.showinfo("Warning","Quantity doesn't contain alphabets or spaces")
    rt=int(rateVar.get())
    qt=quantityVar.get()
    if qt=='':
        costVar.set('')
    else:
        qt=int(qt)
        cost=rt*qt
        costVar.set(cost)

def namFieldListener(a,b,c):
    a=namvar.get()
    global restchk
    restchk=1
    for i in a:
        if i.isdigit() or i in "!@#$%^&*()-_+=:;,.?/":
            namvar.set('')
            restchk=0
            messagebox.showwarning("Warning","Name doesn't contain digits or special characters")

def fstFieldListener(a,b,c):
    a=fstnmevar.get()
    for i in a:
        if ord(i)<65 or ord(i)>122:
            fstnmevar.set('')
            messagebox.showwarning("Warning","Name doesn't contain digits or special characters")

def sndFieldListener(a,b,c):
    a=sndnmevar.get()
    for i in a:
        if ord(i)<65 or ord(i)>122:
            sndnmevar.set('')
            messagebox.showwarning("Warning","Name doesn't contain digits or special characters")


def adhListener(a,b,c):
    a=adhVar.get()
    for i in a:
        
        if i.isalpha() or i.isspace():
            adhVar.set('')
            messagebox.showinfo("Warning","Aadhaar No. doesn't contain alphabets or spaces")
    
def costFieldListner(a, b, c):
    global quantityVar
    global costVar
    global itemRate
    global rateVar
    q = quantityVar.get()
    cost = costVar.get()
    if cost != '' and q == '' and itemRate == 0:
        costVar.set('')
        messagebox.showwarning('Warning', "Enter 'Quantity' value to get the cost...!")
    elif cost != '' and q == '' and itemRate != 0:
        costVar.set('')
        messagebox.showwarning('Warning', "Enter 'Quantity' value to get the cost...!")


def itemFieldListener(a, b, c):
    global itemRate
    global itemVariable
    global namvar
    global pnovar
    global adressvar
    global reset
    global restchk
    global restchk2
    nam = namvar.get()
    pno = pnovar.get()
    adrs = adressvar.get()
    if reset != 0:
        check = pf.check_empty(nam, pno, adrs)
        if check:
            clr = pf.check_for_items(nam, pno, adrs)
            if clr:
                Product = itemVariable.get()
                if Product != '':
                    try:
                        restchk = 1
                        restchk2 = 1
                        itemRate = Productrate[Product]
                        rateVar.set(itemRate)
                        indianRegion = Productplace[Product]
                    except Exception:
                        itemRate = 0
                        rateVar.set(itemRate)
                else:
                    pass
            else:
                pass
        else:
            messagebox.showinfo("Information", "Recommended to enter all the details")
    else:
        reset += 1


def slpno_check():
    while True:
        r = random.randint(1000000000, 9999999999)
        c = pf.checkslpno(r)
        if c == 1:
            continue
        else:
            return r


# _=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_Initializations_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_


window = Tk()
supfrm = Frame(window)
supfrm.pack()

# =========================== Variables ===============================


# ----------------------------- String vars ----------------------------

itemVariable = StringVar()
rateVar = StringVar()
quantityVar = StringVar()
costVar = StringVar()
namvar = StringVar()
pnovar = StringVar()
Datevar = StringVar()
slpvar = StringVar()
adressvar = StringVar()
psVar=tk.StringVar()

usernameVar = StringVar()
passwordVar = StringVar()
gmailVar = StringVar()
adhVar=StringVar()

fstnmevar = StringVar()
sndnmevar = StringVar()
epnovar = StringVar()
emlvar = StringVar()
pass1var = StringVar()
pass2var = StringVar()
pwddb = StringVar()
sqpin=StringVar()
cpvar=StringVar()
cppvar=StringVar()
sctpin=StringVar()

# ---------------------------- Get variables and options --------------

options, Productrate, Productplace = pf.getOptions()

# ----------------------------- Trace Vars -----------------------------

itemVariable.trace('w', itemFieldListener)
quantityVar.trace('w', quantityFieldlistener)
costVar.trace('w', costFieldListner)
epnovar.trace('w',PnoFieldListener)
adhVar.trace('w',adhListener)
pnovar.trace('w',PnoListener)
namvar.trace('w',namFieldListener)
fstnmevar.trace('w',fstFieldListener)
sndnmevar.trace('w',sndFieldListener)

# ----------------------------- initial vars ---------------------------

itemRate = 0
totalcost = 0
Productdic = {}
pwd = ''

# ----------------------------- Set Vars -------------------------------

rateVar.set(itemRate)
Datevar.set(time.strftime("%d/%m/%Y"))
slpvar.set(slpno_check())
itemVariable.set('Select')

# =========================== FRAMES ===================================

restchk = 0
restchk2 = 0
genchk = 0
prntchk = 0


def reset_all(a, b, c):
    global restchk
    global reset
    global Productdic
    global genchk
    global prntchk
    c.focus_set()
    if restchk > 0:
        quantityVar.set(0)
        reset = 0
        costVar.set(0.0)
        rateVar.set(0)
        namvar.set('')
        pnovar.set('')
        adressvar.set('')
        slpvar.set(slpno_check())
        a.delete("1.0", END)
        rec = b.get_children()
        for elm in rec:
            b.delete(elm)
        restchk = 0
        genchk = 0
        prntchk = 0
        Productdic = {}
    else:
        messagebox.showinfo("Information", "Page already been reset...!")


def rest_above(b):
    global restchk2
    global reset
    quantityVar.set(0)
    reset = 0
    restchk2 = 0
    itemVariable.set('')
    costVar.set(0.0)
    rateVar.set(0)
    b.delete("1.0", END)
    conn = sqlite3.connect('record.db')
    cr = conn.cursor()
    cr.execute(f"DELETE FROM customers WHERE Slip_No = {slpvar.get()}")
    conn.commit()
    conn.close()


def go_to_main(a):
    a.destroy()
    mainwindow(supfrm)


def go_to_create(a):
    a.destroy()
    create_page()


def go_to_login(a):
    a.destroy()
    log_in_page()


def log_out(a):
    global pwd
    ans = messagebox.askyesno("Confirmation", "Do you really want to LogOut...?")
    if ans > 0:
        pwd = ''
        a.destroy()
        log_in_page()
    else:
        pass


def ext_creat(a):
    ans = messagebox.askyesno("Confirmation", "Confirm you do not want to Create New User")
    if ans > 0:
        messagebox.showinfo("Information", "You will be directed to Login Page...!")
        a.destroy()
        log_in_page()
    else:
        pass


def prnt_bill(a):
    global prntchk
    global file
    if genchk > 0:
        
        
        q = a.get('1.0', END)
        open(file, 'w').write(q)
        os.startfile(file, "print")
            
        
    else:
        messagebox.showwarning("Warning", "Your bill is not Generated...!")


def add_item(a):
    global quantityVar
    global itemVariable
    global Datevar
    global costVar
    global totalcost
    global Productdic
    global restchk
    it = itemVariable.get()
    dt = Datevar.get()
    qn = int(quantityVar.get())
    co = float(costVar.get())
    qn2 = qn
    restchk=1
    if it != '' and qn != '' and co != '':
        totalcost += co
        qn = qn // 1
        if qn == 0:
            messagebox.showwarning("Warning", "There is no quantity entered. Cannot add the selected item '" + it + "'")
        else:
            if it in Productdic:
                Productdic[it][0] += qn2
                Productdic[it][1] += co
            else:
                tpl = [qn2, co]
                Productdic[it] = tpl
            a.insert('', END, text=it, values=(dt, qn2, co))
        
        quantityVar.set(0)
        costVar.set(0.0)
        rateVar.set(0)
    else:
        messagebox.showerror("Error", "Some required fields are empty...!")


def generate_bill(a):
    global Datevar
    global namvar
    global pnovar
    global slpvar
    global adressvar
    global totalcost
    global Productdic
    global genchk,restchk
    global file
    genchk = 0
    nam = namvar.get()
    pno = pnovar.get()
    slp = slpvar.get()
    adrs = adressvar.get()
    dte = Datevar.get()
    
    file = tempfile.mktemp('.txt', '', 'Bills\\')
    if nam != '' and pno != '' and adrs != '':
        if totalcost != 0:
            try:
                etrdb = pf.enter_hero_autoparts(nam, pno, adrs, slp, dte, totalcost,file)
                if etrdb:
                    l = 0
                    for i in Productdic.keys():
                        if l < len(i):
                            l = len(i)
                    l += 3
                    a.insert(END, "\t\t\t  HERO AUTOMOBILES   \t\t\t" + "\n")
                    a.insert(END, "\t\t_-_-_-_-_-_-_-_-_-_-_-_-_-_-_ \t\t\t" + "\n")
                    a.insert(END, "\tSlip No. : " + slp + "\t\t" + "Date : " + dte + "\n")
                    a.insert(END, "Customer Name:" + nam + " | Phone Number:" + pno + " | Address:" + adrs + "\n")
                    a.insert(END, "\t\t-----------Your Bill-------------\n")
                    a.insert(END, "\t+" + "-" * (l) + "+" + "-" * (13) + "+" + "-" * (11) + "+" + "\n")
                    a.insert(END, "\t|" + " Product " + " " * (
                                l - 9) + "|" + " " * 2 + "QUANTITY" + " " * 3 + "| " + "FULL COST" + " " + "|" + "\n")
                    a.insert(END, "\t+" + "-" * (l) + "+" + "-" * (13) + "+" + "-" * (11) + "+" + "\n")
                    for item in Productdic.items():
                        a.insert(END, "\t| " + item[0] + " " * (l - len(item[0]) - 1) + "|" + " " * 3 + str(
                            item[1][0]) + " " * (
                                         13 - len(str(item[1][0])) - 3) + "|" + " " * 2 + str(item[1][1]) + " " * (
                                         11 - len(str(item[1][1])) - 2) + "|" + "\n")
                    a.insert(END, "\t+" + "-" * (l) + "+" + "-" * (13) + "+" + "-" * (11) + "+" + "\n")
                    a.insert(END,
                             "\t|" + ' Total Cost' + " " * (l - 11) + ":" + " " * 4 + "-" * 5 + " " * 4 + ":  " + str(
                                 totalcost) + " " * (11 - len(str(totalcost)) - 2) + "|" + "\n")
                    genchk = 1
                    a.insert(END, "\t+" + "-" * (l) + "+" + "-" * (13) + "+" + "-" * (11) + "+" + "\n")
                    a.insert(END, "\t    *************THANK YOU**************")
                    restchk=1
                else:
                    pass
            except sqlite3.IntegrityError:
                genchk = 1
                messagebox.showinfo("Information", "Bill already Generated..")
        else:
            messagebox.showwarning("Warning", "You don't have any item in your list...!")
    else:
        messagebox.showwarning("Warning", "Please Enter customer details")


def custo_tble(a, c, x, y, edtdb):
    global chkbtn

    def chk(a, paswor, d, b, x, y):

        ask=b.get()
        def Booking(event):
            value=cusdbtbl.item(cusdbtbl.selection())
            fc = value['values']
            dbs=sqlite3.connect('record.db')
            con=dbs.cursor()
            con.execute(f"Select bill from customers where Slip_No='{fc[3]}'")
            data=con.fetchall()
            os.startfile(data[0][0])
        if ask == paswor:

            a.destroy()

            z = Frame(x, bd=3, relief=RIDGE, width=750, height=620)
            z.pack(after=y, expand=True)

            dbsbr = Scrollbar(z)
            dbsbr.pack(side=RIGHT, fill='y')

            cusdbtbl = ttk.Treeview(z, height=44)
            cusdbtbl["columns"] = ("one", "two", "three", "four", "five", "six")
            cusdbtbl.column("#0", width=60, minwidth=60, stretch=NO)
            cusdbtbl.column("one", width=240, minwidth=240, stretch=NO)
            cusdbtbl.column("two", width=150, minwidth=150, stretch=NO)
            cusdbtbl.column("three", width=200, minwidth=200, stretch=NO)
            cusdbtbl.column("four", width=150, minwidth=150, stretch=NO)
            cusdbtbl.column("five", width=120, minwidth=120, stretch=NO)
            cusdbtbl.column("six", width=120, minwidth=120, stretch=NO)

            cusdbtbl.heading("#0", text="SL.NO.", anchor=W)
            cusdbtbl.heading("one", text="Customer Name", anchor=W)
            cusdbtbl.heading("two", text="Phone Number", anchor=W)
            cusdbtbl.heading("three", text="Address", anchor=W)
            cusdbtbl.heading("four", text="Slip Number", anchor=W)
            cusdbtbl.heading("five", text="Date", anchor=W)
            cusdbtbl.heading("six", text="Total Cost", anchor=W)
            cusdbtbl.pack(side=TOP)
            cusdbtbl.bind('<Double-Button-1>',Booking)
            dbsbr.config(command=cusdbtbl.yview)
            cusdbtbl.config(yscrollcommand=dbsbr.set)

            conn = sqlite3.connect('record.db')
            cn = conn.cursor()
            q = "SELECT * FROM customers"
            cn.execute(q)
            data = cn.fetchall()
            data = sorted(data)
            l = len(data)
            for i in range(l):
                cusdbtbl.insert('', END, text=str(i + 1) + '.', values=(data[i][0], data[i][1], data[i][2],
                                                                        data[i][3], data[i][4],
                                                                        data[i][5]))
            conn.close()

            d.destroy()
        else:
            messagebox.showinfo("Sorry", "You are unauthorised to see the database...")
            d.destroy()

    edtdb.config(bg='red3')
    chkbtn = 2
    askdir = Tk()
    askdir.geometry("500x273")
    askdir.title("Enter Password")
    askdir.config(bg='cyan')
    frm = Frame(askdir, bg='wheat4')
    frm.pack()
    frm1 = Frame(frm, bd=3, relief=RIDGE, bg='dark slate gray')
    frm1.pack(side=TOP, fill='x')
    frm2 = Frame(frm, bd=3, relief=RIDGE)
    frm2.pack(after=frm1)
    frm3 = Frame(frm, bd=3, relief=RIDGE)
    frm3.pack(after=frm2)
    frm1lbl = Label(frm1, text='Please Enter your login password\nto see the CUSTOMER\ndatabase...',
                    font=('Bell MT', 20, 'bold'), bg='snow3')
    frm1lbl.grid(padx=20, pady=10)
    inpfrm = Entry(frm2, textvariable=psVar, width=30,show='*', font=('MV Boli', 20, 'bold'))
    inpfrm.grid()
    btn = Button(frm3, text='OK', bd=2, height=1, width=10, font=('arial', 20, 'bold'),
                 command=lambda: chk(a, c, askdir, inpfrm, x, y)).grid()

    askdir.mainloop()


def save_in_db(a, b, c, key, main):
    food = a.get("1.0", END)
    food = food[:-1]
    rate = b.get("1.0", END)
    rate = int(rate[:-1])
    region = c.get("1.0", END)
    region = region[:-1]
    done = pf.update_food_db(food, rate, region, key)
    main.destroy()
    if done:
        messagebox.showinfo("Information", "Successfully Updated the Selected Item")
    else:
        messagebox.showerror("Error", "Failed to Update the database")


def update_item(l, ch, ed):
    if ed:
        if ch:
            update = Tk()
            update.geometry('540x470')
            update.title('Update Item')
            update.config(bg='cyan4')

            frm = Frame(update, bd=3, bg='wheat4')
            frm.pack(expand=True)
            frminf = Frame(frm, bd=2, relief=RIDGE, bg='saddle brown')
            frminf.pack(side=TOP, fill='x')
            frminp = Frame(frm, bd=2, relief=RIDGE, bg='snow3')
            frminp.pack(after=frminf, fill='both')
            frmbtn = Frame(frm, bd=2, relief=RIDGE)
            frmbtn.pack(after=frminp, pady=15)

            tit = Label(frminf, text='Action Center', font=('Viner Hand ITC', 32, 'bold'), bg='saddle brown')
            tit.grid(padx=115, pady=25)

            footit = Label(frminp, text='Product Name : ', font=('Bradley Hand ITC', 22, 'bold'), bg='snow3')
            footit.grid(row=0, column=0, sticky=W, pady=10)
            ratetit = Label(frminp, text='Price \t   : ', font=('Bradley Hand ITC', 22, 'bold'), bg='snow3')
            ratetit.grid(row=1, column=0, sticky=W, pady=10)
            regtit = Label(frminp, text='Brand \t   : ', font=('Bradley Hand ITC', 22, 'bold'), bg='snow3')
            regtit.grid(row=2, column=0, sticky=W, pady=10)

            fooetry = Text(frminp, font=('Courier New', 16, 'bold'), height=1, width=25)
            fooetry.grid(row=0, column=1, pady=10, padx=10)
            fooetry.bind('<Enter>', pf.showtime)
            fooetry.bind('<Leave>', pf.showtimeends)

            ratetry = Text(frminp, font=('Courier New', 16, 'bold'), height=1, width=25)
            ratetry.grid(row=1, column=1, pady=10, padx=10)
            ratetry.bind('<Enter>', pf.showtime)
            ratetry.bind('<Leave>', pf.showtimeends)

            regetry = Text(frminp, font=('Courier New', 16, 'bold'), height=1, width=25)
            regetry.grid(row=2, column=1, pady=10, padx=10)
            regetry.bind('<Enter>', pf.showtime)
            regetry.bind('<Leave>', pf.showtimeends)

            fooetry.insert(END, l[0])
            ratetry.insert(END, l[1])
            regetry.insert(END, l[2])

            delbtn = Button(frmbtn, text='DELETE DATA', width=12, font=('Copperplate Gothic Bold', 18, 'bold'),
                            command=lambda: pf.delete_food_frm_db(l, edt_btn),  bg='bisque',)
            delbtn.grid(row=0, column=0)
            delbtn.bind('<Enter>', pf.E_lst)
            delbtn.bind('<Leave>', pf.L_lst)

            savebtn = Button(frmbtn, text='SAVE CHANGES', width=14, font=('Copperplate Gothic Bold', 18, 'bold'),
                             command=lambda: save_in_db(fooetry, ratetry, regetry, l[0], update), bg='bisque',)
            savebtn.grid(row=0, column=1)
            savebtn.bind('<Enter>', pf.E_lst)
            savebtn.bind('<Leave>', pf.L_lst)

            cnclbtn = Button(frm, text='CANCEL', width=8, font=('Copperplate Gothic Bold', 18, 'bold'), bd=4,
                             command=lambda: update.destroy(),  bg='bisque',)
            cnclbtn.pack(after=frmbtn)
            cnclbtn.bind('<Enter>', pf.E_lst)
            cnclbtn.bind('<Leave>', pf.L_lst)

            update.mainloop()
        else:
            messagebox.showinfo("Information", "You have not Activated the Update Button..")
    else:
        pass


def Productdb_tble(a, b, c, edtdb):
    global chkbtn
    global edt_btn
    global updt_btn

    a.destroy()

    edtdb.config(bg='dark green')
    chkbtn = 1

    z = Frame(b, bd=3, relief=RIDGE, width=750, height=620)
    z.pack(after=c, expand=True)

    dbsbr = Scrollbar(z)
    dbsbr.pack(side=RIGHT, fill='y')

    cusdbtbl = ttk.Treeview(z, height=44)
    cusdbtbl["columns"] = ("one", "two", "three")
    cusdbtbl.column("#0", width=50, minwidth=50, stretch=NO)
    cusdbtbl.column("one", width=200, minwidth=200, stretch=NO)
    cusdbtbl.column("two", width=150, minwidth=150, stretch=NO)
    cusdbtbl.column("three", width=200, minwidth=200, stretch=NO)

    def func_to_edit(event):
        try:
            value = cusdbtbl.item(cusdbtbl.selection())
            fc = value['values'][0]
            update_item(value['values'], updt_btn, edt_btn)
        except IndexError:
            messagebox.showwarning("Warning", "Select Item Properly...!")

    cusdbtbl.heading("#0", text="Sl.No.", anchor=W)
    cusdbtbl.heading("one", text="Product Name", anchor=W)
    cusdbtbl.heading("two", text="Price ", anchor=W)
    cusdbtbl.heading("three", text="Brand", anchor=W)

    cusdbtbl.pack(side=TOP)
    cusdbtbl.bind('<Double-Button-1>', func_to_edit)

    dbsbr.config(command=cusdbtbl.yview)
    cusdbtbl.config(yscrollcommand=dbsbr.set)

    conn = sqlite3.connect('autoparts.db')
    cn = conn.cursor()
    q = "SELECT * FROM hero_parts"
    cn.execute(q)
    data = cn.fetchall()
    data = sorted(data)
    l = len(data)
    for i in range(l):
        cusdbtbl.insert('', END, text=str(i + 1) + '.', values=(data[i][0], data[i][1], data[i][2]))
    conn.close()


def Usrdb_tble(a, c, x, y, edtdb):
    global chkbtn

    def chk(a, paswor, d, b, x, y):
        global psVar
        ask=b.get()
        if ask == paswor:

            a.destroy()

            z = Frame(x, bd=3, relief=RIDGE, width=750, height=620)
            z.pack(after=y, expand=True)

            dbsbr = Scrollbar(z)
            dbsbr.pack(side=RIGHT, fill='y')

            cusdbtbl = ttk.Treeview(z, height=44)
            cusdbtbl["columns"] = ("one", "two", "three", "four")
            cusdbtbl.column("#0", width=50, minwidth=50, stretch=NO)
            cusdbtbl.column("one", width=150, minwidth=150, stretch=NO)
            cusdbtbl.column("two", width=150, minwidth=150, stretch=NO)
            cusdbtbl.column("three", width=250, minwidth=250, stretch=NO)
            cusdbtbl.column("four", width=150, minwidth=150, stretch=NO)

            cusdbtbl.heading("#0", text="SL.NO.", anchor=W)
            cusdbtbl.heading("one", text="User Name", anchor=W)
            cusdbtbl.heading("two", text="Phone Number", anchor=W)
            cusdbtbl.heading("three", text="G-mail", anchor=W)
            cusdbtbl.heading("four", text="Aadhaar No.", anchor=W)
            cusdbtbl.pack(side=TOP)

            dbsbr.config(command=cusdbtbl.yview)
            cusdbtbl.config(yscrollcommand=dbsbr.set)

            conn = sqlite3.connect('record.db')
            cn = conn.cursor()
            q = "SELECT * FROM User_ids"
            cn.execute(q)
            data = cn.fetchall()
            data = sorted(data)
            l = len(data)
            for i in range(l):
                cusdbtbl.insert('', END, text=str(i + 1) + '.', values=(data[i][0], data[i][1], data[i][2],
                                                                        data[i][5]))
            conn.close()
            d.destroy()
        else:
            messagebox.showinfo("Sorry", "You are unauthorised to see the database...")
            d.destroy()

    edtdb.config(bg='red3')
    chkbtn = 2
    askdir = Tk()
    askdir.geometry("380x200")
    askdir.title("Enter Password")
    frm = Frame(askdir)
    frm.pack()
    frm1 = Frame(frm, bd=3, relief=RIDGE, bg='snow3')
    frm1.pack(side=TOP, fill='x')
    frm2 = Frame(frm, bd=3, relief=RIDGE)
    frm2.pack(after=frm1)
    frm3 = Frame(frm, bd=3, relief=RIDGE)
    frm3.pack(after=frm2)
    frm1lbl = Label(frm1, text='Please Enter your login password\nto see the customer\ndatabase...',
                    font=('Bell MT', 16, 'bold'), bg='snow3')
    frm1lbl.grid(padx=20, pady=10)
    inpfrm = Entry(frm2, textvariable=psVar,show='*', width=30, font=('Bell MT', 14, 'bold'))
    inpfrm.grid()
    btn = Button(frm3, text='OK', bd=2, height=1, width=10, font=('Bell MT', 20, 'bold'),
                 command=lambda: chk(a, c, askdir, inpfrm, x, y)).grid()
    askdir.mainloop()


def custo_srch_tble(a, x, y, edtdb):
    global chkbtn

    def srch_date(a, x, y, d, fm):
        def Booking(event):
            value=cusdbtbl.item(cusdbtbl.selection())
            fc = value['values']
            dbs=sqlite3.connect('record.db')
            con=dbs.cursor()
            con.execute(f"Select bill from customers where Slip_No='{fc[3]}'")
            data=con.fetchall()
            os.startfile(data[0][0])
            
        
        sc = d.get("1.0", END)
        if sc == '':
            messagebox.showerror("Error", "There is not date entered to search...!")
        else:
            src = sc[:-1]

            conn = sqlite3.connect('record.db')
            cn = conn.cursor()
            q = "SELECT * FROM customers WHERE Date='{}'".format(src)
            cn.execute(q)
            data = cn.fetchall()

            if not data:
                messagebox.showinfo("Information", "There is no entry on the entered date "+src)
                fm.destroy()
            else:
                a.destroy()

                z = Frame(x, bd=3, relief=RIDGE, width=750, height=620)
                z.pack(after=y, expand=True)

                dbsbr = Scrollbar(z)
                dbsbr.pack(side=RIGHT, fill='y')

                cusdbtbl = ttk.Treeview(z, height=44)
                cusdbtbl["columns"] = ("one", "two", "three", "four", "five", "six")
                cusdbtbl.column("#0", width=60, minwidth=60, stretch=NO)
                cusdbtbl.column("one", width=240, minwidth=240, stretch=NO)
                cusdbtbl.column("two", width=150, minwidth=150, stretch=NO)
                cusdbtbl.column("three", width=200, minwidth=200, stretch=NO)
                cusdbtbl.column("four", width=150, minwidth=150, stretch=NO)
                cusdbtbl.column("five", width=120, minwidth=120, stretch=NO)
                cusdbtbl.column("six", width=120, minwidth=120, stretch=NO)

                cusdbtbl.heading("#0", text="SL.NO.", anchor=W)
                cusdbtbl.heading("one", text="Customer Name", anchor=W)
                cusdbtbl.heading("two", text="Phone Number", anchor=W)
                cusdbtbl.heading("three", text="Address", anchor=W)
                cusdbtbl.heading("four", text="Slip Number", anchor=W)
                cusdbtbl.heading("five", text="Date", anchor=W)
                cusdbtbl.heading("six", text="Total Cost", anchor=W)
                cusdbtbl.pack(side=TOP)
                cusdbtbl.bind('<Double-Button-1>',Booking)

                dbsbr.config(command=cusdbtbl.yview)
                cusdbtbl.config(yscrollcommand=dbsbr.set)
                
                l = len(data)
                for i in range(l):
                    cusdbtbl.insert('', END, text=str(i + 1) + '.', values=(data[i][0], data[i][1], data[i][2],
                                                                            data[i][3], data[i][4], data[i][5]))
                fm.destroy()
            conn.close()

    edtdb.config(bg='red3')
    chkbtn = 2
    askdir = Tk()
    askdir.geometry("570x180")
    askdir.title("Enter Password")
    askdir.config(bg='cyan')
    frm = Frame(askdir, bg='wheat4')
    frm.pack()
    frm1 = Frame(frm, bd=3, relief=RIDGE, bg='dark slate gray')
    frm1.pack(side=TOP)
    frm2 = Frame(frm, bd=3, relief=RIDGE)
    frm2.pack(after=frm1)
    frm3 = Frame(frm, bd=3, relief=RIDGE)
    frm3.pack(after=frm2)
    frm1lbl = Label(frm1, text='Enter Date to Search (dd/mm/yyyy) : ',
                    font=('Viner Hand ITC', 20, 'bold'), bg='snow3')
    frm1lbl.grid(padx=10, pady=10)
    inpfrm = Text(frm2, height=1, width=30, font=('MV Boli', 18, 'bold'))
    inpfrm.grid()
    btn = Button(frm3, text='Search', bd=2, height=1, width=14, font=('arial', 18, 'bold'),
                 command=lambda: srch_date(a, x, y, inpfrm, askdir)).grid(row=0, column=0)

    askdir.mainloop()


def mainwindow(pi):

    pi.destroy()
    window.geometry("1210x780+150+3")
    window.maxsize(1210, 780)
    window.title("HERO AUTOMOBILES")
    window.config(bg='SkyBlue1')

    MainFrame = Frame(window, bg="black", relief=RIDGE)
    MainFrame.pack(fill='both', expand=True)

    titframe = Frame(MainFrame, bg='SkyBlue1', bd=10, pady=3, relief=RIDGE)
    titframe.pack(side=TOP, fill='x')

    rigtfrm = Frame(MainFrame, bd=2, bg='white')
    rigtfrm.pack(side=RIGHT, fill='both', expand=NO)
    rigtfrm.bind('<Enter>', pf.E_widgets)
    rigtfrm.bind('<Leave>', pf.L_widgets)

    lftfrm = Frame(MainFrame, bd=2, bg='white')
    lftfrm.pack(side=LEFT, fill='both', expand=NO)
    lftfrm.bind('<Enter>', pf.E_widgets)
    lftfrm.bind('<Leave>', pf.L_widgets)

    # ------------------- customer data input frame ----------------------

    contframe = Frame(lftfrm, bg='black', bd=6, relief=RIDGE)
    contframe.pack(side=TOP)

    custframe = Frame(contframe, bg="cyan", bd=2, relief=RIDGE)
    custframe.pack(fill='x')
    custframe.bind('<Enter>', pf.E_widgets)
    custframe.bind('<Leave>', pf.L_widgets)

    custitfrm = Frame(custframe, bg='firebrick4', bd=4, relief=RIDGE)
    custitfrm.pack(side=TOP)

    cus1 = Frame(custframe, bg='grey77', bd=2, relief=RIDGE)
    cus1.pack(fill='x')

    srchcutfrm = Frame(contframe, bd=2, relief=RIDGE)
    srchcutfrm.pack(side=BOTTOM, fill='x')
    srchcutfrm.bind('<Enter>', pf.E_SDG)
    srchcutfrm.bind('<Leave>', pf.L_SDG)

    # -------------------- Product data input frame --------------------------

    Productdata = Frame(rigtfrm, bg="grey77", bd=6, relief=RIDGE)
    Productdata.pack(side=TOP, fill='x')

    Productfrm = Frame(Productdata, bg="grey77", bd=2, relief=RIDGE)
    Productfrm.pack(fill='x')
    Productfrm.bind('<Enter>', pf.E_widgets)
    Productfrm.bind('<Leave>', pf.L_widgets)

    Producttitfrm = Frame(Productfrm, bg="firebrick4", bd=4, relief=RIDGE)
    Producttitfrm.pack(side=TOP, fill='x')

    Product1 = Frame(Productfrm, bg="grey77", bd=2, relief=RIDGE)
    Product1.pack(fill='x')

    # --------------------------- Button Store Frame --------------------------------------

    btnframe = Frame(rigtfrm, bg='Cadet Blue', bd=10, relief=RIDGE)
    btnframe.pack(after=Productdata, fill='x')

    btnfrm1 = Frame(btnframe, bg='cyan', bd=2, relief=RIDGE)
    btnfrm1.pack(side=LEFT)

    btnfrm2 = Frame(btnframe, bg='cyan', bd=2, relief=RIDGE)
    btnfrm2.pack(side=RIGHT)

    # ----------------------------- Bill Frame -------------------------------------

    btmfrm = Frame(rigtfrm, bd=2, bg='Cadet Blue')
    btmfrm.pack(side=BOTTOM, after=btnframe, fill='both', expand=True)
    btmfrm.bind('<Enter>', pf.E_widgets)
    btmfrm.bind('<Leave>', pf.L_widgets)

    sbilbr = Scrollbar(btmfrm)
    sbilbr.pack(side=RIGHT, fill='y')

    biltbl = ttk.Treeview(btmfrm, height=22)
    biltbl["columns"] = ("one", "two", "three")
    biltbl.column("#0", width=230, minwidth=230, stretch=NO)
    biltbl.column("one", width=135, minwidth=135, stretch=NO)
    biltbl.column("two", width=130, minwidth=130, stretch=NO)
    biltbl.column("three", width=130, minwidth=130, stretch=NO)

    biltbl.heading("#0", text="Product Name", anchor=W)
    biltbl.heading("one", text="Date Ordered", anchor=W)
    biltbl.heading("two", text="Quantity", anchor=W)
    biltbl.heading("three", text="Cost", anchor=W)

    biltbl.pack(side=TOP)

    sbilbr.config(command=biltbl.yview)
    biltbl.config(yscrollcommand=sbilbr.set)

    # ---------------------------------- Receipt Frame ------------------------------------

    recptfrm = Frame(lftfrm, height=395, width=570, bd=3, bg='khaki3', relief=RIDGE)
    recptfrm.pack(side=BOTTOM, after=contframe)
    recptfrm.bind('<Enter>', pf.E_rcptfem)
    recptfrm.bind('<Leave>', pf.L_recptfrm)

    textreciept = Text(recptfrm)
    textreciept.pack(fill='both')
    textreciept.config(state='normal')
    textreciept.bind('<Enter>', pf.E_reciept)
    textreciept.bind('<Leave>', pf.L_reciept)

    #  _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_LABELS and ENTRIES and BUTTONS_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

    # ------------------------------------ Main Label -------------------------------------

    lblTitle = Label(titframe, font=('Bell MT', 55, 'bold'), text=" HERO AUTOMOBILES  ",
                     bd=21, bg='SkyBlue1', fg='AntiqueWhite1', justify=CENTER)
    lblTitle.grid(row=0, column=0, padx=185)

    # -------------------------------- Customer frame label ---------------------------------

    lblcustitfrm = Label(custitfrm, font=('Bell MT', 24, 'bold'), text='Customer Details',
                         bg='firebrick4', fg='gold')
    lblcustitfrm.grid(padx=140, pady=2)

    # -------------------------------- Product frame label ------------------------------------

    lblProducttitfrm = Label(Producttitfrm, font=('Bell MT', 24, 'bold'), text='Select Product from below',
                          bg='firebrick4', fg='gold', justify=CENTER)
    lblProducttitfrm.grid(row=0, column=0, padx=85, pady=2)

    # _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_ BUTTONS _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

    srchbutton = Button(srchcutfrm, text='Data Base\nCharts', font=('Bell MT', 18, 'bold'), width=20,
                        bg='orange red', command=lambda: db_chrt_btn(pwd, MainFrame))
    srchbutton.grid(row=0, column=0, padx=15, pady=5)
    srchbutton.bind('<Enter>', pf.E_srchcusto)
    srchbutton.bind('<Leave>', pf.L_srchcusto)

    resetbtn = Button(srchcutfrm, text='Reset All', font=('Bell MT', 14, 'bold'), width=14, height=2, bg='medium orchid',
                      command=lambda: reset_all(textreciept, biltbl, namEntry))
    resetbtn.grid(row=0, column=1, padx=15)
    resetbtn.bind('<Enter>', pf.E_resetbtn)
    resetbtn.bind('<Leave>', pf.L_resetbtn)

    prntbtn = Button(btnfrm1, text='Print Bill', width=7, height=2, font=('Bell MT', 16, 'bold'), bg='medium aquamarine',
                     bd=2, command=lambda: prnt_bill(textreciept))
    prntbtn.grid(row=0, column=2)
    prntbtn.bind('<Enter>', pf.E_prntbtn)
    prntbtn.bind('<Leave>', pf.L_prntbtn)

    addbtn = Button(btnfrm1, text='Add Item', width=8, height=2, font=('Bell MT', 16, 'bold'),
                    bg='medium aquamarine', command=lambda: add_item(biltbl))
    addbtn.grid(row=0, column=0)
    addbtn.bind('<Enter>', pf.E_addbtn)
    addbtn.bind('<Leave>', pf.L_addbtn)

    ttlbtn = Button(btnfrm1, text='Reset one side', width=12, height=2, font=('Bell MT', 16, 'bold'),
                    bg='medium aquamarine', command=lambda: rest_above(textreciept))
    ttlbtn.grid(row=0, column=1)
    ttlbtn.bind('<Enter>', pf.E_totbtn)
    ttlbtn.bind('<Leave>', pf.L_totbtn)

    billbtn = Button(btnfrm2, text='Generate Bill', width=10, height=2, font=('Bell MT', 16, 'bold'),
                     bg='medium aquamarine', command=lambda: generate_bill(textreciept))
    billbtn.grid(row=0, column=0)
    billbtn.bind('<Enter>', pf.E_billbtn)
    billbtn.bind('<Leave>', pf.L_billbtn)

    extbtn = Button(btnfrm2, text='Log Out', width=7, height=2, font=('Bell MT', 16, 'bold'),
                    bg='medium aquamarine', command=lambda: log_out(MainFrame))
    extbtn.grid(row=0, column=1)
    extbtn.bind('<Enter>', pf.E_exitbtn)
    extbtn.bind('<Leave>', pf.L_exitbtn)

    # ----------------------------------- Customer frame details ------------------------------

    slp = Label(cus1, text="SLIP NO.       \t:    ", font=('Bell MT', 18, 'bold'), bg='deep pink')
    slp.grid(row=0, column=0, sticky=W, padx=8, pady=8)
    slpno = Entry(cus1, textvariable=slpvar, font=('Bell MT', 18, 'bold'), state='disable')
    slpno.grid(row=0, column=1, padx=8, pady=8)
    slpno.bind('<Enter>', pf.showtime)
    slpno.bind('<Leave>', pf.showtimeends)

    dte = Label(cus1, text="Date\t\t:    ", font=('Bell MT', 18, 'bold'), bg='deep pink')
    dte.grid(row=1, column=0, sticky=W, padx=8, pady=8)
    tdte = Entry(cus1, textvariable=Datevar, font=('Bell MT', 18, 'bold'), state='disable')
    tdte.grid(row=1, column=1, padx=8, pady=8)
    tdte.bind('<Enter>', pf.showtime)
    tdte.bind('<Leave>', pf.showtimeends)

    def nxtfcus1(event):
        pnoEntry.focus_set()

    def nxtfcus2(event):
        adresentry.focus_set()

    nam = Label(cus1, text="Name\t\t:    ", font=('Bell MT', 18, 'bold'), bg='deep pink')
    nam.grid(row=2, column=0, sticky=W, padx=8, pady=8)
    namEntry = Entry(cus1, textvariable=namvar, font=('Bell MT', 18, 'bold'))
    namEntry.grid(row=2, column=1, padx=8, pady=8)
    namEntry.focus_set()
    namEntry.bind('<Enter>', pf.showtime)
    namEntry.bind('<Leave>', pf.showtimeends)
    namEntry.bind('<Return>', nxtfcus1)

    pno = Label(cus1, text="Phone No.\t:    ", font=('Bell MT', 18, 'bold'), bg='deep pink')
    pno.grid(row=3, column=0, sticky=W, padx=8, pady=8)
    pnoEntry = Entry(cus1, textvariable=pnovar, font=('Bell MT', 18, 'bold'))
    pnoEntry.grid(row=3, column=1, padx=8, pady=8)
    pnoEntry.bind('<Enter>', pf.showtime)
    pnoEntry.bind('<Leave>', pf.showtimeends)
    pnoEntry.bind('<Return>', nxtfcus2)

    adres = Label(cus1, text="Address      \t:    ", font=('Bell MT', 18, 'bold'), bg='deep pink')
    adres.grid(row=4, column=0, sticky=W, padx=8, pady=8)
    adresentry = Entry(cus1, textvariable=adressvar, font=('Bell MT', 18, 'bold'))
    adresentry.grid(row=4, column=1, padx=8, pady=8)
    adresentry.bind('<Enter>', pf.showtime)
    adresentry.bind('<Leave>', pf.showtimeends)

    # ----------------------------- Product frame details ---------------------------------


    foditem = Label(Product1, text='Select Product    \t\t:', font=('Bell MT', 18, 'bold'), bg='deep pink')
    foditem.grid(row=1, column=0, sticky=W, padx=5, pady=5)

    # ------------------------------ List of Product -----------------------------------------------

    def datafetch(event):
        global itemVariable
        x = lbx.get(ACTIVE)
        conn = sqlite3.connect('autoparts.db')
        cn = conn.cursor()
        q = f"SELECT Price FROM hero_parts WHERE Products='{x}' "
        cn.execute(q)
        data = cn.fetchall()
        itemVariable.set(x)
        rateVar.set(int(data[0][0]))
        quantityEntry.focus_set()

    fodslct = Frame(Product1, bd=2, relief=RIDGE)
    fodslct.grid(row=1, column=1)
    sbr = Scrollbar(fodslct)
    sbr.pack(side=RIGHT, fill='y')
    lbx = Listbox(fodslct, font=('Bell MT', 14, 'bold'), width=21, height=3)
    lbx.pack(fill='both', expand=True)
    lbx.bind('<Double-Button-1>', datafetch)
    lbx.bind('<Enter>', pf.showtime)
    lbx.bind('<Leave>', pf.showtimeends)
    for i in options:
        lbx.insert(END, i)
    sbr.config(command=lbx.yview)
    lbx.config(yscrollcommand=sbr.set)
    # -----------------------------------------------------------

    def additem(event):
        add_item(biltbl)

    def mke_bil(event):
        generate_bill(textreciept)

    rateLabel = Label(Product1, text='Price of Product    \t\t:', font=('Bell MT', 18, 'bold'), bg='deep pink')
    rateLabel.grid(row=2, column=0, sticky=W, padx=5, pady=5)
    rateValue = Label(Product1, textvariable=rateVar, font=('Bell MT', 18, 'bold'), bg='grey77')
    rateValue.grid(row=2, column=1, padx=5, pady=5)
    rateValue.bind('<Enter>', pf.showtime)
    rateValue.bind('<Leave>', pf.showtimeends)

    quantityLabel = Label(Product1, text='Quantity     \t\t:', font=('Bell MT', 18, 'bold'), bg='deep pink')
    quantityLabel.grid(row=3, column=0, sticky=W, padx=5, pady=5)
    quantityEntry = Entry(Product1, textvariable=quantityVar, font=('Bell MT', 18, 'bold'))
    quantityEntry.grid(row=3, column=1, padx=5, pady=5)
    quantityEntry.bind('<Enter>', pf.showtime)
    quantityEntry.bind('<Leave>', pf.showtimeends)
    quantityEntry.bind('<Return>', additem)

    costLabel = Label(Product1, text='Cost (in Rupees)    \t\t:', font=('Bell MT', 18, 'bold'), bg='deep pink')
    costLabel.grid(row=4, column=0, sticky=W, padx=5, pady=5)
    costEntry = Entry(Product1, textvariable=costVar, font=('Bell MT', 18, 'bold'))
    costEntry.grid(row=4, column=1, sticky=W, padx=5, pady=5)
    costEntry.bind('<Enter>', pf.showtime)
    costEntry.bind('<Leave>', pf.showtimeends)
    costEntry.bind('<Return>', mke_bil)


# @@@@@@@@@@@@@@@@@@@@@@@ Create user page @@@@@@@@@@@@@@@@@@@@


def create_page():
    def create():
        global fstnmevar
        global sndnmevar
        global epnovar
        global emlvar
        global pass1var
        global pass2var
        global adhVar
        global sqpin

        first = fstnmevar.get()
        second = sndnmevar.get()
        phone = epnovar.get()
        email = emlvar.get()
        passwd1 = pass1var.get()
        passwd2 = pass2var.get()
        adh=adhVar.get()
        sqp=sqpin.get()

        checkblank = pf.detail_blank(first, second, phone, email, passwd1, passwd2,adh,sqp)
        check = False
        checkpswd = False
        w = 0
        if checkblank:
            w = 1
            check = pf.check_creat_details(first, second, phone, email)
            if check:
                checkpswd = pf.check_create_password(passwd1, passwd2)
                if checkpswd:
                    ed = pf.creating_new_user(first, second, phone, email, passwd2,adh,sqp, w)
                    if ed:
                        messagebox.showinfo("Information", "Successfully created User ID...!")
                        ans = messagebox.askyesno("", "Do you directly want to go to the MainPage...?")
                        if ans > 0:
                            go_to_main(Createfrm)
                        else:
                            messagebox.showinfo("Information", "Your page is been redirected to Login Page...")
                            messagebox.showinfo("", "Login securely...!")
                            go_to_login(Createfrm)
                    else:
                        messagebox.showerror("Error", "Sorry, Failed to create your account...!")
                        return
                else:
                    pass1var.set('')
                    pass2var.set('')
                    messagebox.showinfo("Information", "Try re-entering your password...!")
                    return
            else:
                messagebox.showinfo("Information", "Please Enter your details Carefully...!")
                return
        else:
            pass

    # _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_ Frames _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

    Createfrm = Frame(window, bg="cyan")
    Createfrm.pack(fill='both', expand=True)

    frm = Frame(Createfrm, bd=3)
    frm.pack(fill='both', expand=True)
    frm.bind('<Enter>', pf.E_widgets)
    frm.bind('<Leave>', pf.L_widgets)

    frm1 = Frame(frm, bd=3)
    frm1.pack(fill='both', expand=True)
    frm1.bind('<Enter>', pf.E_lgtit)
    frm1.bind('<Leave>', pf.L_lgtit)

    titlefem = Frame(frm1, bd=5, bg='thistle2', relief=RIDGE)
    titlefem.pack(side=TOP, fill='x')

    btmfrm = Frame(frm1, bd=5, bg='antique white', height=480, width=520, relief=RIDGE)
    btmfrm.pack(after=titlefem, expand=True, fill='both')

    ttle = Label(titlefem, text='CREATE NEW USER', font=('Bell Mt', 34, 'bold'), bg='thistle2',
                 fg='deep pink')
    ttle.grid(row=0, column=0, padx=70, pady=5)

    usrnmfrm = Frame(btmfrm, bd=1, bg='antique white', relief=RIDGE, height=20)
    usrnmfrm.pack(fill='x', pady=15)

    pswdfrm = Frame(btmfrm, bd=1, bg='antique white', relief=RIDGE, height=20)
    pswdfrm.pack(after=usrnmfrm, fill='x')

    btnfrm = Frame(btmfrm, bd=4, bg='antique white', relief=RIDGE, height=20, width=100)
    btnfrm.pack(after=pswdfrm, pady=20)

    extfrm = Frame(btmfrm, bd=4, bg='antique white', relief=RIDGE)
    extfrm.pack(after=btnfrm, pady=10)

    # _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_ Labels_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

    def nxtetry(event):
        usrttlenrty2.focus_set()

    def nxtetry1(event):
        numtitetry.focus_set()

    def nxtetry2(event):
        adhtitetry.focus_set()

    def nxtetry3(event):
        emlttlenrty.focus_set()

    def nxtetry4(event):
        paslbl1etry.focus_set()

    def nxtetry5(event):
        paslbl2etry.focus_set()

    def nxtetry6(event):
        splbl2etry.focus_set()

    def crtusr(event):
        create()

    usrttl = Label(usrnmfrm, text='First name        :', font=('Courier New', 18, 'bold'), bg='antique white')
    usrttl.grid(row=1, column=1, sticky=W, padx=20, pady=10)
    usrttlenrty = Entry(usrnmfrm, textvariable=fstnmevar, font=('Microsoft JhengHei', 14, 'bold'))
    usrttlenrty.grid(row=1, column=3, padx=20, pady=10)
    usrttlenrty.focus_set()
    usrttlenrty.bind('<Enter>', pf.showtime)
    usrttlenrty.bind('<Leave>', pf.showtimeends)
    usrttlenrty.bind('<Return>', nxtetry)

    usrtt2 = Label(usrnmfrm, text='Last name         :', font=('Courier New', 18, 'bold'), bg='antique white')
    usrtt2.grid(row=2, column=1, sticky=W, padx=20, pady=10)
    usrttlenrty2 = Entry(usrnmfrm, textvariable=sndnmevar, font=('Microsoft JhengHei', 14, 'bold'))
    usrttlenrty2.grid(row=2, column=3, padx=20, pady=10)
    usrttlenrty2.bind('<Enter>', pf.showtime)
    usrttlenrty2.bind('<Leave>', pf.showtimeends)
    usrttlenrty2.bind('<Return>', nxtetry1)

    numtit = Label(usrnmfrm, text='Phone No.         :', font=('Courier New', 18, 'bold'), bg='antique white')
    numtit.grid(row=3, column=1, sticky=W, padx=20, pady=10)
    numtitetry = Entry(usrnmfrm, textvariable=epnovar, font=('Microsoft JhengHei', 14, 'bold'))
    numtitetry.grid(row=3, column=3, padx=20, pady=10)
    numtitetry.bind('<Enter>', pf.showtime)
    numtitetry.bind('<Leave>', pf.showtimeends)
    numtitetry.bind('<Return>', nxtetry2)

    adhtit = Label(usrnmfrm, text='Aadhaar No.       :', font=('Courier New', 18, 'bold'), bg='antique white')
    adhtit.grid(row=4, column=1, sticky=W, padx=20, pady=10)
    adhtitetry = Entry(usrnmfrm, textvariable=adhVar, font=('Microsoft JhengHei', 14, 'bold'))
    adhtitetry.grid(row=4, column=3, padx=20, pady=10)
    adhtitetry.bind('<Enter>', pf.showtime)
    adhtitetry.bind('<Leave>', pf.showtimeends)
    adhtitetry.bind('<Return>', nxtetry3)
    

    emlttl = Label(usrnmfrm, text='Email             :', font=('Courier New', 18, 'bold'), bg='antique white')
    emlttl.grid(row=5, column=1, sticky=W, padx=20, pady=10)
    emlttlenrty = Entry(usrnmfrm, textvariable=emlvar, font=('Microsoft JhengHei', 14, 'bold'))
    emlttlenrty.grid(row=5, column=3, padx=20, pady=10)
    emlttlenrty.bind('<Enter>', pf.showtime)
    emlttlenrty.bind('<Leave>', pf.showtimeends)
    emlttlenrty.bind('<Return>', nxtetry4)

    paslbl1 = Label(pswdfrm, text='Password\t  :', font=('Courier New', 18, 'bold'), bg='antique white')
    paslbl1.grid(row=1, column=1, sticky=W, padx=20, pady=10)
    paslbl1etry = Entry(pswdfrm, textvariable=pass1var, show='*', font=('Courier New', 14, 'bold'))
    paslbl1etry.grid(row=1, column=3, padx=20, pady=10)
    paslbl1etry.bind('<Enter>', pf.showtime)
    paslbl1etry.bind('<Leave>', pf.showtimeends)
    paslbl1etry.bind('<Return>', nxtetry5)

    paslbl2 = Label(pswdfrm, text='Confirm password  :', font=('Courier New', 18, 'bold'), bg='antique white')
    paslbl2.grid(row=2, column=1, sticky=W, padx=20, pady=10)
    paslbl2etry = Entry(pswdfrm, textvariable=pass2var,show='*', font=('Courier New', 14, 'bold'))
    paslbl2etry.grid(row=2, column=3, padx=20, pady=10)
    paslbl2etry.bind('<Enter>', pf.showtime)
    paslbl2etry.bind('<Leave>', pf.showtimeends)
    paslbl2etry.bind('<Return>', nxtetry6)

    splbl2 = Label(pswdfrm, text='Security Pin           :', font=('Courier New', 18, 'bold'), bg='antique white')
    splbl2.grid(row=3, column=1, sticky=W, padx=20, pady=10)
    splbl2etry = Entry(pswdfrm, textvariable=sqpin, font=('Courier New', 14, 'bold'))
    splbl2etry.grid(row=3, column=3, padx=20, pady=10)
    splbl2etry.bind('<Enter>', pf.showtime)
    splbl2etry.bind('<Leave>', pf.showtimeends)
    splbl2etry.bind('<Return>', crtusr)

    # _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_ BUTTONS _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

    crtusrbtn = Button(btnfrm, text='Create User', font=('Copperplate Gothic Bold', 16, 'bold'),
                       bd=3, width=15, height=2, bg='plum2', command=create)
    crtusrbtn.pack(side=LEFT)
    crtusrbtn.bind('<Enter>', pf.E_cr_usr_btn)
    crtusrbtn.bind('<Leave>', pf.L_cr_usr_btn)

    cncl = Button(btnfrm, text='Cancel', font=('Copperplate Gothic Bold', 16, 'bold'), bd=3,
                  width=8, height=2, bg='tomato2', command=lambda: ext_creat(Createfrm))
    cncl.pack(side=RIGHT)
    cncl.bind('<Enter>', pf.E_cl_usr_btn)
    cncl.bind('<Leave>', pf.L_cl_usr_btn)


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ LOGIN PAGE @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def log_in_page():
    global pwd
    sctpin=StringVar()
    cpvar=StringVar()
    cppvar=StringVar()

    def logging():
        global gmailVar
        global passwordVar
        global pwd

        mail = gmailVar.get()
        pwrd = passwordVar.get()

        chkblnk = False

        chkblnk = pf.check_login_blanks(mail, pwrd)
        if chkblnk:
            chklog = pf.check_login_details(mail, pwrd)
            if chklog:
                pwd = pwrd
                go_to_main(LogFrame)
            else:
                gmailVar.set('')
                passwordVar.set('')
                messagebox.showerror("Error", "Credentials input are invalid...!")
        else:
            messagebox.showinfo("Information", "Necessary to fill the details..!")

    # _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_ Frames _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

    gmailVar.set('')
    passwordVar.set('')

    window.title("Login Page")
    
    window.configure(bg='bisque2',border='1px solid')

    LogFrame = Frame(window, bg="gray55")
    LogFrame.pack(fill='both')

    frm = Frame(LogFrame, bd=3)
    frm.pack()
    frm.bind('<Enter>', pf.E_widgets)
    frm.bind('<Leave>', pf.L_widgets)

    frm1 = Frame(frm, bd=3,bg='bisque2')
    frm1.pack()
    frm1.bind('<Enter>', pf.E_lgtit)
    frm1.bind('<Leave>', pf.L_lgtit)

    titlefem = Frame(frm1, bd=5, bg='gold', relief=GROOVE)
    titlefem.pack(side=TOP, fill='x')

    btmfrm = Frame(frm1, bd=5, bg='floral white', height=480, width=520, relief=RIDGE)
    btmfrm.pack(after=titlefem, expand=True, fill='both')

    ttle = Label(titlefem, text='LOGIN PAGE', font=('ALGERIAN', 50, 'bold'), bg='gold',
                 fg='white')
    ttle.grid(row=0, column=0, padx=140, pady=5)
    global bg
    bg=PhotoImage(file=r"download.png")
    phtfrm=Label(btmfrm,image=bg)
    phtfrm.pack(anchor=CENTER)
    
    usrnmfrm = Frame(btmfrm, bd=4, bg='light goldenrod', relief=RIDGE, height=20)
    usrnmfrm.pack(fill='x', pady=(20,30))

    pswdfrm = Frame(btmfrm, bd=4, bg='light goldenrod', relief=RIDGE, height=20)
    pswdfrm.pack(after=usrnmfrm, fill='x')

    btnfrm = Frame(btmfrm, bd=1, bg='floral white', relief=FLAT, height=20, width=100)
    btnfrm.pack(after=pswdfrm)

    btnfrme = Frame(btmfrm, bd=1, bg='floral white', relief=FLAT, height=20, width=100)
    btnfrme.pack(after=btnfrm)

    extfrm = Frame(btmfrm, bd=1, bg='floral white', relief=FLAT)
    extfrm.pack(after=btnfrme)

    def saveDb(a,b,c,f,e):
        global sctpin,cpvar,cppvar
        a = a.get()
        b=b.get()
        c=c.get()
        ml=gmailVar.get()
        if a==f[0][0]:
            if  b!='' and c!='':
                if b==c:
                    mydb=sqlite3.connect('record.db')
                    mycr=mydb.cursor()
                    mycr.execute(f"update User_ids set Password='{b}' where Gmail='{ml}'")
                    mydb.commit()
                    mydb.close()
                    messagebox.showinfo("Success","Password changed successfully")
                    e.destroy()
                else:
                    messagebox.showinfo("Error","Enter the same password")
            else:
                messagebox.showinfo("Error","Enter the password first")
        else:
            messagebox.showinfo("Error","Incorrect security pin")

            
        
    def fgpWin(a):
        global sctpin
        global cpvar
        global cppvar
        update = Tk()
        update.geometry('540x420')
        update.title('Change password')
        update.config(bg='cyan4')

        frm = Frame(update, bd=3, bg='wheat4')
        frm.pack(expand=True)
        frminp = Frame(frm, bd=2, relief=RIDGE, bg='snow3')
        frminp.pack(fill='both')
        frmbtn = Frame(frm, bd=2, relief=RIDGE)
        frmbtn.pack(after=frminp, pady=15)

        footit = Label(frminp, text='Security Pin : ', font=('Bradley Hand ITC', 22, 'bold'), bg='snow3')
        footit.grid(row=0, column=0, sticky=W, pady=10)
        ratetit = Label(frminp, text='New Password  : ', font=('Bradley Hand ITC', 22, 'bold'), bg='snow3')
        ratetit.grid(row=1, column=0, sticky=W, pady=10)
        ratetit = Label(frminp, text='Confirm New Password: ', font=('Bradley Hand ITC', 22, 'bold'), bg='snow3')
        ratetit.grid(row=2, column=0, sticky=W, pady=10)

        sv1 = Entry(frminp, textvariable=sctpin,font=('Courier New', 16))
        sv1.grid(row=0, column=1, pady=10, padx=10)

        sv2 =Entry(frminp,textvariable=cpvar, show='*', font=('Courier New', 16))
        sv2.grid(row=1, column=1, pady=10, padx=10)
        
        sv3 = Entry(frminp, textvariable=cppvar, show='*',font=('Courier New', 16))
        sv3.grid(row=2, column=1, pady=10, padx=10)
        
        savebtn = Button(frmbtn, text='SAVE CHANGES', width=14, font=('Copperplate Gothic Bold', 18, 'bold'),
                             command=lambda: saveDb(sv1,sv2,sv3,a,update), bg='bisque')
        savebtn.grid(row=0, column=1)
        savebtn.bind('<Enter>', pf.E_lst)
        savebtn.bind('<Leave>', pf.L_lst)

        cnclbtn = Button(frm, text='CANCEL', width=8, font=('Copperplate Gothic Bold', 18, 'bold'), bd=4,
                         command=lambda: update.destroy(),  bg='bisque')
        cnclbtn.pack(after=frmbtn)
        cnclbtn.bind('<Enter>', pf.E_lst)
        cnclbtn.bind('<Leave>', pf.L_lst)
        update.mainloop()
    def fgpas():
        ml=gmailVar.get()
        if ml!='':
            conn = sqlite3.connect('record.db')
            c = conn.cursor()
            q = f"select spin from user_ids where Gmail='{ml}'"
            c.execute(q)
            data=c.fetchall()
            conn.close()
            if len(data)>0:
                fgpWin(data)
            else:
                messagebox.showerror("Error", "No such user exists...!")
        else:
            messagebox.showerror("Error", "Please enter the email first")


    
    # _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_ Labels_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

    def nxtfrmlg(event):
        pswdentry.focus_set()
    sctpin=StringVar()
    cpvar=StringVar()
    cppvar=StringVar()
    emlttl = Label(usrnmfrm, text='E-mail\t    :', font=('BankGothic Md BT', 18, 'bold'), bg='light goldenrod')
    emlttl.grid(row=4, column=1, sticky=W, padx=20, pady=20)
    emlttlenrty = Entry(usrnmfrm, textvariable=gmailVar, font=('Courier New', 14, 'bold'))
    emlttlenrty.grid(row=4, column=3, padx=20, pady=20)
    emlttlenrty.focus_set()
    emlttlenrty.bind('<Enter>', pf.showtime)
    emlttlenrty.bind('<Leave>', pf.showtimeends)
    emlttlenrty.bind('<Return>', nxtfrmlg)

    def nxtfrmlg1(event):
        logging()
        

    pswdlbl = Label(pswdfrm, text='Password    :', font=('BankGothic Md BT', 18, 'bold'), bg='light goldenrod')
    pswdlbl.grid(row=0, column=1, sticky=W, padx=20, pady=20)
    pswdentry = Entry(pswdfrm, textvariable=passwordVar, show='*', font=('Courier New', 14, 'bold'))
    pswdentry.grid(row=0, column=3, padx=20, pady=20)
    pswdentry.bind('<Enter>', pf.showtime)
    pswdentry.bind('<Leave>', pf.showtimeends)
    pswdentry.bind('<Return>', nxtfrmlg1)

    # _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_ BUTTONS _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

    crtbtn = Button(btnfrm, text='Create New User', font=('Copperplate Gothic Bold', 16, 'bold'),
                    bd=3, width=15, height=2, bg='thistle2', command=lambda: go_to_create(LogFrame))
    crtbtn.pack(side=LEFT)
    crtbtn.bind('<Enter>', pf.E_crete_n_usr)
    crtbtn.bind('<Leave>', pf.L_crete_n_usr)

    lginbtn = Button(btnfrm, text='Log In', font=('Copperplate Gothic Bold', 16, 'bold'), bd=3,
                     width=8, height=2, bg='SpringGreen2', command=logging)
    lginbtn.pack(side=RIGHT)
    lginbtn.bind('<Enter>', pf.E_lg_login_btn)
    lginbtn.bind('<Leave>', pf.L_lg_login_btn)

    fgbtn = Button(extfrm, text='Forgot Password', font=('Copperplate Gothic Bold', 16, 'bold'), bd=3,
                    width=15, height=1, command=fgpas, bg='coral')
    fgbtn.pack(side=TOP)
    fgbtn.bind('<Enter>', pf.E_exitbtn)
    fgbtn.bind('<Leave>', pf.L_lgextbtn)
    
    extbtn = Button(extfrm, text='Exit', font=('Copperplate Gothic Bold', 16, 'bold'), bd=3,
                    width=8, height=1, command=lambda: pf.exit_btn(window), bg='coral')
    extbtn.pack(side=BOTTOM,pady=5)
    extbtn.bind('<Enter>', pf.E_exitbtn)
    extbtn.bind('<Leave>', pf.L_lgextbtn)


def updt_pas():
    global updt_btn
    if not updt_btn:
        updt_btn = True
        messagebox.showinfo("Information", "Updater is Now Activated....!")
    else:
        updt_btn = False
        messagebox.showinfo("Information", "Updater is Now Deactivated...!")


def add_it_in_db(a, b, c, main):
    item = a.get("1.0", END)
    item = item[:-1]
    rate = b.get("1.0", END)
    rate = int(rate[:-1])
    brand = c.get("1.0", END)
    brand = brand[:-1]
    l = [item, rate, brand]
    main.destroy()
    done = pf.add_in_db(l)
    if done:
        messagebox.showinfo("Information", "Successfully Added...!")
    else:
        messagebox.showerror("Error", "Unable to add new Item...!")


def add_food():

    add_it = Tk()
    add_it.geometry('540x415')
    add_it.title('Update Item')
    add_it.config(bg='cyan4')

    frm = Frame(add_it, bd=3, bg='wheat4')
    frm.pack(expand=True)
    frminf = Frame(frm, bd=2, relief=RIDGE, bg='saddle brown')
    frminf.pack(side=TOP, fill='x')
    frminp = Frame(frm, bd=2, relief=RIDGE, bg='snow3')
    frminp.pack(after=frminf, fill='both')
    frmbtn = Frame(frm, bd=2, relief=RIDGE)
    frmbtn.pack(after=frminp, pady=15)

    tit = Label(frminf, text='Add New Item', font=('Viner Hand ITC', 32, 'bold'), bg='saddle brown')
    tit.grid(padx=115, pady=25)

    footit = Label(frminp, text='Item Name : ', font=('Bradley Hand ITC', 22, 'bold'), bg='snow3')
    footit.grid(row=0, column=0, sticky=W, pady=10)
    ratetit = Label(frminp, text='Rate \t   : ', font=('Bradley Hand ITC', 22, 'bold'), bg='snow3')
    ratetit.grid(row=1, column=0, sticky=W, pady=10)
    regtit = Label(frminp, text='Brand \t   : ', font=('Bradley Hand ITC', 22, 'bold'), bg='snow3')
    regtit.grid(row=2, column=0, sticky=W, pady=10)

    fooetry = Text(frminp, font=('Courier New', 16, 'bold'), height=1, width=25)
    fooetry.grid(row=0, column=1, pady=10, padx=10)
    fooetry.bind('<Enter>', pf.showtime)
    fooetry.bind('<Leave>', pf.showtimeends)

    ratetry = Text(frminp, font=('Courier New', 16, 'bold'), height=1, width=25)
    ratetry.grid(row=1, column=1, pady=10, padx=10)
    ratetry.bind('<Enter>', pf.showtime)
    ratetry.bind('<Leave>', pf.showtimeends)

    regetry = Text(frminp, font=('Courier New', 16, 'bold'), height=1, width=25)
    regetry.grid(row=2, column=1, pady=10, padx=10)
    regetry.bind('<Enter>', pf.showtime)
    regetry.bind('<Leave>', pf.showtimeends)

    savebtn = Button(frmbtn, text='ADD ITEM', width=14, font=('Copperplate Gothic Bold', 18, 'bold'), bg='lavender',
                     command=lambda: add_it_in_db(fooetry, ratetry, regetry, add_it))
    savebtn.grid(row=0, column=0)
    savebtn.bind('<Enter>', pf.E_lst)
    savebtn.bind('<Leave>', pf.L_lst)

    cnclbtn = Button(frmbtn, text='CANCEL', width=8, font=('Copperplate Gothic Bold', 18, 'bold'), bg='lavender',
                     command=lambda: add_it.destroy())
    cnclbtn.grid(row=0, column=1)
    cnclbtn.bind('<Enter>', pf.E_lst)
    cnclbtn.bind('<Leave>', pf.L_lst)

    add_it.mainloop()


def edit_any_db(val, a, z, c, d, pwd, x):
    global edt_btn
    edt_btn = True
    if val == 0:
        messagebox.showinfo("Information", "Please Select the Database...!")
    elif val == 2:
        messagebox.showwarning("Warning", "Cannot Edit this Database...!")
    else:
        a.destroy()

        btnfuncfrm = Frame(z, bd=4, relief=RIDGE, bg='OliveDrab4')
        btnfuncfrm.pack(after=c, fill='x')

        btn1 = Button(btnfuncfrm, text='ADD NEW PRODUCT', height=1, width=20, font=('Informal Roman', 22, 'bold'),
                      command=add_food, bg='misty rose')
        btn1.grid(row=0, column=0, padx=30, pady=20)
        btn1.bind('<Enter>', pf.E_lst)
        btn1.bind('<Leave>', pf.L_lst)

        btn2 = Button(btnfuncfrm, text='UPDATE DATABASE', height=1, width=21, font=('Informal Roman', 22, 'bold'),
                      command=updt_pas, bg='misty rose')
        btn2.grid(row=0, column=1, padx=30, pady=20)
        btn2.bind('<Enter>', pf.E_lst)
        btn2.bind('<Leave>', pf.L_lst)

        btn3 = Button(btnfuncfrm, text='GO BACK', height=1, width=11, font=('Informal Roman', 22, 'bold'),
                      command=lambda: db_chrt_btn(pwd, x), bg='misty rose')
        btn3.grid(row=0, column=2, padx=30, pady=20)
        btn3.bind('<Enter>', pf.E_lst)
        btn3.bind('<Leave>', pf.L_lst)

        messagebox.showinfo("Information", "Double click Left Mouse Button on any item to Open Action center...!")


def db_chrt_btn(pwd, x):

    global updt_btn
    updt_btn = False

    x.destroy()

    global chkbtn
    global edt_btn
    edt_btn = False
    chkbtn = 0

    window.maxsize(1024, 840)

    SearchFrm = Frame(window, height=740, width=640, bg='wheat')
    SearchFrm.pack(side=TOP, fill='both', expand=True)

    SerchTitFrm = Frame(SearchFrm, bd=6, relief=RIDGE, bg='gold')
    SerchTitFrm.pack(side=TOP, fill='x')

    SerchBtnFrm = Frame(SearchFrm, bd=4, relief=RIDGE, bg='OliveDrab4')
    SerchBtnFrm.pack(side=TOP, fill='x')

    SerchDisplaFrm = Frame(SearchFrm, bd=3, relief=RIDGE, width=750, height=620)
    SerchDisplaFrm.pack(after=SerchBtnFrm, expand=True)

    # ====================== Label ==========================

    serchtit = Label(SerchTitFrm, text='Data Base Chart', font=('Old English Text MT', 72, 'bold'),
                     fg='red3', bg='yellow')
    serchtit.grid(padx=170, pady=5)

    # ++++++++++++++++++++++++ Buttons +++++++++++++++++++++++++

    fooddbBtn = Button(SerchBtnFrm, text='Product Database', font=('Copperplate Gothic Bold', 18, 'bold'),
                       width=16, bd=2, command=lambda: Productdb_tble(SerchDisplaFrm, SearchFrm, SerchBtnFrm, edtdb),
                       bg='deep pink')
    fooddbBtn.grid(row=0, column=0, padx=5, pady=5)
    fooddbBtn.bind('<Enter>', pf.E_fooddb)
    fooddbBtn.bind('<Leave>', pf.L_fooddb)

    custodbBtn = Button(SerchBtnFrm, text='Customer Database', font=('Copperplate Gothic Bold', 18, 'bold'),
                        bg='brown4', fg='gray60', width=17, bd=2, command=lambda: custo_tble(SerchDisplaFrm, pwd,
                                                                                             SearchFrm, SerchBtnFrm,
                                                                                             edtdb))
    custodbBtn.grid(row=0, column=1, padx=5, pady=5)
    custodbBtn.bind('<Enter>', pf.E_custodb)
    custodbBtn.bind('<Leave>', pf.L_custodb)

    usrdbBtn = Button(SerchBtnFrm, text='User Database', font=('Copperplate Gothic Bold', 18, 'bold'), bg='purple4',
                      fg='gray60', width=14, bd=2, command=lambda: Usrdb_tble(SerchDisplaFrm, pwd, SearchFrm,
                                                                              SerchBtnFrm, edtdb))
    usrdbBtn.grid(row=0, column=2, padx=5, pady=5)
    usrdbBtn.bind('<Enter>', pf.E_usrdb)
    usrdbBtn.bind('<Leave>', pf.L_usrdb)

    edtdb = Button(SerchBtnFrm, text='Edit', font=('Copperplate Gothic Bold', 18, 'bold'), bg='DodgerBlue2',
                   fg='black', width=9, bd=2, command=lambda: edit_any_db(chkbtn, SerchBtnFrm, SearchFrm, SerchTitFrm,
                                                                          SerchDisplaFrm, pwd, SearchFrm))
    edtdb.grid(row=1, column=0, padx=5, pady=5)

    extbtn = Button(SerchBtnFrm, text='Exit', font=('Copperplate Gothic Bold', 18, 'bold'), bg='dark orange',
                    width=7, bd=2, command=lambda: mainwindow(SearchFrm))
    extbtn.grid(row=1, column=2, padx=5, pady=5)
    extbtn.bind('<Enter>', pf.E_exit_db)
    extbtn.bind('<Leave>', pf.L_exit_db)

    searchbtn = Button(SerchBtnFrm, text='Search Customer Database', font=('Copperplate Gothic Bold', 18, 'bold'),
                       width=23, bd=2, command=lambda: custo_srch_tble(SerchDisplaFrm, SearchFrm, SerchBtnFrm, edtdb),
                       bg='gray10', fg='gray65')
    searchbtn.grid(row=1, column=1, padx=5, pady=5)
    searchbtn.bind('<Enter>', pf.E_srch_db_btn)
    searchbtn.bind('<Leave>', pf.L_srch_db_btn)

    # ::::::::::::::::::::::::::::::::: Table Fromation :::::::::::::::::::::::::::::


log_in_page()
window.mainloop()

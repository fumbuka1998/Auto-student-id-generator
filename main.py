from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import pymysql
import os


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Automated Students ID Generator")
        self.root.geometry("1366x700+0+0")
        self.root.resizable(True, True)
        self.loginform() 


# ---------------------------------------------------------------LOGIN PAGE -------------------------------
    def loginform(self):
        Frame_login = Frame(self.root, bg="light blue")
        Frame_login.place(x=0, y=0, height=700, width=1366)

        #self.img = ImageTk.PhotoImage(file="bg.jpg")
        #img = Label(Frame_login, image = self.img).place(x=0, y=0, height=700, width=1366)

        frame_input = Frame(self.root, bg="white")
        frame_input.place(x=500, y=130, height=450, width=350)

        label1 = Label(frame_input, text="LOGIN HERE", font=('impact', 32, 'bold'),
                       fg="black", bg="white")
        label1.place(x=75, y=20)

        label2 = Label(frame_input, text="Staff No: ", font=("Goudy old style", 20, "bold"),
                       fg='red', bg='white')
        label2.place(x=30, y=95)
        self.staffNo = Entry(frame_input, font=("times new roman", 15, "bold"),
                               bg='lightgray')
        self.staffNo.place(x=30, y=145, width=270, height=35)


        label3 = Label(frame_input, text="Password:", font=("Goudy old style", 20, "bold"),
                       fg='red', bg='white')
        label3.place(x=30, y=195)

        self.password = Entry(frame_input, font=("times new roman", 15, "bold"),
                             bg='lightgray', show="*")
        self.password.place(x=30, y=245, width=270, height=35)

        btn1 =Button(frame_input, text="forget password?", cursor='hand2',
                      font=('calibri', 10), bg='white', fg='black', bd=0)
        btn1.place(x=125, y=305)

        btn2 = Button(frame_input, text="Login", cursor='hand2', command=self.login,
                      font=('times new roman', 15), bg='white', fg='red', bd=2)
        btn2.place(x=150, y=330)

        btn3 = Button(frame_input, text="Not Registered?register", command=self.Register, cursor='hand2',
                     font=('calibri', 10), bg='white', fg='black', bd=0)
        btn3.place(x=110, y=370)

# ---------------------------------------------------------------LOGIN FUNCTION -------------------------------
    def login(self):
        if self.staffNo.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='', database='mydb')
                cur = con.cursor()
                cur.execute('select * from myadmin where staffNo=%s and password=%s',
                            (self.staffNo.get(), self.password.get()))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror('Error', 'Invalid Username and Password', parent=self.root)
                    self.loginClear()
                    self.staffNo.focus()
                else:
                    self.appscreen()
                    con.close()
            except Exception as es:
                messagebox.showerror('Error', f'Error Due to : {str(es)}', parent=self.root)



# ---------------------------------------------------------------REGISTRATION PAGE -------------------------------
    def Register(self):
        Frame_register = Frame(self.root, bg="white")
        Frame_register.place(x=0, y=0, height=700, width=1366)

        self.img = ImageTk.PhotoImage(file="bg.jpg")
        img = Label(Frame_register, image=self.img).place(x=0, y=0, height=700, width=1366)

        frame_input = Frame(self.root, bg="white")
        frame_input.place(x=320, y=130, height=450, width=700)

        label1 = Label(frame_input, text="REGISTER HERE", font=('impact', 32, 'bold'),
                       fg="black", bg="white")
        label1.place(x=45, y=20)

        label2 = Label(frame_input, text="Full Name: ", font=("Goudy old style", 20, "bold"),
                       fg='red', bg='white')
        label2.place(x=30, y=95)
        self.fullName = Entry(frame_input, font=("times new roman", 15, "bold"),
                             bg='lightgray')
        self.fullName.place(x=30, y=145, width=270, height=35)

        label3 = Label(frame_input, text="Staff No: ", font=("Goudy old style", 20, "bold"),
                       fg='red', bg='white')
        label3.place(x=30, y=195)
        self.staffNo = Entry(frame_input, font=("times new roman", 15, "bold"),
                             bg='lightgray')
        self.staffNo.place(x=30, y=245, width=270, height=35)

        label3 = Label(frame_input, text="Password:", font=("Goudy old style", 20, "bold"),
                       fg='red', bg='white')
        label3.place(x=330, y=95)

        self.password = Entry(frame_input, font=("times new roman", 15, "bold"),
                              bg='lightgray', show="*")
        self.password.place(x=330, y=145, width=270, height=35)

        label3 = Label(frame_input, text="Confirm Password:", font=("Goudy old style", 20, "bold"),
                       fg='red', bg='white')
        label3.place(x=330, y=195)

        self.confirmPassword = Entry(frame_input, font=("times new roman", 15, "bold"),
                              bg='lightgray', show="*")
        self.confirmPassword.place(x=330, y=245, width=270, height=35)

        btn2 = Button(frame_input, text="Register", cursor='hand2', command=self.register,
                      font=('times new roman', 15), bg='white', fg='red', bd=2)
        btn2.place(x=280, y=320)

        btn3 = Button(frame_input, text="Already Registered?Login", command=self.loginform, cursor='hand2',
                      font=('calibri', 10), bg='white', fg='black', bd=0)
        btn3.place(x=260, y=360)

# ---------------------------------------------------------------REGISTRATION FUNCTION -------------------------------
    def register(self):
        if self.fullName.get() == "" or self.staffNo.get() == "" or self.password.get() == "" or \
                self.confirmPassword.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.password.get() != self.confirmPassword.get():
            messagebox.showerror("Error", "password and confirm password should be the same", parent=self.root)

        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="mydb")
                cur = con.cursor()
                cur.execute("select * from myadmin where staffNo=%s", self.staffNo.get())
                row = cur.fetchone()
                if row !=None:
                    messagebox.showerror("Error", "User already exist, "
                                                  "Please try with another staff number", parent=self.root)
                    self.regClear()
                    self.staffNo.focus()
                else:
                    cur.execute("insert into myadmin values(%s,%s,%s,%s)",
                                (self.fullName.get(), self.staffNo.get(),
                                 self.password.get(), self.confirmPassword.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Register successful", parent=self.root)
                    self.regClear()

            except Exception as es:
                messagebox.showerror('Error', f'Error Due to : {str(es)}', parent=self.root)


# --------------------------------------------HOME SCREEN -------------------------------
    def appscreen(self):
        import tkinter.messagebox
        import tempfile
        import os
        #Frame_login = Frame(self.root, bg="white")
        #Frame_login.place(x=0, y=0, height=700, width=1366)

        #self.img = ImageTk.PhotoImage(file="bg.jpg")
        #img = Label(Frame_login, image=self.img).place(x=0, y=0, height=700, width=1366)

        #frame_input3 = Frame(self.root, bg="lightblue")
        #frame_input3.place(x=300, y=50, height=800, width=1050)

        MenuFrame = Frame(self.root, bg="Cadet Blue", bd=5, relief=RIDGE)
        MenuFrame.pack()

        FraTitle = Frame(MenuFrame, bg="yellow", bd=5, relief=RIDGE)
        FraTitle.pack(side=TOP)

        ReceiptCal_F = Frame(MenuFrame, bg="powder Blue", bd=5, relief=RIDGE)
        ReceiptCal_F.pack(side=TOP)

        Buttons_F = Frame(self.root, bg="yellow", bd=3, relief=RIDGE)
        Buttons_F.pack(side=BOTTOM)


# ==============================LABEL, BUTTON ANA TEXT WIDGETS==============================================
        
        lblTitle = Label(FraTitle, width=30, bg="white", fg="black", bd=4,
                         font=('arial', 24, 'bold'), text="ID GENERATOR SYSTEM")
        lblTitle.grid(row=0, column=0)

        txtReceipt = Text(ReceiptCal_F, width=50, height=14, bg="light blue", fg="black", bd=4, font=('arial', 24, 'bold'))
        txtReceipt.grid(row=1, column=0)

# --------------------------------CODE FOR INTERFACE FRONT ID---------------------------------------------

        frame_input1 = Frame(ReceiptCal_F, bg="white")
        frame_input1.place(x=110, y=50, height=450, width=330)

        label1 = Label(frame_input1, text="NATIONAL INSTITUTE OF TRANSPORT", font=('Times new roman', 11, 'bold'),
                       fg="black", bg="white")
        label1.place(x=25, y=10)

        label2 = Label(frame_input1, text="STUDENT IDENTITY CARD", font=('Times new roman', 11, 'bold'),
                       fg="black", bg="white")
        label2.place(x=50, y=30)

# ---------------------------------image entry box--------------------------------------------------------
        self.imag = Entry(frame_input1)
        self.imag.place(x=100, y=100, width=120, height=120)

        label3 = Label(frame_input1, text="PROGRAMME:", font=('Times new roman', 12, 'bold'),
                       fg="black", bg="white")
        label3.place(x=25, y=260)

        self.prog = Entry(frame_input1, font=("times new roman", 15,),
                          bg='white', bd=0)
        self.prog.place(x=145, y=260, width=180, height=25)

        label4 = Label(frame_input1, text="NAME:", font=('Times new roman', 12, 'bold'),
                       fg="black", bg="white")
        label4.place(x=25, y=290)

        self.name = Entry(frame_input1, font=("times new roman", 15,),
                          bg='white', bd=0)
        self.name.place(x=90, y=290, width=195, height=25)

        label5 = Label(frame_input1, text="REG#:", font=('Times new roman', 12, 'bold'),
                       fg="black", bg="white")
        label5.place(x=25, y=320)

        self.reg = Entry(frame_input1, font=("times new roman", 15),
                         bg='white', bd=0)
        self.reg.place(x=90, y=320, width=180, height=25)

        label6 = Label(frame_input1, text="Signature:", font=('Times new roman', 12, 'bold'),
                       fg="black", bg="white")
        label6.place(x=25, y=350)

        self.sign = Entry(frame_input1, font=("times new roman", 15),
                          bg='white', bd=0)
        self.sign.place(x=100, y=350, width=180, height=25)

        label7 = Label(frame_input1, text="EXP.DATE:", font=('Times new roman', 12, 'bold'),
                       fg="black", bg="white")
        label7.place(x=25, y=380)

        self.expD = Entry(frame_input1, font=("times new roman", 15),
                          bg='white', bd=0)
        self.expD.place(x=110, y=380, width=180, height=25)

        # -------------------------------------CODE FOR INTERFACE BACK ID---------------------------------------

        frame_input = Frame(ReceiptCal_F, bg="white")
        frame_input.place(x=500, y=50, height=450, width=335)

        label1 = Label(frame_input, text="National Institute of Transport", font=('Times new roman', 11, 'bold'),
                       fg="black", bg="white")
        label1.place(x=25, y=10)

        label2 = Label(frame_input, text="Official Student Identification", font=('Times new roman', 11, 'bold'),
                       fg="black", bg="white")
        label2.place(x=50, y=30)

        label3 = Label(frame_input, text="1. This is an Institute property and not transferable",
                       font=('Times new roman', 10),
                       fg="black", bg="white")
        label3.place(x=5, y=50)

        label4 = Label(frame_input, text="2. Use of this card is subject to the cardholder agreement.",
                       font=('Times new roman', 10),
                       fg="black", bg="white")
        label4.place(x=5, y=70)
        label5 = Label(frame_input, text="3.For lost or stolen card report to the nearest police station.",
                       font=('Times new roman', 10),
                       fg="black", bg="white")
        label5.place(x=5, y=90)

        label6 = Label(frame_input, text="4. This card must be returned to Dean Office on terminating the course.",
                       font=('Times new roman', 8),
                       fg="black", bg="white")
        label6.place(x=5, y=110)

        label7 = Label(frame_input, text="5.This card must be worn at all official times",
                       font=('Times new roman', 10),
                       fg="black", bg="white")
        label7.place(x=5, y=130)

        label8 = Label(frame_input, text="Contact:", font=('Times new roman', 12, 'bold'),
                        fg="black", bg="white")
        label8.place(x=5, y=170)

        label9 = Label(frame_input, text="Rector",
                       font=('Times new roman', 11),
                       fg="black", bg="white")
        label9.place(x=5, y=190)

        label10 = Label(frame_input, text="P.O. Box 705,Dar es Salaam",
                        font=('Times new roman', 11,),
                        fg="black", bg="white")
        label10.place(x=5, y=210)

        label11 = Label(frame_input, text="Tel:(255)22 2400148",
                        font=('Times new roman', 11),
                        fg="black", bg="white")
        label11.place(x=5, y=230)

        label12 = Label(frame_input, text="Fax:(255)22 2400846",
                        font=('Times new roman', 11),
                        fg="black", bg="white")
        label12.place(x=5, y=250)

        label13 = Label(frame_input, text="E-mail: rector@nit.ac.tz",
                        font=('Times new roman', 11),
                        fg="black", bg="white")
        label13.place(x=5, y=270)

        label14 = Label(frame_input, text="Website: www.nit.ac.tz",
                        font=('Times new roman', 11),
                        fg="black", bg="white")
        label14.place(x=5, y=290);

        self.signRector = Entry(frame_input, font=("times new roman", 15),
                                bg='white', bd=1)
        self.signRector.place(x=5, y=320, width=180, height=25)

        label15 = Label(frame_input, text="Rector Signature",
                        font=('Times new roman', 11, "bold"),
                        fg="black", bg="white")
        label15.place(x=5, y=350)

        # ==============================         functionalities      ==============================================

        # ---------------------------------------------------------------MANUAL PRINT FUNCTION -------------------------------

        def manualPrint():
            if self.reg.get() == "":
                messagebox.showerror("Error", "registration number is required", parent=self.root)

            else:

                con = pymysql.connect(host="localhost", user="root", password="", database="mydb")
                cur = con.cursor()


                cur.execute("select * from registeredstudents where regNo=%s and count=0", self.reg.get())

                rows = cur.fetchmany()
                for row in rows:

                    self.prog.insert(0, row[0])
                    self.name.insert(0, row[1])
                    self.sign.insert(0, row[3])
                    self.imag.insert(0, row[5])
                    self.regNo.focus()

                #txtReceipt = tempfile.mkdtemp(".txt")
                #open(txtReceipt, "w")
                file_path = "txtReceipt.text"
                os.startfile(file_path, "print")

                con.close()

        self.frontIdClear()


        # ---------------------------------------------------------------AUTO PRINT FUNCTION -------------------------------

        def autoPrint():
            con = pymysql.connect(host="localhost", user="root", password="", database="mydb")
            cur = con.cursor()
            cur.execute("select * from registeredstudents where count=0")
            rows = cur.fetchmany()
            for row in rows:
                self.prog.insert(0, row[0])
                self.name.insert(0, row[1])
                self.reg.insert(0, row[2])
                self.sign.insert(0, row[3])
                self.imag.insert(0, row[5])

            con.close()
            # self.frontIdClear()ed

        def iExit():
            import tkinter.messagebox
            iExit = tkinter.messagebox.askyesno("Quit System", "Do you want to quit")
            if iExit > 0:
                root.destroy()
                return


        btn1 = Button(Buttons_F, font=('arial', 16, 'bold'), width=19, text="manualPrint", command= manualPrint)
        btn1.grid(row=1, column=0)

        btn2 = Button(Buttons_F, font=('arial', 16, 'bold'), width=19, text="autoPrint", command=autoPrint)
        btn2.grid(row=1, column=1)

        btn3 = Button(Buttons_F, font=('arial', 16, 'bold'), width=19, text="Exit", command=iExit)
        btn3.grid(row=1, column=2)





#--------------------------creating the clear function------------------------------------------------------


    def regClear(self):
        self.fullName.delete(0, END)
        self.staffNo.delete(0, END)
        self.password.delete(0, END)
        self.confirmPassword.delete(0, END)

    def loginClear(self):
        self.staffNo.delete(0, END)
        self.password.delete(0, END)

    def frontIdClear(self):
        self.imag.delete(0, END)
        self.prog.delete(0, END)
        self.name.delete(0, END)
        self.reg.delete(0, END)
        self.sign.delete(0, END)
        self.expD.delete(0, END)




root=Tk()
ob = Login(root)
root.mainloop()
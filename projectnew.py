from tkinter import *
import sqlite3
import tkinter.messagebox

conn=sqlite3.connect('Data.db')
c=conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS user12(username TEXT  , password TEXT )")
c.execute("SELECT * FROM user12")
conn.commit()
conn.close()
class main:

    def __init__(self,master):
        self.master=master
        self.username=StringVar()
        self.password=StringVar()
        self.n_username=StringVar()
        self.n_password=StringVar()
    def gui(self):
        top=tkinter.Tk()
        top.minsize(height=250,width=400)
        res=0
        tfprs=" "
        def and1(a,b):
            global res
            res=int(a & b)
        def or1(a,b):
            global res
            res=int(a | b)
        def  not1(a):
            global res
            res=int(not a)
        def xor1(a,b):
            global res
            res=int((a and not b) or (not a and b))
        def result(event=None):
            global res,E3
            text=StringVar()
            E3=tkinter.Entry(top,bg="powder blue",width=25,textvariable=text,bd=5)
            E3.place(x=100,y=200)
            text.set(str(res))
        def exit1(top):
            top.destroy()
        def exit2(top1):
            top1.destroy()
        def selected():
            global tfprs
            t=var.get()
            if t==1:
                      tfprs="AND"
            elif t==2:
                      tfprs="OR"
            elif t==3:
                      tfprs="NOT"
            else :
                      tfprs="XOR"
        def explanation(a,b):
            global tfprs,res
            binary1=StringVar()
            binary2=StringVar()
            top1=tkinter.Toplevel(top)
            value1=IntVar()
            l1=tkinter.Label(top1,text="Number 1").grid(row=0,column=0)
            e1=tkinter.Entry(top1,bg="powder blue",textvariable=value1,bd=5)
            value1.set(a)
            e1.grid(row=0,column=1)
            e3=tkinter.Entry(top1,bg="powder blue",textvariable=binary1,bd=5)
            l3=tkinter.Label(top1,text="Binary Number 1").grid(row=0,column=2)
            binary1.set(format(a,'b'))
            e3.grid(row=0,column=3)
            value2=IntVar()
            l2=tkinter.Label(top1,text="Number 2").grid(row=1,column=0)
            e2=tkinter.Entry(top1,bg="powder blue",textvariable=value2,bd=5)
            value2.set(b)
            e2.grid(row=1,column=1)
            l4=tkinter.Label(top1,text="Binary Number 2").grid(row=1,column=2)
            e4=tkinter.Entry(top1,textvariable=binary2,bg="powder blue",bd=5)
            binary2.set(format(b,'b'))
            e4.grid(row=1,column=3)
            l5=tkinter.Label(top1,text="Operation ").grid(row=2,column=2)
            operator=StringVar()
            e5=tkinter.Entry(top1,textvariable=operator,bg="powder blue",bd=5)
            operator.set(tfprs)
            e5.grid(row=2,column=3)
            dres=IntVar()
            l6=tkinter.Label(top1,text="Decimal Result").grid(row=3,column=1)
            e6=tkinter.Entry(top1,textvariable=dres,bg="powder blue",bd=5)
            dres.set(res)
            e6.grid(row=3,column=2)
            b1=tkinter.Button(top1,bd=5,text="Exit",bg="brown",fg="white",command=lambda top1=top1:exit2(top1)).grid(row=4,column=0)
            top.mainloop()
        def dotwo(a,b):
            selected()
            explanation(a,b)
        n1="Welcome : "+ self.username.get()
        num1=IntVar()
        tkinter.Label(top,text=n1,font=("bold",20),bg="light grey",padx=120).grid(row=0,column=0)
        L1=tkinter.Label(top,text="Number 1")
        L1.place(x=10,y=39)
        E1=tkinter.Entry(top,textvariable=num1,bg="powder blue",bd=5)
        num1.set("")
        E1.place(x=70,y=38)
        num2=IntVar()
        L2=tkinter.Label(top,text="Number 2")
        L2.place(x=230,y=39)
        E2=tkinter.Entry(top,textvariable=num2,bg="powder blue",bd=5)
        num2.set("")
        E2.place(x=290,y=38)
        var=IntVar()
        R1=tkinter.Radiobutton(top,text="AND",variable=var,value=1,command=lambda: and1(int(E1.get()),int(E2.get())))
        R1.place(x=50,y=80)
        R2=tkinter.Radiobutton(top,text="OR",variable=var,value=2,command=lambda: or1(int(E1.get()),int(E2.get())))
        R2.place(x=150,y=80)
        R3=tkinter.Radiobutton(top,text="NOT",variable=var,value=3,command=lambda: not1(int(E1.get())))
        R3.place(x=50,y=120)
        R4=tkinter.Radiobutton(top,text="XOR",variable=var,value=4,command=lambda: xor1(int(E1.get()),int(E2.get())))
        R4.place(x=150,y=120)
        label=tkinter.Label(top)
        label.grid()
        B1=tkinter.Button(top,text="Result is:",bg="brown",fg="white",command=result,bd=5)
        B1.place(x=40,y=150)

        B2=tkinter.Button(top,text="Explanation",bg="brown",fg="white",command=lambda: dotwo(int(E1.get()),int(E2.get())),bd=5)
        B2.place(x=150,y=150)
        B3=tkinter.Button(top,bd=5,text="Exit",bg="brown",width=5,fg="white",command=lambda top=top:exit1(top))
        B3.place(x=280,y=150)
        L3=tkinter.Label(top,text="Result :")
        L3.place(x=40,y=200)
        E3=tkinter.Entry(top,bg="powder blue",width=25,bd=5)
        E3.place(x=100,y=200)
        top.mainloop()
        

    

    def login(self):
        conn=sqlite3.connect('Data.db')
        c=conn.cursor()
        find_user=("SELECT * FROM user12  WHERE username=? AND password=?")
        c.execute(find_user,[(self.username.get()),(self.password.get())])
        results=c.fetchall()
        if results :
            self.master.destroy()
            self.gui()
        else:
            tkinter.messagebox.showwarning("Oops !! ","Username not matched !")
        conn.commit()
        conn.close()
    def new_user(self):
        conn=sqlite3.connect('Data.db')
        c=conn.cursor()
        find_user=("SELECT * FROM user12 WHERE username=? AND password=?")
        c.execute(find_user,[(self.username.get()),(self.password.get())])
        if c.fetchall():
            tkinter.messagebox.showwarning("Oops !!","Username taken !!")
        else:
            tkinter.messagebox.showinfo("Success !!","Account created ")
            self.log()
        insert="INSERT INTO user12(username,password)VALUES(?,?)"
        c.execute(insert,[(self.n_username.get()),(self.n_password.get())])
        conn.commit()
    def log(self):
        self.username.set(" ")
        self.password.set(" ")
        self.crf.pack_forget()
        self.head["text"]="  LOGIN   "
        self.logf.pack()
    def cr(self):
        self.n_username.set(" ")
        self.n_password.set(" ")
        self.head["text"]="Create Account "
        self.new()
        self.logf.pack_forget()
        self.crf.pack()
    def widget(self):
        self.head=tkinter.Label(self.master,text="   LOGIN     ",bg="light grey",font=("bold",25),pady=4,padx=120)
        self.head.pack()
        
        self.logf=tkinter.Frame(self.master,padx=10,pady=20)
        tkinter.Label(self.logf,text=" Username : ",font=("freesansbold",15),padx=5,pady=0).grid()
        tkinter.Entry(self.logf,textvariable=self.username,bd=5,bg="powder blue",font=("Calibri",15,"bold")).grid(row=0,column=1)
        tkinter.Label(self.logf,text=" Password : ",font=("freesansbold",15),padx=5,pady=10).grid(row=1,column=0)
        self.password.set("")
        tkinter.Entry(self.logf,textvariable=self.password,bd=5,bg="powder blue",font=("Calibri",15,"bold"),show="*").grid(row=1,column=1)
        tkinter.Button(self.logf,text="Login",bg="brown",fg="white",bd=5,font=("monaco",15,"bold"),padx=0,pady=0,command=self.login).grid(row=3)
        tkinter.Button(self.logf,text="Make new account",bg="brown",fg="white",bd=5,font=("monaco",15,"bold"),padx=5,pady=0,command=self.cr).grid(row=3,column=1)
        self.logf.pack()
    def new(self):
        self.crf=tkinter.Frame(self.master,padx=20,pady=30)
        tkinter.Label(self.crf,text=" Username : ",font=("freesansbold",15),padx=5,pady=0).grid(row=0,column=0)
        tkinter.Entry(self.crf,textvariable=self.n_username,bd=5,bg="powder blue",font=("Calibri",15,"bold")).grid(row=0,column=1)
        tkinter.Label(self.crf,text=" Password : ",font=("freesansbold",15),padx=5,pady=10).grid(row=1,column=0)
        self.n_password.set("")
        tkinter.Entry(self.crf,textvariable=self.n_password,bd=5,bg="powder blue",font=("Calibri",15,"bold"), show="*").grid(row=1,column=1)
        tkinter.Button(self.crf,text="Go to Login",bg="brown",fg="white",bd=5,font=("monaco",15,"bold"),padx=0,pady=0,command=self.log).grid(row=3,column=0)
        tkinter.Button(self.crf,text="Create Account",bg="brown",fg="white",bd=5,font=("monaco",15,"bold"),padx=5,pady=0,command=self.new_user).place(x=180,y=83)
        self.crf.pack()
        
        

root=tkinter.Tk()
root.title("Boolean Calculator")
ob=main(root)
ob.widget()
root.maxsize(height=250,width=420)
root.mainloop()

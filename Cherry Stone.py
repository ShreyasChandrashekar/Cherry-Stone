from tkinter import *
from tkinter import ttk
from tkinter.font import Font
import os

import mysql.connector

mydb = mysql.connector.connect(
       host="localhost",
       user="root",
       passwd="1234",
       database="project4"
       )

mycursor = mydb.cursor()

CUSTID=0
CUSTNAME=''
ADDRESS=''
PHONE=''
Total=0
addrow=2
global pay
DATE=''
AMOUNT1=''

def customer_details():

    global custid
    global custname
    global address
    global phone
    
    global customer_entry
    global customer_name_entry
    global customer_address_entry
    global customer_phone_entry
    
    custid=StringVar()
    custname=StringVar()
    address=StringVar()
    phone=StringVar()
    
    global screen6
    screen6 = Toplevel(root)
    screen6.title("Customer Details")
    screen6.configure(background="mediumorchid1")
    screen6.geometry('600x600')
    
    Label(screen6,text = "Customer-ID",bg='mediumorchid1').pack(padx=10,pady=20)
    customer_entry=Entry(screen6, textvariable = custid)
    customer_entry.pack(padx=10,pady=10)

    Label(screen6,text = "Customer-Name",bg='mediumorchid1').pack(padx=10,pady=20)
    customer_name_entry=Entry(screen6, textvariable = custname)
    customer_name_entry.pack(padx=10,pady=10)

    Label(screen6,text = "Customer-ADDRESS",bg='mediumorchid1').pack(padx=10,pady=20)
    customer_address_entry=Entry(screen6, textvariable = address)
    customer_address_entry.pack(padx=10,pady=10)

    Label(screen6,text = "Customer-Phone_no.",bg='mediumorchid1').pack(padx=10,pady=20)
    customer_phone_entry=Entry(screen6, textvariable = phone)
    customer_phone_entry.pack(padx=10,pady=10)

    Button(screen6,text="OK",width=20,height=2,bg="violetred3",command=customer_enter).pack(padx = 10,pady = 20)
    
    Button(screen6,text="NEXT",width=20,height=2,bg="violetred3",command=product).pack(padx = 10,pady = 20)
   

def customer_enter():

    print("Entered Function....")
    global CUSTID
    CUSTID=custid.get()
    CUSTNAME=custname.get()
    ADDRESS=address.get()
    PHONE=phone.get()

    sql="INSERT INTO customer(CustID,CustName,ADDRESS,PhoneNo)VALUES(%s,%s,%s,%s)"
    val=(CUSTID,CUSTNAME,ADDRESS,PHONE)
    mycursor.execute(sql,val)
    mydb.commit()

    print(CUSTID)
    print(CUSTNAME)
    print(ADDRESS)
    print(PHONE)

    customer_entry.delete(0,END)
    customer_name_entry.delete(0,END)
    customer_address_entry.delete(0,END)
    customer_phone_entry.delete(0,END)


    

def product():
    
    global screen7
    global quantityEntry
    screen7 = Toplevel(root)
    screen7.title("Product Selection")
    screen7.configure(background="mediumorchid1")
    screen7.geometry('900x600')

    titleLabel =Label(screen7,text="Cherry Stone",font="Arial 30",fg="green")
    titleLabel.grid(row=0,column=1,columnspan=3,pady=(10,0))

    logoutBtn = Button(screen7, text = "Logout",width=15, height=2)
    logoutBtn.grid(row=1, column=5,pady=(10,0))

    itemLabel = Label(screen7, text="Select Item")
    itemLabel.grid(row=2,column=0,padx=(5,0),pady=(10,0))

    items = ['Maggie-10','Hide n Seek-20' , 'Frooti-10' , 'Coca Cola-45', 'Diary Milk-10','StrawberryIC-50','Cupcake-15','Eggs-5','Bread-20']
    itemDropDown=ttk.Combobox(screen7,values=items)
    itemDropDown.grid(row=2,column=1,padx=(10,0),pady=(5,0))
    print(itemDropDown.get())

    quantityLabel = Label(screen7,text="Quantity")
    quantityLabel.grid(row=2,column=2,padx=(5,0),pady=(10,0))
    quantityEntry = Entry(screen7,font='Arial')
    quantityEntry.grid(row=2,column=3,padx=(5,0),pady=(10,0))
    
    addNewItem = Button(screen7,text="Add Item",width=15,height=2,command=lambda:additem(itemDropDown,quantityEntry))
    addNewItem.grid(row=1,column=0,padx=(10,0),pady=(10,0))

    buttonBill = Button(screen7,text="Payment",width=15,command=payment)
    buttonBill.grid(row=2,column=5,padx=(5,0),pady=(10,0))

    ButtonDone = Button(screen7,text='Done',width=15,command=lambda:Total1())
    ButtonDone.grid(row=3,column=5,padx=(5,0),pady=(10,0))

def Total1():

    print('Working')

    global Total
    xd=Total
    totalLabel = Label(screen7,text='Total :-')
    totalLabel.grid(row=5,column=5,padx=(5,0),pady=(10,0))

    totalLabel = Label(screen7,text=(xd,'RS'))
    totalLabel.grid(row=5,column=6,padx=(5,0),pady=(10,0))

    


def payment():

    global screen8
    screen8 = Toplevel(root)
    screen8.title("Payment")
    screen8.configure(background="mediumorchid1")
    screen8.geometry("600x600")
    
    global payDropDown
    global payDescLabel
    global payDateLabel
    global payDateEntry
    global payAmountEntry
    
    global pay
    global date_get
    global amount_get
    
    date_get=StringVar()
    amount_get=StringVar()
    
    print('Enter Screen 8')
    
    pay = ['Debit','Credit','Cash']
    payDescLabel = Label(screen8,text='Mode Of Payment')
    payDescLabel.grid(row=1,column=1,padx=(10,0),pady=(5,0))
    
    payDropDown=ttk.Combobox(screen8,values=pay)
    payDropDown.grid(row=2,column=1,padx=(10,0),pady=(5,0))
    
    print(payDropDown.get())

    payDateLabel = Label(screen8,text='Payment Date')
    payDateLabel.grid(row=3,column=2,padx=(10,0),pady=(5,0))

    payDateEntry = Entry(screen8,font='Arial',textvariable=date_get)
    payDateEntry.grid(row=4,column=2,padx=(10,0),pady=(5,0))

    payAmountLabel = Label(screen8,text='Amount',)
    payAmountLabel.grid(row=5,column=3,padx=(10,0),pady=(5,0))

    payAmountEntry = Entry(screen8,font='Arial',textvariable=amount_get)
    payAmountEntry.grid(row=6,column=3,padx=(10,0),pady=(5,0))

    OKButton = Button(screen8,text="OK",width=15,command=lambda:SQLPayment(date_get,amount_get,payDropDown.get()))
    OKButton.grid(row=7,column=2,padx=(5,0),pady=(10,0))

    GeneratebuttonBill = Button(screen8,text="Genrate bill",width=15,command=FinalBill)
    GeneratebuttonBill.grid(row=8,column=2,padx=(5,0),pady=(10,0))

    

def SQLPayment(date_get,amount_get,paytype):
    
    global DATE
    global AMOUNT1

    DATE=date_get.get()
    AMOUNT1=amount_get.get()

    payDateEntry.delete(0,END)
    payAmountEntry.delete(0,END)
    
    sql="INSERT INTO payment(PayDesc,PayDate,Amount)VALUES(%s,%s,%s)"
    val=(paytype,DATE,AMOUNT1)
    mycursor.execute(sql,val)
    mydb.commit()

def FinalBill():

    global screen9
    screen9 = Toplevel(root)
    screen9.title("Thank You")
    screen9.configure(background="mediumorchid1")
    screen9.geometry("600x600")

    print('Working.....')

    CGSTLabel = Label(screen9,text='THANK YOU ')
    CGSTLabel.grid(row=1,column=1,padx=(10,0),pady=(5,0))

    #SGSTLabel = Label(screen9,text='SGST :- ')
    #SGSTLabel.grid(row=2,column=1,padx=(10,0),pady=(5,0))

    #FinalBillLabel = Label(screen9,text='Grand Total :- ')
    #FinalBillLabel.grid(row=3,column=1,padx=(10,0),pady=(5,0))
        

    
def additem(items,quantity):
    global Total
    global screen7
    global addrow
    global CUSTID
    addrow+=1
    print('id',CUSTID)
    print(items)
    if items.get()== 'Maggie-10':
        quantityLabel = Label(screen7,text=("Maggie   -   " ))
        quantityLabel.grid(row=addrow,column=0)
        priceLabel = Label(screen7,text=(10*int(quantity.get()),"RS"))
        priceLabel.grid(row=addrow,column=1)
        
        sql="INSERT INTO product(PName,Price,ExpDate,CID)VALUES(%s,%s,%s,%s)"
        val=(items.get(),10*int(quantity.get()),'2019-07-10',CUSTID)
        mycursor.execute(sql,val)
        mydb.commit()
        Total=Total+10*int(quantity.get())
        
    elif items.get()== 'Hide n Seek-20':
        quantityLabel = Label(screen7,text=("Hide n Seek   -   "))
        quantityLabel.grid(row=addrow,column=0)
        priceLabel = Label(screen7,text=(20*int(quantity.get()),"RS"))
        priceLabel.grid(row=addrow,column=1)

        sql="INSERT INTO product(PName,Price,ExpDate,CID)VALUES(%s,%s,%s,%s)"
        val=(items.get(),20*int(quantity.get()),'2019-12-10',CUSTID)
        mycursor.execute(sql,val)
        mydb.commit()
        Total=Total + 20*int(quantity.get())
        
    elif items.get()== 'Coca Cola-45':
        quantityLabel = Label(screen7,text=("Coca Cola   -   "))
        quantityLabel.grid(row=addrow,column=0)
        priceLabel = Label(screen7,text=(45*quantity.get(),"RS"))
        priceLabel.grid(row=addrow,column=1)

        sql="INSERT INTO product(PName,Price,ExpDate,CID)VALUES(%s,%s,%s,%s)"
        val=(items.get(),45*int(quantity.get()),'2019-09-10',CUSTID)
        mycursor.execute(sql,val)
        mydb.commit()
        Total=Total+45*int(quantity.get())
        
    elif items.get()== 'Frooti-10':
        quantityLabel = Label(screen7,text=("Frooti   -   "))
        quantityLabel.grid(row=addrow,column=0)
        priceLabel = Label(screen7,text=(10*int(quantity.get()),"RS"))
        priceLabel.grid(row=addrow,column=1)

        sql="INSERT INTO product(PName,Price,ExpDate,CID)VALUES(%s,%s,%s,%s)"
        val=(items.get(),10*int(quantity.get()),'2019-10-10',CUSTID)
        mycursor.execute(sql,val)
        mydb.commit()
        Total=Total+10*int(quantity.get())

    elif items.get()== 'Diary Milk-10':
        quantityLabel = Label(screen7,text=("Diary Milk   -   "))
        quantityLabel.grid(row=addrow,column=0)
        priceLabel = Label(screen7,text=(10*int(quantity.get()),"RS"))
        priceLabel.grid(row=addrow,column=1)

        sql="INSERT INTO product(PName,Price,ExpDate,CID)VALUES(%s,%s,%s,%s)"
        val=(items.get(),10*int(quantity.get()),'2018-10-10',CUSTID)
        mycursor.execute(sql,val)
        mydb.commit()
        Total=Total+10*int(quantity.get())

    elif items.get()== 'StrawberryIC-50':
        quantityLabel = Label(screen7,text=("StrawberryIC   -   "))
        quantityLabel.grid(row=addrow,column=0)
        priceLabel = Label(screen7,text=(50*int(quantity.get()),"RS"))
        priceLabel.grid(row=addrow,column=1)

        sql="INSERT INTO product(PName,Price,ExpDate,CID)VALUES(%s,%s,%s,%s)"
        val=(items.get(),50*int(quantity.get()),'2018-11-10',CUSTID)
        mycursor.execute(sql,val)
        mydb.commit()
        Total=Total+50*int(quantity.get())

    elif items.get()== 'Cupcake-15':
        quantityLabel = Label(screen7,text=("Cupcake   -   "))
        quantityLabel.grid(row=addrow,column=0)
        priceLabel = Label(screen7,text=(15*int(quantity.get()),"RS"))
        priceLabel.grid(row=addrow,column=1)

        sql="INSERT INTO product(PName,Price,ExpDate,CID)VALUES(%s,%s,%s,%s)"
        val=(items.get(),15*int(quantity.get()),'2018-11-10',CUSTID)
        mycursor.execute(sql,val)
        mydb.commit()
        Total=Total+15*int(quantity.get())

    elif items.get()== 'Eggs-5':
        quantityLabel = Label(screen7,text=("Eggs   -   "))
        quantityLabel.grid(row=addrow,column=0)
        priceLabel = Label(screen7,text=(5*int(quantity.get()),"RS"))
        priceLabel.grid(row=addrow,column=1)

        sql="INSERT INTO product(PName,Price,ExpDate,CID)VALUES(%s,%s,%s,%s)"
        val=(items.get(),5*int(quantity.get()),'2019-03-10',CUSTID)
        mycursor.execute(sql,val)
        mydb.commit()
        Total=Total+5*int(quantity.get())

    elif items.get()== 'Bread-20':
        quantityLabel = Label(screen7,text=("Bread   -   "))
        quantityLabel.grid(row=addrow,column=0)
        priceLabel = Label(screen7,text=(20*int(quantity.get()),"RS"))
        priceLabel.grid(row=addrow,column=1)

        sql="INSERT INTO product(PName,Price,ExpDate,CID)VALUES(%s,%s,%s,%s)"
        val=(items.get(),20*int(quantity.get()),'2018-04-10',CUSTID)
        mycursor.execute(sql,val)
        mydb.commit()
        Total=Total+20*int(quantity.get())
        
    


        
    
def delete3():
  screen4.destroy()
 
def delete4():
  screen5.destroy()
    

def login_sucess():
    
    global screen3
    screen3 = Toplevel(root)
    screen3.title("Sucess")
    screen3.configure(background="mediumorchid1")
    screen3.geometry("600x600")
    f1 = Font(family="Calibri",size=18,weight="bold",underline=0)
    Label(screen3,text = "Login Sucess",bg="mediumorchid1",fg="green",font=f1).pack(padx=10,pady=10)
    Button(screen3,text = "OK",width=20,height=2,bg="violetred3",command=customer_details).pack(padx=10,pady=10)
    

def password_not_recognised():
    
    global screen4
    screen4 = Toplevel(root)
    screen4.title("Success")
    screen4.configure(background="mediumorchid1")
    screen4.geometry("600x600")
    Label(screen4, text = "Invalid Password",bg="mediumorchid1").pack(padx=15,pady=20)
    Button(screen4, text = "OK",width=20,height=2,bg="violetred3", command =delete3).pack(padx=15,pady=20)

def user_not_found():
    
    global screen5
    screen5 = Toplevel(root)
    screen5.title("Success")
    screen5.configure(background="mediumorchid1")
    screen5.geometry("600x600")
    Label(screen5, text = "User Not Found",bg="mediumorchid1").pack(padx=15,pady=20)
    Button(screen5, text = "OK",width=20,height=2,bg="violetred3",command =delete4).pack(padx=15,pady=20)
    

def register_user():
    
    username_info=username.get()
    password_info=password.get()

    file=open(username_info,"w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0,END)
    password_entry.delete(0,END)
    
    f1 = Font(family="Calibri",size=11,weight="bold",underline=0)
    Label(screen1,text = "Registration Sucess",fg="green",bg="mediumorchid1",font=f1).pack()

def login_verify():
    
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0,END)
    password_entry1.delete(0,END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1,"r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
        else:
            password_not_recognised()
    else:
        user_not_found()

    
    
def register():

    global screen1    
    screen1 = Toplevel(root)
    screen1.title("Register")
    screen1.configure(background="mediumorchid1")
    screen1.geometry('600x600')
    
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    
    f1 = Font(family="Times New Roman",size=20,weight="bold",underline=0)
    Label(screen1,text= " Enter Your Details Below ",bg="violetred3",width="600",height="2",font=f1).pack()
   
    
    Label(screen1,text= " Username * ",bg="violetred3").place(x = 15,y = 70)
    username_entry=Entry(screen1,textvariable = username)
    username_entry.place(x = 15,y = 100)
    
    
    Label(screen1,text= " Password * ",bg="violetred3").place(x = 15,y = 140)
    password_entry=Entry(screen1,textvariable = password)
    password_entry.place(x = 15,y = 170)
 
    
    Button(screen1,text="Register",width=20,height=2,bg="grey",command=register_user).place(x = 15,y = 220)
        
        
def login():
    
      global screen2
      screen2 = Toplevel(root)
      screen2.title("Login")
      screen2.geometry("600x600")
      screen2.configure(background="mediumorchid1")
      f2 = Font(family="Times New Roman",size=20,weight="bold",underline=0)
      Label(screen2,bg="violetred3",width="600",height="2",text="Enter Your Details Below to Log-in",font=f2).pack()
      Label(screen2,text = "",bg="mediumorchid1").pack()
      Label(screen2,text= "",bg="mediumorchid1").pack()
      Label(screen2,text= "",bg="mediumorchid1").pack()
     
      global username_verify
      global password_verify
       
      username_verify = StringVar()
      password_verify = StringVar()
     
      global username_entry1
      global password_entry1
       
      Label(screen2, text = "Username * ",bg="mediumorchid1").pack()
      username_entry1 = Entry(screen2, textvariable = username_verify)
      username_entry1.pack()
      Label(screen2, text = "",bg="mediumorchid1").pack()
      
      Label(screen2, text = "Password * ",bg="mediumorchid1").pack()
      password_entry1 = Entry(screen2, textvariable = password_verify)
      password_entry1.pack()
      Label(screen2, text = "",bg="mediumorchid1").pack()
      
      Button(screen2, text = "Login", width = 10, height = 1, command = login_verify).pack()
    

    
def main_screen():

        global root
        root=Tk()
        root.geometry('600x600')
        root.configure(background="mediumorchid1");
        root.title("Cherry Stone Supermarket")
        
        f = Font(family="Times New Roman",size=20,weight="bold",underline=0)
        Label(root,bg="violetred3",width="600",height="2",text="Welcome To Cherry Stone Super Market",font=f).pack()
        Label(text="",bg="mediumorchid1").pack()
        Label(text="",bg="mediumorchid1").pack()
        Label(text="",bg="mediumorchid1").pack()
        Button(text="Login",height="2",width="30", command = login).pack()
        Label(text="",bg="mediumorchid1").pack()
        Button(text="Register",height="2",width="30", command = register).pack()
        root.mainloop()
        
main_screen()



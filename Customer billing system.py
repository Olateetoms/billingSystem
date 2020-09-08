from tkinter import*
from tkinter import ttk
import random
import tkinter.messagebox
from datetime import datetime
import time;

class customer:
    
    def __init__(self, roo):
        self.root = root
        self.root.title("Customer Billing System")
        self.root.geometry("1350x750+0+0")
        self.root.config(background="powder blue")

        ABC = Frame(self.root, bg="powder blue", bd=20, relief=RIDGE)
        ABC.grid()
        ABC1 = Frame(ABC, bd=14, width=1350, height=100, padx=8, relief=RIDGE, bg="powder blue")
        ABC1.grid(row=0, column=0, columnspan=3, sticky=W)
        ABC2 = Frame(ABC, bd=14, width=450, height=488, padx=10, relief=RIDGE, bg="cadet blue")
        ABC2.grid(row=1, column=0, columnspan=4, sticky=W)
        ABC3 = Frame(ABC, bd=14, width=450, height=488, padx=10, relief=RIDGE, bg="powder blue")
        ABC3.grid(row=1, column=1, columnspan=4, sticky=W)
        ABC4 = Frame(ABC, bd=14, width=460, height=488, padx=10, relief=RIDGE, bg="cadet blue")
        ABC4.grid(row=1, column=2, columnspan=4, sticky=W)
        ABC5 = Frame(ABC4, bd=14, width=370, height=340, padx=10, relief=RIDGE, bg="cadet blue")
        ABC5.grid(row=0, column=0, columnspan=4, sticky=W)
        ABC6 = Frame(ABC4, bd=14, width=370, height=120, padx=10, relief=RIDGE, bg="cadet blue")
        ABC6.grid(row=1, column=0, columnspan=4, sticky=W)

        Date1 = StringVar()
        Time1 = StringVar()
        Date1.set(time.strftime("%d/%m/%Y"))
        Time1.set(time.strftime("%H:%M:%S"))

        Customer_Ref = StringVar()
        First_Name = StringVar()
        Surname = StringVar()
        Address = StringVar()
        PostCode = StringVar()
        Mobile = StringVar()
        Email = StringVar()
        Nationality = StringVar()
        DOB = StringVar()
        IDType = StringVar()
        Gender = StringVar()
        CheckInDate = StringVar()
        CheckOutDate = StringVar()
        Meal = StringVar()
        RoomType = StringVar()
        RoomNo = StringVar()
        RoomExtNo = StringVar()
        TotalCost = StringVar()
        SubTotal = StringVar()
        PaidTax = StringVar()
        TotalDays = StringVar()


        var1 =  IntVar()
        var2 =  IntVar()
        var3 =  IntVar()
        var4 =  IntVar()
        var5 =  IntVar()
        var6 =  IntVar()
        var7 =  IntVar()
        var8 =  IntVar()

        E_Espresso=StringVar()
        E_Milk_Shake=StringVar()
        E_Vanilla_Ice=StringVar()
        E_Iced_Tea=StringVar()
        E_American_Coffee=StringVar()
        E_Cappuccino=StringVar()
        E_Green_Tea=StringVar()
        E_African_Coffee=StringVar()

        E_Espresso.set("0")
        E_Milk_Shake.set("0")
        E_Vanilla_Ice.set("0")
        E_Iced_Tea.set("0")
        E_American_Coffee.set("0")
        E_Cappuccino.set("0")
        E_Green_Tea.set("0")
        E_African_Coffee.set("0")

        self.lblTitle = Label(ABC1, textvariable=Date1,font=('arial',30,'bold'),pady=9,bd=5,bg="Cadet Blue",fg="Cornsilk").grid(row=0, column=0)
                  
        self.lblTitle = Label(ABC1, text="Customer Billing System\t\t\t",font=('arial',30,'bold'),pady=12,bd=5,bg="Cadet Blue",justify=CENTRE,
                              fg="Cornsilk").grid(row=0, column=1)
                  
        self.lblTitle = Label(ABC1, textvariable=Time1,font=('arial',30,'bold'),pady=9,bd=5,bg="Cadet Blue",fg="Cornsilk").grid(row=0, column=2)

        def Exit():
            Exit = tkinter.messagebox.askyesno("Customer Billing System", "Confirm if you want to exit")
            if Exit > 0:
                root.destroy()
                return
        def Reset():
            self.txtReceipt.delete("1.0", END)
            E_Espresso.set("0")
            E_Milk_Shake.set("0")
            E_Vanilla_Ice.set("0")
            E_Iced_Tea.set("0")
            E_American_Coffee.set("0")
            E_Cappuccino.set("0")
            E_Green_Tea.set("0")
            E_African_Coffee.set("0")

            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            var5.set(0)
            var6.set(0)
            var7.set(0)
            var8.set(0)

            Customer_Ref.set("")
            First_Name.set("")
            Surname.set("")
            Address.set("")
            PostCode.set("")
            Mobile.set("")
            Email.set("")
            Nationality.set("")
            DOB.set("")
            IDType.set("")
            Gender.set("")
            CheckInDate.set("")
            CheckOutDate.set("")
            Meal.set("")
            RoomType.set("")
            RoomNo.set("")
            RoomExtNo.set("")
            TotalCost.set("")
            SubTotal.set("")
            PaidTax.set("")
            TotalDays.set("")


        self.txtReceipt = Text(ABC2, height=19, width=43, bd=10, font=('arial', 9, 'bold'))
        self.txtReceipt.grid(row=0, column=0)
            
        self.lblCus_Ref = Label(ABC2, font=('arial',12,'bold'), text="Customer Ref:", padx=2,pady=2,fg="Cornsilk", bg="Cadet Blue")
        self.lblCus_Ref.grid(row=0, column=0, sticky=W)
        self.txtCus_Ref = Entry(ABC2, font=('arial',12,'bold'), textvariable=Customer_Ref, width=20)
        self.txtCus_Ref.grid(row=0, column=1, pady=3, padx=20)

        self.lblFirst_Name = Label(ABC2, font=('arial',12,'bold'), text="FirstName:", padx=2,pady=2,fg="Cornsilk", bg="Cadet Blue")
        self.lblFirst_Name.grid(row=1, column=0, sticky=W)
        self.txtFirst_Name = Entry(ABC2, font=('arial',12,'bold'), textvariable=First_Name, width=20)
        self.txtFirst_Name.grid(row=1, column=1, pady=3, padx=20)

        self.lblSurname = Label(ABC2, font=('arial',12,'bold'), text="Surname:", padx=2,pady=2, fg="Cornsilk", bg="Cadet Blue")
        self.lblSurname.grid(row=2, column=0, sticky=W)
        self.txtSurname = Entry(ABC2, font=('arial',12,'bold'), textvariable=Surname, width=20)
        self.txtSurname.grid(row=2, column=1, pady=3, padx=20)

        self.lblAddress = Label(ABC2, font=('arial',12,'bold'), text="Address:", padx=2,pady=2, fg="Cornsilk", bg="Cadet Blue")
        self.lblAddress.grid(row=3, column=0, sticky=W)
        self.txtAddress = Entry(ABC2, font=('arial',12,'bold'), textvariable=Address, width=20)
        self.txtAddress.grid(row=3, column=1, pady=3, padx=20)

        self.lblPostCode = Label(ABC2, font=('arial',12,'bold'), text="PostCode:", padx=2,pady=2, fg="Cornsilk", bg="Cadet Blue")
        self.lblPostCode.grid(row=4, column=0, sticky=W)
        self.txtPostCode = Entry(ABC2, font=('arial',12,'bold'), textvariable=Address, width=20)
        self.txtPostCode.grid(row=4, column=1, pady=3, padx=20)

        self.lblMobile = Label(ABC2, font=('arial',12,'bold'), text="Mobile:", padx=2,pady=2, fg="Cornsilk", bg="Cadet Blue")
        self.lblMobile.grid(row=5, column=0, sticky=W)
        self.txtMobile = Entry(ABC2, font=('arial',12,'bold'), textvariable=Mobile, width=20)
        self.txtMobile.grid(row=5, column=1, pady=3, padx=20)

        self.lblEmail = Label(ABC2, font=('arial',12,'bold'), text="Email:", padx=2,pady=2, fg="Cornsilk", bg="Cadet Blue")
        self.lblEmail.grid(row=6, column=0, sticky=W)
        self.txtEmail = Entry(ABC2, font=('arial',12,'bold'), textvariable=Email, width=20)
        self.txtEmail.grid(row=6, column=1, pady=3, padx=20)

        self.lblN = Label(ABC2, font=('arial',12,'bold'), text="Nationality:", padx=2,pady=2, fg="Cornsilk", bg="Cadet Blue")
        self.lblN .grid(row=7, column=0, sticky=W)
        self.cboN = ttk.Combobox(ABC2, textvariable=Nationality, state='readonly', font=('arial',12,'bold'),  width=20)
        self.cboN['value']=('','Britain','Nigeria','Ghana','Kenya','Canada','France','Norway','United States','Germany',)
        self.cboN.current(0)
        self.cboN.grid(row=7, column=1, pady=3, padx=20)

        self.lblDOB = Label(ABC2, font=('arial',12,'bold'), text="DOB:", padx=2,pady=2, fg="Cornsilk", bg="Cadet Blue")
        self.lblDOB.grid(row=8, column=0, sticky=W)
        self.txtDOB = Entry(ABC2, font=('arial',12,'bold'), textvariable=DOB, width=20)
        self.txtDOB.grid(row=8, column=1, pady=3, padx=20)

        self.lblIDType = Label(ABC2, font=('arial',12,'bold'), text="IDType:", padx=2,pady=2, fg="Cornsilk", bg="Cadet Blue")
        self.lblIDType.grid(row=9, column=0, sticky=W)
        self.cboIDType = ttk.Combobox(ABC2, textvariable=IDType, state='readonly', font=('arial',12,'bold'),  width=20)
        self.cboIDType['value']=('','Driving License','Student ID','Passport')
        self.cboIDType.current(0)
        self.cboIDType.grid(row=9, column=1, pady=3, padx=20)

        self.lblGender = Label(ABC2, font=('arial',12,'bold'), text="Gender:", padx=2,pady=2, fg="Cornsilk", bg="Cadet Blue")
        self.lblGender.grid(row=10, column=0, sticky=W)
        self.cboGender = ttk.Combobox(ABC2, textvariable=Gender, state='readonly', font=('arial',12,'bold'),  width=18)
        self.cboGender['value']=('','Male','Female','Transgender')
        self.cboGender.current(0)
        self.cboGender.grid(row=10, column=1, pady=3, padx=20)

        self.lblCheck_In_Date = Label(ABC2, font=('arial',12,'bold'), text="Check In Date:", padx=2,pady=2, fg="Cornsilk", bg="Cadet Blue")
        self.lblCheck_In_Date.grid(row=11, column=0, sticky=W)
        self.txtCheck_In_Date = Entry(ABC2, font=('arial',12,'bold'), textvariable=CheckInDate, width=20)
        self.txtCheck_In_Date.grid(row=11, column=1, pady=3, padx=40)

        self.lblCheck_Out_Date = Label(ABC2, font=('arial',12,'bold'), text="Check Out Date:", padx=2,pady=2, fg="Cornsilk", bg="Cadet Blue")
        self.lblCheck_Out_Date.grid(row=12, column=0, sticky=W)
        self.txtCheck_Out_Date = Entry(ABC2, font=('arial',12,'bold'), textvariable=CheckOutDate, width=20)
        self.txtCheck_Out_Date.grid(row=12, column=1, pady=3, padx=40)

        self.lblMeal = Label(ABC2, font=('arial',12,'bold'), text="Meal:", padx=2,pady=2, fg="Cornsilk", bg="Cadet Blue")
        self.lblMeal.grid(row=13, column=0, sticky=W)
        self.cboMeal = ttk.Combobox(ABC2, textvariable=Meal, state='readonly', font=('arial',12,'bold'),  width=18)
        self.cboMeal['value']=('','BreakFast','Lunch','Dinner')
        self.cboMeal.current(0)
        self.cboMeal.grid(row=13, column=1, pady=3, padx=20)

        self.lblRoomType = Label(ABC2, font=('arial',12,'bold'), text="Room Type:", padx=2,pady=2, fg="Cornsilk", bg="Cadet Blue")
        self.lblRoomType.grid(row=14, column=0, sticky=W)
        self.cboRoomType = ttk.Combobox(ABC2, textvariable=RoomType, state='readonly', font=('arial',12,'bold'),  width=18)
        self.cboRoomType['value']=('','Single','Double','Family')
        self.cboRoomType.current(0)
        self.cboRoomType.grid(row=14, column=1, pady=3, padx=20)

        self.Espresso = Checkbutton(ABC3, text="Espresso", variable=var1, onvalue=1, offvalue=0, font=('arial', 12, 'bold'), bg="powder blue").grid(row=0, sticky=W)
        self.txtEspresso = Entry(ABC3, font=('arial', 12, 'bold'), textvariable=E_Espresso, bd=8, width=20, justify='left', state = DISABLED)
        self.txtEspresso.grid(row=1, column=1)

        self.Milk_Shake = Checkbutton(ABC3, text="Milk Shake", variable=var1, onvalue=1, offvalue=0, font=('arial', 12, 'bold'), bg="powder blue").grid(row=0, sticky=W)
        self.txtMilk_Shake = Entry(ABC3, font=('arial', 12, 'bold'), textvariable=E_Milk_Shake, bd=8, width=20, justify='left', state = DISABLED)
        self.txtMilk_Shake.grid(row=2, column=1)

        self.Vanilla_Ice = Checkbutton(ABC3, text="Vanilla Ice", variable=var1, onvalue=1, offvalue=0, font=('arial', 12, 'bold'), bg="powder blue").grid(row=0, sticky=W)
        self.txtVanilla_Ice = Entry(ABC3, font=('arial', 12, 'bold'), textvariable=E_Vanilla_Ice, bd=8, width=20, justify='left', state = DISABLED)
        self.txtVanilla_Ice.grid(row=3, column=1)

        self.Iced_Tea = Checkbutton(ABC3, text="Iced Tea", variable=var1, onvalue=1, offvalue=0, font=('arial', 12, 'bold'), bg="powder blue").grid(row=0, sticky=W)
        self.txtIced_Tea = Entry(ABC3, font=('arial', 12, 'bold'), textvariable=E_Iced_Tea, bd=8, width=20, justify='left', state = DISABLED)
        self.txtIced_Tea.grid(row=4, column=1)

        self.American_Coffee = Checkbutton(ABC3, text="American Coffee", variable=var1, onvalue=1, offvalue=0, font=('arial', 12, 'bold'), bg="powder blue").grid(row=0, sticky=W)
        self.txtAmerican_Coffee = Entry(ABC3, font=('arial', 12, 'bold'), textvariable=E_American_Coffee, bd=8, width=20, justify='left', state = DISABLED)
        self.txtAmerican_Coffee.grid(row=5, column=1)

        self.Cappuccino = Checkbutton(ABC3, text="Cappuccino", variable=var1, onvalue=1, offvalue=0, font=('arial', 12, 'bold'), bg="powder blue").grid(row=0, sticky=W)
        self.txtCappuccino = Entry(ABC3, font=('arial', 12, 'bold'), textvariable=E_Cappuccino, bd=8, width=20, justify='left', state = DISABLED)
        self.txtCappuccino.grid(row=6, column=1)

        self.Green_Tea = Checkbutton(ABC3, text="Green Tea", variable=var1, onvalue=1, offvalue=0, font=('arial', 12, 'bold'), bg="powder blue").grid(row=0, sticky=W)
        self.txtGreen_Tea = Entry(ABC3, font=('arial', 12, 'bold'), textvariable=E_Green_Tea, bd=8, width=20, justify='left', state = DISABLED)
        self.txtGreen_Tea.grid(row=7, column=1)

        self.African_Coffee = Checkbutton(ABC3, text="African Coffee", variable=var1, onvalue=1, offvalue=0, font=('arial', 12, 'bold'), bg="powder blue").grid(row=0, sticky=W)
        self.txtAfrican_Coffee = Entry(ABC3, font=('arial', 12, 'bold'), textvariable=E_African_Coffee, bd=8, width=20, justify='left', state = DISABLED)
        self.txtAfrican_Coffee.grid(row=8, column=1)

        self.lblspace=Label(ABC3, text="Tax and Total Sum", font=('arial', 18, 'bold'), pady=1, bd=9, bg="cadet Blue", fg="Cornsilk", width=26,
                            justify=CENTRE).grid(row=8, colunm=0, colunmspan=4)

        self.lblPaidTax = Label(ABC3, font=('arial',12,'bold'), text="Paid Tax",bd=7, fg="Black", bg="powder Blue")
        self.lblPaidTax .grid(row=10, column=0, sticky=W)
        self.txtPaidTax  = Entry(ABC3, font=('arial',12,'bold'), textvariable=PaidTax, bd=7, bg="White", width=20, justify=LEFT)
        self.txtPaidTax .grid(row=10, column=1)        

        self.lblSubTotal = Label(ABC3, font=('arial',12,'bold'), text="Sub Total",bd=7, fg="Black", bg="powder Blue")
        self.lblSubTotal .grid(row=11, column=0, sticky=W)
        self.txtSubTotal  = Entry(ABC3, font=('arial',12,'bold'), textvariable=SubTotal, bd=7, bg="White", width=20, justify=LEFT)
        self.txtSubTotal .grid(row=11, column=1)

        self.lblTotalCost = Label(ABC3, font=('arial',12,'bold'), text="Total Cost",bd=7, fg="Black", bg="powder Blue")
        self.lblTotalCost .grid(row=12, column=0, sticky=W)
        self.txtTotalCost  = Entry(ABC3, font=('arial',12,'bold'), textvariable=TotalCost, bd=7, bg="White", width=20)
        self.txtTotalCost .grid(row=12, column=1)


        self.btnTotal = Button(ABC6, padx=14, pady=7, bd=5, fg="black", font=('arial',16,'bold'), width =5, height=2,
                               bg="powder blue", text="Total").grid(row=0, column=0)

        self.btnReset = Button(ABC6, padx=14, pady=7, bd=5, fg="black", font=('arial',16,'bold'), width =5, height=2,
                               bg="powder blue", text="Reset", command=Reset).grid(row=0, column=1)

        self.btnExit = Button(ABC6, padx=14, pady=7, bd=5, fg="black", font=('arial',16,'bold'), width =5, height=2,
                               bg="powder blue", text="Exit", command=Exit).grid(row=0, column=2)
        

if __name__=='__main__':
    root = Tk()
    application = customer(root)
    root.mainloop()

from tkinter import*
import math,random
from tkinter import messagebox
class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color="#074463"
        title=Label(self.root,text="Amazing Grace Store",bd=12, relief=GROOVE,bg=bg_color,fg="white", font=('arial', 30, 'bold'),pady=2).pack(fill=X)
        #====================Variables====
        self.soap = IntVar()
        self.face_cream = IntVar()
        self.face_wash = IntVar()
        self.hair_spray = IntVar()
        self.hair_gell = IntVar()
        self.body_lotion = IntVar()
        self.hair_cream = IntVar()

        self.grains = IntVar()
        self.bread = IntVar()
        self.cereals = IntVar()
        self.food_oil = IntVar()
        self.sugar = IntVar()
        self.beverages = IntVar()
        self.nuts = IntVar()

        self.alcohol = IntVar()
        self.cocacola = IntVar()
        self.fanta = IntVar()
        self.juices = IntVar()
        self.wines = IntVar()
        self.sprite = IntVar()
        self.vodkas = IntVar()

        self.cosmetic_prices = StringVar()
        self.grocery_prices = StringVar()
        self.drink_prices = StringVar()

        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.drink_tax = StringVar()

        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search = StringVar()
        
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details", font=('times new roman', 15, 'bold'),fg='gold',bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)
        #====================Customer detail Frame====
        cname_lbl=Label(F1, text="Customer Name",bg=bg_color,fg="white",font=('arial', 18, 'bold')).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15, textvariable=self.c_name, font="arial 15", bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        
        cphn_lbl=Label(F1, text="Phone No.",bg=bg_color,fg="white",font=('arial', 18, 'bold')).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,width=15, textvariable=self.c_phone, font="arial 15", bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        c_bill_lbl=Label(F1, text="Bill Number",bg=bg_color,fg="white",font=('arial', 18, 'bold')).grid(row=0,column=4,padx=20,pady=5)
        c_bill_txt=Entry(F1,width=15,textvariable=self.bill_no, font="arial 15", bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        bill_btn=Button(F1,text="Search",width=10,textvariable=self.search, bd=7,font='arial 12 bold').grid(row=0,column=6, pady=10, padx=10)


        #===========COSTMETIC FRAME=====
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics", font=('times new roman', 15, 'bold'),fg='gold',bg=bg_color)
        F2.place(x=5,y=180,width=325,height=380)

        bath_lbl=Label(F2, text="Bath Soap", font=('times new roman', 16, 'bold'),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.soap, font=('times new roman', 16, 'bold'),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Face_cream_lbl=Label(F2, text="Face Cream", font=('times new roman', 16, 'bold'),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Face_cream_txt=Entry(F2,width=10,textvariable=self.face_cream,font=('times new roman', 16, 'bold'),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        Face_w_lbl=Label(F2, text="Face Wash", font=('times new roman', 16, 'bold'),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Face_w_txt=Entry(F2,width=10,textvariable=self.face_wash,font=('times new roman', 16, 'bold'),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        Hair_s_lbl=Label(F2, text="Hair Spray", font=('times new roman', 16, 'bold'),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Hair_s_txt=Entry(F2,width=10,textvariable=self.hair_spray,font=('times new roman', 16, 'bold'),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        Hair_g_lbl=Label(F2, text="Hair Gell", font=('times new roman', 16, 'bold'),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Hair_g_txt=Entry(F2,width=10,textvariable=self.hair_gell,font=('times new roman', 16, 'bold'),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        Body_l_lbl=Label(F2, text="Body Lotion", font=('times new roman', 16, 'bold'),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Body_l_txt=Entry(F2,width=10,textvariable=self.body_lotion,font=('times new roman', 16, 'bold'),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        Hair_c_lbl=Label(F2, text="Hair Cream", font=('times new roman', 16, 'bold'),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Hair_c_txt=Entry(F2,width=10,textvariable=self.hair_cream,font=('times new roman', 16, 'bold'),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        
        #===========GROCERY FRAME=====
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Groceries", font=('times new roman', 15, 'bold'),fg='gold',bg=bg_color)
        F3.place(x=340,y=180,width=325,height=380)

        g1_lbl=Label(F3, text="Grains", font=('times new roman', 16, 'bold'),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        g1_txt=Entry(F3,width=10,textvariable=self.grains,font=('times new roman', 16, 'bold'),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        g2_lbl=Label(F3, text="Bread", font=('times new roman', 16, 'bold'),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        g2_txt=Entry(F3,width=10,textvariable=self.bread,font=('times new roman', 16, 'bold'),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        g3_lbl=Label(F3, text="Cereals", font=('times new roman', 16, 'bold'),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        g3_txt=Entry(F3,width=10,textvariable=self.cereals,font=('times new roman', 16, 'bold'),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        g4_lbl=Label(F3, text="Food Oil", font=('times new roman', 16, 'bold'),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        g4_txt=Entry(F3,width=10,textvariable=self.food_oil,font=('times new roman', 16, 'bold'),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        g5_lbl=Label(F3, text="Sugar", font=('times new roman', 16, 'bold'),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        g5_txt=Entry(F3,width=10,textvariable=self.sugar,font=('times new roman', 16, 'bold'),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        g6_lbl=Label(F3, text="Beverages", font=('times new roman', 16, 'bold'),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        g6_txt=Entry(F3,width=10,textvariable=self.beverages,font=('times new roman', 16, 'bold'),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        g7_lbl=Label(F3, text="Nuts", font=('times new roman', 16, 'bold'),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        g7_txt=Entry(F3,width=10,textvariable=self.nuts, font=('times new roman', 16, 'bold'),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        
        #===========DRINK FRAME=====
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Drinks", font=('times new roman', 15, 'bold'),fg='gold',bg=bg_color)
        F4.place(x=670,y=180,width=325,height=380)

        c1_lbl=Label(F4, text="Alcohol", font=('times new roman', 16, 'bold'),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        c1_txt=Entry(F4,width=10,textvariable=self.alcohol,font=('times new roman', 16, 'bold'),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        c2_lbl=Label(F4, text="Coca Cola", font=('times new roman', 16, 'bold'),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        c2_txt=Entry(F4,width=10,textvariable=self.cocacola,font=('times new roman', 16, 'bold'),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        c3_lbl=Label(F4, text="Fanta", font=('times new roman', 16, 'bold'),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        c3_txt=Entry(F4,width=10,textvariable=self.fanta,font=('times new roman', 16, 'bold'),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        c4_lbl=Label(F4, text="Juices", font=('times new roman', 16, 'bold'),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        c4_txt=Entry(F4,width=10,textvariable=self.juices,font=('times new roman', 16, 'bold'),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        c5_lbl=Label(F4, text="Wines", font=('times new roman', 16, 'bold'),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        c5_txt=Entry(F4,width=10,textvariable=self.wines,font=('times new roman', 16, 'bold'),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        c6_lbl=Label(F4, text="Sprite", font=('times new roman', 16, 'bold'),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        c6_l_txt=Entry(F4,width=10,textvariable=self.sprite,font=('times new roman', 16, 'bold'),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        c7_lbl=Label(F4, text="Vodkas", font=('times new roman', 16, 'bold'),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        c7_l_txt=Entry(F4,width=10,textvariable=self.vodkas,font=('times new roman', 16, 'bold'),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #========bill area======
        F5=LabelFrame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1010,y=180,width=350,height=380)
        bill_title=Label(F5,text="Bill Area",font='arial 15 bold',bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #=======button Frame=========

        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu", font=("times new roman", 15, "bold"),fg='gold',bg=bg_color)
        F6.place(x=0,y=560,relwidth=1,height=140)
        n1_lbl=Label(F6, text="Total Cosmetics price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        n1_txt=Entry(F6,width=18,textvariable=self.cosmetic_prices,font='arial 10 bold',bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        n2_lbl=Label(F6, text="Total Groceries price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        n2_txt=Entry(F6,width=18,textvariable=self.grocery_prices,font='arial 10 bold',bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        n3_lbl=Label(F6, text="Total Drinks price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        n3_txt=Entry(F6,width=18,textvariable=self.drink_prices,font='arial 10 bold',bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)
        
        c1_lbl=Label(F6, text="Cosmetic Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_txt=Entry(F6,width=18,textvariable=self.cosmetic_tax,font='arial 10 bold',bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        c2_lbl=Label(F6, text="Groceries Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_txt=Entry(F6,width=18,textvariable=self.grocery_tax,font='arial 10 bold',bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        c3_lbl=Label(F6, text="Drinks Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_txt=Entry(F6,width=18,textvariable=self.drink_tax,font='arial 10 bold',bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)
        
        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=750,width=580,height=105)

        total_btn=Button(btn_F,command=self.total,text="Total",bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
        GBill_btn=Button(btn_F,text="Generate Bill",command=self.bill_area,bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5)
        Reset_btn=Button(btn_F,text="Reset",bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=5)
        Exit_btn=Button(btn_F,text="Exit",bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()

    def total(self):
        self.c_s_p=self.soap.get()*40
        self.c_fc_p=self.face_cream.get()*120
        self.c_fw_p=self.face_wash.get()*60
        self.c_hs_p=self.hair_spray.get()*180
        self.c_hg_p=self.hair_gell.get()*140
        self.c_bl_p=self.body_lotion.get()*180
        self.c_hr_p=self.hair_cream.get()*140
        
        self.total_cosmetic_price=float(
                                    self.c_s_p+
                                    self.c_fc_p+
                                    self.c_fw_p+
                                    self.c_hs_p+
                                    self.c_hg_p+
                                    self.c_bl_p+
                                    self.c_hr_p
                                    )
        self.cosmetic_prices.set("N "+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set("N "+str(self.c_tax))

        
        self.g_g_p=self.grains.get()*80
        self.g_b_p=self.bread.get()*180
        self.g_c_p=self.cereals.get()*60
        self.g_f_p=self.food_oil.get()*240
        self.g_s_p=self.sugar.get()*45
        self.g_b_p=self.beverages.get()*150
        self.g_n_p=self.nuts.get()*45

        self.total_groceries_price=float(
                                    self.g_g_p+
                                    self.g_b_p+
                                    self.g_c_p+
                                    self.g_f_p+
                                    self.g_s_p+
                                    self.g_b_p+
                                    self.g_n_p
                                    )
        self.grocery_prices.set("N "+str(self.total_groceries_price))
        self.g_tax=round((self.total_groceries_price*0.05),2)
        self.grocery_tax.set("N "+str(self.g_tax))


        self.d_a_p=self.alcohol.get()*60
        self.d_c_p=self.cocacola.get()*60
        self.d_f_p=self.fanta.get()*40
        self.d_j_p=self.juices.get()*50
        self.d_w_p=self.wines.get()*45
        self.d_s_p=self.sprite.get()*60
        self.d_v_p=self.vodkas.get()*40

        self.total_drinks_price=float(
                                 self.d_a_p+
                                 self.d_c_p+
                                 self.d_f_p+
                                 self.d_j_p+
                                 self.d_w_p+
                                 self.d_s_p+
                                 self.d_v_p
                                    )
        
        self.drink_prices.set("N "+str(self.total_drinks_price))
        self.d_tax=round((self.total_drinks_price*0.05),2)
        self.drink_tax.set("N "+str(self.d_tax))

        self.Total_bill=float(  self.total_cosmetic_price+
                                self.total_groceries_price+
                                self.total_drinks_price+
                                self.c_tax+
                                self.g_tax+
                                self.d_tax
                              )
                                

    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END,"\tWelcome Amazing-Grace Retail \tStore")
        self.txtarea.insert(END,f"\nBill Number : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\nCustomer Name : {self.c_name.get()}")
        self.txtarea.insert(END,f"\nPhone Number : {self.c_phone.get()}")
        self.txtarea.insert(END,f"\n======================================")
        self.txtarea.insert(END,f"\n Products\t\tQTY\t\tPrice ")
        self.txtarea.insert(END,f"\n======================================")
        
    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error", "Customer details must be included")
        elif self.cosmetic_prices.get()=="N 0.0" and self.grocery_prices.get()=="N 0.0" and self.drink_prices.get()=="N 0.0":
            messagebox.showerror("Error","No Products selected")
        else:
            self.welcome_bill()
            #====cosmetics======
            if self.soap.get()!=0:
                self.txtarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")
            if self.face_cream.get()!=0:
                self.txtarea.insert(END,f"\n Face Cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
            if self.face_wash.get()!=0:
                self.txtarea.insert(END,f"\n Face Wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
            if self.hair_spray.get()!=0:
                self.txtarea.insert(END,f"\n Hair Spray\t\t{self.hair_spray.get()}\t\t{self.c_hs_p}")
            if self.hair_gell.get()!=0:
                self.txtarea.insert(END,f"\n Hair Gell\t\t{self.hair_gell.get()}\t\t{self.c_hg_p}")
            if self.body_lotion.get()!=0:
                self.txtarea.insert(END,f"\n Body Lotion\t\t{self.body_lotion.get()}\t\t{self.c_bl_p}")
            if self.hair_cream.get()!=0:
                self.txtarea.insert(END,f"\n Hair Cream\t\t{self.hair_cream.get()}\t\t{self.c_hc_p}")

            #====Groceries======
            if self.grains.get()!=0:
                self.txtarea.insert(END,f"\n Grains\t\t{self.grains.get()}\t\t{self.g_g_p}")
            if self.bread.get()!=0:
                self.txtarea.insert(END,f"\n Bread\t\t{self.bread.get()}\t\t{self.g_b_p}")
            if self.cereals.get()!=0:
                self.txtarea.insert(END,f"\n Cereals\t\t{self.cereals.get()}\t\t{self.g_c_p}")
            if self.food_oil.get()!=0:
                self.txtarea.insert(END,f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_f_p}")
            if self.sugar.get()!=0:
                self.txtarea.insert(END,f"\n Sugar\t\t{self.sugar.get()}\t\t{self.g_s_p}")
            if self.beverages.get()!=0:
                self.txtarea.insert(END,f"\n Beverages\t\t{self.beverages.get()}\t\t{self.g_b_p}")
            if self.nuts.get()!=0:
                self.txtarea.insert(END,f"\n Nuts\t\t{self.nuts.get()}\t\t{self.g_n_p}")

            #====Drinks======
            if self.alcohol.get()!=0:
                self.txtarea.insert(END,f"\n Alcohol\t\t{self.alcohol.get()}\t\t{self.d_a_p}")
            if self.cocacola.get()!=0:
                self.txtarea.insert(END,f"\n Coca Cola\t\t{self.cocacola.get()}\t\t{self.d_c_p}")
            if self.fanta.get()!=0:
                self.txtarea.insert(END,f"\n Fanta\t\t{self.fanta.get()}\t\t{self.d_f_p}")
            if self.juices.get()!=0:
                self.txtarea.insert(END,f"\n Juices\t\t{self.juices.get()}\t\t{self.d_j_p}")
            if self.wines.get()!=0:
                self.txtarea.insert(END,f"\n Wines\t\t{self.wines.get()}\t\t{self.d_w_p}")
            if self.sprite.get()!=0:
                self.txtarea.insert(END,f"\n Sprite\t\t{self.sprite.get()}\t\t{self.d_s_p}")
            if self.vodkas.get()!=0:
                self.txtarea.insert(END,f"\n Vodkas\t\t{self.vodkas.get()}\t\t{self.d_v_p}")

        self.txtarea.insert(END,f"\n--------------------------------------")
        if self.cosmetic_tax.get()!="N0.0":
            self.txtarea.insert(END,f"\n Cosmetic Tax\t\t\t\t\{self.cosmetic_tax.get()}")
        if self.grocery_tax.get()!="N0.0":
            self.txtarea.insert(END,f"\n Groceries Tax\t\t\t\t\{self.grocery_tax.get()}")
        if self.drink_tax.get()!="N0.0":
            self.txtarea.insert(END,f"\n Drinks Tax\t\t\t\t\{self.drink_tax.get()}")

        self.txtarea.insert(END,f"\n Total Bill :\t\t\t\t\{self.Total_bill}")
        self.txtarea.insert(END,f"\n--------------------------------------")
                        
        


                
root=Tk()
obj = Bill_App(root)
root.mainloop()

from tkinter import *
import json, requests
from tkinter import ttk
from tkinter import messagebox as tmsg
import sqlite3
from PIL import Image,ImageTk

class GUI(Tk): #CLASS GUI

    def __init__(self, url, access_key):
        
        super().__init__()      #Calling super class's ('TK') constructor                
        
        #USING TWO API's 1.'http://data.fixer.io/api/'
        #               2.'https://api.exchangerate-api.com/v4/latest/USD'
        
        #Because of request limits....
        
        try:                                                 #trying API-1 ('https://data.fixer.io/api/')
            self.access_key = access_key
            self.url = url
            self.mainurl = self.url + 'latest?access_key=' + self.access_key
            self.response = requests.get(self.mainurl)
            self.data = self.response.json()
            self.currencies=self.data['rates']
            self.date=self.data['date']
            #print(self.currencies)
        
        except:  #if API_1 does not works then this except part for API-2('https://api.exchangerate-api.com/v4/latest/USD')
            
            self.response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
            self.data = self.response.json()
            self.currencies=self.data['rates']
            self.date=self.data['date']
            #print(self.currencies)
        
        #coverpage..
        
        self.geometry("700x426")
        self.maxsize(700,526)                
        self.title("Currency Converter")               
        self.wm_iconbitmap("hnet.com-image.ico") ##LPU_ICON
        #self['background']='#856ff8'
        self.image=Image.open('currency_converter.jpg')
        self.photo=ImageTk.PhotoImage(self.image)
        self.label=Label(image=self.photo)
        self.label.place(x=0,y=0)
        
        
        statusvar=StringVar()

        statusvar.set(" GOOD MORNING EVERYONE..")
        sbar=Label(self, textvariable=statusvar, font="comicsansms 21 bold ",bg="black", fg="white",relief=RAISED,pady=15,justify=CENTER)
        sbar.place(x=70,y=10)
        sbar.update()
        import time
        time.sleep(4)
        statusvar.set("WELCOME TO CURRENCY CONVERTER")
        
        #course code and course name..
        
        self.course_name_label=Label(text="INT-213 PYTHON", font="comicsansms 15 underline",bg="purple", fg="white",relief=RAISED,justify=CENTER)
        self.course_name_label.place(x=70,y=100)
        
        #group-no..
        self.group_name_label=Label(text="Group-20", font="comicsansms 15 underline",bg="purple", fg="white",relief=RAISED,justify=CENTER)
        self.group_name_label.place(x=70,y=130)
        
        #group members..
        self.group_member_label=Label(text="Group Members:-\nAbhishek Kumar Singh\nPalak Bhushan\nKaran Singh Naruka", font="comicsansms 15 italic",bg="yellow", fg="black",relief=RAISED,justify=LEFT)
        self.group_member_label.place(x=70,y=180)
        
        #roll_number..
        self.roll_label=Label(text="Roll Number\n15\n27\n26", font="comicsansms 15 italic",bg="yellow", fg="black",relief=RAISED,justify=CENTER)
        self.roll_label.place(x=500,y=180)
        
        Button(self,text="OPEN APP",bg="red",fg="white",font="comicsansms 15 bold",command=self.app_gui).place(x=290,y=305)

        #coverpage ends...
        
       
    
        
    #GUI PART
    def app_gui(self):
                
        self.image=Image.open('backgg.jpg')
        self.photo=ImageTk.PhotoImage(self.image)
        self.label=Label(image=self.photo)
        self.label.place(x=0,y=0)
        
         
        
        self.geometry("700x526")
        self.maxsize(700,526)                
        self.title("Currency Converter")               
        self.wm_iconbitmap("hnet.com-image.ico")   ##LPU_ICON
        
        
        
        
        
        ##sql connection...
        

        self.conn=sqlite3.connect('newdb.sqlite')
        self.cursor=self.conn.cursor()


        self.cursor.execute('drop table if exists counts')
        self.cursor.execute('CREATE TABLE counts(DATE TEXT, FROM_CURRENCY TEXT, TO_CURRENCY TEXT, AMOUNT TEXT, RESULT INTEGER)')
        
        
        
        
        #GUI widgetes, variables and labels...
        
        Label(text="CURRENCY CONVERTER", font="comicsansms 21 bold",bg="black", fg="white",relief=RAISED,pady=15).pack(fill=X)
        self.date_label = Label(self,
                                text=f"Date : {self.data['date']}",
                                relief=SOLID, borderwidth=5,font="courier,10")
        
        self.date_label.pack(pady=10)

        #variables...
        self.result=0
        self.from_=StringVar()
        self.from_.set("USD")
        
        self.amount=DoubleVar()
        self.to=StringVar()
        self.to.set("INR")
        
        #DROPDOWN MENUs...
        
        self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_,values=list(self.currencies.keys()),
                                                   font="comicsansms 18 bold",state='readonly', width=10,justify=CENTER)
        self.from_currency_dropdown.place(x=100,y=140)
        
        self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to,
                                                 values=list(self.currencies.keys()),
                                                 font="comicsansms 18 bold",state='readonly', width=10,justify=CENTER)
        self.to_currency_dropdown.place(x=460,y=140)
        
        
        #ENTRY..
        self.from_amount=Entry(self, textvariable=self.amount,width=17, relief=RIDGE,
                               justify=CENTER,font="comicsansms 12 bold", borderwidth=3).place(x=100,y=200)
        
        #OUTPUT LABEL...
        self.converted_amount_field_label = Label(self, text='0.0', fg='black',
                                                  bg='white', relief=RIDGE,
                                                  justify=CENTER, width=15, borderwidth=3,font="comicsansms 12 bold")
        self.converted_amount_field_label.place(x=460,y=200)
        
        #BUTTONS...
        
        Button(text="CONVERT",padx=10,pady=10,width=15,bg="red",fg="white",font="comicsansms 10 bold",command=self.conversion).place(x=290,y=280)
        Button(text="SAVE",padx=10, pady=8, width=10,bg="yellow", fg="black", font="comicsansms 9 bold", command=self.save).place(x=210, y=350)
        Button(text="SHOW DATA", padx=10, pady=8, width=10, bg="yellow", fg="black", font="comicsansms 9 bold", command= self.showdata).place (x=430, y=350)
        Button(text="Exit",padx=10,pady=8,width=10, bg="purple",fg="white",font="comicsansms 9 bold",command=self.destroy).place(x=320, y=350)
        
        Label(text="", font="comicsansms 21 bold",bg="black", fg="white",relief=RAISED,pady=15).pack(side=BOTTOM,fill=X)
    
    
    #CONVERSION FUNCTION
    
    def conversion(self):
        try:
            rate_from =self.data['rates'][self.from_.get()]
            rate_to = self.data['rates'][self.to.get()]
            self.result = (self.amount.get() * rate_to) / rate_from
            self.result=round(self.result,2)
            self.converted_amount_field_label.config(text=str(self.result))
            
        except Exception as e: #EXCEPTION FOR INVALID INPUT
            
            tmsg.showerror("Warning","Invalid Input:")     #WARNING MESSAGE_BOX FOR INVALID INPUT
    
    #SAVE FUNCTION
    
    def save(self):
    
        self.cursor=self.conn.cursor()
 
        self.cursor.execute('''insert into counts values(? , ? , ? , ? , ?)''',(self.date,self.from_.get(),self.to.get(),self.amount.get(),self.result))
        
        self.conn.commit()
    
    #SHOW DATA FUNCTION...
    
    def showdata(self):
        self.cursor=self.conn.cursor()
        self.cursor.execute('select * from counts')
        self.mydata=self.cursor.fetchall()
        print("                YOUR TABLE")
        print()
        print("('  DATE','   FROM','  TO','AMOUNT','RESULT')")
        for data in self.mydata:
            print(data)


if __name__ == '__main__':
    baseurl='http://data.fixer.io/api/'
    accesskey='d8bb0828eecaa42b3119f51bc492c06b'

    converter = GUI(baseurl, accesskey)
    mainloop()
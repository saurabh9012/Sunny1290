from tkinter import *#ye humne module import kr liya hai.
from tkinter import ttk #ye module neche ttk combobox chalne ki leye hai.
from tkinter import messagebox #ye module message show krne ki leye use kiya jata hai neche humne messagebox function use kiya hai.
import datetime #ye module import kiya hai date time ka current time use krne ki leye neche dekhe ek jgha use kr rhe hai.
#yha neche humne mysql ko import kiya hai fr neche library name ki ek library name ka datbase bnaya hai jo localhost pr show hoga.
import tkinter # ye import kiya hai neche message box diya hai yes or No ki leye hai.
import pymysql as mq
from requests import delete


con=mq.connect(host="localhost",user="root",password="")
cursor=con.cursor()
try:
     db="create database IF NOT EXISTS Library2"  #ye if not exists jo hai ye operator hai sql ka ese use kiya hai bcoz same name ki 
                                                   #databse pr wo baar baar ye bol rha tha ki already exists bt ab nhi aayega eske lgne ki leye.
     cursor.execute(db)
     print("Database created")
except:
    print("Database error..")#yha tk vhe kiya hai.mysql mein library name ka database create kiya hai.
#Ab hum table create krege neche dekhe kaise.

con=mq.connect(host="localhost",user="root",password="",database="Library2")
mysql=con.cursor() #yha pr cursor ko start kiya hai.
tc="create table IF NOT EXISTS LibraryManagementSystem(Member_Type varchar(45), PRN_No varchar(45) primary key,ID_No varchar(45),FirstName varchar(45),LastName varchar(45),Address1 varchar(45),Address2 varchar(45),Post_Code varchar(45),Mobile varchar(10),Book_Id varchar(45),Book_Title varchar(45),Auther_Name varchar(45),Date_Borrowed varchar(45),Date_Due varchar(45),Days_On_Book varchar(45),Late_Return_Fine varchar(45),Date_Over_Due varchar(45),Actual_Price varchar(45))"
mysql.execute(tc)


class LibraryManagementSystem: #ye humne ek class bnaye hai
    def __init__(self,root): #fr humne ek constructor bnaya hai or self ki saath window ka name diya hai root.
        self.root=root #yha pr maine self ko initlize kiya hai.
        self.root.title("Library Management System") #ye hum window ka title de rhe hai or window ka name hai root.
        self.root.geometry("1550x800+0+0") #ye window ka size btaya hai.

        #Humne text box ki text lene ki leye variable bna rhe jo ki us text mein jo bhi hum entry fill mein enter krege wo data humare databse 
        #mein show hona chaye to uske leye kuch variable bna rhe hai neche dekhe kaise.
        self.Member_Type_var=StringVar() #yha pr datatype bhi dena hota hai bt hum koi calculation perform to kr nhi rhe hai esliye maine sbme string hi liya hai.
        self.PRN_No_var=StringVar()
        self.ID_No_var=StringVar()
        self.FirstName_var=StringVar()
        self.LastName_var=StringVar()
        self.Address1_var=StringVar()
        self.Address2_var=StringVar()
        self.Post_Code_var=StringVar()
        self.Mobile_var=StringVar()
        self.Book_Id_var=StringVar()
        self.Book_Title_var=StringVar()
        self.Auther_Name_var=StringVar()
        self.Date_Borrowed_var=StringVar()
        self.Date_Due_var=StringVar()
        self.Days_On_Book_var=StringVar()
        self.Late_Return_Fine_var=StringVar()
        self.Date_Over_Due_var=StringVar()
        self.Actual_Price_var=StringVar()
        				
        


        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",20,"bold"),padx=2,pady=6) 
        #hum yha pr label bna rhe hai or jha bnana hai uska name de rhe hai.or fr esme label ka name de rhe hai.or size etc.uper vaale line mein
        lbltitle.pack(side=TOP,fill=X) #eske line ki help se display hoga window pr or fr ese hume pack krna hota hai esko pack kr rhe hai or fr side ka 
                                 #name de rhe hai jis side mein ye label daalna hai.

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue") #ye ek frame bna rhe hai or wo bhi window mein bna rhe hai to uska name bhi self.root diya hai.
        frame.place(x=0,y=80,width=1360,height=400) #yha pr frame ko place kr rhe hai or uske leye hume place ki value dene hoti x nd y.
        
    
        #Ab hum 2 or frame bna rhe hai uper jo frame bnaya tha uske under hi.ek left side mein or dusra right side.neche dekhe kaise.
    
        #==================================================DataFrameLeft=============================================================
        DataFrameLeft=LabelFrame(frame,text="Library Memebership Information",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=720,height=350) #ye x=0 ka mtlb hai ki start se use ho.
        
        #Ab hume DataFrameLeft mein ek Label bnana hai member ki leye.neche dekhe kaise bna rhe hai.
        lblMember=Label(DataFrameLeft,text="MemberType:",bg="powder blue",font=("time new roman",12,"bold"),padx=2,pady=6) #ye line label bnane ki leye hi hai.
        lblMember.grid(row=0,column=0,sticky=W) #ye humne grid kiya haikyu ki ye frame ki under hai or line se aayega to uske leye grid hi acha 
                                                #rhega.or grid mein hume raw nd column dene hoti hai.or sticky mtlb kis side or W ka mtlb west side.
        
        #hum neche entry vaale line mein or com member vaale line mein sbme jo textvariable=self.MemberType es trha se saare text entry mein
        #jo diya hai wo esliye diya hai kyu ki vha humne jo uper variables name diye hai xampp ki database ki read ki leye to yha bhi usse ki
        # leye use kr rhe hai ye baad mein use kiya hai xampp mein database create ki baad.neche dekhe kaise kiya hai use sbhi mein.
         
        #Ab hume ese ki under combo box chaye or ye ttk ki help se bnayege.neche dekhe kaise.
        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.Member_Type_var,font=("time new roman",13,"bold"),width=22,state="readonly") #ye humne jo bracket mein lekha hai name diya hai jgha ka ki kha chaye.
                                                                                                        #or ye state jo use kiya or esme read only esliye diya hai bcoz 
                                                                                                        #jo show ho rha tha Admin staff etc wo change bhi ho rha tha bt wo nhi hona 
                                                                                                        # chaye to eske help se ab nhi hoga.
        comMember["values"]=("Admin Staff","Student","Lecturer") #ye values dene hai list lga kr or wo values mein tuple pass krauga main mtlb ki tuple ka use kr ki.
        comMember.grid(row=0,column=1) #ye grid mein row same rhege bt column change hoga.bcoz jo label lekha hua hai member vaala uske aage chaye.

        #Ab or entry bnayege PRN NO DataframeLeft vaale mein member label ki neche.show hoga wo.
        lblPRN_No=Label(DataFrameLeft,text="PRN No:",bg="powder blue",font=("time new roman",12,"bold"),padx=2,pady=6) #ye line ka use PRN no ka label laane ki leye kiya hai membar vaale label ki baad 
        lblPRN_No.grid(row=1,column=0,sticky=W) #ye Display krne ki leye use kiya hai.
        #Ab hume ek entry box chaye entry krne PRN No ki aage neche dekhe kaise,member vaale ki leye to combo box chaye tha bt yha pr entry box chaye.
        textPRN_No=Entry(DataFrameLeft,textvariable=self.PRN_No_var,font=("times new roman",13,"bold"),width=24)
        textPRN_No.grid(row=1,column=1)

        #ye jo lable or entry bne hai neche lblTitle vaale name se ID no vaale entry hai.
        lblTitle=Label(DataFrameLeft,text="ID No:",bg="powder blue",font=("time new roman",12,"bold"),padx=2,pady=4)
        lblTitle.grid(row=2,column=0,sticky=W)
        textTitle=Entry(DataFrameLeft,textvariable=self.ID_No_var,font=("times new roman",13,"bold"),width=24)
        textTitle.grid(row=2,column=1)

        #Ab ek entry First Name ki leye bnege.neche dekhe kaise.
        lblFirstName=Label(DataFrameLeft,text="FirstName:",bg="powder blue",font=("time new roman",12,"bold"),padx=2,pady=4)
        lblFirstName.grid(row=3,column=0,sticky=W)
        textFirstName=Entry(DataFrameLeft,textvariable=self.FirstName_var,font=("times new roman",13,"bold"),width=24)
        textFirstName.grid(row=3,column=1)

        #Ab Last Name ki leye ek lable or entry bnayege.neche dekhe kaise.
        lblLastName=Label(DataFrameLeft,text="LastName:",bg="powder blue",font=("time new roman",12,"bold"),padx=2,pady=4)
        lblLastName.grid(row=4,column=0,sticky=W)
        textLastName=Entry(DataFrameLeft,textvariable=self.LastName_var,font=("times new roman",13,"bold"),width=24)
        textLastName.grid(row=4,column=1)

        #Ab Address1 ki leye ek lable or entry bnayege .neche dekhe kaise. 
        lblAddress1=Label(DataFrameLeft,text="Address1:",bg="powder blue",font=("time new roman",12,"bold"),padx=2,pady=4)
        lblAddress1.grid(row=5,column=0,sticky=W)
        textAddress1=Entry(DataFrameLeft,textvariable=self.Address1_var,font=("times new roman",13,"bold"),width=24)
        textAddress1.grid(row=5,column=1)

        #Ab address2 ki leye ek lable or entry bnayege neche dekhe kaise.
        lblAddress2=Label(DataFrameLeft,text="Address2:",bg="powder blue",font=("time new roman",12,"bold"),padx=2,pady=4)
        lblAddress2.grid(row=6,column=0,sticky=W)
        textAddress2=Entry(DataFrameLeft,textvariable=self.Address2_var,font=("times new roman",13,"bold"),width=24)
        textAddress2.grid(row=6,column=1)

        #Ab PostCode ki leye ek lable or entry bnayege neche dekhe kaise krege.
        lblPostCode=Label(DataFrameLeft,text="Post Code:",bg="powder blue",font=("time new roman",12,"bold"),padx=2,pady=4)
        lblPostCode.grid(row=7,column=0,sticky=W)
        textPostCode=Entry(DataFrameLeft,textvariable=self.Post_Code_var,font=("times new roman",13,"bold"),width=24)
        textPostCode.grid(row=7,column=1)

        #Ab Mobile no ki leye ek lable or entry bnayege neche dekhe kaise.
        lblMobile=Label(DataFrameLeft,text="Mobile:",bg="powder blue",font=("time new roman",12,"bold"),padx=2,pady=4)
        lblMobile.grid(row=8,column=0,sticky=W)
        textMobile=Entry(DataFrameLeft,textvariable=self.Mobile_var,font=("times new roman",13,"bold"),width=24)
        textMobile.grid(row=8,column=1)

        #Ab krege Book Id ki leye ek label or entry banyege bt ab sochege ki yrr Dataframe left jo tha wo to full  hogya ab kaise krege bt nhi ab hum
        #dusre side lekehege phle humne row 8 tk lekha row 0 se lekr, ab jo lekhege row 0 se fr se start krege bt column change 
        #krege jaise phle column hum 0 mein to name dete the or column 1 mein hum entry dete the. So aise ab hum column 2 mein name dege
        #or column 3 mein entry dege neche dekhe kaise krege.
        lblBookId=Label(DataFrameLeft,text="Book ID:",bg="powder blue",font=("time new roman",12,"bold"),padx=2,pady=4)
        lblBookId.grid(row=0,column=2,sticky=W)
        textBookId=Entry(DataFrameLeft,textvariable=self.Book_Id_var,font=("times new roman",13,"bold"),width=24)
        textBookId.grid(row=0,column=3)

        #Ab Book Title ki leye ek Lable or entry banyege neche dekhe.
        lblBookTitle=Label(DataFrameLeft,text="Book Title:",bg="powder blue",font=("time new roman",12,"bold"),padx=2,pady=4)
        lblBookTitle.grid(row=1,column=2,sticky=W)
        textBookTitle=Entry(DataFrameLeft,textvariable=self.Book_Title_var,font=("times new roman",13,"bold"),width=24)
        textBookTitle.grid(row=1,column=3)

        #Ab Book Author ki leye ek lable or entry bnayege neche dekhe.
        lblAuther=Label(DataFrameLeft,text="Auther Name:",bg="powder blue",font=("time new roman",12,"bold"),padx=2,pady=4)
        lblAuther.grid(row=2,column=2,sticky=W)
        textAuther=Entry(DataFrameLeft,textvariable=self.Auther_Name_var,font=("times new roman",13,"bold"),width=24)
        textAuther.grid(row=2,column=3)

        #Ab Date Borrowed ki leye ek lable or entry bnayege neche dekhe kaise.
        lblDateIssue=Label(DataFrameLeft,text="Date Borrowed:",bg="powder blue",font=("time new roman",12,"bold"),padx=2,pady=4)
        lblDateIssue.grid(row=3,column=2,sticky=W)
        textDateIssue=Entry(DataFrameLeft,textvariable=self.Date_Borrowed_var,font=("times new roman",13,"bold"),width=24)
        textDateIssue.grid(row=3,column=3)

        #Ab Date Due ki leye ek lable or entry bnayege neche dekhe kaise.
        lblDateDue=Label(DataFrameLeft,text="Date Due:",bg="powder blue",font=("time new roman",12,"bold"),padx=2,pady=4)
        lblDateDue.grid(row=4,column=2,sticky=W)
        textDateDue=Entry(DataFrameLeft,textvariable=self.Date_Due_var,font=("times new roman",13,"bold"),width=24)
        textDateDue.grid(row=4,column=3)

        #Ab Days on  Book ki leye ek lable or entry bnayege neche dekhe kaise.
        lblDaysOnBook=Label(DataFrameLeft,text="Days On Book:",bg="powder blue",font=("time new roman",12,"bold"),padx=2,pady=4)
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        textDaysOnBook=Entry(DataFrameLeft,textvariable=self.Days_On_Book_var,font=("times new roman",13,"bold"),width=24)
        textDaysOnBook.grid(row=5,column=3)

        #Ab Late Return Fine ki leye ek lable or entry bnayege neche dekhe kaise.
        lblLateReturnFine=Label(DataFrameLeft,text="Late ReturnFine:",bg="powder blue",font=("time new roman",12,"bold"),padx=2,pady=4)
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        textLateReturnFine=Entry(DataFrameLeft,textvariable=self.Late_Return_Fine_var,font=("times new roman",13,"bold"),width=24)
        textLateReturnFine.grid(row=6,column=3)

        #Ab Date Over date ki leye ek lable or entry bnayege neche dekhe kaise.
        lblDateOverdate=Label(DataFrameLeft,text="Date Over date:",bg="powder blue",font=("time new roman",12,"bold"),padx=2,pady=4)
        lblDateOverdate.grid(row=7,column=2,sticky=W)
        textDateOverdate=Entry(DataFrameLeft,textvariable=self.Date_Over_Due_var,font=("times new roman",13,"bold"),width=24)
        textDateOverdate.grid(row=7,column=3)

        #Ab ek Actual price ki leye lable or entry bnayege neche dekhe kaise.
        lblActualPrice=Label(DataFrameLeft,text="Actual Price:",bg="powder blue",font=("time new roman",12,"bold"),padx=2,pady=4)
        lblActualPrice.grid(row=8,column=2,sticky=W)
        textActualPrice=Entry(DataFrameLeft,textvariable=self.Actual_Price_var,font=("times new roman",13,"bold"),width=24)
        textActualPrice.grid(row=8,column=3)




        
        #==================================================DataFrameRight==============================================================
        DataFrameRight=LabelFrame(frame,text="Book Details",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameRight.place(x=720,y=5,width=580,height=350) #or ye x=910 ka mtlb hai ki jo uper frame bnaya hai wo 900 tk tha to ab 910 se start ho.
        
        #Ab hume DataFrameRight ki under ek text Box chaye,dekhte hai neche kaise bnayege.
        self.txtBox=Text(DataFrameRight,font=("times new roman",12,"bold"),width=32,height=15,padx=2,pady=6) #ye line text box ki leye hi use kr rhe hai.
        self.txtBox.grid(row=0,column=2)
        #Ab hume ek list box bhi chahye wo bnayege ab.neche dekhe kaise.bt usse phle books ki list or scroll bar bna lete hai neche dekhe.
        listScrollbar=Scrollbar(DataFrameRight) #ye scroll bar bnane ki leye hai
        listScrollbar.grid(row=0,column=1,sticky="ns") #sticky ns ka mtlb north south mein show ho ye scroll bar.
        

        listBooks=['Head Firt Book','Learn Python The Hard Way','Python Programming','Secrete Rahshy','Python CookBook','Intro to Machine Learning','Fluent Python','Machine Tecno','My Python','Machine Python','Advance Python','Python'] #ye humne list bnaye hai jisme book ki name hai or ye list box mein show krege.
        #yha pr hum ek function bn rhe h kyu ki jb bhi hum book pr click kre to uske saare details automatically show hone lge to uske leye ye
        #function use kr rhe hai neche dekhe kaise.
        def SelectBook(event=""): #yha pr hum event paas kr rhe hai.
            value=str(listBox.get(listBox.curselection())) #ab value paas kra rhe hai or string format mein krege or hum book ki list le rhe hai list box kyu ki list box mein to books hai.
            x=value
            if (x=="Head Firt Book"):
                self.Book_Id_var.set("BKID9012")
                self.Book_Title_var.set("Python Manual")
                self.Auther_Name_var.set("Paul Barry")
                d1=datetime.date.today() # ye jo uper module import kiya hai date or time ka uske leye hai date or time correct btaye yha vhe kr rhe hai.
                d2=datetime.timedelta(days=15) #jo bhi borrow kre 15 ka gap kiya hai. 
                d3=d1+d2 #ye plus kr diya hai time or date ko 
                self.Date_Borrowed_var.set(d1) #ye d1 esliye diya kyu ki jo time ko issue hue hai book us ki hesab se aaye na.
                self.Date_Due_var.set(d3)
                self.Days_On_Book_var.set(15)
                self.Late_Return_Fine_var.set("Rs.50")
                self.Date_Over_Due_var.set("No")
                self.Actual_Price_var.set("Rs.788")

            elif (x=="Learn Python The Hard Way"):
                self.Book_Id_var.set("BKID5454")
                self.Book_Title_var.set("Basic Of Python")
                self.Auther_Name_var.set("ZED A.SHAW")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.Date_Borrowed_var.set(d1) 
                self.Date_Due_var.set(d3)
                self.Days_On_Book_var.set(15)
                self.Late_Return_Fine_var.set("Rs.50")
                self.Date_Over_Due_var.set("No")
                self.Actual_Price_var.set("Rs.650")
            
            elif (x=="Python Programming"):
                self.Book_Id_var.set("BKID8790")
                self.Book_Title_var.set("Introduction Of Python")
                self.Auther_Name_var.set("John Zhelle")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.Date_Borrowed_var.set(d1) 
                self.Date_Due_var.set(d3)
                self.Days_On_Book_var.set(15)
                self.Late_Return_Fine_var.set("Rs.50")
                self.Date_Over_Due_var.set("No")
                self.Actual_Price_var.set("Rs.600")

            elif (x=="Secrete Rahshy"):
                self.Book_Id_var.set("BKID8788")
                self.Book_Title_var.set("Introduction Of Python")
                self.Auther_Name_var.set("Kapil Garg")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.Date_Borrowed_var.set(d1) 
                self.Date_Due_var.set(d3)
                self.Days_On_Book_var.set(15)
                self.Late_Return_Fine_var.set("Rs.50")
                self.Date_Over_Due_var.set("No")
                self.Actual_Price_var.set("Rs.625")
            
            elif (x=="Python CookBook"):
                self.Book_Id_var.set("BKID1278")
                self.Book_Title_var.set("Python")
                self.Auther_Name_var.set("Brian Jones")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.Date_Borrowed_var.set(d1) 
                self.Date_Due_var.set(d3)
                self.Days_On_Book_var.set(15)
                self.Late_Return_Fine_var.set("Rs.50")
                self.Date_Over_Due_var.set("No")
                self.Actual_Price_var.set("Rs.325")
            
            elif (x=="Intro to Machine Learning"):
                self.Book_Id_var.set("BKID1256")
                self.Book_Title_var.set("Intro to Machine Learning")
                self.Auther_Name_var.set("Sarah Guaido")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.Date_Borrowed_var.set(d1) 
                self.Date_Due_var.set(d3)
                self.Days_On_Book_var.set(15)
                self.Late_Return_Fine_var.set("Rs.50")
                self.Date_Over_Due_var.set("No")
                self.Actual_Price_var.set("Rs.525")
            
            elif (x=="Fluent Python"):
                self.Book_Id_var.set("BKID4290")
                self.Book_Title_var.set("Learn Python")
                self.Auther_Name_var.set("G.Garg")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.Date_Borrowed_var.set(d1) 
                self.Date_Due_var.set(d3)
                self.Days_On_Book_var.set(15)
                self.Late_Return_Fine_var.set("Rs.50")
                self.Date_Over_Due_var.set("No")
                self.Actual_Price_var.set("Rs.925")
            
            elif (x=="Machine Tecno"):
                self.Book_Id_var.set("BKID1290")
                self.Book_Title_var.set("Machine Learning with Python")
                self.Auther_Name_var.set("RK.Verma")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.Date_Borrowed_var.set(d1) 
                self.Date_Due_var.set(d3)
                self.Days_On_Book_var.set(15)
                self.Late_Return_Fine_var.set("Rs.50")
                self.Date_Over_Due_var.set("No")
                self.Actual_Price_var.set("Rs.1025")

            elif (x=="My Python"):
                self.Book_Id_var.set("BKID8787")
                self.Book_Title_var.set("Python")
                self.Auther_Name_var.set("RK.Verma")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.Date_Borrowed_var.set(d1) 
                self.Date_Due_var.set(d3)
                self.Days_On_Book_var.set(15)
                self.Late_Return_Fine_var.set("Rs.50")
                self.Date_Over_Due_var.set("No")
                self.Actual_Price_var.set("Rs.1120")
            
            elif (x=="Machine Python"):
                self.Book_Id_var.set("BKID8787")
                self.Book_Title_var.set("Machine Python")
                self.Auther_Name_var.set("PK.Sharma")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.Date_Borrowed_var.set(d1) 
                self.Date_Due_var.set(d3)
                self.Days_On_Book_var.set(15)
                self.Late_Return_Fine_var.set("Rs.50")
                self.Date_Over_Due_var.set("No")
                self.Actual_Price_var.set("Rs.920")
            
            elif (x=="Advance Python"):
                self.Book_Id_var.set("BKID8787")
                self.Book_Title_var.set("Advance Python")
                self.Auther_Name_var.set("Sarah Guaido")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.Date_Borrowed_var.set(d1) 
                self.Date_Due_var.set(d3)
                self.Days_On_Book_var.set(15)
                self.Late_Return_Fine_var.set("Rs.50")
                self.Date_Over_Due_var.set("No")
                self.Actual_Price_var.set("Rs.500")
            
            elif (x=="Python"):
                self.Book_Id_var.set("BKID8787")
                self.Book_Title_var.set("Advance Python")
                self.Auther_Name_var.set("Sarah Guaido")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.Date_Borrowed_var.set(d1) 
                self.Date_Due_var.set(d3)
                self.Days_On_Book_var.set(15)
                self.Late_Return_Fine_var.set("Rs.50")
                self.Date_Over_Due_var.set("No")
                self.Actual_Price_var.set("Rs.500")


            
        #Ab enko show krne ki leye ek list box bnayege jiska name se listbook rhege neche dekhe kaise.
        listBox=Listbox(DataFrameRight,font=("times new roman",12,"bold"),width=20,height=15)
        listBox.bind("<<ListboxSelect>>",SelectBook) #ab ye hum bind kr rhe hai jo humne uper books ka data diya hai selectbook function mein ye hum bind ki under function hota hai listbox name ka usse bind kr rhe hai.
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview) #ye hum config kr rhe hai scroll bar ko ki kha show hona chaye or ye humne name de diya hai ki listbox mein ho.
        
        #Ab hum listbox mein listBooks daalne hai uske leye neche dekhe kya krege.
        for item in listBooks:
            listBox.insert(END,item) #ye humne for loop use kiya hai listbooks ko show krne ki leye listbox mein.



        #==================Ab Hum buttons frames bnayege.or wo frame left or right jo frame bne hai unke neche bnega.======================
        Framebuttons=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue") #ye humne coding button frame ki leye ki hai.
        Framebuttons.place(x=0,y=480,width=1360,height=70) #fr usko display kr rhe hai button frame ko.
        
        #Ab hum ye jo uper buttons frame bna hu hai eske under button bnayege neche dekhe kaise.
        btnAddData=Button(Framebuttons,command=self.add_data,text="Add Data",font=("times new roman",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)
        #Ab hum ek button show data ki leye bnayege esme mein.neche dekhe kaise.
        btnAddData=Button(Framebuttons,command=self.showData,text="Show Data",font=("times new roman",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=1)
        #Ab ek button Update ki leye bnayege.neche dekhe kaise.
        btnAddData=Button(Framebuttons,command=self.update,text="Update",font=("times new roman",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=2)
        #Ab ek button Delete ki leye bnayege neche dekhe kaise.
        btnAddData=Button(Framebuttons,command=self.delete,text="Delete",font=("times new roman",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=3)
        #Ab ek button Reset ki leye bnayege neche dekhe kaise.
        btnAddData=Button(Framebuttons,command=self.reset,text="Reset",font=("times new roman",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=4)
        #Ab ek button Exit ki leye bnayege neche dekhe kaise.
        btnAddData=Button(Framebuttons,command=self.iExit,text="Exit",font=("times new roman",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=5)


    

        #================Database ka data show krne ki leye ek frame or banyege.Information Frame,wo button frame ki neche bnega.=============
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=551,width=1360,height=136)
        #Ab es vaale frame mein bhi ek data table bnayege database ka data show krne ki leye.neche dekhe kaise.
        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1300,height=110)
        #Ab es frame mein hume ek grid system bnane hai column name aayege jo bhi column hoga jo database mein save hoga wo column name.neche dekhe
        #usko bnane ki leye hume ek tree view bnana hota hai.or grid system ki leye hota hai neche dekhe kaise.

        #Bt ese phle hum ek scrollbar bnayege ttk ki help se neche dekhe kaise.Esko esliye bna rhe kyu ki database ki columns hai unko aage peche kr ki dekh sekte ho
        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL) #scrollbar=ttk ki help se fr kiske under to table frame ki under or fr orient mein btana hai kaise aaye scrollbar. 
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL) 

        self.library_table=ttk.Treeview(Table_frame,column=("MemberType","PRN No","ID No","FirstName","LastName","Address1","Address2",
                                                            "Post Code","Mobile","Book Id","Book Title","Auther Name","Date Borrowed","Date Due","Days On Book",
                                                            "Late Return Fine","Date Over Due","Actual Price"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set) #fr scrollbar ko esme set kr diya.
                                                            #humne library table name rkh deya hai,or kha pr bnana hai table frame ki under.
                                                            #uske baad column mein hum ek dumy data de rhe hai.
        xscroll.pack(side=BOTTOM,fill=X) #yha pr fr humne pack kiya hai scrollbar ko 
        yscroll.pack(side=RIGHT,fill=Y) #same yha pr bhi.

        #Ab scrollbox ko config krege view krane ki leye.neche dekhe kaise.
        xscroll.config(command=self.library_table.xview) #bracket mein wo diya hai ki kiske saath config krna hai.to library table mein krna hai.
        yscroll.config(command=self.library_table.yview)
      
        
        self.library_table.heading("MemberType",text="Member Type") #Ab ye hum actual mein heading user ko show krana hai wo yha pr lekh rhe hai.fr heading ki leye
                                       #first hume jo dumy humne uper lekha hai fr uske dena hoga fr ek text= dene hai jo bhi user ko dekhana hai.
        #Aise saare lekhne hai hume.neche dekhe kaise.
        self.library_table.heading("PRN No",text="PRN No")
        self.library_table.heading("ID No",text="ID No")
        self.library_table.heading("FirstName",text="FirstName")
        self.library_table.heading("LastName",text="LastName")
        self.library_table.heading("Address1",text="Address1")
        self.library_table.heading("Address2",text="Address2")
        self.library_table.heading("Post Code",text="Post Code")
        self.library_table.heading("Mobile",text="Mobile")
        self.library_table.heading("Book Id",text="Book Id")
        self.library_table.heading("Book Title",text="Book Title")
        self.library_table.heading("Auther Name",text="Auther Name")
        self.library_table.heading("Date Borrowed",text="Date Borrowed")
        self.library_table.heading("Date Due",text="Date Due")
        self.library_table.heading("Days On Book",text="Days On Book")
        self.library_table.heading("Late Return Fine",text="Late Return Fine")
        self.library_table.heading("Date Over Due",text="Date Over Due")
        self.library_table.heading("Actual Price",text="Actual Price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        #Ab hum jo heading aarhe hai column mein library table ki under usko size thek krte hai width dekr.neche dekhe kaise.
        self.library_table.column("MemberType",width=100) #or esme dumy name jo diye the uper wo dumy name fr se dege yha pr bhi.
        self.library_table.column("PRN No",width=100)
        self.library_table.column("ID No",width=100)
        self.library_table.column("FirstName",width=100)
        self.library_table.column("LastName",width=100)
        self.library_table.column("Address1",width=100)
        self.library_table.column("Address2",width=100)
        self.library_table.column("Post Code",width=100)
        self.library_table.column("Mobile",width=100)
        self.library_table.column("Book Id",width=100)
        self.library_table.column("Book Title",width=100)
        self.library_table.column("Auther Name",width=100)
        self.library_table.column("Date Borrowed",width=100)
        self.library_table.column("Date Due",width=100)
        self.library_table.column("Days On Book",width=100)
        self.library_table.column("Late Return Fine",width=100)
        self.library_table.column("Date Over Due",width=100)
        self.library_table.column("Actual Price",width=100)

        self.fatch_data() #ye esliye ki jb hum table mein data enter kre to vhe pr show hojaye humara data.
        #Ab yha pr neche jo kiya hai usme data automatically click krne pr entry field mein aaye ye sb uske leye yha pr bind kr rhe hai.
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)

#Ab Add data name ka ek function bna rhe hai es function ki help se hum database mein humara data add kiya hai.neche dekhe kaise.

    def add_data(self):
        conn=mq.connect(host="localhost",user="root",password="",database="Library2")  #ab connection dene ki leye ek conn name ka variable bna liya hai ab connect kr rhe hai.
        mycursor=conn.cursor()
        mycursor.execute("insert into LibraryManagementSystem values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                                                                                            (   self.Member_Type_var.get(),
                                                                                                                self.PRN_No_var.get(),
                                                                                                                self.ID_No_var.get(),
                                                                                                                self.FirstName_var.get(),
                                                                                                                self.LastName_var.get(),
                                                                                                                self.Address1_var.get(),
                                                                                                                self.Address2_var.get(),
                                                                                                                self.Post_Code_var.get(),
                                                                                                                self.Mobile_var.get(),
                                                                                                                self.Book_Id_var.get(),
                                                                                                                self.Book_Title_var.get(),
                                                                                                                self.Auther_Name_var.get(),
                                                                                                                self.Date_Borrowed_var.get(),
                                                                                                                self.Date_Due_var.get(),
                                                                                                                self.Days_On_Book_var.get(),
                                                                                                                self.Late_Return_Fine_var.get(),
                                                                                                                self.Date_Over_Due_var.get(),
                                                                                                                self.Actual_Price_var.get()
                                                                                                           ))
        conn.commit()
        self.fatch_data() #ye ki jo bhi data hai wo esme add hojaye.
        conn.close()
        messagebox.showinfo("Success","Member Has been inserted successfully")
    
    #ye neche jo kr rhe hai ye esliye kr rhe h bcoz jo humne data fill kiya hai entry box mein ki kya name hai book price etc
    #wo neche jo sbse infromation name ka hai jo database se connect hai wo show hona chaye.esliye ye fatch function use kr rhe hai.
    def fatch_data(self):
        conn=mq.connect(host="localhost",user="root",password="",database="Library2")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from LibraryManagementSystem")
        rows=my_cursor.fetchall() #ye rows name ka variable bna leya hai fr fetchall ki help se fetch kr rha hu.
        
        #Ab es data ko insert krna hai table ki under to if use krege
        if len(rows)!=0: #ab equal nhi hai to kuch to data hoga eske under
            self.library_table.delete(*self.library_table.get_children()) #To phle es data ko delete kr lete hai, yha se sbhi data delete hoga.
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()

        
    #Ab hume kya krna hai jb bhi hum wo neche sbse jo information show ho rhe hai ki kya book name hai kisne le hai etc us pr jb bhi click kre 
    #to entry field mein wo automatically show ho us pr krege neche kaam.
    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus() #ye cursor_row name ka variable bna liya hai. or es cursor row pr focus kiya hai.
        content=self.library_table.item(cursor_row) #fr eske under ka content jo bhi content hai eske under ki item cursor row se es content    #meinaajaye.
        row=content["values"] #ek varibale or bna rha hu, fr jo bhi content mein hai wo le lege.

        self.Member_Type_var.set(row[0]),
        self.PRN_No_var.set(row[1]),
        self.ID_No_var.set(row[2]),
        self.FirstName_var.set(row[3]),
        self.LastName_var.set(row[4]),
        self.Address1_var.set(row[5]),
        self.Address2_var.set(row[6]),
        self.Post_Code_var.set(row[7]),
        self.Mobile_var.set(row[8]),
        self.Book_Id_var.set(row[9]),
        self.Book_Title_var.set(row[10]),
        self.Auther_Name_var.set(row[11]),
        self.Date_Borrowed_var.set(row[12]),
        self.Date_Due_var.set(row[13]),
        self.Days_On_Book_var.set(row[14]),
        self.Late_Return_Fine_var.set(row[15]),
        self.Date_Over_Due_var.set(row[16]),
        self.Actual_Price_var.set(row[17])
    
    #Ab jo button hai Add data ki side mein show data uske leye kaam krege ab neche dekhe kaise.
    def showData(self):
        #show krne ki leye data hume text field mein jo bhi entry field hai usme data insert krna hai.neche dekhe kaise kr rhe hai.
        self.txtBox.insert(END,"MemeberType:\t\t"+ self.Member_Type_var.get() + "\n")
        self.txtBox.insert(END,"PRN No:\t\t"+ self.PRN_No_var.get() + "\n")
        self.txtBox.insert(END,"ID No:\t\t"+self.ID_No_var.get() + "\n")
        self.txtBox.insert(END,"FirstName:\t\t"+self.FirstName_var.get() + "\n")
        self.txtBox.insert(END,"LastName:\t\t"+self.LastName_var.get() + "\n")
        self.txtBox.insert(END,"Address1:\t\t"+self.Address1_var.get() + "\n")
        self.txtBox.insert(END,"Address2:\t\t"+self.Address2_var.get() + "\n")
        self.txtBox.insert(END,"Post Code:\t\t"+self.Post_Code_var.get() + "\n")
        self.txtBox.insert(END,"Mobile:\t\t"+self.Mobile_var.get() + "\n")
        self.txtBox.insert(END,"Book Id:\t\t"+self.Book_Id_var.get() + "\n")
        self.txtBox.insert(END,"Book Title:\t\t"+self.Book_Title_var.get() + "\n")
        self.txtBox.insert(END,"Auther Name:\t\t"+self.Auther_Name_var.get() + "\n")
        self.txtBox.insert(END,"Date Borrowed:\t\t"+self.Date_Borrowed_var.get() + "\n")
        self.txtBox.insert(END,"Date Due:\t\t"+self.Date_Due_var.get() + "\n")
        self.txtBox.insert(END,"Date On Book:\t\t"+self.Days_On_Book_var.get() + "\n")
        self.txtBox.insert(END,"Late ReturnFine:\t\t"+self.Late_Return_Fine_var.get() + "\n")
        self.txtBox.insert(END,"Date Over Due:\t\t"+self.Date_Over_Due_var.get() + "\n")
        self.txtBox.insert(END,"Actual Price:\t\t"+self.Actual_Price_var.get() + "\n")
        
    #Ab hum reset ki leye kaam krege.neche dekhe kaise.
    def reset(self):
        self.Member_Type_var.set(""),
        self.PRN_No_var.set(""),
        self.ID_No_var.set(""),
        self.FirstName_var.set(""),
        self.LastName_var.set(""),
        self.Address1_var.set(""),
        self.Address2_var.set(""),
        self.Post_Code_var.set(""),
        self.Mobile_var.set(""),
        self.Book_Id_var.set(""),
        self.Book_Title_var.set(""),
        self.Auther_Name_var.set(""),
        self.Date_Borrowed_var.set(""),
        self.Date_Due_var.set(""),
        self.Days_On_Book_var.set(""),
        self.Late_Return_Fine_var.set(""),
        self.Date_Over_Due_var.set(""),
        self.Actual_Price_var.set("")
        self.txtBox.delete("1.0",END) #ye delete ki leye kiya hai.
    

    #Ab hum exit ki leye work krege.
    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Management System","Do you want to exit") #yha pr tkinter ki help se hum message box dege yes or no ka we want to exit or Not.bt usse phle hume impoert krna hogatkinter ko.
        if iExit>0:
            self.root.destroy() #humne if condtiton de or bola ki agar wo yes bole to humare jo self.root window hai wo destroy hojaye.
            return #agar no kha to vhe pr return hojaye.

    #Ab hum update ki leye work krege.neche dekhe kaise.
    def update(self):
        conn=mq.connect(host="localhost",user="root",password="",database="Library2")
        my_cursor=conn.cursor()
        my_cursor.execute("UPDATE LibraryManagementSystem SET Member_Type=%s,ID_No=%s,FirstName=%s,LastName=%s,Address1=%s,Address2=%s,Post_Code=%s,Mobile=%s,Book_Id=%s,Book_Title=%s,Auther_Name=%s,Date_Borrowed=%s,Date_Due=%s,Days_On_Book=%s,Late_Return_Fine=%s,Date_Over_Due=%s,Actual_Price=%s where PRN_No=%s",(
                                                    self.Member_Type_var.get(),
                                                    self.ID_No_var.get(),
                                                    self.FirstName_var.get(),
                                                    self.LastName_var.get(),
                                                    self.Address1_var.get(),
                                                    self.Address2_var.get(),
                                                    self.Post_Code_var.get(),
                                                    self.Mobile_var.get(),
                                                    self.Book_Id_var.get(),
                                                    self.Book_Title_var.get(),
                                                    self.Auther_Name_var.get(),
                                                    self.Date_Borrowed_var.get(),
                                                    self.Date_Due_var.get(),
                                                    self.Days_On_Book_var.get(),
                                                    self.Late_Return_Fine_var.get(),
                                                    self.Date_Over_Due_var.get(),
                                                    self.Actual_Price_var.get(),
                                                    self.PRN_No_var.get()
                                                )) #sbko update ki leye where Prn no se select kiya hai ye add 
                                                     #function ki trha uper vaale bs prn no last mein lekhna hai.
        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close()
        messagebox.showinfo("Success","Member has been Updated") #ye message bhi show kra rhe hai user ko dekhe.
    
    #Ab hum delete function pr work krege.
    def delete(self):
        if self.PRN_No_var.get()=="" or self.ID_No_var.get()=="":#ye condition use kr rhe hai ki agar data ko select kiya to hi mera data delete hojaye.
            messagebox.showerror("Error","First Select the Member")
        else:
            conn=mq.connect(host="localhost",user="root",password="",database="Library2")
            my_cursor=conn.cursor()
            query="delete from LibraryManagementSystem where PRN_No=%s"
            value=(self.PRN_No_var.get(),)
            my_cursor.execute(query,value)
            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success","Member has been Deleted")


        





        
if __name__=="__main__": #ye humne main function bnaya hai.
    root=Tk() #fr object bnaya Tk class ka.
    obj=LibraryManagementSystem(root) #object bnaya hai class ka or fr usme humne window lekha hai jo window ka name hai root.

    root.mainloop() #root ko maine mainloop se close kr diya hai.








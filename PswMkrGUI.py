from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import sqlite3
from random import randint
from typing import Type
#--------------------------------------------------------
#methods

#Open add password menu
def OpenAddMenu():
    HideAllFrames()
    add_password_frame.pack(fill='both', expand=1)
    AddMenuStructure()
#Struture code for the Add Password Menu
def AddMenuStructure():
    backcol="#151f56"
    #title
    titulo=Label(add_password_frame,text="Add Password",bg = backcol,fg = "white",font = font_title)#main title
    titulo.place(x=80, y=25)

    #input variables
    add_site=StringVar()
    add_user=StringVar()
    add_pass=StringVar()

    #user inputs label
    add_site_label=Label(add_password_frame,text="Site:", bg=backcol, fg = "white",font = font_normal)
    add_site_label.place(x=30, y=130)

    add_user_label=Label(add_password_frame,text="Username:", bg=backcol, fg = "white",font = font_normal)
    add_user_label.place(x=30, y=200)

    add_pass_label=Label(add_password_frame,text="Password:", bg=backcol, fg = "white",font = font_normal)
    add_pass_label.place(x=30, y=270)

    #user inputs
    add_site_entry = Entry(add_password_frame,textvariable=add_site,bg="white", font="Bebas_Neue 12")#web site info
    add_site_entry.place(x=90,y=135, height=25, width=340)

    add_user_entry = Entry(add_password_frame,textvariable=add_user,bg="white", font="Bebas_Neue 12")#username info
    add_user_entry.place(x=160,y=205, height=25, width=270)

    add_pass_entry = Entry(add_password_frame,textvariable=add_pass,bg="white", font="Bebas_Neue 12")#username info
    add_pass_entry.place(x=155,y=275, height=25, width=275)

    #button
    create_password_button = Button(add_password_frame,text="Add Password", width="12", height="1", command=lambda:NoticeAddPas(add_user,add_site,add_pass,add_pass_entry,add_user_entry,add_site_entry), bg="white",font="Bebas_Neue 19 bold")
    create_password_button.place(x=160,y=350)
#Check if all the inputs are valid and gives notification
def NoticeAddPas(user_info,site_info,pass_info,add_pass_entry,add_user_entry,add_site_entry):
    user_info=user_info.get()
    site_info=site_info.get()
    pass_info=pass_info.get()
    if site_info=="" or user_info=="" or pass_info=="":
        tkinter.messagebox.showerror("Error",f"Please fill in all the data")
    else:
        tkinter.messagebox.showinfo("Registry created","Click ok to continue")
        add_pass_entry.delete(0, END)
        add_user_entry.delete(0, END)
        add_site_entry.delete(0, END)
        OpenVerifyMenu(site_info,user_info,pass_info)
#Close all and call the  verify menu with all the info from the Add passwor dmenu
def OpenVerifyMenu(site_data, user_data, pass_data):
    HideAllFrames()
    verify_password_frame.pack(fill='both', expand=1)
    VerifyInfoStructure(site_data, user_data, pass_data)
#Structure code for the verify menu
def VerifyInfoStructure(site_data, user_data, pass_data):
    backcol="#151f56"
    user_data_info="User: "+user_data
    pass_data_info="Pass: "+pass_data
    #title
    titulo=Label(verify_password_frame,text="Verify",bg = backcol,fg = "white",font = font_title)#main title
    titulo.place(x=60, y=25)
    #Information form AddPassword
    SiteName=Label(verify_password_frame,text="Site:",bg = backcol,fg = "white",font = font_normal)
    SiteName.place(x=50,y=140)
    SiteName=Label(verify_password_frame,text=site_data,bg = backcol,fg = "white",font = "Bebas_Neue 9")
    SiteName.place(x=110,y=145)
    UserName=Label(verify_password_frame,text=user_data_info,bg = backcol,fg = "white",font = font_normal)
    UserName.place(x=50,y=200)
    PassName=Label(verify_password_frame,text=pass_data_info,bg = backcol,fg = "white",font = font_normal)
    PassName.place(x=50,y=260)
    #Change Button
    ChangeInfo=Button(verify_password_frame,text="Change", command=OpenAddMenu, font="Bebas_Neue 19 bold")
    ChangeInfo.place(x=40,y=360,height=60, width=130)
    #Apply Button
    ApplyInfo=Button(verify_password_frame,text="Confirm",command=lambda:CommitComfirm(site_data, user_data, pass_data), font="Bebas_Neue 19 bold")
    ApplyInfo.place(x=300,y=360,height=60, width=130)
#Notify User data has been saved ---INCOMPLETE---
def CommitComfirm(site_data, user_data, pass_data):
    try:
        con=sqlite3.connect('testbd.db')
        cur=con.cursor()
        id=getID(cur)

        print("New id=",id,type(id))
        cur.execute(f"INSERT INTO list VALUES('{site_data}','{user_data}','{pass_data}',{id})")
        con.commit()
        con.close()
        tkinter.messagebox.showinfo("Registry created",f"Data:\nSite: {site_data}\nUser: {user_data}\nPass: {pass_data}\nClick ok to continue")
    except Exception as e:
        tkinter.messagebox.showerror("ERROR",f"{e}")
    HideAllFrames()

def getID(cur):
    cur.execute("SELECT id FROM List ORDER BY id;")
    id=cur.fetchall()
    try:
        id=str(id)
        counter=1
    
        for i in id:
            if i !='(' and i !=')' and i != ',' and i != '[' and i != ']' and i != ' ':
                if counter==int(i):
                    counter=counter+1
                else:
                    return counter+1
        return counter
    except Exception as e:
        return 1
#Open search password menu
def OpenSearchMenu():
    HideAllFrames()
    search_password_frame.pack(fill='both', expand=1)
    OpenSearchMenuStructure()

def OpenSearchMenuStructure():
    backcol="white"
    titulo=Label(search_password_frame,text="Search Password",bg = backcol,fg = "black",font = font_title)
    titulo.place(x=10, y=5)

    #input variables
    query=StringVar()
    currentvar=StringVar()

    #List of options
    options=['Site','User','Pass']

    #user inputs
    searcher = Entry(search_password_frame,textvariable=query,
                        bg=backcol, font="Bebas_Neue 12")#web site info

    searcher.place(x=10,y=70, height=30, width=300)

    #Dropbox
    filterinfo=OptionMenu(search_password_frame ,currentvar,options[0],options[1],options[2])
    
    #Set the current option
    currentvar.set(options[0])
  
    filterinfo.place(x=310,y=70, width=70, height=30)

    #button
    searchB= Button(search_password_frame,text="Search",
                    command=lambda:refresh(query.get(),
                    currentvar.get(),infotable), font="Bebas_Neue 12")
    searchB.place(x=380,y=70,width=70, height=30)

    #Remove selected
    deleteB= Button(search_password_frame,text="Delete",
                    command=lambda:deleteRow(infotable.selection()),
                    font="Bebas_Neue 12")
    deleteB.place(x=400,y=450,width=70)
    #Copy selected
    copyB= Button(search_password_frame,text="Copy Selected",
                    command=lambda:copyRow(infotable.selection()),
                    font="Bebas_Neue 12")
    copyB.place(x=40,y=450, width=160)
    #Edit selected
    editB= Button(search_password_frame,text="Edit",
                    command=lambda:updateRow(infotable.selection()),
                    font="Bebas_Neue 12")
    editB.place(x=300,y=450,width=90)

    #table
    infotable=ttk.Treeview(search_password_frame, columns=(1,2,3,4), show="headings", height=5)
    infotable.column(1,width=30, anchor="c")
    infotable.column(2,width=110, anchor="c")
    infotable.column(3,width=130, anchor="c")
    infotable.column(4,width=210, anchor="c")
    infotable.heading(1,text="ID")
    infotable.heading(2,text="Web Site")
    infotable.heading(3,text="User name / email")
    infotable.heading(4,text="Password")
    infotable.place(x=10, y=120, height=300)

    sub=Label(search_password_frame,text="Options",bg = backcol,fg = "black",font = font_normal)
    sub.place(x=10, y=400)
#hide all frames
def HideAllFrames():
    print("All frames are hidden")
    add_password_frame.pack_forget()
    search_password_frame.pack_forget()
    verify_password_frame.pack_forget()
    modify_data_frame.pack_forget()

def openModifyMenu(user,site, pswrd,id):
    HideAllFrames()
    modify_data_frame.pack(fill='both', expand=1)
    ModifyMenuStructure(user,site, pswrd,id)

def ModifyMenuStructure(user,site,pswrd,id):
    backcol="white"
    size=19
    #title
    titulo=Label(modify_data_frame,text="Modify",bg = backcol,fg = "black",font = font_title)#main title
    titulo.place(x=60, y=15)
    #variables
    InSite=StringVar()
    InSite.set(site)
    InUser=StringVar()
    InUser.set(user)
    InPwrd=StringVar()
    InPwrd.set(pswrd)
    #inputs to modify info
    OGsite=Label(modify_data_frame,text='Site:',bg = backcol,fg = "black",font= f'Bebas_Neue {size} bold')
    OGsite.place(x=20,y=90)
    NWsite=Entry(modify_data_frame,textvariable=InSite,font=font_normal)
    NWsite.place(x=20,y=130)

    OGuser=Label(modify_data_frame,text='User:',bg = backcol,fg = "black",font= f'Bebas_Neue {size} bold')
    OGuser.place(x=20,y=190)
    NWuser=Entry(modify_data_frame,textvariable=InUser,font=font_normal)
    NWuser.place(x=20,y=240)

    OGpwrd=Label(modify_data_frame,text='Password:',bg = backcol,fg = "black",font= f'Bebas_Neue {size} bold')
    OGpwrd.place(x=20,y=320)
    NWpass=Entry(modify_data_frame,textvariable=InPwrd,font='Bebas_Neue 10 bold')
    NWpass.place(x=20,y=370,width=300)
    
    #Change Button
    CancelB=Button(modify_data_frame,text="Cancel", command=ReturnToSearch, font="Bebas_Neue 19 bold")
    CancelB.place(x=20,y=420,height=60, width=130)
    #Apply Button
    ConfirmB=Button(modify_data_frame,text="Confirm",command=lambda:NoticeModification(InSite.get(), InUser.get(), InPwrd.get(), user,site, pswrd,id), font="Bebas_Neue 19 bold")
    ConfirmB.place(x=350,y=420,height=60, width=130)

def ReturnToSearch():
    HideAllFrames()
    OpenSearchMenu()

def NoticeModification(site_data, user_data, pass_data,user,site, pswrd,id):
    warn=False
    if not site_data:
        site_data=site
        warn=True
    if not user_data:
        user_data=user
        warn=True
    if not pass_data:
        pass_data=pswrd
        warn=True
    if warn: tkinter.messagebox.showwarning("Warning","The original information will be used to replace th empty input")
    con=sqlite3.connect('testbd.db')
    cur=con.cursor()
    try:
        print(f"UPDATE List SET site='{site_data}',user='{user_data}',pass='{pass_data}' WHERE id={id};")
        cur.execute(f"UPDATE List SET site='{site_data}',user='{user_data}',pass='{pass_data}' WHERE id={id};")
        con.commit()
        tkinter.messagebox.showinfo("UPDATED",'The database has been updated')
    except Exception as e:
        tkinter.messagebox.showerror("Error",e)
    con.close()
    OpenSearchMenu()
    
#password created notification
def NoticeCrtPas(password):
    user_info=username.get()
    site_info=site.get()

    if site_info!="" or user_info!="":
        try:
            con=sqlite3.connect('testbd.db')
            cur=con.cursor()
            id=getID(cur)
            cur.execute(f"INSERT INTO list VALUES('{site_info}','{user_info}','{password}',{id})")
            con.commit()
            con.close()
            tkinter.messagebox.showinfo("Password created",f"Your password:{password} has been\nadded to the data base")
            site_entry.delete(0, END)
            user_entry.delete(0, END)
        except Exception as e:
            tkinter.messagebox.showerror("Error",e)
    else:
        tkinter.messagebox.showerror("Error",f"Please fill in the site and user data")
#Search button for the search table
def refresh(inputdata,type,table):
    for i in table.get_children():
        table.delete(i)
    try:
        if inputdata:
            sequence=f"SELECT * FROM list WHERE {type} LIKE '%{inputdata}%' ORDER BY id"
        else: sequence='SELECT * FROM list ORDER BY id'
        print(sequence)
        isrtDataInTbl(table,sequence)
    except Exception as e:
        print("--ERROR:",e)
        isrtDataInTbl(table)

def isrtDataInTbl(infotable,command=None):
    if command:
        conexion = sqlite3.connect('testbd.db')
        cur=conexion.cursor()
        #Run command
        cur.execute(command)
        rows = cur.fetchall()
        for dt in rows:
            infotable.insert('','end',iid=dt[3],values=(dt[3],dt[0],dt[1],dt[2]))
        conexion.close()
    else:
        infotable.insert("",'end',text="L1",
                        values=('',"NONE","NONE",
                            "NONE"))

def CreatePass():
    lowerLetters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    UpperLetters=['A', 'B', 'C', 'D', 'E', 'F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    symbols=['|','#','$','&','%','/','-','+','_']
    password=process(lowerLetters,UpperLetters,symbols)
    NoticeCrtPas(password)
def process(lowerLetters,UpperLetters,symbols):
    final='' #Create empty string to store password
    for i in range(30):#Create a password with 30 characters
        key=randint(1,1000)#Chooses a number between 1 and 1000
        #first checks if the number can be devided by 2
        if (key%2)==0:
            #It will add a random character from a specific list of characters
            #depending if the "key" is greater of smaller then 500
            if key<=500:
                #uselower
                temp=lowerLetters[randint(0,len(lowerLetters)-1)] 
                #choose a character without overlapping ammount of characters available
            if key>500:
                #useupper
                temp=UpperLetters[randint(0,len(UpperLetters)-1)]
        else: #If it is not divisible by 2 it will do the same process but with different characters
            if key<=500:
                #useNumber
                temp=str(randint(0,10))
            if key>500:
                #useSymbol
                temp=symbols[randint(0,len(symbols)-1)]

        #Adds selected character to the final string
        final+=temp
    return final#returns the final string (the generated password)

def deleteRow(sel):
    try:
        print (sel[0])
        con=sqlite3.connect('testbd.db')
        cur=con.cursor()
        cur.execute(f'SELECT * FROM List WHERE ID ={sel[0]}')
        res= cur.fetchall()
        print(res)
        con.close()
    except Exception as e:
        tkinter.messagebox.showerror("Error",f"Nothing selected")

def copyRow(sel):
    try:
        root.clipboard_clear()
        print(sel[0])
        con=sqlite3.connect('testbd.db')
        cur=con.cursor()
        cur.execute(f'SELECT pass FROM List WHERE id = {sel[0]}')
        pswrd=cur.fetchone()
        pswrd=str(pswrd[0])
        total=''
        for i in pswrd:
            if i!='(' and i!=')' and i != ',' and i != ' ' and i != '[' and i != ']':
                total=total+i
        root.clipboard_append(total)
        con.close()
    except Exception as e:
        print(e)

def updateRow(sel):
    try:
        id=extractInfo(sel[0])
        con=sqlite3.connect('testbd.db')
        cur=con.cursor()
        data=['site','user','pass']
        counter=0
        for i in data:
            cur.execute(f"SELECT {i} FROM List WHERE id={id}")
            temp=cur.fetchone()
            data[counter]=extractInfo(temp)
            counter=counter+1
        openModifyMenu(data[1],data[0],data[2],id)
    except Exception as e:
        tkinter.messagebox.showwarning("Warning",e)
    
def extractInfo(info):
    id=str(info)
    res=''
    for i in id:
        if i!='(' and i !=')' and i!=',' and i != "'":
            res=res+i
    return res
#--------------------------------------------------------
#root settings
root=Tk()
root.title("Password Manager")
root.geometry("500x500")
root.resizable(False, False)
#esthetics Font
font_title=("Bebas_Neue",35,"bold")
font_normal=("Bebas_Neue",19)
#colors
background_color="#131f2e"
buttonColor="#1992b6"
root ['bg']='#131f2e'

#----------------------------------------------------------------
#variables
site=StringVar()
username=StringVar()
password=""

#main page
titulo=Label(text="Create Password",bg = background_color,fg = "white",font = font_title)#main title
titulo.place(x=55, y=30)

#user entries label
site_label=Label(text="Web Site:", fg="white", bg = background_color, font=font_normal)
site_label.place(x=50,y=165)
user_label=Label(text="Username:", fg="white", bg = background_color, font=font_normal)
user_label.place(x=40,y=255)
#user entries
site_entry = Entry(textvariable=site,bg="white", font="Bebas_Neue 12")#web site info
user_entry = Entry(textvariable=username,bg="white", font="Bebas_Neue 19")#username
site_entry.place(x=170,y=168, height=30, width=260)
user_entry.place(x=170,y=260, height=30, width=260)

#button for entry
create_password_button = Button(text="Create", width="10", height="1",
                                command=CreatePass,
                                bg="white",font="Bebas_Neue 19 bold")
create_password_button.place(x=175,y=360)
#----------------------------------------------------------------

#menu config
menubar= Menu(root)
root.config(menu=menubar)

#create menu item
CreateMenu=Menu(menubar, tearoff=0)
menubar.add_cascade(label="Create", menu=CreateMenu)
CreateMenu.add_command(label="Create Password", command=HideAllFrames)
CreateMenu.add_separator()
CreateMenu.add_command(label="Add Password", command=OpenAddMenu)

#Search menu
SearchMenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Search", menu=SearchMenu)
SearchMenu.add_command(label="Search Password", command=OpenSearchMenu)
#------------------------------------------------------------------
#creation of frames
#default frame is the "create frame"
add_password_frame= Frame(root, width=500, height=500, bg='#151f56')
verify_password_frame= Frame(root, width=500, height=500, bg='#151f56')
search_password_frame= Frame(root, width=500, height=500, bg='white')
modify_data_frame= Frame(root, width=500, height=500, bg='white')
#------------------------------------------------------------------

root.mainloop()
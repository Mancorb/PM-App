from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import sqlite3
from random import randint
#--------------------------------------------------------
#methods
#UNIVERSAL METHODS
#-------------------------------------------------------------
#Get a new ID for the registry
def getID(cur):
    cur.execute("SELECT id FROM List ORDER BY id;")
    id=cur.fetchall()
    try:
        id=str(id)
        temp=''
        specialChars ="[](),'"
        for specialChar in specialChars:
            id=id.replace(specialChar,'')
        if id=='':
            return 1

        for i in id:
            if i !=' ':
                temp=temp+i
            if i==' ':
                temp=''
        return int(temp)+1
    except Exception as e:
        tkinter.messagebox.showerror("Error",e)
#hide all frames
def HideAllFrames():
    add_password_frame.pack_forget()
    search_password_frame.pack_forget()
    verify_password_frame.pack_forget()
    modify_data_frame.pack_forget()
    delete_data_frame.pack_forget()
    HODB_frame.pack_forget()
#-------------------------------------------------------------

#ADD PASSWORD Methods
#-------------------------------------------------------------
#Open add password menu
def OpenAddMenu():
    HideAllFrames()
    add_password_frame.pack(fill='both', expand=1)
    AddMenuStructure()
#Struture code for the Add Password Menu
def AddMenuStructure():
    backcol=background_color
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
        add_pass_entry.delete(0, END)
        add_user_entry.delete(0, END)
        add_site_entry.delete(0, END)
        CommitComfirm(site_info,user_info,pass_info)
#Notify User data has been saved ---INCOMPLETE---
def CommitComfirm(site_data, user_data, pass_data):
    try:
        con=sqlite3.connect('testbd.db')
        cur=con.cursor()
        id=getID(cur)

        cur.execute(f"INSERT INTO list VALUES('{site_data}','{user_data}','{pass_data}',{id})")
        con.commit()
        con.close()
        tkinter.messagebox.showinfo("Registry created",f"Data:\nSite: {site_data}\nUser: {user_data}\nPass: {pass_data}\nClick ok to continue")
    except Exception as e:
        tkinter.messagebox.showerror("ERROR",f"{e}")
    ReturnToAdd()
#Closes the screen and open the add password menu
def ReturnToAdd():
    HideAllFrames()
    OpenAddMenu()
#-------------------------------------------------------------

#CREATE PASSWORD Methods
#-------------------------------------------------------------
def CreatePass():
    lowerLetters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    UpperLetters=['A', 'B', 'C', 'D', 'E', 'F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    symbols=['|','#','$','&','%','/','-','+','_']
    password=process(lowerLetters,UpperLetters,symbols)
    NoticeCrtPas(password)
#Process to generate the password
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
#-------------------------------------------------------------

#SEARCH PASSWORDS Methods
#-------------------------------------------------------------
#Open search password menu
def OpenSearchMenu():
    HideAllFrames()
    search_password_frame.pack(fill='both', expand=1)
    OpenSearchMenuStructure()
#Structure of the Search menu
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
                    command=lambda:openDeleteMenu(infotable.selection()),
                    font="Bebas_Neue 12")
    deleteB.place(x=400,y=440,width=70)
    #Copy selected
    copyB= Button(search_password_frame,text="Copy Selected",
                    command=lambda:copyRow(infotable.selection()),
                    font="Bebas_Neue 12")
    copyB.place(x=40,y=440, width=160)
    #Edit selected
    editB= Button(search_password_frame,text="Edit",
                    command=lambda:updateRow(infotable.selection()),
                    font="Bebas_Neue 12")
    editB.place(x=300,y=440,width=90)

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
#Search button for the search table
def refresh(inputdata,type,table):
    for i in table.get_children():
        table.delete(i)
    try:
        if inputdata:
            sequence=f"SELECT * FROM list WHERE {type} LIKE '%{inputdata}%' ORDER BY id"
        else: sequence='SELECT * FROM list ORDER BY id'
        isrtDataInTbl(table,sequence)
    except Exception as e:
        tkinter.messagebox.showerror("Error",e)
        isrtDataInTbl(table)
#Inserts the obtained data from the DB into the TKinter table
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
#Hide all screens and open the delete menu screen
def openDeleteMenu(cel):
    if cel:
        HideAllFrames()
        delete_data_frame.pack(fill='both',expand=1)
        cel=extractInfo(cel)
        DeleteMenuStructure(cel)
    else:tkinter.messagebox.showwarning("Warning","Nothing selected")
#Screen used to delete a registry
def DeleteMenuStructure(cel):
    backcol="red"
    #title
    titulo=Label(delete_data_frame,text="WARNING",bg = backcol,fg = "black",font = font_title)#main title
    titulo.place(x=140, y=15)
    
    text=Label(delete_data_frame,
                text="You are about to PERMANENTLY DELETE\nthis PASSWORD and all the related DATA!\nARE YOU SURE?",
                bg = backcol,fg = "black",font = 'Bebas_Neue 18 bold')
    text.place(x=10,y=120)

    #confirm Button
    ConfirmB=Button(delete_data_frame,text="YES", command=lambda:deleteRow(cel), font="Bebas_Neue 19 bold")
    ConfirmB.place(x=350,y=300,height=60, width=130)
    
    #deny Button
    DenyB=Button(delete_data_frame,text="NO",command=ReturnToSearch, font="Bebas_Neue 19 bold")
    DenyB.place (x=20,y=300,height=60, width=130)
#Deletes the selected row from the DB
def deleteRow(id):
    con=sqlite3.connect('testbd.db')
    cur=con.cursor()
    try:
        cur.execute(f"DELETE FROM List WHERE id={id}")
        con.commit()
    except Exception as e:
        tkinter.messagebox.showerror("Error",e)
    con.close()
    ReturnToSearch()
#Copy the password of the selected Row
def copyRow(sel):
    try:
        root.clipboard_clear()
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
        tkinter.messagebox.showerror("Error","Nothing selected")
#Checks if any row is selected to modify
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
        tkinter.messagebox.showwarning("Warning","Nothing selected")
#Hides all screens and shows the modify screen
def openModifyMenu(user,site, pswrd,id):
    HideAllFrames()
    modify_data_frame.pack(fill='both', expand=1)
    ModifyMenuStructure(user,site, pswrd,id)
#Structure of the Modify entry screen
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
    NWsite.place(x=20,y=130, width=370)

    OGuser=Label(modify_data_frame,text='User:',bg = backcol,fg = "black",font= f'Bebas_Neue {size} bold')
    OGuser.place(x=20,y=190)
    NWuser=Entry(modify_data_frame,textvariable=InUser,font=font_normal)
    NWuser.place(x=20,y=240, width=370)

    OGpwrd=Label(modify_data_frame,text='Password:',bg = backcol,fg = "black",font= f'Bebas_Neue {size} bold')
    OGpwrd.place(x=20,y=320)
    NWpass=Entry(modify_data_frame,textvariable=InPwrd,font='Bebas_Neue 10 bold')
    NWpass.place(x=20,y=370,width=370)
    
    #Change Button
    CancelB=Button(modify_data_frame,text="Cancel", command=ReturnToSearch, font="Bebas_Neue 19 bold")
    CancelB.place(x=20,y=410,height=60, width=130)
    #Apply Button
    ConfirmB=Button(modify_data_frame,text="Confirm",command=lambda:NoticeModification(InSite.get(), InUser.get(), InPwrd.get(), user,site, pswrd,id), font="Bebas_Neue 19 bold")
    ConfirmB.place(x=350,y=410,height=60, width=130)
#Notify the user that the data has been modified
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
        cur.execute(f"UPDATE List SET site='{site_data}',user='{user_data}',pass='{pass_data}' WHERE id={id};")
        con.commit()
        tkinter.messagebox.showinfo("UPDATED",'The database has been updated')
    except Exception as e:
        tkinter.messagebox.showerror("Error",e)
    con.close()
    OpenSearchMenu()
#Hides the current screen and shows the search screen again
def ReturnToSearch():
    HideAllFrames()
    OpenSearchMenu()
#delete any format symbols from the SQL result
def extractInfo(info):
    id=str(info)
    res=''
    for i in id:
        if i!='(' and i !=')' and i!=',' and i != "'":
            res=res+i
    return res
#-------------------------------------------------------------

#Hands_On_DataBase Methods
#--------------------------------------------------------
#Hide all screens and open HODB Screen
def OpenHOBDMenu():
    HideAllFrames()
    HODB_frame.pack(fill='both', expand=1)
    HODBMenuStructure()
#Structure of the HODB Screen
def HODBMenuStructure():
    backcol="white"
    command=''
    titulo=Label(HODB_frame,text="Hands on DataBase",bg = backcol,fg = "black",font = font_title)
    titulo.place(x=10, y=5)

    comand=StringVar()
    comandEntry=Entry(HODB_frame,textvariable=comand, bg="white", font="RobotoSlab 12")
    comandEntry.place(x=10,y=70, height=35, width=400)

    #List of options
    var=StringVar()

    RunCommandB= Button(HODB_frame,text="RUN", width="5", height="1",
                        command=lambda:RunComand(comand.get(), var),
                        font="Bebas_Neue 13 bold", fg='white', bg="black")
    RunCommandB.place(x=420, y=70)
    #chat space
    resTxt = Label(HODB_frame,textvariable=var, relief="raised", fg='green', bg='black', width=65,height=22, anchor='n', padx=15, pady=10)
    var.set("--------------------------------------------------------------------------\n--------------------------------------------------------------------------\n--------------\nWRITE AN SQL COMMAND\n--------------")
    resTxt.place(x=6,y=113)
#Check if the command is SELECT or otherwise
def RunComand(comand, conTxt):
    comand=comand.lower()
    if comand=='':
        conTxt.set("--------------------------------------------------------------------------\n--------------------------------------------------------------------------\n--------------\nWRITE A VALID SQL COMMAND\n--------------")
    if 'select' in comand and 'from' in comand:
        result=searchInfo(comand)
    else:
        result=execute(comand)
    txt=adjustText(result)
    conTxt.set("--------------------------------------------------------------------------\n--------------------------------------------------------------------------\n"+txt)
#Run SELECT command in DB and return results
def searchInfo(query):
    con=sqlite3.connect('testbd.db')
    cur=con.cursor()
    try:
        #Run command
        cur.execute(query)

        rows = cur.fetchall()
        return(rows)

    except Exception as e:
        con.close()
        result=f"--ERROR:{e}"
        return result
#Run DB command
def execute(command):
    try:
        con=sqlite3.connect('testbd.db')
        cur=con.cursor()
        cur.execute(command)
        con.commit()
        con.close()
        return(f"{command}\n--Success--")
    except Exception as e:
        con.close()
        result=f"{command}\nERROR:\n{e}"
        return result  
#adjust the command line to match the screen
def adjustText(txt):
    txt=str(txt)
    Result=""
    counter=0
    for i in txt:
        Result=Result+i
        if counter==100 or i==')':
            Result=Result+'\n\n'
            counter = 0
        counter+=1
    return Result

#--------------------------------------------------------

#root settings
root=Tk()
root.title("Password Manager")
root.geometry("500x500")
root.resizable(False, False)
root.iconbitmap("logo_icono.ico")
#esthetics Font
font_title=("Bebas_Neue",35,"bold")
font_normal=("Bebas_Neue",19)
#colors
global background_color
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
menubar.add_cascade(label="Search", command=OpenSearchMenu)
#SearchMenu.add_command(label="Search Password", command=OpenSearchMenu)

#Hands on Database menu
HODBMenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="DataBase",command=OpenHOBDMenu)
#------------------------------------------------------------------
#creation of frames
#default frame is the "create frame"
add_password_frame= Frame(root, width=500, height=500, bg=background_color)
verify_password_frame= Frame(root, width=500, height=500, bg=background_color)
search_password_frame= Frame(root, width=500, height=500, bg='white')
modify_data_frame= Frame(root, width=500, height=500, bg='white')
delete_data_frame= Frame(root, width=500, height=500, bg='red')
HODB_frame=Frame(root, width=500, height=500, bg='white')
#------------------------------------------------------------------

root.mainloop()
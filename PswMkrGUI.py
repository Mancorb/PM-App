from tkinter import *
import tkinter.messagebox
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
    tkinter.messagebox.showinfo("Registry created",f"Data:\nSite: {site_data}\nUser: {user_data}\nPass: {pass_data}\nClick ok to continue")
    HideAllFrames()
    
#Open search password menu
def OpenSearchMenu():
    HideAllFrames()
    search_password_frame.pack(fill='both', expand=1)
    
#hide all frames
def HideAllFrames():
    print("All frames are hidden")
    add_password_frame.pack_forget()
    search_password_frame.pack_forget()
    verify_password_frame.pack_forget()
#click command
def dummy():
    pass

#password created notification
def NoticeCrtPas(password):

    user_info=username.get()
    site_info=site.get()

    if site_info!="" or user_info!="":
        tkinter.messagebox.showinfo("Password created",f"Your password:{password} has been\nadded to the data base")
        site_entry.delete(0, END)
        user_entry.delete(0, END)
    else:
        tkinter.messagebox.showerror("Error",f"Please fill in the site and user data")



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
create_password_button = Button(text="Create", width="10", height="1", command=lambda:NoticeCrtPas(password), bg="white",font="Bebas_Neue 19 bold")
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
#------------------------------------------------------------------



root.mainloop()
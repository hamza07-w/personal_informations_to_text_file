from tkinter import *
from PIL import ImageTk, Image 
from tkinter import messagebox
root = Tk()
root.title("informations ")
root.iconbitmap('c:/img/man.ico')
root.geometry("800x610")
"""
head = Label(root, text="     save your all informations in a text file", heigh=3, font=("Arial", 15))
head.grid(row=0, column=0)
"""
bg_n = "blue"
# loading the image 
icon_username = ImageTk.PhotoImage(Image.open("c:/img/usern.ico")) 
# reading the image 
panel_user = Label(root, image = icon_username)
panel_user.grid(row=1, column=0)
txt_icon = ImageTk.PhotoImage(Image.open("c:/img/txt.ico"))
panel_txt = Label(root, image = txt_icon)
panel_txt.grid(row=1, column=1)
first_name = Label(root, text="First Name:", heigh=3, font=("Arial", 15))
first_name.grid(row=2, column=0)
fname_data = StringVar()
fname_input = Entry(root, width=25, font=("Arial", 12), textvariable=fname_data, borderwidth=3, bg=bg_n, fg="white")
fname_input.grid(row=2, column=1)
last_name = Label(root, text="Last Name:", heigh=3, font=("Arial", 15))
last_name.grid(row=3, column=0)
last_data = StringVar()
last_input = Entry(root, width=25, font=("Arial", 12), textvariable=last_data, borderwidth=3, bg=bg_n, fg="white")
last_input.grid(row=3, column=1)

email = Label(root, text="Email:", heigh=3, font=("Arial", 15))
email.grid(row=4, column=0)
email_data = StringVar()
email_input = Entry(root, width=25, font=("Arial", 12), textvariable=email_data, borderwidth=3, bg=bg_n, fg="white")
email_input.grid(row=4, column=1)
nember = Label(root, text="phone nember:", heigh=3, font=("Arial", 15))
nember.grid(row=5, column=0)
nem_data = StringVar()
nem_input = Entry(root, width=25, font=("Arial", 12), textvariable=nem_data, borderwidth=3, bg=bg_n, fg="white")
nem_input.grid(row=5, column=1)

def submit():
	
	a = False
	b = False
	c = False
	d = False
	
	get_name = fname_input.get()
	if len(get_name) <=12 and len(get_name) >= 1:
		a =True
		
	get_last = last_input.get()
	if len(get_last) <=12 and len(get_last) >= 1:
		b = True
		
	get_email = email_input.get()
	if get_email[:10] == "@gmail.com":
		c = True
		
	get_nember = nem_input.get()
	if len(get_nember) == 10:
		d = True
		
	if a and b and d:
		with open(get_name+".txt" , "w") as file:
			f=file.write(f"{get_name}\n{get_last}\n{get_email}\n{get_nember}\n")
			
	else:
		
		msg = "length error."
		messagebox.showinfo("sorry!", " ".join(msg))




subm = Button(root, text="SUMBMIT", heigh=2, font=("Arial", 10), bg="black", fg="white", command=submit)
subm.grid(row=6, column=0)




root.mainloop()

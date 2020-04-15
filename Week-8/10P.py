from tkinter import *
root= Tk()

idli = IntVar()
dosa = IntVar()
puri = IntVar()
vada = IntVar()
palav = IntVar()
biryani = IntVar()

def var_states():
   a=idli.get()
   b=dosa.get()
   c=puri.get()
   d=vada.get()
   e=palav.get()
   f=biryani.get()
   root1 = Tk()
   root1.geometry("200x200")
   cost = a*15 + b*50 + c*35 + d*15 + e*45 + f*120
   Label(root1, text="the cost was : "+str(cost),justify = CENTER,padx = 20).pack()


root.geometry("500x500") 
Label(root, text="Simple Restaurant menu :",justify = CENTER,padx = 20).pack()
Label(root, text="",justify = CENTER,padx = 20).pack()

Label(root, text="ITEM",justify = CENTER,padx = 40).place(relx = 0.1, rely = 0.1)
Label(root, text="PRICE",justify = CENTER,padx = 40).place(relx = 0.5, rely = 0.1)

Checkbutton(root, text="IDLI",padx = 20, variable=idli).place(relx = 0.1, rely = 0.17)
Label(root, text="Rs. 15",justify = CENTER,padx = 40).place(relx = 0.5, rely = 0.17)

Checkbutton(root,text="MASALA DOSA", padx = 20,  variable=dosa).place(relx = 0.1, rely = 0.23)
Label(root, text="Rs. 50",justify = CENTER,padx = 40).place(relx = 0.5, rely = 0.23)

Checkbutton(root,text="PURI", padx = 20,  variable=puri).place(relx = 0.1, rely = 0.29)
Label(root, text="Rs. 35",justify = CENTER,padx = 40).place(relx = 0.5, rely = 0.29)

Checkbutton(root,text="VADA", padx = 20,  variable=vada).place(relx = 0.1, rely = 0.35)
Label(root, text="Rs. 15",justify = CENTER,padx = 40).place(relx = 0.5, rely = 0.35)

Checkbutton(root,text="PALAV", padx = 20,  variable=palav).place(relx = 0.1, rely = 0.41)
Label(root, text="Rs. 45",justify = CENTER,padx = 40).place(relx = 0.5, rely = 0.41)

Checkbutton(root,text="BIRYANI", padx = 20,  variable=biryani).place(relx = 0.1, rely = 0.47)
Label(root, text="Rs. 120",justify = CENTER,padx = 40).place(relx = 0.5, rely = 0.47)

Button(root, text='Quit', command=root.quit).place(relx = 0.20, rely = 0.60)
Button(root, text='Submit', command=var_states).place(relx = 0.40, rely = 0.60)

root.mainloop()

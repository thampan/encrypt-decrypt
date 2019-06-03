 #****************************************************************************
 #* Filename        : crypto.py
 #* Description     : See associated readMe
 #* Author          : Jishnu M Thampan
 #****************************************************************************

import pyAesCrypt
import os
from tkinter import *
from tkinter import messagebox

bufferSize = 128 * 1024

fileList=[]#Specify the needed files here

def encrypt():
   password = e1.get();
   try:
       for file in fileList:
           pyAesCrypt.encryptFile(file, file+".encrypted", password, bufferSize)
           os.remove(file)
       messagebox.showinfo("Info", "Successfully Encrypted!")
       master.destroy()
   except:
       messagebox.showerror ("Error", "Exception occured!")
       master.destroy()


def decrypt():
    password = e1.get();
    try:
        for file in fileList:
            pyAesCrypt.decryptFile(file+".encrypted", file, password, bufferSize)
            os.remove(file+".encrypted")
        messagebox.showinfo("Info", "Successfully Decrypted!")
        master.destroy()
    except:
        messagebox.showerror ("Error", "Exception occured!")
        master.destroy()

master = Tk()
Label(master, text="Password").grid(row=0)

e1 = Entry(master)
e1.grid(row=0, column=1)

Button(master, text='Encrypt', command=encrypt).grid(row=6, column=0, sticky=W, pady=4)
Button(master, text='Decrypt', command=decrypt).grid(row=6, column=5, sticky=W, pady=4)

mainloop( )

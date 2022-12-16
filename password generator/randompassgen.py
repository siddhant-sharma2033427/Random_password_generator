#module to work with random numbers or random choices
import random
#module to create gui
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
#to work with clipboard
import pyperclip


#creating global root variable for all functions
root = tk.Tk()
#adding title to software
root.title("password generator")
#PhotoImage use to open image to be used in gui
iconimg = tk.PhotoImage(file = "ico.png")
#iconphoto is a function to add logo in our tkinter window
root.iconphoto(True, iconimg)#if first value is true then same logo will appear in all window
#class to generate password
class generator:
    def __init__(self,root):
        self.root = root
        #frame to password generator 
        self.frame1 = tk.Frame(self.root)
        self.frame1.grid(row = 0,column = 0)
        self.label = tk.Label(self.frame1,text = "password generator")
        self.label.grid(row = 0,column = 0,sticky="w")
        
        #fram for entry widgit and button
        self.frame2 = tk.Frame(self.root)
        self.frame2.grid(row = 1,column = 0,sticky="w")
        
        #inputing length of passord
        self.enterlen = tk.Label(self.frame2,text = "Enter length of password: ")
        self.enterlen.grid(row = 0,column =0,sticky="w")
        
        self.max_len = tk.IntVar()
        self.max_len_entry = tk.Entry(self.frame2,textvariable=self.max_len)
        self.max_len_entry.grid(row = 0,column = 1)
        self.max_len_entry.delete(0,'end')
        
        #outputting passord to user
        tk.Label(self.frame2,text = "Generated Password:").grid(row = 1,column = 0,sticky = "w")
        self.output_text = tk.StringVar()
        self.output_entry = tk.Entry(self.frame2,textvariable = self.output_text)
        self.output_entry.grid(row = 1,column = 1,sticky = "w")
        photo = tk.PhotoImage(file = "copytoclip.png")
        self.clip_btn = ttk.Button(self.frame2,image = photo,command = self.copytoclip)
        self.clip_btn.grid(row = 1,column = 2,sticky = "w")

        #variable for Entry widget
        self.include_numbers = tk.IntVar()
        self.include_lower_char = tk.IntVar()
        self.include_upper_char = tk.IntVar()
        self.include_special_char = tk.IntVar()
        
        checkbtn_1 = ttk.Checkbutton(self.frame2,variable = self.include_numbers,text = "Include numbers")
        checkbtn_1.grid(row = 2,column = 0,sticky="w")
        checkbtn_1.invoke()
        checkbtn_2 = ttk.Checkbutton(self.frame2,variable = self.include_lower_char,text = "Include lower case characters")
        checkbtn_2.grid(row =3,column = 0,sticky="w")
        checkbtn_2.invoke()
        checkbtn_3 = ttk.Checkbutton(self.frame2,variable = self.include_upper_char,text = "Include upper case characters")
        checkbtn_3.grid(row = 4,column = 0,sticky="w")
        checkbtn_3.invoke()
        checkbtn_4 = ttk.Checkbutton(self.frame2,variable = self.include_special_char,text = "Include symbols")
        checkbtn_4.grid(row = 5,column = 0,sticky="w")
        checkbtn_4.invoke()
        
        #generate button
        self.button = ttk.Button(self.frame2,text = "Generate",command = lambda : self.passgen(self.max_len))
        self.button.grid(row = 6,column =0,sticky="w")
        
        self.root.mainloop()
    #this function generate random number and return it.
    def numgen(self):
        #random number will be generated from below list
        DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        rand_digit = random.choice(DIGITS)
        return rand_digit
    #This function generate random lowercase letter and return it.
    def lowerchargen(self):
         #random lowercase letter will be generated from below list
        LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                            'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                            'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                            'z']
        rand_lower = random.choice(LOCASE_CHARACTERS)
        return rand_lower
    #This function generate random uppercase letter and return it.
    def upperchargen(self):
        #random uppercase letter will be generated from below list
        UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                            'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                            'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                            'Z']
        rand_upper = random.choice(UPCASE_CHARACTERS)
        return rand_upper
     #This function generate random sysmbols letter and return it.
    def symgen(self):
        #random symbols letter will be generated from below list
        SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
                '*', '(', ')', '<']
        rand_symbol = random.choice(SYMBOLS)
        return rand_symbol
    #this function is a main part of the program where
    #random password will be generated
    def passgen(self,max_len):
        password = ""
        count = 0
        #if there is no tick in check box then it will produce error
        try:
            #getting atleast one character from each condition
            if(self.include_numbers.get() == 1):
                #calling function for random number
                password+=self.numgen()
                count+=1
            if(self.include_lower_char.get() == 1):
                 #calling function for random lower character
                password+=self.lowerchargen()
                count+=1
            if(self.include_upper_char.get() == 1):
                 #calling function for random uppercase
                password+=self.upperchargen()
                count+=1
            if(self.include_special_char.get() == 1):
                 #calling function for random special symbol
                password+=self.symgen()
                count+=1
            #to ensure that there is no error in following line(it can produce error in some conditions)
            try:
                #getting passowrd length that user want 
                max_len = max_len.get()
                #subtracting 'count' from total length as lenth 'count' password already generated
                max_len = max_len-count
                i=0
                #generating remaning passowrd
                while(i < max_len):
                    if(self.include_numbers.get() == 1 and i < max_len):
                        password+=self.numgen()
                        i+=1
                    if(self.include_lower_char.get() == 1 and i < max_len):
                        password+=self.lowerchargen()
                        i+=1
                    if(self.include_upper_char.get() == 1 and i < max_len):
                        password+=self.upperchargen()
                        i+=1
                    if(self.include_special_char.get() == 1 and i < max_len):
                        password+=self.symgen()
                        i+=1
                
            except Exception as e:
                pass
            #converting string into list using list comprihension
            templis = [i for i in password]
            #shuffling elements of templist ie final password
            random.shuffle(templis)
            password = ""
            #converting linst into string
            for i in templis:
                password+=i
            #deleting any element from generated password field in gui
            self.output_entry.delete(0,"end")
            #adding final password into generated passowrd field in gui
            self.output_entry.insert(0,password)
            
        except:
            pass
    def copytoclip(self):
        #adding passord to clipboard
        pyperclip.copy(self.output_text.get())
obj = generator(root)

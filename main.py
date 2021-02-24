from tkinter import *
import pyperclip
from tkinter import font
from tkinter import filedialog
from functools import partial

#function to change selected region style BOLD
def textBold():
    boldFont = font.Font(textBox, textBox.cget("font"))
    boldFont.configure(weight="bold")

    textBox.tag_configure("bold", font=boldFont)

    currentTags = textBox.tag_names("sel.first")

    if "bold" in currentTags:
        textBox.tag_remove("bold", "sel.first", "sel.last")
    else:
        textBox.tag_add("bold", "sel.first", "sel.last")
    return None

#function to change selected region style ITALIC
def textItalic():
    #get font of textbox
    italicFont = font.Font(textBox, textBox.cget("font"))
    #change font to style italic
    italicFont.configure(slant="italic")

    textBox.tag_configure("italic", font=italicFont)

    currentTags = textBox.tag_names("sel.first")

    if "italic" in currentTags:
        textBox.tag_remove("italic", "sel.first", "sel.last")
    else:
        textBox.tag_add("italic", "sel.first", "sel.last")
    return None

#function to COPY user text to clipboard
def textCopy():
    selection = textBox.selection_get()
    copy = pyperclip.copy(selection)
    #write code to copy text to clipboard
    return None

#function to CUT user text from textfield and COPY it to clipboard

def textCut():
        selection = textBox.selection_get()
        copy = pyperclip.copy(selection)
        delete = textBox.delete("sel.first", "sel.last")
   
    #function to SAVE document as txt file
def textSave():
    userText = textBox.get("1.0", "end-1c")
    newFile = filedialog.asksaveasfilename(initialdir="../desktop/textfiles", title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    newFile = open(newFile, "w")
    newFile.write(userText)
    newFile.close()

    #write code to save text
    return None


root = Tk()
frame = Frame(root, highlightbackground='red', height=2, width=450)
frame.grid(row=0, column=0, columnspan=5, padx=20, pady=0)
root.geometry("450x450+450+450")


#highLighted = pyperclip.copy(userInput)


#Font editing labels(top of screen)
bold = Button(frame, text='B', command=textBold)
italic = Button(frame, text='I', command=textItalic)
copy = Button(frame, text='C', command=textCopy)
cut = Button(frame, text='cut', command=textCut)


#binders
bold.bind('<B1-Motion>', textBold)
italic.bind('<B1-Motion>', textItalic)


#(bottom of screen)

#save button
save = Button(root, text='Save', command=textSave)


#file name entry field
#v = StringVar()
#fileNameLabel = Label(root, text='File Name')
#fileNameEntry = Entry(root, textVariable=v)

#textbox box and formating
textBox = Text(root, height=25, width=62)

#Placing buttons on the screen
bold.grid(row=0, column=0, padx=1, sticky=NSEW,)
italic.grid(row=0, column=1, padx=1, sticky=NSEW,)
copy.grid(row=0, column=2, padx=1, sticky=NSEW,)
cut.grid(row=0, column=3, padx=1, sticky=NSEW,)
save.grid(row=7, column=2, padx=1, sticky=W,)

#Placing text box on the screen
textBox.grid(row=1, column=0, columnspan=5, rowspan=4, padx=4, pady=6)

root.mainloop()

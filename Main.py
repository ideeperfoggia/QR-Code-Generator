import qrcode
import qrcode.image.svg
from qrcode.image.pure import PyPNGImage
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tksvg
from PIL import ImageTk, Image
import os

#Creating the window
win = Tk()
win.title('QR Code Generator')
win.geometry('650x950')
win.config(bg='DarkTurquoise')

#Function to generate the QR code and save it
def generateCode():
    #Select an appropriate factory
    if fileFormat.get() == 'SVG':
        factory = qrcode.image.svg.SvgImage
        format = ".svg"
    else:
        factory = PyPNGImage
        format = ".png"
    #Creating a QRCode object of the size specified by the user
    
    # qr = qrcode.QRCode(version = size.get(),box_size = 10,border = 5, image_factory=factory) 

    qr = qrcode.QRCode(image_factory=factory) 
    qr.add_data(text.get()) #Adding the data to be encoded to the QRCode object
    qr.make(fit = True) #Making the entire QR Code space utilized
    img = qr.make_image() #Generating the QR Code
    fileDir=loc.get()+'\\'+name.get() #Getting the directory where the file has to be save
    finalDir=fileDir + format
    img.save(f'{finalDir}') #Saving the QR Code

    # Showing the successful saving of the QR Code
    FrameImg = Frame(win,bg="DarkTurquoise")
    FrameImg.place(relx=0.1,rely=0.5,relwidth=0.7,relheight=0.4)
    
    successLabel = Label(FrameImg,text="QR Code is saved successfully!",bg="DarkTurquoise",fg='azure',font=('FiraMono',14,'bold'))
    successLabel.place(relx=0.05,rely=0.1, relheight=0.08)

    if fileFormat.get() == 'SVG':
        svgImage = tksvg.SvgImage(file=finalDir, scaletoheight = 250)
        panel = Label(FrameImg, image=svgImage)
        panel.place(relx=0.05,rely=0.2)
    else:
        openedImage = Image.open(finalDir)
        openedImage = openedImage.resize((250,250))
        photoImage = ImageTk.PhotoImage(openedImage)
        panel = Label(FrameImg, image=photoImage)
        panel.image = photoImage
        panel.place(relx=0.05,rely=0.2)

    
#Label for the window
headingFrame = Frame(win,bg="azure",bd=5)
headingFrame.place(relx=0.15,rely=0.05,relwidth=0.7,relheight=0.05)
headingLabel = Label(headingFrame, text="Generate QR Code", bg='azure', font=('Times',12,'bold'))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

#Taking the input of the text or URL to get QR code 
Frame1 = Frame(win,bg="DarkTurquoise")
Frame1.place(relx=0.1,rely=0.1,relwidth=0.7,relheight=0.2)
    
label1 = Label(Frame1,text="Enter the text/URL: ",bg="DarkTurquoise",fg='azure',font=('FiraMono',13,'bold'))
label1.place(relx=0.05,rely=0.2, relheight=0.08)

text = Entry(Frame1,font=('Century 12'))
text.place(relx=0.05,rely=0.3, relwidth=1, relheight=0.2)

#Getting input of the location to save QR Code
Frame2 = Frame(win,bg="DarkTurquoise")
Frame2.place(relx=0.1,rely=0.2,relwidth=0.7,relheight=0.2)

label2 = Label(Frame2,text="Enter the location to save the QR Code: ",bg="DarkTurquoise",fg='azure',font=('FiraMono',13,'bold'))
label2.place(relx=0.05,rely=0.2, relheight=0.08)

loc = Entry(Frame2,font=('Century 12'))
loc.place(relx=0.05,rely=0.3, relwidth=1, relheight=0.2)

#Getting input of the QR Code image name 
Frame3 = Frame(win,bg="DarkTurquoise")
Frame3.place(relx=0.1,rely=0.3,relwidth=0.7,relheight=0.2)

label3 = Label(Frame3,text="Enter the name of the QR Code: ",bg="DarkTurquoise",fg='azure',font=('FiraMono',13,'bold'))
label3.place(relx=0.05,rely=0.2, relheight=0.08)

name = Entry(Frame3,font=('Century 12'))
name.place(relx=0.05,rely=0.3, relwidth=1, relheight=0.2)

#Getting the file format of the QR Code
Frame4 = Frame(win,bg="DarkTurquoise")
Frame4.place(relx=0.1,rely=0.4,relwidth=0.7,relheight=0.2)

label5 = Label(Frame4,text="Enter the format of the QR Code: ",bg="DarkTurquoise",fg='azure',font=('FiraMono',13,'bold'))
label5.place(relx=0.05,rely=0.2, relheight=0.08)

fileFormat = StringVar()
fileFormatCombo = ttk.Combobox(Frame4, textvariable=fileFormat)
fileFormatCombo['values'] = ('SVG', 'PNG')
fileFormatCombo.place(relx=0.05,rely=0.3, relwidth=0.95, relheight=0.2)
fileFormatCombo.current(0) 

# #Getting the input of the size of the QR Code
# Frame5 = Frame(win,bg="DarkTurquoise")
# Frame5.place(relx=0.1,rely=0.5,relwidth=0.7,relheight=0.2)

# label5 = Label(Frame5,text="Enter the size from 1 to 40 with 1 being 21x21: ",bg="DarkTurquoise",fg='azure',font=('FiraMono',13,'bold'))
# label5.place(relx=0.05,rely=0.2, relheight=0.08)

# size = Entry(Frame5,font=('Century 12'))
# size.place(relx=0.05,rely=0.3, relwidth=1, relheight=0.2)

#Button to generate and save the QR Code
button = Button(win, text='Generate Code',font=('FiraMono',15,'normal'),command=generateCode)
button.place(relx=0.35,rely=0.9, relwidth=0.25, relheight=0.05)

#Runs the window till it is closed manually
win.mainloop()
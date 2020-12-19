from pytube import YouTube

from tkinter import *

root= Tk()

root.geometry("400x500")
root.title("Youtube video downloader")


label1 = Label(root,text="YouTube Video Link",fg="#D51E23",font=("bold",20))
label1.place(x=60,y=50)


mylink = StringVar()
pastelink = Entry(root,textvariable=mylink,width=50)
pastelink.place(x=50,y=120)


def downloadvideo():
    link = (mylink.get())
    ytvideo = YouTube(link).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    
    ytvideo.download(r"C:\Users\nayan tolani\Desktop\coding")
    print("DOWNLOADING YOUR VIDEO")

b1 = Button(root,text="Download",command=downloadvideo,bg="#A23034",width=30,
            fg="black",height=2)
b1.place(x=80,y=160)

root.mainloop()
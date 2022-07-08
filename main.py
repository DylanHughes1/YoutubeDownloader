from tkinter import *
from tkinter import messagebox as MessageBox
from pytube import YouTube

def download():
    url = YouTube(str(link.get()))
    video = url.streams.get_highest_resolution()
    video.download()
    Label(window, text="Video Descargado", font="calibri 14").place(x=180, y=200)


def initRoot():
    root = Tk()
    root.geometry('500x300')
    root.resizable(0, 0)  # makes the window adjustable with its features
    root.title('Youtube Downloader')
    return root


def initLabels():
    Label(window, text="Descarga videos de Youtube gratis", font='calibri 16 bold').pack()
    link = StringVar()  # Specifying the variable type
    Label(window, text="Pega tu link aca padre", font='calibri 15 bold').place(x=150, y=55)
    link_enter = Entry(window, width=70, textvariable=link).place(x=30, y=85)
    return link


def popup():
    MessageBox.showinfo("Sobre mi", " Pagina de Github: https://github.com/DylanHughes1")


window = initRoot()
link = initLabels()

menubar = Menu(window)
window.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Mas informacion", menu=helpmenu)
helpmenu.add_command(label="Sobre el autor", command=popup)
menubar.add_command(label="Salir", command=window.destroy)

Button(window, text='Descargar', font='san-serif 16 bold', bg='lightblue', padx=2, command=download).place(x=190, y=150)

window.mainloop()

import speedtest
from tkinter.ttk import *
from tkinter import * 
import threading
import tkinter as tk

root = tk.Tk()
root.title("Medidor de Velocidad de Internet")
root.geometry('450x220')
root.resizable(False, False)
root.configure(bg="#ffffff")
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='/home/darkphoenix/Desktop/Curso Hacking con Python_Tectroya_Youtube/speed.gif'))

# Diseñando la Etiqueta
Label(root, text = 'VELOCIDAD DE INTERNET', bg='#ffffff', fg='#404042' , font = 'arial 25 bold').pack()
Label(root, text = 'BY: @darkphoenix87_ethical_hacking', bg='#fff', fg='#404042', font = 'arial 15 bold').pack(side =BOTTOM)

# Haciendo la Etiqueta para mostrar la Velocidad de Internet
bajar_etiqueta = Label(root, text = "Velocidad de Descarga - ", bg='#fff', fg = 'blue', font = 'arial 10 bold')
bajar_etiqueta.place(x = 90, y = 50)
subir_etiqueta = Label(root, text = "Velocidad de Subida - ", bg='#fff', fg = 'blue', font = 'arial 10 bold')
subir_etiqueta.place(x = 90, y = 80)

# Funcion para comprobar la velocidad
def Comprobar_velocidad():
    global velocidad_descarga, velocidad_subida
    prueba_velocidad = speedtest.Speedtest()
    descarga = prueba_velocidad.download()
    subida = prueba_velocidad.upload()

    velocidad_descarga = round(descarga / (10 ** 6), 2)
    velocidad_subida = round(subida / (10 ** 6), 2)

# Funcion para la Barra de Progreso y Actualizar el Texto
def Actualizar_texto():
    hilo = threading.Thread(target = Comprobar_velocidad, args = ())
    hilo.start()
    progreso = Progressbar(root, orient = HORIZONTAL, length = 210, mode = 'indeterminate')
    progreso.place(x = 85, y = 110)
    progreso.start()
    while hilo.is_alive():
        root.update()
        pass
    bajar_etiqueta.config(text = "Velocidad de Descarga - " + str(velocidad_descarga) + "Mbps")
    subir_etiqueta.config(text = "Velocidad de Subida - " + str(velocidad_subida) + "Mbps")

    progreso.stop()
    progreso.destroy()

# Boton para llamar a la Funcion
boton = Button(root, text = "Comprobar Velocidad", width = 30, bd = 0, bg = '#404042', fg = '#fff', pady = 5, command = Actualizar_texto)
boton.place(x = 85, y = 140)
root.mainloop()
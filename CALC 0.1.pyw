# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 12:52:59 2020

@author: frua

"""
from tkinter import *

raiz=Tk()

miFrame=Frame()
miFrame.pack()

#PANTALLA##################################################################

pantalla=Entry(miFrame)
pantalla.grid(row=0, column=0, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="white", justify="right", text="0")

#BOTONES##################################################################
#Fila1
boton7=Button(miFrame, text="7", width=3)
boton7.grid(row=1, column=0, padx=10, pady=10)
boton8=Button(miFrame, text="8", width=3)
boton8.grid(row=1, column=1, padx=10, pady=10)
boton9=Button(miFrame, text="9", width=3)
boton9.grid(row=1, column=2, padx=10, pady=10)
botonX=Button(miFrame, text="X", width=3)
botonX.grid(row=1, column=3, padx=10, pady=10)
#Fila2
boton4=Button(miFrame, text="4", width=3)
boton4.grid(row=2, column=0, padx=10, pady=10)
boton8=Button(miFrame, text="5", width=3)
boton8.grid(row=2, column=1, padx=10, pady=10)
boton9=Button(miFrame, text="6", width=3)
boton9.grid(row=2, column=2, padx=10, pady=10)
botonDIVIDIR=Button(miFrame, text="/", width=3)
botonDIVIDIR.grid(row=2, column=3, padx=10, pady=10)
#Fila3
boton1=Button(miFrame, text="1", width=3)
boton1.grid(row=3, column=0, padx=10, pady=10)
boton2=Button(miFrame, text="2", width=3)
boton2.grid(row=3, column=1, padx=10, pady=10)
boton3=Button(miFrame, text="3", width=3)
boton3.grid(row=3, column=2, padx=10, pady=10)
botonSUMA=Button(miFrame, text="+", width=3)
botonSUMA.grid(row=3, column=3, padx=10, pady=10)
#Fila4
botonCOMA=Button(miFrame, text=",", width=3)
botonCOMA.grid(row=4, column=0, padx=10, pady=10)
boton0=Button(miFrame, text="0", width=3)
boton0.grid(row=4, column=1, padx=10, pady=10)
botonIGUAL=Button(miFrame, text="=", width=3)
botonIGUAL.grid(row=4, column=2, padx=10, pady=10)
botonRESTA=Button(miFrame, text="-", width=3)
botonRESTA.grid(row=4, column=3, padx=10, pady=10)

raiz.mainloop()


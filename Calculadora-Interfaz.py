# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 12:52:59 2020

@author: frua

"""
###############################################################################

from tkinter import *
from tkinter import messagebox
from datetime import date
#import tkinter as tk
import tkinter.font as tkFont
import math
#import sqlite3

#RAIZ##########################################################################

raiz=Tk()
raiz.title("Calculadora")
#cambiando 0 1 podes activar o desactivar el ajuste de la ventana en ambas direcciones
raiz.resizable(0,0)
#Icono de la ventana del programa
raiz.iconbitmap("pene.ico")
#Frame_uno es el marco adentro de la ventana principal (creo que se pueden meter varios)
#en una misma ventana
Frame_uno=Frame()
Frame_uno.pack()
Frame_uno.config(bg="green",width="650", height="500")


#FUNCIONES MENU################################################################

def crear_BBSS():
      x=5
#        try:

#            miConexion=sqlite3.connect("BBDD-CALCULADORA")
#
#            miCursor=miConexion.cursor()
#
#            miCursor.execute("""
#                    CREATE TABLE DATOSGUARDADOS (
#                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
#                    VALOR FLOAT(10,6),
#                    COMENTARIO VARCHAR(200),
#                    FECHA DATE)
#                    """)
#
#            miConexion.commit()
#            miCursor.close()
#            miConexion.close()
#
#            messagebox.showinfo("BBDD", "La base de datos se creo con éxito")
#
#        except:
#
#            messagebox.showinfo("BBDD", "La base de datos ya fue creada")
#
def guardar(num):
    
    valor_pantalla=num
    
    #RAIZ Y MARCO##############################################################
    
    raizguardar=Tk()
    raizguardar.title("Guardar")
    #raizguardar.resizable(0,0)
    raizguardar.iconbitmap("pene.ico")
    
    Frame_Guardar=Frame(raizguardar)
    Frame_Guardar.pack()
    
    
    fontStyleBBDD = tkFont.Font(family="Lucida Grande", size=5)
    fontStyleBBDDdos = tkFont.Font(family="Lucida Grande", size=1)

    #DISEÑO ID PARA ACTUALIZAR##############################################
    
    etiqueta_id=Label(Frame_Guardar, text="ID (SOLO PARA ACTUALIZAR): ")
    etiqueta_id.grid(row=0, column=0, padx=3, pady=3, sticky="e")
    etiqueta_id.config(justify="center")
    
    textoID=Text(Frame_Guardar, width=4, height=1)
    textoID.grid(row=0, column=1, padx=3, pady=3)
    textoID.config(font=fontStyleBBDD)

    #DISEÑO CAMPO VALOR#####################################################

    etiqueta_valor=Label(Frame_Guardar, text="Valor a guardar: ")
    etiqueta_valor.grid(row=1, column=0, padx=3, pady=3, sticky="e")
    etiqueta_valor.config(justify="center")
    
    etiqueta_valoraguardar=Label(Frame_Guardar, text=valor_pantalla)
    etiqueta_valoraguardar.grid(row=1, column=1, padx=3, pady=3)
    etiqueta_valoraguardar.config(justify="center", font=fontStyleBBDD)
    
    #NO LOGRO HACER QUE APAREZCA EL VALOR DE LA PANTALLA EN EL ENTRY
    #valor_pantalla=StringVar()
    #campo_valor=Entry(Frame_Guardar, textvariable=valor_pantalla, width=14)
    #campo_valor.grid(row=1, column=1, padx=3, pady=3, columnspan=2)
    #campo_valor.config(justify="center", font=fontStyleBBDD)

    #DISEÑO CAMPO COMENTARIO##################################################

    etiqueta_comentario=Label(Frame_Guardar, text="Comentario: ")
    etiqueta_comentario.grid(row=3, column=0, padx=3, pady=3, sticky="e")
    
    textoComentarios=Text(Frame_Guardar, width=16, height=7)
    textoComentarios.grid(row=3, column=1, padx=3, pady=3)
    barrascroll=Scrollbar(Frame_Guardar, command=textoComentarios.yview)
    barrascroll.grid(row=3, column=2, padx=3, sticky="nsew")
    textoComentarios.config(yscrollcommand=barrascroll.set)
    
    #DISEÑO CAMPO FECHA#######################################################
    
    etiqueta_fecha=Label(Frame_Guardar, text="Fecha: ")
    etiqueta_fecha.grid(row=4, column=0, padx=3, pady=3, sticky="e")
    
    valor_fecha=date.today()
    etiqueta_valorfecha=Label(Frame_Guardar, text=valor_fecha)
    etiqueta_valorfecha.grid(row=4, column=1, padx=3, pady=3)

    #DISEÑO BOTONES############################################################
    
    Frame_BotonesGuardar=Frame(raizguardar)
    Frame_BotonesGuardar.pack()
    
    botonGuardar=Button(Frame_BotonesGuardar, text="GUARDAR", command=lambda:guardar_valor())
    botonGuardar.grid(row=0, column=0, padx=3, pady=3, sticky="w")
    
    botonSalir=Button(Frame_BotonesGuardar, text="ACTUALIZAR",command=lambda:actualizar())
    botonSalir.grid(row=0, column=3, padx=3, pady=3, sticky="e")    
    
    
    #FUNCIONES BOTONES#########################################################
    
    def guardar_valor():
        x=5
#        try:
#
#            miConexion=sqlite3.connect("BBDD-CALCULADORA")
#
#            miCursor=miConexion.cursor()
#
#            info_insertar=(valor_pantalla, textoComentarios.get("1.0",END),valor_fecha)
#
#            miCursor.execute("INSERT INTO DATOSGUARDADOS VALUES (NULL,?,?,? )", info_insertar)
#
#            miConexion.commit()
#            miCursor.close()
#            miConexion.close()
#
#            messagebox.showinfo("BBDD", "Se agrego la información a la BBDD")
#
#        except:
#
#            messagebox.showinfo("BBDD", "Error, no se pudo agregar info a la BBDD")
#
    def actualizar():
        x=5
#
#        try:
#
#            miConexion=sqlite3.connect("BBDD-CALCULADORA")
#
#            miCursor=miConexion.cursor()
#
#            #OTRA OPCION (CREO QUE MENOS SEGURA, ALGO DECIA EN UN VIDEO)
#            #miCursor.execute("UPDATE DATOSGUARDADOS SET COMENTARIO='" + str(textoComentarios.get("1.0",END))+"' WHERE ID=" + str(textoID.get("1.0",END)))
#
#            info_actualizar=(str(textoComentarios.get("1.0",END)),str(textoID.get("1.0",END)))
#            #ESTE OTRO METODO SE LLAMA SEGUN ME PARECE, CONSULTA PARAMETRIZADA (Y PARACE SER MAS SEGURO QUE EL DE ARRIBA)
#            miCursor.execute("UPDATE DATOSGUARDADOS SET COMENTARIO=? WHERE ID=?", info_actualizar)
#
#            miConexion.commit()
#
#            miCursor.close()
#            miConexion.close()
#
#            messagebox.showinfo("BBDD", "Se actualizado la información a la BBDD")
#
#        except:
#
#            messagebox.showinfo("BBDD", "Error, no se pudo actualizar la info a la BBDD")
#
#    ###########################################################################
#    raizguardar.mainloop()
    ###########################################################################
    
def abrir():
    
    #RAIZ Y MARCO##############################################################
    
    raizabrir=Tk()
    raizabrir.title("Abrir")
    #raizabrir.resizable(0,0)
    raizabrir.iconbitmap("pene.ico")
    
    Frame_Abrir=Frame(raizabrir)
    Frame_Abrir.pack()
    
    
    fontStyleBBDD = tkFont.Font(family="Lucida Grande", size=5)
    fontStyleBBDDdos = tkFont.Font(family="Lucida Grande", size=1)

    #DISEÑO ETIQUETAS##########################################################

    etiqueta_leer=Label(Frame_Abrir, text="INFORMACION GUARDADA EN LA BBDD")
    etiqueta_leer.grid(row=0, column=0, padx=3, pady=3)
    
    #DISEÑO DATOS A OPERAR#####################################################
    
    textoGuardado=Text(Frame_Abrir, width=40, height=25)
    textoGuardado.grid(row=1, column=0, padx=3, pady=3)
    barrascroll=Scrollbar(Frame_Abrir, command=textoGuardado.yview)
    barrascroll.grid(row=1, column=1, padx=3, sticky="nsew")
    textoGuardado.config(yscrollcommand=barrascroll.set)
    
    #DISEÑO BOTONES############################################################
    
    Frame_BotonesAbrir=Frame(raizabrir)
    Frame_BotonesAbrir.pack()
    
    botonActualizar=Button(Frame_BotonesAbrir, text="ACTUALIZAR", command=lambda:Actualizar_Abrir())
    botonActualizar.grid(row=2, column=0, padx=3, pady=3, sticky="w")   
    
    #FUNCIONES BOTONES#########################################################
    
    def Actualizar_Abrir():
        x=5

 #           miConexion=sqlite3.connect("BBDD-CALCULADORA")
 #
 #           miCursor=miConexion.cursor()
 #
 #           miCursor.execute("SELECT ID, VALOR, COMENTARIO FROM DATOSGUARDADOS")
 #
 #           datosguardados=miCursor.fetchall()
 #
 #
 #           textoGuardado.delete(1.0, END)
 #
 #           for i in datosguardados:
 #
 #               textoGuardado.insert(tk.INSERT, "ID:")
 #               textoGuardado.insert(tk.INSERT, "[")
 #               textoGuardado.insert(tk.INSERT, i[0])
 #               textoGuardado.insert(tk.INSERT, "]")
 #               textoGuardado.insert(tk.INSERT, " - ")
 #               textoGuardado.insert(tk.INSERT, "Valor: ")
 #               textoGuardado.insert(tk.INSERT, i[1])
 #               textoGuardado.insert(tk.INSERT, "\n")
 #               textoGuardado.insert(tk.INSERT, "Comentario: ")
 #               textoGuardado.insert(tk.INSERT, i[2])
 #               textoGuardado.insert(tk.INSERT, "\n")
 #
 #           miConexion.commit()
 #           miCursor.close()
 #           miConexion.close()
            
    ###########################################################################
  #  raizabrir.mainloop()
    ###########################################################################

def eliminar():
    
    #RAIZ Y MARCO##############################################################
    
    raizeliminar=Tk()
    raizeliminar.title("Eliminar")
    #raizguardar.resizable(0,0)
    raizeliminar.iconbitmap("pene.ico")
    
    Frame_Eliminar=Frame(raizeliminar)
    Frame_Eliminar.pack()
    
    fontStyleBBDD = tkFont.Font(family="Lucida Grande", size=5)
    fontStyleBBDDdos = tkFont.Font(family="Lucida Grande", size=1)

    #DISEÑO ETIQUETAS##########################################################

    etiqueta_eliminar=Label(Frame_Eliminar, text="ID del dato a eliminar: ")
    etiqueta_eliminar.grid(row=0, column=0, padx=3, pady=3, sticky="e")

    
    #DISEÑO DATOS A OPERAR#####################################################
    
    id_eliminar=Text(Frame_Eliminar, width=40, height=1)
    id_eliminar.grid(row=0, column=1, padx=3, pady=3)
    
    #QUE CARAJO ESTA PASADO CON LOS ENTRYS QUE NO ME DEJA TOMAR EL VALOR 
    #FUCK
    #FUCK
    #FUCK
    #ideliminar=StringVar()
    #valor_eliminar=Entry(Frame_Eliminar, textvariable=ideliminar)
    #valor_eliminar.grid(row=1, column=1, padx=3, pady=3)
    #valor_eliminar.config(font=fontStyleBBDD)
    
    #DISEÑO BOTONES############################################################
    
    Frame_BotonesEliminar=Frame(raizeliminar)
    Frame_BotonesEliminar.pack()
    
    botonEliminar=Button(Frame_BotonesEliminar, text="ELIMINAR", command=lambda:eliminar_valor())
    botonEliminar.grid(row=1, column=0, padx=3, pady=3, sticky="w")
    
    #FUNCIONES BOTONES#########################################################
    
    def eliminar_valor():
         x=5
#       try:
#
#            miConexion=sqlite3.connect("BBDD-CALCULADORA")
#            miCursor=miConexion.cursor()
#            #numero=6
#            #miCursor.execute("DELETE FROM DATOSGUARDADOS WHERE ID=" + str(numero))
#            #NO ME ESTA TOMANDO EL VALOR DE LA CASILLA
#            #comando_borrar="DELETE FROM DATOSGUARDADOS WHERE ID=" + "'" + str(id_eliminar.get("1.0",END)) +"'"
#            comando_borrar="DELETE FROM DATOSGUARDADOS WHERE ID="  + str(id_eliminar.get("1.0",END))
#            miCursor.execute(comando_borrar)
#            miConexion.commit()
#            #miCursor.close()
#            #miConexion.close()
            
            
#            messagebox.showinfo("BBDD", "Se eliminó el dato de la BBDD")
#
#       except:
#
#            messagebox.showinfo("BBDD", "Error, no se pudo elminar el dato de la BBDD")
            
    ###########################################################################  
#    raizeliminar.mainloop()
    ###########################################################################
            
def salir():
    valor=messagebox.askquestion("Salir", "¿Desea salir del programa? :´(")
    
    if valor=="yes":
        raiz.destroy()
        
def ayuda():
    valor=messagebox.showinfo("Ayuda", "Tu viejo te va a ayudar")
    
#BARRA DE MENU#################################################################

barraMenu=Menu(raiz)
raiz.config(menu=barraMenu, width = 350, height=300 )

archivoMenu=Menu(barraMenu, tearoff=0)
#Aca agregamos las etiquetas adentro del menu.
archivoMenu.add_command(label="Nuevo", command=crear_BBSS)
archivoMenu.add_command(label="Abrir", command=abrir)
archivoMenu.add_command(label="Guardar", command=lambda:guardar(entradaPantalla.get()))
archivoMenu.add_command(label="Eliminar", command=eliminar)

archivoMenu.add_separator()
archivoMenu.add_command(label="Salir - 8====D ", command=salir)

editarMenu=Menu(barraMenu, tearoff=0)
editarMenu.add_command(label="Buscar", command=lambda:messagebox.showwarning("...", "Funcion en construccion.") )
editarMenu.add_command(label="Filtrar", command=lambda:messagebox.showwarning("...", "Funcion en construccion.") )


ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Ayuda", command=ayuda)

#esta funcione añade en el orden pedido los menues (con sus etiquetas adentro) 
#a la barra, con un nombre que elijamos

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)

barraMenu.add_cascade(label="Buscar", menu=editarMenu)

barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

#PANTALLA######################################################################
entradaPantalla=StringVar()
entradaPantalla.set("0")

fontStyle = tkFont.Font(family="Lucida Grande", size=20)
fontStyle2 = tkFont.Font(family="Lucida Grande", size=40)

#A cuantos pixeles equivale widht depende del tamaño de la letra, 
#mientras mas grande, mas pixeles equivale, NO PENSAR QUE SIEMPRE EQUIVALE LO MISMO.

pantalla=Entry(Frame_uno, textvariable=entradaPantalla, state='disabled', width=17)
pantalla.grid(row=0, column=0, padx=3, pady=3, columnspan=4 , rowspan = 2)
pantalla.config(background="black", fg="white", justify="right", font=fontStyle2)

#VARIABLES FUNCIONES############################################################

resultado=0
resta_memoria=0
suma_memoria=0
dividir_memoria=0
multiplicacion_memoria=0
iniciopantalla=0
operacion=" "
cant_decimales=0
indicador_decimales=0
ancho=15

#FUNCIONES#####################################################################

def decimales(num):
    global cant_decimales
    global indicador_decimales
    
    indicador_decimales=float(num)
    int (cant_decimales)
    if indicador_decimales == 1:
        cant_decimales+=1
        
    else:
        cant_decimales-=1
        
    if cant_decimales <= 2:
        cant_decimales=2
        entradaPantalla.set(f"{resultado:{ancho}.{cant_decimales}}")
        
    else:
        int (cant_decimales)
        entradaPantalla.set(f"{resultado:{ancho}.{cant_decimales}}")

def reseteo(num):
    global iniciopantalla
    global resultado
    global resta_memoria
    global suma_memoria
    global dividir_memoria
    global multiplicacion_memoria
    global operacion
    global cant_decimales
    
    entradaPantalla.set(num)
    cant_decimales=0
    resultado=0
    resta_memoria=0
    suma_memoria=0
    dividir_memoria=0
    multiplicacion_memoria=0
    iniciopantalla=0
    operacion=" "

def entradaBoton(num):
    global iniciopantalla
    global operacion
    if iniciopantalla==0:
        entradaPantalla.set(num)
        iniciopantalla=1
    else:
        entradaPantalla.set(entradaPantalla.get() + num)
        
def Igual(num):
    global iniciopantalla
    global resultado
    global resta_memoria
    global suma_memoria
    global dividir_memoria
    global multiplicacion_memoria
    global operacion
        
    if operacion=="suma":
        resultado=suma_memoria+float(num)
        #Abajo lo que se hace es redondear a 10 digitos la cantidad maxima que se muestra en pantalla
        entradaPantalla.set("{:.15}".format(resultado))
                
    elif operacion=="resta":
        resultado=resta_memoria-float(num)
        entradaPantalla.set("{:.15}".format(resultado))
                        
    elif operacion=="dividir":
        resultado=dividir_memoria / float(num)
        entradaPantalla.set("{:.15}".format(resultado))
        
    elif operacion=="multiplicar":
        resultado=multiplicacion_memoria * float(num)
        entradaPantalla.set("{:.15}".format(resultado))
            
    else:
        resultado=float(num)
        entradaPantalla.set("{:.15}".format(resultado))
        
    iniciopantalla=0
    cant_decimales=0
    operacion=" "  
    
def Suma(num):
    global iniciopantalla
    global operacion
    global resultado
    global suma_memoria
    global cant_decimales
    
    float(resultado)
    if operacion=="suma":
        resultado+=suma_memoria + float(num)
        suma_memoria=0
        round = (resultado, 5)
        entradaPantalla.set("{:.14}".format(resultado))
        
    else:
        operacion="suma"
        suma_memoria=float(num)
        
    cant_decimales=0
    iniciopantalla=0
    
def Resta(num):
    global iniciopantalla
    global operacion
    global resultado
    global resta_memoria
    global cant_decimales
    
    float(resultado)
    if operacion=="resta":
        resultado=resta_memoria
        resultado=resultado-float(num)
        round = (resultado, 5)
        resta_memoria=resultado
        entradaPantalla.set("{:.14}".format(resultado))
        
    else:
        operacion="resta"
        resta_memoria=float(num)
        
    iniciopantalla=0
    cant_decimales=0
    
def Dividir(num):
    global iniciopantalla
    global operacion
    global resultado
    global dividir_memoria
    global cant_decimales
    
    if operacion=="dividir":
        resultado=dividir_memoria
        resultado=resultado/float(num)
        round = (resultado, 5)
        dividir_memoria=resultado
        entradaPantalla.set("{:.14}".format(resultado))
        
    else:
        operacion="dividir"
        dividir_memoria=float(num)
        
    iniciopantalla=0
    cant_decimales=0
    
def Multiplicar(num):
    global iniciopantalla
    global operacion
    global resultado
    global multiplicacion_memoria
    global cant_decimales
    
    if operacion=="multiplicar":
        resultado=multiplicacion_memoria
        resultado=resultado*float(num)
        round = (resultado, 5)
        multiplicacion_memoria=resultado
        round = (resultado, 5)
        entradaPantalla.set("{:.14}".format(resultado))
        
    else:
        operacion="multiplicar"
        multiplicacion_memoria=float(num)
        
    iniciopantalla=0
    cant_decimales=0
        

#BOTONES#######################################################################
#Fila1
botonCE=Button(Frame_uno, text="RES", font=fontStyle, width=4,height=1, command=lambda:reseteo("0"))
botonCE.grid(row=2, column=0, padx=15, pady=15, columnspan=1)
botonMENOSDEC=Button(Frame_uno, text="<<", font=fontStyle, width=4,height=1, command=lambda:decimales("1"))
botonMENOSDEC.grid(row=2, column=1, padx=15, pady=15)
botonMASSDEC=Button(Frame_uno, text=">>", font=fontStyle, width=4,height=1,command=lambda:decimales("0"))
botonMASSDEC.grid(row=2, column=2, padx=15, pady=15)
botonX=Button(Frame_uno, text="X", font=fontStyle, width=4,height=1, command=lambda:Multiplicar(entradaPantalla.get()))
botonX.grid(row=2, column=3, padx=10, pady=15)
    
    
#Fila2
boton7=Button(Frame_uno, text="7", font=fontStyle, width=4,height=1, command=lambda:entradaBoton("7"))
boton7.grid(row=3, column=0, padx=15, pady=15)
boton8=Button(Frame_uno, text="8", font=fontStyle, width=4,height=1, command=lambda:entradaBoton("8"))
boton8.grid(row=3, column=1, padx=15, pady=15)
boton9=Button(Frame_uno, text="9", font=fontStyle, width=4,height=1, command=lambda:entradaBoton("9"))
boton9.grid(row=3, column=2, padx=15)
botonDIVIDIR=Button(Frame_uno, text="/", font=fontStyle, width=4,height=1, command=lambda:Dividir(entradaPantalla.get()))
botonDIVIDIR.grid(row=3, column=3, padx=15, pady=15)
#Fila3
boton4=Button(Frame_uno, text="4", font=fontStyle, width=4,height=1, command=lambda:entradaBoton("4"))
boton4.grid(row=4, column=0, padx=15, pady=15)
boton8=Button(Frame_uno, text="5", font=fontStyle, width=4,height=1, command=lambda:entradaBoton("5"))
boton8.grid(row=4, column=1, padx=15, pady=15)
boton9=Button(Frame_uno, text="6", font=fontStyle, width=4,height=1, command=lambda:entradaBoton("6"))
boton9.grid(row=4, column=2, padx=15, pady=15)
botonSUMA=Button(Frame_uno, text="+", font=fontStyle, width=4,height=1, command=lambda:Suma(entradaPantalla.get()))
botonSUMA.grid(row=4, column=3, padx=15, pady=15)
#Fila4
boton1=Button(Frame_uno, text="1", font=fontStyle, width=4,height=1, command=lambda:entradaBoton("1"))
boton1.grid(row=5, column=0, padx=15, pady=15)
boton2=Button(Frame_uno, text="2", font=fontStyle, width=4,height=1, command=lambda:entradaBoton("2"))
boton2.grid(row=5, column=1, padx=15, pady=15)
boton3=Button(Frame_uno, text="3", font=fontStyle, width=4,height=1, command=lambda:entradaBoton("3"))
boton3.grid(row=5, column=2, padx=15, pady=15)
botonRESTA=Button(Frame_uno, text="-", font=fontStyle, width=4,height=1, command=lambda:Resta(entradaPantalla.get()))
botonRESTA.grid(row=5, column=3, padx=15, pady=15)
#Fila5
boton314=Button(Frame_uno, text="PI", font=fontStyle, width=4,height=1, command=lambda:entradaBoton(math.pi))
boton314.grid(row=6, column=0, padx=15, pady=15)
boton0=Button(Frame_uno, text="0", font=fontStyle, width=4,height=1, command=lambda:entradaBoton("0"))
boton0.grid(row=6, column=1, padx=15, pady=15)
botonCOMA=Button(Frame_uno, text=",", font=fontStyle, width=4,height=1, command=lambda:entradaBoton("."))
botonCOMA.grid(row=6, column=2, padx=15, pady=15)
botonIGUAL=Button(Frame_uno, text="=", font=fontStyle, width=4,height=1, command=lambda:Igual(entradaPantalla.get()))
botonIGUAL.grid(row=6, column=3, padx=15, pady=15)

#Fila6
#calculos=""
#pantalla2=Entry(Frame_uno, textvariable=calculos)
#pantalla2.grid(row=6, column=0, padx=15, pady=15, columnspan=4)
#pantalla2.config(background="black", fg="white", justify="center")

###############################################################################
raiz.mainloop()
###############################################################################


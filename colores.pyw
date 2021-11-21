from tkinter import *

ventana = Tk()
ventana.title("Paleta de colores")
ventana.geometry("400x240")
ventana.resizable(0, 0)

def hexadecimal(num):
    ''' Convierte a hexadecimal el valor obtenido del control deslizante'''    
    hexa = ""
    dic_hexa={10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
    while num != 0:
        valor = num 
        num = num // 16 
        resto = valor % 16 
        if resto <= 9:
            hexa = str(resto) + hexa
        else:
            hexa = str(dic_hexa.get(resto)) + hexa
    return hexa

def cambiar(n):
    '''A partir de los valores obtenidos de la función "hexadecimal", construye el código
    del nuevo color'''
    valor_rojo = hexadecimal(rojo.get())
    if valor_rojo == "": valor_rojo="00"
    rojo_hexa.config(text=valor_rojo)
    valor_verde = hexadecimal(verde.get())
    if valor_verde == "": valor_verde="00"
    verde_hexa.config(text=valor_verde)
    valor_azul = hexadecimal(azul.get())
    if valor_azul == "": valor_azul="00"
    azul_hexa.config(text=valor_azul)  
    color = "#" + valor_rojo + valor_verde + valor_azul
    color_hexa.config(text=color)
    muestra.config(bg=color)

#Controles deslizantes:
rojo = Scale(ventana, from_=0, to=255, orient=HORIZONTAL, length=300, command=cambiar, showvalue=False)
rojo.place(x=50, y=20)
verde = Scale(ventana, from_=0, to=255, orient=HORIZONTAL, length=300, command=cambiar, showvalue=False)
verde.place(x=50, y=60)
azul = Scale(ventana, from_=0, to=255, orient=HORIZONTAL, length=300, command=cambiar, showvalue=False)
azul.place(x=50, y=100)

#Etiqueta que muestra el color:
muestra = Label(ventana, bg="#000000", width=38, height=2)
muestra.place(x=50, y=130)

#Etiquetas delante de los controles deslizantes:
label_rojo = Label(ventana, text="Rojo: ").place(x=10, y=20)
label_verde = Label(ventana, text="Verde: ").place(x=10, y=60)
label_azul = Label(ventana, text="Azul: ").place(x=10, y=100)

#Etiquetas que muestran el valor hexadecimal de cada color detrás de los controles deslizantes
rojo_hexa=Label(ventana, text="00")
rojo_hexa.place(x=360, y=20)
verde_hexa=Label(ventana, text="00")
verde_hexa.place(x=360, y=60)
azul_hexa=Label(ventana, text="00")
azul_hexa.place(x=360, y=100)

#Etiqueta que muestra el código hexadecimal de la muestra:
color_hexa=Label(ventana, text="#000000")
color_hexa.place(x=330, y=140)

#Botón para cerrar la aplicación.
salir = Button(ventana, text="Salir", width=8, command=lambda: ventana.destroy())
salir.place(x=320, y=200)

ventana.mainloop()
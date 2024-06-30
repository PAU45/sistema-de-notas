import tkinter as tk
from tkinter import font
import mysql.connector
from styles import *

# Función para obtener los datos del estudiante seleccionado y abrir la ventana de edición
def editar_estudiante(estudiante):
    ventana_edicion = tk.Toplevel()
    ventana_edicion.geometry("1500x900")  
    ventana_edicion.resizable(False, False)
    ventana_edicion.title("Gestión de Usuarios")

    titulo_font = font.Font(family=FontFamily, size=FontSizeTitles, weight=FontBold)
    Campos = font.Font(family=FontFamily, size=FontInput)
    Spaces = font.Font(size=FontSpaces)
    boton_font = font.Font(family=FontSizeTitles, size=FontSizeBtn, weight=FontBold)

    # Crear el título
    titulo_label = tk.Label(ventana_edicion, text="Editar Alumno", font=titulo_font)
    titulo_label.pack(pady=50)

    # Crear los campos de texto y etiquetas para la ventana de edición
    label_nombre = tk.Label(ventana_edicion, text="Nombre:", font=Campos)
    label_nombre.pack()
    entry_nombre = tk.Entry(ventana_edicion, width=30, font=Campos)
    entry_nombre.pack()

    label_apellido = tk.Label(ventana_edicion, text="Apellido:", font=Campos)
    label_apellido.pack()
    entry_apellido = tk.Entry(ventana_edicion, width=30, font=Campos)
    entry_apellido.pack()

    label_edad = tk.Label(ventana_edicion, text="Edad:", font=Campos)
    label_edad.pack()
    entry_edad = tk.Entry(ventana_edicion, width=30, font=Campos)
    entry_edad.pack()

    label_dni = tk.Label(ventana_edicion, text="DNI:", font=Campos)
    label_dni.pack()
    entry_dni = tk.Entry(ventana_edicion, width=30, font=Campos)
    entry_dni.pack()

    label_año_ingreso = tk.Label(ventana_edicion, text="Año de Ingreso:", font=Campos)
    label_año_ingreso.pack()
    entry_año_ingreso = tk.Entry(ventana_edicion, width=30, font=Campos)
    entry_año_ingreso.pack()

    label_grado = tk.Label(ventana_edicion, text="Grado:", font=Campos)
    label_grado.pack()
    entry_grado = tk.Entry(ventana_edicion, width=30, font=Campos)
    entry_grado.pack()

    label_seccion = tk.Label(ventana_edicion, text="Sección:", font=Campos)
    label_seccion.pack()
    entry_seccion = tk.Entry(ventana_edicion, width=30, font=Campos)
    entry_seccion.pack()

    # Obtener los datos del estudiante seleccionado
    id_estudiante = estudiante[0]
    nombre = estudiante[2]
    apellido = estudiante[3]
    edad = estudiante[4]
    dni = estudiante[1]
    año_de_ingreso = estudiante[5]
    grado = estudiante[6]  # Suponiendo que el grado está en la posición 6 del estudiante
    seccion = estudiante[7]  # Suponiendo que la sección está en la posición 7 del estudiante

    # Preencher los campos de entrada con la información actual del estudiante
    entry_nombre.insert(0, nombre)
    entry_apellido.insert(0, apellido)
    entry_edad.insert(0, edad)
    entry_dni.insert(0, dni)
    entry_año_ingreso.insert(0, año_de_ingreso)
    entry_grado.insert(0, grado)
    entry_seccion.insert(0, seccion)

    # Función para guardar los cambios realizados en la edición del estudiante
    def guardar_cambios():
        # Obtener los nuevos valores ingresados en los campos de texto
        nuevo_nombre = entry_nombre.get()
        nuevo_apellido = entry_apellido.get()
        nueva_edad = entry_edad.get()
        nuevo_dni = entry_dni.get()
        nuevo_año_ingreso = entry_año_ingreso.get()
        nuevo_grado = entry_grado.get()
        nueva_seccion = entry_seccion.get()

        # Realizar la conexión a la base de datos
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="estudiantespy"
        )

        # Crear un cursor para ejecutar consultas
        cursor = connection.cursor()

        # Ejecutar la consulta para actualizar la información del estudiante
        consulta = "UPDATE estudiantes SET nombre=%s, apellido=%s, edad=%s, dni=%s, año_de_ingreso=%s, grado=%s, seccion=%s WHERE id_estudiante=%s"
        valores = (nuevo_nombre, nuevo_apellido, nueva_edad, nuevo_dni, nuevo_año_ingreso, nuevo_grado, nueva_seccion, id_estudiante)
        cursor.execute(consulta, valores)

        # Confirmar los cambios en la base de datos
        connection.commit()

        # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()

        # Cerrar la ventana de edición
        ventana_edicion.destroy()

    # Crear el botón de guardar cambios
    Spacio = tk.Label(ventana_edicion, text=" ", font=Spaces)
    Spacio.pack()
    boton_guardar = tk.Button(ventana_edicion, text="Guardar Cambios", command=guardar_cambios, font=boton_font, bg=colorBtns, fg=colorFont)
    boton_guardar.pack(side=tk.TOP, padx=10, pady=10)

# Ejemplo de uso: editar_estudiante([1, 12345678, "Juan", "Perez", 25, 2020, "Primero", "A"])

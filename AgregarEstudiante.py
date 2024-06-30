import tkinter as tk
from tkinter import font
import mysql.connector
from styles import *

def cerrar_ventana_agregar_estudiante():
    ventana_agregar_estudiante.destroy()

def agregar_estudiante():
    global entry_nombre, entry_apellido, entry_edad, entry_dni, entry_año_ingreso, entry_grado, entry_seccion, mensaje_label

    # Obtener los valores ingresados en los campos de texto
    nombre = entry_nombre.get().strip()
    apellido = entry_apellido.get().strip()
    edad = entry_edad.get().strip()
    dni = entry_dni.get().strip()
    año_de_ingreso = entry_año_ingreso.get().strip()
    grado = entry_grado.get().strip()
    seccion = entry_seccion.get().strip()

    # Verificar que los campos no estén vacíos
    if nombre == "":
        mensaje_label.configure(text="El campo Nombre no puede estar vacío", fg="red")
        return
    if edad == "":
        mensaje_label.configure(text="El campo Edad no puede estar vacío", fg="red")
        return

    # Realizar la conexión a la base de datos
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="estudiantespy"
        )

        # Crear un cursor para ejecutar consultas
        cursor = connection.cursor()

        # Ejecutar la consulta para agregar el nuevo estudiante
        consulta = "INSERT INTO estudiantes (nombre, apellido, edad, dni, año_de_ingreso, grado, seccion) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        valores = (nombre, apellido, edad, dni, año_de_ingreso, grado, seccion)
        cursor.execute(consulta, valores)

        # Confirmar los cambios en la base de datos
        connection.commit()

        # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()

        # Limpiar los campos de texto
        entry_nombre.delete(0, tk.END)
        entry_apellido.delete(0, tk.END)
        entry_edad.delete(0, tk.END)
        entry_dni.delete(0, tk.END)
        entry_año_ingreso.delete(0, tk.END)
        entry_grado.delete(0, tk.END)
        entry_seccion.delete(0, tk.END)

        # Mostrar un mensaje de éxito
        mensaje_label.configure(text="Nuevo estudiante agregado correctamente", fg="green")

    except mysql.connector.Error as error:
        print(f"Error al conectar con la base de datos: {error}")
        mensaje_label.configure(text="Error al conectar con la base de datos", fg="red")

def crear_ventana_agregar_estudiante():
    global ventana_agregar_estudiante, entry_nombre, entry_apellido, entry_edad, entry_dni, entry_año_ingreso, entry_grado, entry_seccion, mensaje_label

    # Crear la ventana de agregar estudiante
    ventana_agregar_estudiante = tk.Toplevel()
    ventana_agregar_estudiante.title("Agregar Estudiante")
    ventana_agregar_estudiante.geometry("1500x9000")  # Tamaño ajustado según necesidades
    ventana_agregar_estudiante.resizable(False, False)

    # Configurar la fuente del título
    titulo_font = font.Font(family=FontFamily, size=FontSizeTitles, weight=FontBold)
    titles_campos = font.Font(family=FontFamily, size=FontInput)
    boton_font = font.Font(family=FontFamily, size=FontSizeBtn, weight=FontBold)

    # Crear el título
    titulo_label = tk.Label(ventana_agregar_estudiante, text="Nuevo Estudiante", font=titulo_font)
    titulo_label.grid(row=0, column=0, columnspan=2, pady=20)

    # Crear los campos de texto y etiquetas
    label_nombre = tk.Label(ventana_agregar_estudiante, text="Nombre:", font=titles_campos)
    label_nombre.grid(row=1, column=0, padx=10, pady=10, sticky="e")
    entry_nombre = tk.Entry(ventana_agregar_estudiante, width=30, font=titles_campos)
    entry_nombre.grid(row=1, column=1, padx=10, pady=10)

    label_apellido = tk.Label(ventana_agregar_estudiante, text="Apellido:", font=titles_campos)
    label_apellido.grid(row=2, column=0, padx=10, pady=10, sticky="e")
    entry_apellido = tk.Entry(ventana_agregar_estudiante, width=30, font=titles_campos)
    entry_apellido.grid(row=2, column=1, padx=10, pady=10)

    label_edad = tk.Label(ventana_agregar_estudiante, text="Edad:", font=titles_campos)
    label_edad.grid(row=3, column=0, padx=10, pady=10, sticky="e")
    entry_edad = tk.Entry(ventana_agregar_estudiante, width=30, font=titles_campos)
    entry_edad.grid(row=3, column=1, padx=10, pady=10)

    label_dni = tk.Label(ventana_agregar_estudiante, text="DNI:", font=titles_campos)
    label_dni.grid(row=4, column=0, padx=10, pady=10, sticky="e")
    entry_dni = tk.Entry(ventana_agregar_estudiante, width=30, font=titles_campos)
    entry_dni.grid(row=4, column=1, padx=10, pady=10)

    label_año_ingreso = tk.Label(ventana_agregar_estudiante, text="Año de Ingreso:", font=titles_campos)
    label_año_ingreso.grid(row=5, column=0, padx=10, pady=10, sticky="e")
    entry_año_ingreso = tk.Entry(ventana_agregar_estudiante, width=30, font=titles_campos)
    entry_año_ingreso.grid(row=5, column=1, padx=10, pady=10)

    label_grado = tk.Label(ventana_agregar_estudiante, text="Grado:", font=titles_campos)
    label_grado.grid(row=6, column=0, padx=10, pady=10, sticky="e")
    entry_grado = tk.Entry(ventana_agregar_estudiante, width=30, font=titles_campos)
    entry_grado.grid(row=6, column=1, padx=10, pady=10)

    label_seccion = tk.Label(ventana_agregar_estudiante, text="Sección:", font=titles_campos)
    label_seccion.grid(row=7, column=0, padx=10, pady=10, sticky="e")
    entry_seccion = tk.Entry(ventana_agregar_estudiante, width=30, font=titles_campos)
    entry_seccion.grid(row=7, column=1, padx=10, pady=10)

    # Mensaje de estado para mostrar resultados o errores
    mensaje_label = tk.Label(ventana_agregar_estudiante, text="", font=titles_campos)
    mensaje_label.grid(row=8, column=0, columnspan=2, pady=10)

    # Crear botones
    boton_agregar = tk.Button(ventana_agregar_estudiante, text="Agregar Estudiante", font=boton_font, bg=colorBtns, fg=colorFont, command=agregar_estudiante)
    boton_agregar.grid(row=9, column=0, columnspan=2, pady=20)

    boton_cerrar = tk.Button(ventana_agregar_estudiante, text="Cerrar", font=boton_font, bg=colorBtns, fg=colorFont, command=cerrar_ventana_agregar_estudiante)
    boton_cerrar.grid(row=10, column=0, columnspan=2, pady=20)

    # Centrar la ventana en la pantalla
    

    # Mantener la ventana abierta
    ventana_agregar_estudiante.mainloop()











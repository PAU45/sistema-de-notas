import tkinter as tk
from tkinter import font, simpledialog, messagebox
import mysql.connector
from styles import *  # Asumiendo que tienes un archivo styles.py con definiciones de estilo
import subprocess  # Para ejecutar otro script de Python

# Función para gestionar cursos
def gestionar_cursos(usuario):
    # Configuración de la ventana principal
    ventana_cursos = tk.Toplevel()
    ventana_cursos.geometry(pantalla)  # Pantalla debe estar definida en tu archivo styles.py
    ventana_cursos.resizable(False, False)
    ventana_cursos.title(f"Gestionar Cursos - {usuario[1]}")
   
    # Definición de fuentes
    titulo_fontone = font.Font(family=FontFamily, size=FontSizeTitles, weight=FontBold)
    titulo_font = font.Font(family=FontFamily, size=FontInput)
    boton_font = font.Font(family=FontFamily, size=FontSizeBtn2, weight=FontBold)
    
    # Título de la ventana
    titulo_label = tk.Label(ventana_cursos, text=f"Cursos de {usuario[1]}", font=titulo_fontone)
    titulo_label.pack(pady=20)
    
    # Frame para contener la lista de cursos y sus botones
    frame_cursos = tk.Frame(ventana_cursos, borderwidth=2, relief="groove", padx=20, pady=20)
    frame_cursos.pack(pady=20)
    
    # Función para actualizar la lista de cursos
    def actualizar_lista_cursos():
        for widget in frame_cursos.winfo_children():
            widget.destroy()
        
        try:
            # Conexión a la base de datos
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",  # Aquí debes colocar la contraseña de tu MySQL si está configurada
                database="estudiantespy"
            )
            
            cursor = connection.cursor()
            
            # Consulta para obtener los cursos del estudiante
            consulta_cursos = "SELECT id_curso, nombre FROM Cursos WHERE id_estudiante = %s"
            cursor.execute(consulta_cursos, (usuario[0],))
            cursos = cursor.fetchall()
            
            for curso in cursos:
                curso_id = curso[0]
                curso_nombre = curso[1]
                
                frame_curso = tk.Frame(frame_cursos)
                frame_curso.pack(fill=tk.X, pady=5)
                
                label_curso = tk.Label(frame_curso, text=f"{curso_id} - {curso_nombre}", font=titulo_font)
                label_curso.pack(side=tk.LEFT, padx=10)
                
                boton_ver_notas = tk.Button(
                    frame_curso, 
                    text="Ver Notas", 
                    font=boton_font, 
                    command=lambda id=curso_id: abrir_otro_script(id),
                    bg="#4CAF50",  # Color de fondo del botón
                    fg="white",  # Color del texto del botón
                    relief="raised",  # Relieve del botón
                    bd=3,  # Borde del botón
                    padx=10,  # Espaciado horizontal interno
                    pady=5  # Espaciado vertical interno
                )
                boton_ver_notas.pack(side=tk.RIGHT, padx=10)
                
            connection.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
    
    # Llamar a la función para llenar la lista al inicio
    actualizar_lista_cursos()
    
    # Función para agregar un nuevo curso
    def agregar_curso():
        nuevo_curso = simpledialog.askstring("Agregar Curso", "Nombre del nuevo curso:")
        if nuevo_curso:
            try:
                connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="estudiantespy"
                )
                
                cursor = connection.cursor()
                
                # Consulta para insertar un nuevo curso
                insertar_curso = "INSERT INTO Cursos (nombre, descripcion, id_estudiante) VALUES (%s, %s, %s)"
                cursor.execute(insertar_curso, (nuevo_curso, "", usuario[0]))
                connection.commit()
                
                connection.close()
                
                # Actualizar la lista de cursos
                actualizar_lista_cursos()
            except mysql.connector.Error as err:
                print(f"Error: {err}")
    
    # Función para editar un curso seleccionado
    def editar_curso():
        curso_id = simpledialog.askstring("Editar Curso", "Ingrese el ID del curso que desea editar:")
        if curso_id:
            nuevo_nombre = simpledialog.askstring("Editar Curso", "Nuevo nombre del curso:")
            if nuevo_nombre:
                try:
                    connection = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="estudiantespy"
                    )
                    
                    cursor = connection.cursor()
                    
                    # Consulta para actualizar el nombre del curso
                    actualizar_curso = "UPDATE Cursos SET nombre = %s WHERE id_curso = %s AND id_estudiante = %s"
                    cursor.execute(actualizar_curso, (nuevo_nombre, curso_id, usuario[0]))
                    connection.commit()
                    
                    connection.close()
                    
                    # Actualizar la lista de cursos
                    actualizar_lista_cursos()
                except mysql.connector.Error as err:
                    print(f"Error: {err}")
    
    # Función para eliminar un curso seleccionado
    def eliminar_curso():
        curso_id = simpledialog.askstring("Eliminar Curso", "Ingrese el ID del curso que desea eliminar:")
        if curso_id:
            confirmar = messagebox.askyesno("Confirmar Eliminación", f"¿Está seguro de que desea eliminar el curso con ID {curso_id}?")
            if confirmar:
                try:
                    connection = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="estudiantespy"
                    )
                    
                    cursor = connection.cursor()
                    
                    # Consulta para eliminar el curso
                    eliminar_curso = "DELETE FROM Cursos WHERE id_curso = %s AND id_estudiante = %s"
                    cursor.execute(eliminar_curso, (curso_id, usuario[0]))
                    connection.commit()
                    
                    connection.close()
                    
                    # Actualizar la lista de cursos
                    actualizar_lista_cursos()
                except mysql.connector.Error as err:
                    print(f"Error: {err}")
    
    # Función para abrir otro script de Python
    def abrir_otro_script(curso_id):
        # Aquí debes reemplazar "otro_script.py" por el nombre de tu script de Python
        subprocess.Popen(["python", "calificarnotas.py", str(curso_id)])
    
    # Botones para agregar, editar y eliminar cursos
    #boton_agregar = tk.Button(
       # ventana_cursos, 
        #text="Agregar Curso", 
        #font=boton_font, 
       # command=agregar_curso,
        #bg="#2196F3",  # Color de fondo del botón
        #fg="white",  # Color del texto del botón
        #relief="raised",  # Relieve del botón
        #bd=3,  # Borde del botón
        #padx=10,  # Espaciado horizontal interno
        #pady=5  # Espaciado vertical interno
    #)
    #boton_agregar.pack(side=tk.LEFT, padx=10, pady=20)
    
    boton_editar = tk.Button(
        ventana_cursos, 
        text="Editar Curso", 
        font=boton_font, 
        command=editar_curso,
        bg="#FFC107",  # Color de fondo del botón
        fg="white",  # Color del texto del botón
        relief="raised",  # Relieve del botón
        bd=3,  # Borde del botón
        padx=10,  # Espaciado horizontal interno
        pady=5  # Espaciado vertical interno
    )
    boton_editar.pack(side=tk.LEFT, padx=10, pady=20)
    
    boton_eliminar = tk.Button(
        ventana_cursos, 
        text="Eliminar Curso", 
        font=boton_font, 
        command=eliminar_curso,
        bg="#F44336",  # Color de fondo del botón
        fg="white",  # Color del texto del botón
        relief="raised",  # Relieve del botón
        bd=3,  # Borde del botón
        padx=10,  # Espaciado horizontal interno
        pady=5  # Espaciado vertical interno
    )
    boton_eliminar.pack(side=tk.LEFT, padx=10, pady=20)
    
    # Botón para salir de la ventana
    boton_salir = tk.Button(
        ventana_cursos, 
        text="Salir", 
        font=boton_font, 
        command=ventana_cursos.destroy,
        bg="#9E9E9E",  # Color de fondo del botón
        fg="white",  # Color del texto del botón
        relief="raised",  # Relieve del botón
        bd=3,  # Borde del botón
        padx=10,  # Espaciado horizontal interno
        pady=5  # Espaciado vertical interno
    )
    boton_salir.pack(side=tk.RIGHT, padx=10, pady=20)
# Función para ajustar el tamaño del canvas

# Aquí iría el resto de tu código, como inicializar tu aplicación principal de tkinter, etc.

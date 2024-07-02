import tkinter as tk
from tkinter import font
import mysql.connector
import EditarEstudiante
import EliminarEstudiante
import Generarcursos
import Informes
from styles import *

def Consultar_estudiante():
    ventana_Consulta = tk.Toplevel()
    ventana_Consulta.geometry(pantalla)
    ventana_Consulta.resizable(False, False)
    ventana_Consulta.title("Gestión de Usuarios")

    titulo_fontone = font.Font(family=FontFamily, size=FontSizeTitles, weight=FontBold)
    titulo_font = font.Font(family=FontFamily, size=FontInput)

    titulo_label = tk.Label(ventana_Consulta, text="Informacion de Alumnos", font=titulo_fontone)
    titulo_label.pack(pady=50)

    lista_usuarios = tk.Listbox(ventana_Consulta)
    lista_usuarios.pack()

    def obtener_informacion_usuario(usuario):
        print("Información del usuario:", usuario)
        EditarEstudiante.editar_estudiante(usuario)
        ventana_Consulta.destroy()

    def eliminar_usuario(usuario):
        print("Eliminar usuario:", usuario)
        EliminarEstudiante.eliminar_estudiante(usuario)
        ventana_Consulta.destroy()

    def Generar_Informe(usuario):
        print("Agregar calificaciones a usuario:", usuario)
        Informes.generar_reporte(usuario)

    def gestionar_cursos(usuario):
        print("Gestionar cursos del usuario:", usuario)
        Generarcursos.gestionar_cursos(usuario)  

    def actualizar_lista_usuarios():
        lista_usuarios.delete(0, tk.END)

        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="estudiantespy"
        )

        cursor = connection.cursor()

        consulta = "SELECT * FROM estudiantes"
        cursor.execute(consulta)

        usuarios = cursor.fetchall()

        boton_font = font.Font(family=FontSizeTitles, size=FontSizeBtn2, weight=FontBold)

        for usuario in usuarios:
            frame_usuario = tk.Frame(lista_usuarios)
            frame_usuario.pack(fill="x")

            label_usuario = tk.Label(frame_usuario, text=f" Nombre: {usuario[2]}, Apellido: {usuario[3]}, Grado: {usuario[6]}, Sección: {usuario[7]}", font=titulo_font)
            label_usuario.pack(side="left", padx=10)

            boton_editar = tk.Button(frame_usuario, text="Editar", font=boton_font, bg=colorBtns, fg=colorFont, command=lambda u=usuario: obtener_informacion_usuario(u))
            boton_editar.pack(side="left", padx=5)

            boton_eliminar = tk.Button(frame_usuario, text="Eliminar", font=boton_font, bg=colorBtns, fg=colorFont, command=lambda u=usuario: eliminar_usuario(u))
            boton_eliminar.pack(side="left", padx=5)

            InformeBtn = tk.Button(frame_usuario, text="Generar Informe", font=boton_font, bg=colorBtns, fg=colorFont, command=lambda u=usuario: Generar_Informe(u))
            InformeBtn.pack(side="left", padx=5)

            # Botón para gestionar cursos del usuario
            gestionar_cursos_btn = tk.Button(frame_usuario, text="Gestionar Cursos", font=boton_font, bg=colorBtns, fg=colorFont, command=lambda u=usuario: gestionar_cursos(u))
            gestionar_cursos_btn.pack(side="left", padx=5)

        cursor.close()
        connection.close()

    actualizar_lista_usuarios()

if __name__ == '__main__':
    Consultar_estudiante()

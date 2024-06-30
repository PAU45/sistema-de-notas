import tkinter as tk
from tkinter import font
import AgregarEstudiante
import ConsultarEstudiante
from styles import *
import sys
from Login import usuario_actual, flag  # Importa la variable usuario_actual y flag desde login.py

ventana_bienvenida = None  # Variable global para almacenar la ventana de bienvenida

# Definir la función cerrar_programa antes de su uso
def cerrar_programa():
    try:
        ventana_bienvenida.destroy()
    except tk.TclError:
        pass
    sys.exit(0)

# Función para iniciar la aplicación
def iniciar_aplicacion():
    global ventana_bienvenida
    ventana_bienvenida = tk.Tk()
    ventana_bienvenida.title("Sistema de Gestión de Estudiantes - Bienvenida")
    ventana_bienvenida.geometry(pantalla)
    ventana_bienvenida.resizable(False, False)

    # Configurar la fuente del título
    titulo_font = font.Font(family=FontFamily, size=FontSizeTitles, weight=FontBold)

    # Crear el título
    bienvenida_label = tk.Label(ventana_bienvenida, text=f"Bienvenido al sistema, {usuario_actual}", font=("Arial", 18))
    bienvenida_label.pack(pady=20)

    # Crear un marco para contener los botones
    marco = tk.Frame(ventana_bienvenida)
    marco.pack()

    # Configurar la fuente y el tamaño de los botones
    boton_font = font.Font(family=FontFamily, size=FontSizeBtn, weight=FontBold)

    # Crear los botones con diseño personalizado
    boton_agregar_estudiante = tk.Button(marco, text="Agregar Estudiante", font=boton_font, bg=colorBtns, fg=colorFont, width=17, height=2, command=abrir_ventana_agregar_estudiante)
    boton_agregar_estudiante.pack(side=tk.LEFT, padx=10, pady=10)

    boton_ver_estudiantes = tk.Button(marco, text="Ver Estudiantes", font=boton_font, bg=colorBtns, fg=colorFont, width=17, height=2, command=abrir_ventana_Consultar_estudiante)
    boton_ver_estudiantes.pack(side=tk.LEFT, padx=10, pady=10)

    ventana_bienvenida.protocol("WM_DELETE_WINDOW", cerrar_programa)

    # Ejecutar la ventana de bienvenida
    ventana_bienvenida.mainloop()

def abrir_ventana_agregar_estudiante():
    AgregarEstudiante.crear_ventana_agregar_estudiante()

def abrir_ventana_Consultar_estudiante():
    ConsultarEstudiante.Consultar_estudiante()

# Llamada para iniciar la aplicación si el script se ejecuta directamente
if __name__ == "__main__":
    if flag == 1:  # Solo iniciar la aplicación si el inicio de sesión fue exitoso
        iniciar_aplicacion()
    else:
        print("El inicio de sesión no fue exitoso.")

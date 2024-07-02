import time
import tkinter as tk
from tkinter import messagebox
import mysql.connector
import sys

usuario_actual = None
flag = 1
# Función para verificar el login
def verificar_login():
    global usuario_actual# Variable global para almacenar el usuario actual después del inicio de sesión
    codigo = entry_codigo.get()
    contrasena = entry_contrasena.get()

    try:
       
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  
            database="estudiantespy"
        )

        cursor = connection.cursor()

        # Consulta para verificar el código y la contraseña del profesor
        consulta_login = "SELECT id_profesor, nombre FROM Profesores WHERE codigo = %s AND contrasena = %s"
        cursor.execute(consulta_login, (codigo, contrasena))
        resultado = cursor.fetchone()

        connection.close()

        if resultado:
            id_profesor, nombre = resultado
            usuario_actual = nombre  # Establecer el usuario actual

            messagebox.showinfo("Éxito", "Inicio de sesión exitoso")
         
            # Destruir la ventana de inicio de sesión después de 0 segundos
            time.sleep(0)
            ventana_login.destroy()  # Destruir la ventana de inicio de sesión
            
    
            

        else:
            messagebox.showerror("Error", "Código o contraseña incorrectos")
            flag=0 
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error al conectar con la base de datos: {err}")
    
    

    

ventana_login = tk.Tk()
ventana_login.title("Inicio de Sesión")
ventana_login.geometry("300x200")


label_codigo = tk.Label(ventana_login, text="Código:")
label_codigo.pack(pady=5)
entry_codigo = tk.Entry(ventana_login)
entry_codigo.pack(pady=5)

label_contrasena = tk.Label(ventana_login, text="Contraseña:")
label_contrasena.pack(pady=5)
entry_contrasena = tk.Entry(ventana_login, show="*")
entry_contrasena.pack(pady=5)


boton_login = tk.Button(ventana_login, text="Iniciar Sesión", command=verificar_login)
boton_login.pack(pady=20)



def cerrar_programa():
    try:
        ventana_login.destroy()
    except tk.TclError:
        pass
    sys.exit(0)

ventana_login.protocol("WM_DELETE_WINDOW",cerrar_programa)

# Ejecutar la ventana de inicio de sesión
ventana_login.mainloop()

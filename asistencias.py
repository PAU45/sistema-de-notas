import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error
from datetime import date

# Variables globales para los elementos de la interfaz
id_estudiante_entry = None
fecha_asistencia_entry = None
id_asistencia_entry = None


def crear_conexion():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  
            database="estudiantespy"
        )
        if conn.is_connected():
            print('Conexión establecida a MySQL')
            return conn
    except Error as e:
        print(f'Ocurrió un error al conectar a MySQL: {e}')
    return None

# Función para insertar una nueva asistencia en la base de datos MySQL
def insertar_asistencia(conn, id_asistencia, id_estudiante, fecha_asistencia, asistencia):
    try:
        cursor = conn.cursor()
        sql_insert = '''
            INSERT INTO Asistencias(id_asistencia, id_estudiante, fecha_asistencia, asistencia)
            VALUES(%s, %s, %s, %s)
        '''
        cursor.execute(sql_insert, (id_asistencia, id_estudiante, fecha_asistencia, asistencia))
        conn.commit()
        messagebox.showinfo('Éxito', 'Asistencia registrada correctamente.')
    except Error as e:
        print(f'Ocurrió un error al insertar datos de asistencia: {e}')
        messagebox.showerror('Error', 'No se pudo registrar la asistencia.')

# Función para actualizar una asistencia existente en la base de datos MySQL
def actualizar_asistencia(conn, id_asistencia, id_estudiante, fecha_asistencia, asistencia):
    try:
        cursor = conn.cursor()
        sql_update = '''
            UPDATE Asistencias
            SET id_estudiante = %s, fecha_asistencia = %s, asistencia = %s
            WHERE id_asistencia = %s
        '''
        cursor.execute(sql_update, (id_estudiante, fecha_asistencia, asistencia, id_asistencia))
        conn.commit()
        messagebox.showinfo('Éxito', 'Asistencia actualizada correctamente.')
    except Error as e:
        print(f'Ocurrió un error al actualizar datos de asistencia: {e}')
        messagebox.showerror('Error', 'No se pudo actualizar la asistencia.')

# Función para manejar el evento de registrar asistencia desde la interfaz
def registrar_asistencia(tipo_asistencia):
    global id_estudiante_entry, fecha_asistencia_entry, id_asistencia_entry
    
    if id_estudiante_entry is None or fecha_asistencia_entry is None or id_asistencia_entry is None:
        messagebox.showerror('Error', 'Widgets no inicializados correctamente.')
        return
    
    id_asistencia = id_asistencia_entry.get()
    id_estudiante = id_estudiante_entry.get()
    fecha_asistencia = fecha_asistencia_entry.get()
    
    if id_estudiante == '' or fecha_asistencia == '':
        messagebox.showerror('Error', 'Por favor, complete todos los campos obligatorios.')
        return
    
    asistencia = tipo_asistencia
    
    conn = crear_conexion()
    if conn is not None:
        if id_asistencia == '':
            # Si no se proporciona un id_asistencia, insertamos una nueva asistencia
            insertar_asistencia(conn, id_asistencia, id_estudiante, fecha_asistencia, asistencia)
        else:
            # Si se proporciona un id_asistencia, actualizamos la asistencia existente
            actualizar_asistencia(conn, id_asistencia, id_estudiante, fecha_asistencia, asistencia)
        
        conn.close()
    else:
        messagebox.showerror('Error', 'No se pudo conectar a MySQL.')

    limpiar_campos()

# Función para limpiar los campos después de registrar o actualizar
def limpiar_campos():
    id_asistencia_entry.delete(0, tk.END)
    id_estudiante_entry.delete(0, tk.END)
    fecha_asistencia_entry.delete(0, tk.END)
    fecha_asistencia_entry.insert(0, date.today().strftime('%Y-%m-%d'))

# Función para borrar la fecha actual y permitir al usuario ingresar una fecha manualmente
def borrar_fecha_actual():
    fecha_asistencia_entry.delete(0, tk.END)  # Borra el contenido actual del Entry

# Función para crear la ventana principal
def crear_interfaz():
    global id_estudiante_entry, fecha_asistencia_entry, id_asistencia_entry, conn
    
    conn = crear_conexion()
    if conn is None:
        messagebox.showerror('Error', 'No se pudo conectar a MySQL.')
        return
    
    root = tk.Tk()
    root.title('Sistema de Gestión de Asistencias')
    
 
    form_frame = ttk.LabelFrame(root, text='Registro de Asistencia')
    form_frame.grid(row=0, column=0, padx=20, pady=20, sticky=tk.W)
  
    id_asistencia_label = ttk.Label(form_frame, text='ID Asistencia (opcional):')
    id_asistencia_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
    id_asistencia_entry = ttk.Entry(form_frame, width=20)
    id_asistencia_entry.grid(row=0, column=1, padx=5, pady=5)
    
  
    id_estudiante_label = ttk.Label(form_frame, text='ID Estudiante:')
    id_estudiante_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
    id_estudiante_entry = ttk.Entry(form_frame, width=20)
    id_estudiante_entry.grid(row=1, column=1, padx=5, pady=5)
    
    
    fecha_asistencia_label = ttk.Label(form_frame, text='Fecha Asistencia (YYYY-MM-DD):')
    fecha_asistencia_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
    fecha_asistencia_entry = ttk.Entry(form_frame, width=20)
    fecha_asistencia_entry.grid(row=2, column=1, padx=5, pady=5)
    
 
    borrar_fecha_button = ttk.Button(form_frame, text='Borrar Fecha Actual', command=borrar_fecha_actual)
    borrar_fecha_button.grid(row=2, column=2, padx=5, pady=5, sticky=tk.W)
   
    fecha_asistencia_entry.insert(0, date.today().strftime('%Y-%m-%d'))
   
    asistencia_label = ttk.Label(form_frame, text='Tipo de Asistencia:')
    asistencia_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
    
    presente_button = ttk.Button(form_frame, text='Presente', command=lambda: registrar_asistencia('Presente'))
    presente_button.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)
    
    falta_button = ttk.Button(form_frame, text='Falta', command=lambda: registrar_asistencia('Falta'))
    falta_button.grid(row=3, column=2, padx=5, pady=5, sticky=tk.W)
    
    tardanza_button = ttk.Button(form_frame, text='Tardanza', command=lambda: registrar_asistencia('Tardanza'))
    tardanza_button.grid(row=3, column=3, padx=5, pady=5, sticky=tk.W)
    
  
    
    root.mainloop()

if __name__ == '__main__':
    crear_interfaz()

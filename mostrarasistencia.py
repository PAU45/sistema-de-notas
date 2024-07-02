import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error

# Variables globales para los elementos de la interfaz
id_estudiante_entry = None
asistencias_tree = None


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

# Función para consultar las asistencias de un estudiante por su ID
def consultar_asistencias(conn, id_estudiante):
    try:
        cursor = conn.cursor()
        sql_select = '''
            SELECT id_asistencia, fecha_asistencia, asistencia, falta, tardanza
            FROM Asistencias
            WHERE id_estudiante = %s
        '''
        cursor.execute(sql_select, (id_estudiante,))
        asistencias = cursor.fetchall()
        return asistencias
    except Error as e:
        print(f'Ocurrió un error al consultar las asistencias: {e}')
    return None

# Función para mostrar las asistencias del estudiante seleccionado
def mostrar_asistencias():
    global id_estudiante_entry, asistencias_tree
    
    if id_estudiante_entry is None or asistencias_tree is None:
        messagebox.showerror('Error', 'Widgets no inicializados correctamente.')
        return
    
    id_estudiante = id_estudiante_entry.get()
    if id_estudiante == '':
        messagebox.showerror('Error', 'Ingrese un ID de estudiante válido.')
        return
    
    conn = crear_conexion()
    if conn is not None:
        asistencias = consultar_asistencias(conn, id_estudiante)
        conn.close()
        if asistencias:
            # Limpiar árbol antes de mostrar nuevas asistencias
            for record in asistencias_tree.get_children():
                asistencias_tree.delete(record)
            
            # Insertar las asistencias en el árbol
            for asistencia in asistencias:
                asistencias_tree.insert('', tk.END, values=asistencia)
        else:
            messagebox.showinfo('Información', f'No hay asistencias registradas para el estudiante con ID {id_estudiante}.')
    else:
        messagebox.showerror('Error', 'No se pudo conectar a MySQL.')


def crear_interfaz():
    global id_estudiante_entry, asistencias_tree
    
    root = tk.Tk()
    root.title('Sistema de Gestión de Asistencias')
   
    form_frame = ttk.LabelFrame(root, text='Consulta de Asistencias')
    form_frame.grid(row=0, column=0, padx=20, pady=20, sticky=tk.W)
    
   
    id_estudiante_label = ttk.Label(form_frame, text='ID Estudiante:')
    id_estudiante_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
    id_estudiante_entry = ttk.Entry(form_frame, width=20)
    id_estudiante_entry.grid(row=0, column=1, padx=5, pady=5)
    
   
    consultar_button = ttk.Button(form_frame, text='Consultar Asistencias', command=mostrar_asistencias)
    consultar_button.grid(row=1, column=0, columnspan=2, padx=5, pady=10)
    
    asistencias_frame = ttk.LabelFrame(root, text='Asistencias Registradas')
    asistencias_frame.grid(row=1, column=0, padx=20, pady=20, sticky=tk.W)
    
    
    asistencias_tree = ttk.Treeview(asistencias_frame, columns=('ID', 'Fecha', 'Asistencia', 'Falta', 'Tardanza'), show='headings', height=10)
    asistencias_tree.heading('ID', text='ID')
    asistencias_tree.heading('Fecha', text='Fecha')
    asistencias_tree.heading('Asistencia', text='Asistencia')
    asistencias_tree.heading('Falta', text='Falta')
    asistencias_tree.heading('Tardanza', text='Tardanza')
    asistencias_tree.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W+tk.E)
    
   
    scrollbar = ttk.Scrollbar(asistencias_frame, orient='vertical', command=asistencias_tree.yview)
    scrollbar.grid(row=0, column=1, padx=5, pady=5, sticky=tk.N+tk.S)
    asistencias_tree.configure(yscrollcommand=scrollbar.set)
    
    root.mainloop()

if __name__ == '__main__':
    crear_interfaz()
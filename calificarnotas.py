import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import errorcode


try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  
        database="estudiantespy"
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Error: Acceso denegado. Revisa tu usuario y contraseña.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Error: La base de datos especificada no existe.")
    else:
        print(f"Error: {err}")

# Función  las calificaciones por DNI
def listar_calificaciones(dni_estudiante, id_curso, entry_fields, promedio_entries, promedio_total_label):
    try:
        cursor = connection.cursor()
        query = ("SELECT c.calificacion_1A, c.calificacion_2A, c.calificacion_3A, c.calificacion_4A, "
                 "c.calificacion_1B, c.calificacion_2B, c.calificacion_3B, c.calificacion_4B, "
                 "c.calificacion_1C, c.calificacion_2C, c.calificacion_3C, c.calificacion_4C, "
                 "c.calificacion_1D, c.calificacion_2D, c.calificacion_3D, c.calificacion_4D, "
                 "c.promedio1, c.promedio2, c.promedio3, c.promedio4, c.promedio_total "
                 "FROM Calificaciones c "
                 "JOIN Estudiantes e ON c.id_estudiante = e.id_estudiante "
                 "JOIN Cursos cu ON c.id_curso = cu.id_curso "
                 "WHERE e.dni = %s AND c.id_curso = %s")
        cursor.execute(query, (dni_estudiante, id_curso))
        result = cursor.fetchone()

        if result:
            for i, field in enumerate(entry_fields):
                field.delete(0, tk.END)
                field.insert(0, result[i])
            
            for i, promedio_entry in enumerate(promedio_entries):
                promedio_entry.config(state="normal")
                promedio_entry.delete(0, tk.END)
                promedio_entry.insert(0, result[-5 + i])  # Insertar los promedios 1 a 4 y el promedio total
                promedio_entry.config(state="readonly")

            # funcionamiento para mostrar el promedio total (aclaracion del label correspondiente)
            promedio_total_label.config(text=f"Promedio Total: {result[-1]:.2f}")
        else:
            messagebox.showinfo("Información", "No se encontraron calificaciones para el DNI y curso especificados.")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error al listar calificaciones: {err}")
    finally:
        cursor.close()

# Función para actualizar los datos de la tabla
def actualizar_calificaciones(dni_estudiante, id_curso, entry_fields, promedio_entries, promedio_total_label):
    try:
        cursor = connection.cursor()

        # Actualizar las calificaciones en la base de datos
        update_query = (
            "UPDATE Calificaciones SET "
            "calificacion_1A = %s, calificacion_2A = %s, calificacion_3A = %s, calificacion_4A = %s, "
            "calificacion_1B = %s, calificacion_2B = %s, calificacion_3B = %s, calificacion_4B = %s, "
            "calificacion_1C = %s, calificacion_2C = %s, calificacion_3C = %s, calificacion_4C = %s, "
            "calificacion_1D = %s, calificacion_2D = %s, calificacion_3D = %s, calificacion_4D = %s, "
            "promedio1 = %s, promedio2 = %s, promedio3 = %s, promedio4 = %s, promedio_total = %s "
            "WHERE id_estudiante = (SELECT id_estudiante FROM Estudiantes WHERE dni = %s) "
            "AND id_curso = %s"
        )
        
        # Calculo de  los promedios y el promedio total del estudiante
        promedios = calcular_promedios(entry_fields)
        promedio_total = sum(promedios) / 4

        # Parámetros para la actualización de datos del curso
        update_params = (
            entry_fields[0].get(), entry_fields[1].get(), entry_fields[2].get(), entry_fields[3].get(),
            entry_fields[4].get(), entry_fields[5].get(), entry_fields[6].get(), entry_fields[7].get(),
            entry_fields[8].get(), entry_fields[9].get(), entry_fields[10].get(), entry_fields[11].get(),
            entry_fields[12].get(), entry_fields[13].get(), entry_fields[14].get(), entry_fields[15].get(),
            promedios[0], promedios[1], promedios[2], promedios[3], promedio_total,
            dni_estudiante, id_curso
        )
        
        cursor.execute(update_query, update_params)
        connection.commit()

        # Actualizar los campos de entrada de promedio en la GUI
        for i, promedio_entry in enumerate(promedio_entries):
            promedio_entry.config(state="normal")
            promedio_entry.delete(0, tk.END)
            promedio_entry.insert(0, f"{promedios[i]:.2f}")
            promedio_entry.config(state="readonly")

        # Actualizar el label de promedio total
        promedio_total_label.config(text=f"Promedio Total: {promedio_total:.2f}")

        messagebox.showinfo("Éxito", "Calificaciones actualizadas correctamente.")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error al actualizar calificaciones: {err}")
    finally:
        cursor.close()

def calcular_promedios(entry_fields):
    # Convertierte las entradas a números y calcular los promedios directamente
    promedios = []
    for i in range(4):
        calificaciones = [float(entry_fields[j].get()) for j in range(i, len(entry_fields), 4) if entry_fields[j].get()]
        if calificaciones:
            promedio = sum(calificaciones) / len(calificaciones)
        else:
            promedio = 0.0
        promedios.append(promedio)
    return promedios

# Configuración de la interfaz 
import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Gestión de Calificaciones de Estudiantes")
    root.geometry("1050x1050") 

    
    main_frame = tk.Frame(root, bg="#f0f0f0")
    main_frame.pack(fill="both", expand=True)

    
    header_frame = tk.Frame(main_frame, bg="#333", height=50)
    header_frame.pack(fill="x")
    tk.Label(header_frame, text="Gestión de Calificaciones de Estudiantes", font=("Arial", 18, "bold"), fg="white", bg="#333").pack(pady=10)

    
    form_frame = tk.Frame(main_frame, bg="#f0f0f0", padx=20, pady=20)
    form_frame.pack(fill="both", expand=True)

   
    tk.Label(form_frame, text="DNI Estudiante:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)
    dni_entry = tk.Entry(form_frame, font=("Arial", 12), width=20)
    dni_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

    tk.Label(form_frame, text="ID Curso:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)
    id_curso_entry = tk.Entry(form_frame, font=("Arial", 12), width=20)
    id_curso_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

   
    labels_texts = [
        "Calificación 1A", "Calificación 2A", "Calificación 3A", "Calificación 4A",
        "Calificación 1B", "Calificación 2B", "Calificación 3B", "Calificación 4B",
        "Calificación 1C", "Calificación 2C", "Calificación 3C", "Calificación 4C",
        "Calificación 1D", "Calificación 2D", "Calificación 3D", "Calificación 4D"
    ]
    entry_fields = []

    for i, label_text in enumerate(labels_texts):
        row = (i // 4) + 2
        col = (i % 4) * 2
        tk.Label(form_frame, text=label_text, font=("Arial", 10)).grid(row=row, column=col, padx=5, pady=5, sticky=tk.E)
        entry = tk.Entry(form_frame, font=("Arial", 10), width=8)
        entry.grid(row=row, column=col + 1, padx=5, pady=5, sticky=tk.W)
        entry_fields.append(entry)


    promedio_labels = ["Promedio 1", "Promedio 2", "Promedio 3", "Promedio 4"]
    promedio_entries = []

    for i, label_text in enumerate(promedio_labels):
        row = 6
        col = i * 2
        tk.Label(form_frame, text=label_text, font=("Arial", 10)).grid(row=row, column=col, padx=5, pady=5, sticky=tk.E)
        entry = tk.Entry(form_frame, font=("Arial", 10), width=8)
        entry.grid(row=row, column=col + 1, padx=5, pady=5, sticky=tk.W)
        entry.config(state="readonly")
        promedio_entries.append(entry)

    
    tk.Label(form_frame, font=("Arial", 12)).grid(row=7, column=0, padx=10, pady=10, sticky=tk.E)
    promedio_total_label = tk.Label(form_frame, text="", font=("Arial", 12))
    promedio_total_label.grid(row=7, column=1, padx=10, pady=10, sticky=tk.W)

 
    button_frame = tk.Frame(form_frame, bg="#f0f0f0")
    button_frame.grid(row=8, column=0, columnspan=2, pady=20)

    tk.Button(button_frame, text="Listar Calificaciones", font=("Arial", 12), bg="#4CAF50", fg="white", command=lambda: listar_calificaciones(dni_entry.get(), id_curso_entry.get(), entry_fields, promedio_entries, promedio_total_label)).pack(side=tk.LEFT, padx=10)

    tk.Button(button_frame, text="Actualizar Calificaciones", font=("Arial", 12), bg="#2196F3", fg="white", command=lambda: actualizar_calificaciones(dni_entry.get(), id_curso_entry.get(), entry_fields, promedio_entries, promedio_total_label)).pack(side=tk.LEFT, padx=10)


    
    boton_salir = tk.Button(
    button_frame, 
    text="Salir",
    command=root.destroy,  
    bg="#9E9E9E", 
    fg="white",  
    relief="raised",  
    bd=3,  
    padx=10,  
    pady=5  
)
    boton_salir.pack(side=tk.RIGHT, padx=10, pady=20)
    root.mainloop()

def iniciar_interfaz():
    main()                                                                                                                                  

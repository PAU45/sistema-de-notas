import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import mysql.connector

def obtener_calificaciones_estudiante(id_estudiante):
    try:
        
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  
            database="estudiantespy"
        )

        #un cursor para ejecutar consultas
        cursor = connection.cursor()

        # Consulta para obtener las calificaciones del estudiante con el nombre del curso
        consulta = f"""
            SELECT C.nombre, CA.CALIFICACION_1A, CA.CALIFICACION_2A, CA.CALIFICACION_3A, CA.CALIFICACION_4A,
                   CA.CALIFICACION_1B, CA.CALIFICACION_2B, CA.CALIFICACION_3B, CA.CALIFICACION_4B,
                   CA.CALIFICACION_1C, CA.CALIFICACION_2C, CA.CALIFICACION_3C, CA.CALIFICACION_4C,
                   CA.CALIFICACION_1D, CA.CALIFICACION_2D, CA.CALIFICACION_3D, CA.CALIFICACION_4D
            FROM Calificaciones CA
            INNER JOIN Cursos C ON CA.ID_CURSO = C.id_curso
            WHERE CA.ID_ESTUDIANTE = {id_estudiante}
        """
        cursor.execute(consulta)

        # Obtener las calificaciones del estudiante
        calificaciones = cursor.fetchall()

        # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()

        return calificaciones

    except mysql.connector.Error as error:
        print("Error al conectar a MySQL:", error)
        return None

def generar_reporte(usuario):
    ruta_guardado = "notas/carpeta/notas"

    id_estudiante = usuario[0]  
    nombre = usuario[2]
    apellido = usuario[3]
    grado = usuario[6]
    seccion = usuario[7]

    # Obtener las calificaciones del estudiante
    calificaciones = obtener_calificaciones_estudiante(id_estudiante)

    if calificaciones:
        # Crear la carpeta si no existe
        if not os.path.exists(ruta_guardado):
            os.makedirs(ruta_guardado)

        # Nombre del archivo PDF
        nombre_archivo = f"{ruta_guardado}\\Reporte_{nombre}_{apellido}.pdf"

        # Crear el documento PDF
        c = canvas.Canvas(nombre_archivo, pagesize=letter)
        c.setTitle(f"Reporte de {nombre} {apellido}")

        # Información del estudiante en el PDF
        c.setFont("Helvetica-Bold", 14)
        c.drawString(100, 750, f"Informe de Estudiante: {nombre} {apellido}")
        c.setFont("Helvetica", 12)
        c.drawString(100, 730, f"Grado: {grado} - Sección: {seccion}")

        # Información de calificaciones en el PDF
        c.setFont("Helvetica-Bold", 12)
        c.drawString(100, 700, "Calificaciones:")

        # Configuración de posición y conteo de cursos por página
        y_position = 680
        cursos_por_pagina = 4
        cursos_imprimidos = 0
        pagina_actual = 1

        for calificacion in calificaciones:
            nombre_curso = calificacion[0]  # Nombre del curso obtenido de la consulta
            notas = calificacion[1:]  # Notas de los 4 períodos

            # Calcular promedio del curso
            promedio_curso = sum(notas) / len(notas)

            # Imprimir información del curso y notas por período
            c.drawString(120, y_position, f"Curso: {nombre_curso}")
            y_position -= 20

            for i in range(4):
                periodo = f"  Período {i+1}: Nota = {notas[i]}"
                c.drawString(140, y_position, periodo)
                y_position -= 20

            # Imprimir promedio del curso
            c.drawString(140, y_position, f"  Promedio del curso: {round(promedio_curso, 2)}")
            y_position -= 20

            y_position -= 10  # Espacio entre cursos
            cursos_imprimidos += 1

            # Si se han impreso 4 cursos, pasar a la siguiente página
            if cursos_imprimidos == cursos_por_pagina:
                c.drawString(100, 50, f"Página {pagina_actual}")
                pagina_actual += 1
                cursos_imprimidos = 0
                c.showPage()
                c.setFont("Helvetica-Bold", 12)
                c.drawString(100, 700, "Calificaciones:")
                y_position = 680

        # Guardar el PDF y cerrar el archivo
        c.save()

        print(f"Reporte generado correctamente: {nombre_archivo}")
    else:
        print(f"No se encontraron calificaciones para el estudiante: {nombre} {apellido}")



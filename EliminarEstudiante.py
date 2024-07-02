import mysql.connector


def eliminar_estudiante(estudiante):
  
    id_estudiante = estudiante[0]

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="estudiantespy"
    )

    # Crea un cursor para ejecutar consultas
    cursor = connection.cursor()

    try:
        # Deshabilita temporalmente las restricciones de clave externa
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0")

        # Elimina las calificaciones asociadas al estudiante
        consulta_calificaciones = "DELETE FROM Calificaciones WHERE id_estudiante = %s"
        valores_calificaciones = (id_estudiante,)
        cursor.execute(consulta_calificaciones, valores_calificaciones)

        # Elimina al estudiante
        consulta_estudiante = "DELETE FROM Estudiantes WHERE id_estudiante = %s"
        valores_estudiante = (id_estudiante,)
        cursor.execute(consulta_estudiante, valores_estudiante)

        # Confirma los cambios en la base de datos
        connection.commit()

        # Muestra un mensaje de éxito
        print("Eliminación Exitosa: El estudiante y sus calificaciones asociadas han sido eliminados.")
    except Exception as e:
        # Muestra un mensaje de error
        print("Error al eliminar estudiante:", str(e))
    finally:
        # Habilita nuevamente las restricciones de clave externa
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1")

        # Cierra el cursor y la conexión
        cursor.close()
        connection.close()


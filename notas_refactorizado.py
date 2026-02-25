"""
Sergio Alcántara Martínez
Dado los datos de un alumno (nombre y tres notas), muestra por consola su nombre, sus notas, la media de las notas y su calificación (sobresaliente, notable, aprobado o suspenso).
"""

"""
Calcula la media aritmética de tres notas.
Args:
    n1 (float): Primera nota del alumno.
    n2 (float): Segunda nota del alumno.
    n3 (float): Tercera nota del alumno.
Returns:
    float: La media de las tres notas (valor entre 0 y 10).
"""
def medianOf3Numbers(n1, n2, n3): # Si fuese necesario, modificar la funcion de manera que se pueda realizar la media de X numero de notas, en vez de extrictamente 3. Ej pasando un lista de notas en vez de un argumento por nota.
    return (n1 + n2 + n3) / 3

"""
Comprueba de calificación le corresponde a una nota pasada.
Args:
    score (float): nota del alumno.
Returns:
    String: Calificación.
"""
def checkGrade(score):
    if score >= 9:
        return "Sobresaliente"
    elif score >= 7 and score < 9:
        return "Notable"
    elif score >= 5 and score < 7:
        return "Aprobado"
    elif score < 5:
        return "Suspenso"

"""
Muestra por consola todos los datos de un alumno pasados sus nombre y notas.
Args:
    nombre (str): Nombre del alumno.
    n1 (float): Primera nota del alumno.
    n2 (float): Segunda nota del alumno.
    n3 (float): Tercera nota del alumno.
"""
def mostrar(nombre, n1, n2, n3):
    print("Alumno: " + nombre)
    print("Nota 1: " + str(n1))
    print("Nota 2: " + str(n2))
    print("Nota 3: " + str(n3))
    media = medianOf3Numbers(n1, n2, n3) 
    print("Media: " + str(media)) # Codigo modificado por cuestones de consistencia
    calificacion = checkGrade(media)
    print(calificacion)
    print("----------------------")

def main():
    mostrar("Ana García", 8, 7, 9)
    mostrar("Luis Pérez", 4, 5, 3)
    mostrar("Marta Gómez", 6, 7, 5)
main()
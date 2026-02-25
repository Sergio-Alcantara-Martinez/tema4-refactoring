def medianOf3Numbers(n1, n2, n3):
    return (n1 + n2 + n3) / 3
    
def checkGrade(score):
    if score >= 9:
        return "Sobresaliente"
    elif score >= 7 and score < 9:
        return "Notable"
    elif score >= 5 and score < 7:
        return "Aprobado"
    elif score < 5:
        return "Suspenso"

def mostrar(nombre, n1, n2, n3):
    print("Alumno: " + nombre)
    print("Nota 1: " + str(n1))
    print("Nota 2: " + str(n2))
    print("Nota 3: " + str(n3))
    media = medianOf3Numbers(n1, n2, n3)
    print("Media: " + str(media))
    calificacion = checkGrade(media)
    print(calificacion)
    print("----------------------")

def main():
    mostrar("Ana García", 8, 7, 9)
    mostrar("Luis Pérez", 4, 5, 3)
    mostrar("Marta Gómez", 6, 7, 5)
main()
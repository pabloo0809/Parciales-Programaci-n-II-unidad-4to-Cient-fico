import random

nota=random.randint(0,100)
clasificacion=""

if nota <60:
    clasificacion="Reprobado"
    print("el puntaje fue: ", nota, "La clasificacion fue: ", clasificacion)
else:
    clasificacion="Aprobado"
    print("el puntaje fue: ", nota, "La clasificacion fue: ", clasificacion)
if nota <70:
    clasificacion="Recuperacion"
    print("el puntaje fue: ", nota, "La clasificacion fue: ", clasificacion)

elif nota <=90 and nota <100:
    clasificacion="excelente"
    print("el puntaje fue: ", nota, "La clasificacion fue: ", clasificacion)
else:
    clasificacion="Muy bueno"
    print("el puntaje fue: ", nota, "La clasificacion fue: ", clasificacion)




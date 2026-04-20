Algoritmo Parcial_Progra_II_bloque
	Definir nota Como Entero
	nota <- Aleatorio(1,100)
	
	si nota <70 Entonces
		Escribir "recuperacion"
	FinSi
		si nota <60 Entonces
			Escribir "reprobado"
		sino 
			Escribir "Aprobado"
			si nota >=90 Entonces
				Escribir "Excelente"
			SiNo
				Escribir "muy bueno"
		FinSi
		FinSi
	
FinAlgoritmo

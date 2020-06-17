                    ########################################
                    #           EJercicios 1,2             # 
                    #    PROGRAMACIÓN LÓGICA Y FUNCIONAL   #
                    ########################################
                    
                    
                    
########################################
#Garcia Sabino Montserrat              #
#Mejia Chavez Maria Fernanda           #
########################################
"""
# Programación  Lógica



# Modus ponendo ponens

"el modo que, al afirmar, afirma"

P → Q. P ∴ Q


Se puede encadenar usando algunas variables

P → Q. 
Q → S. 
S → T. P ∴ T

Ejercicio 
Defina una funcion que resuelva con verdadero o falso segun corresponada

Laura esta en Queretaro
Alena esta en Paris
Claudia esta en San Francisco
Queretaro esta en Mexico
Paris esta en Francia
San Francisco esta en EUA
Mexico esta en America
Francia esta en Europa
EUA esta en America
"""

#####Ejercicio1 MPP

Base = [
	["Laura","Queretaro"],
    ["Alena","Paris"],
    ["Claudia","San Francisco"],
    ["Queretaro","Mexico"],
    ["Paris","Francia"],
    ["San Francisco","EUA"],
    ["Mexico","America"],
    ["Francia","Europa"],
	["EUA","America"]
]

def ver_fals(X,Y):
	if not X:
		return []
	if len(X):
		if Y == X[0][0]:
			return X[0][1]
		else:
			return ver_fals(X[1:],Y)


def esta (E1,E2):
	R = ver_fals(Base,E1)
	L = ver_fals(Base, R)
	if L == E2 or R == E2:
		return True
	S = ver_fals(Base, L)
	if S == E2:
		return True
	else:
		return False



print(esta("Alena","Europa"))
# true

print(esta("Laura","America"))
# true

print(esta("Laura","Europa"))
# false


#########Ejercicio 2 logfun 
"""
	https://www.computrabajo.com.mx/ofertas-de-trabajo/oferta-de-trabajo-de-desarrollador-batch-exp-sistemas-abiertos-en-queretaro-601BC72F6CEBB0F761373E686DCF3405
	En una empresa solicitan Lic./Ing. en Sistemas, Computación o afín.
	con los siguientes requisitos:
	• Oracle BBDD

	• SQL y PL/SQL

	• Linux

	• Unix

	• Shell (Linux - Unix)

	• C++, Proc*C y Tuxedo V12 o anteriores

	• Visual Basic 6.0

	• Java (Frameworks) , Web Services y Micro Servicios APIs
	
	Realizar un programa que realice preguntas al usuario
	y que apartir de sus respuestas evalue si es cadidato o no
	
	(usen conjuntos)

"""

Requisitos = {
	"Oracle","SQL/PL","Linux","Unix","Shell","C++",
	"Proc*C","TuxedoV12", "VB6", "Java","WebServices","MicroServicios"
} 


print("¿Qué lenguajes de programacion maneja? ")
RequisitoEmp = input()
X = RequisitoEmp.replace(' ','')
R = X.split(',')
S = set(R)
Requisitos = Requisitos <= S

print("¿Es candidato?: ",Requisitos)






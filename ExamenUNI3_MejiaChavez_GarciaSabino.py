                    ########################################
                    #           EXAMEN UNIDAD 3            # 
                    #    PROGRAMACIÓN LÓGICA Y FUNCIONAL   #
                    ########################################
                    
                    
                    
########################################
#Garcia Sabino Montserrat              #
#Mejia Chavez Maria Fernanda           #
########################################
"""

 Primos  <generadores>  30 pts

	Realice una generador que devuelva  de todos lo numeros primos
	existentes de 0 hasta n-1 que cumpla con el siguiente prototipo:
	
	def gprimo(N):
		pass
	
	
	a = gprimo(10)
	z = [e for e in a]
	print(z)
	# [2, 3 ,5 ,7 ]
"""
print('')
print('N U M E R O S  P R I M O S')
def generador1(M):
	j=1
	i=1
	c=0
	while i<(M+1):
		while j<(M+1):
			if i%j==0:
				c=c+1
			j=j+1
		if c == 2:
			yield i
		c=0
		i=i+1
		j=1
a=[z for z in generador1(30)]
print(a)
print('')
"""
Bada Boom!!! <generadores> 20 pts
	
	Defina un generador que reciba un numero entero positivo mayor a 0 N,
	dicho generador proporciona numero de 1 hasta N
	con las siguientes condiciones:
		1) si es multiplo de 3 coloque la cadena "Bada"
		2) si es multiplo de 5 coloque la cadena "Boom!!"
		3) si es multiplo de 3 y 5 coloque "Bada Boom!!"
		
	def genBadaBoom(N):
		pass
		
	a = genBadaBoom(10)
	z = [e for e in a]
	print(z)
	#[1,2,"Bada",4,"Boom","Bada",7,8,"Bada","Boom"]
"""
print('')
print(' B A D A B O O M ')	
def genBadaBoom(max):
	i=1
	while i<max:
		if i%3 ==0 and i%5==0:
			yield "Bada Boom!!"
		elif i%3==0:
			yield "Bada"
		elif i%5==0:
			yield "Boom"
		else:
			yield i
		i = i + 1
a = genBadaBoom(31)
z = [e for e in a]
print(z)

"""
Combinaciones <Comprensión de listas> 30pts

	Una tienda de ropa quiere saber cuantos conjuntos se pueden crear 
	a partir de un grupo de 5 camisas (roja,negra,azul,morada y cafe),      
	4 pantalones (negro, azul, cafe obscuro y crema) y uno de 4 accesorios
	posibles (cinturon, tirantes, lentes, fedora)
	
	1) Obtenga una lista con todos los conjuntos posibles e imprimala en pantalla
	2) imprima un mensaje donde mencione la cantidad de conjuntos posibles
	
"""
print ('')
print(' C O M B I N A C I O N   D E   C O N J U N T O S ')	
C=['roja','negra','azul','morada','cafe']
P=['negro','azul','cafe','obscuro','crema']
A=['cinturon','tirantes', 'lentes', 'fedora']
print([(x, y, z) for x in C for y in P for z in A])
R=[(x, y, z) for x in C for y in P for z in A]
print("Cantidad de combinaciones")
print(len(R))
print('')

"""
    
¿Fedora?  <Comprensión de listas >  15 pts

	Del problema anterior imprima una lista que tenga todos los conjuntos
	que incluyen un sombrero fedora y tambien despliegue su longitud
	
	
"""
print ('')
print(' C O M B I N A C I O N   D E   C O N J U N T O S ** F E D O R A ** ')	
C=['roja','negra','azul','morada','cafe']
P=['negro','azul','cafe','obscuro','crema']
A=['cinturon','tirantes', 'lentes', 'fedora']
print([(x, y, z) for x in C for y in P for z in A if z=='fedora'])
R=[(x, y, z) for x in C for y in P for z in A if z=='fedora']
print("Cantidad de combinaciones")
print(len(R))
print('')

"""
<Monads>   30 pts

--Lacrimosa - Durch Nacht und Flut --   

Die Suche endet jetzt und hier
Gestein kalt und nass
Granit in Deiner Brust
Der Stein der Dich zerdrückt
Der Fels der Dich umgibt
Aus dem gehauen Du doch bist

Despiertate te busco
Mi corazon abreté te libro
Elevate mi luz y prende mi llama
Si a ti, yo se, te encontrare

El fragmento anterior es un canción del duo lacrimosa

Usando Monads obtenga la letra 
que menos se repite por cada linea y obtenga la probabilidad de sacar dicha
letra.

Nota: Pueden ayudarse de funciones recursivas y compresiones de lista. 

"""
print('')
print(' M O N A D S  L A C R I M O S A ')
L=     [
        ("Die Suche endet jetzt und hier"),
        ("Gestein kalt und nass"),
        ("Granit in Deiner Brust"),
        ("Der Stein der Dich zerdrückt"),
        ("Der Fels der Dich umgibt"),
        ("Aus dem gehauen Du doch bist"),
        ("Despiertate te busco"),
        ("Mi corazon abreté te libro"),
        ("Elevate mi luz y prende mi llama"),
        ("Si a ti, yo se, te encontrare"),
        ]
Z = map(lambda a: a ,L)
def cuLetras(a):
    a = list(a)
    return a
R = map(cuLetras,Z)
Y =list(R)
print(cuLetras(Y))
def revisar(let,la,le,li,lo):
    if 0 != len(let):
        if ((let[0]) =='a'):
            la = la + 1
        if ((let[0]) =='e'):
            le = le + 1
        if ((let[0]) =='i'):
            li = li +1
        if ((let[0])=='o'):
            lo = lo +1
        revisar(let[1:],la,le,li,lo)
        print("[",la,",",le,"]")
    return None
revisar(cuLetras(Y),0,0,0,0)
"""
##ESTE EJERCICIO LO INTENTAMOS RESOLVER DE DOS FORMAS LA ANTERIOR Y ESTA COMENTADA##

print(' M O N A D S  L A C R I M O S A **Version 2** ')
Rolon="Die Suche endet jetzt und hier Gestein kalt und nass Granit in Deiner Brust Der Stein der Dich zerdrückt Der Fels der Dich umgibt Aus dem gehauen Du doch bist Despiertate te busco Mi corazon abreté te libro Elevate mi luz y prende mi llama Si a ti, yo se, te encontrare"
def lacrimosa(String):
	Lista=list(String)
	Mapeo=map(lambda e: e,Lista)
	Lmapeo=list(Mapeo)
	Elementos=unicoslacrimosa(Lmapeo)
	menor=repetidoslacrimosa(Elementos,Lmapeo)
	print(menor)
	Probabilidad=probalacrimosa(menor,len(Lmapeo))
	return Probabilidad
	print(Probabilidad)



def unicoslacrimosa(L,A=[]):
	if not L:
		return A
	if not A:
		A = []
	PL = L[0]
	if PL in A:
		return unicoslacrimosa(L[1:],A)
	else:
		return unicoslacrimosa(L[1:], A + [PL])
def unicos2paranoid(L):
	return unicoslacrimosa(L,[])

def repetidoslacrimosa(U,L):
	if not U:
		return
	A=U[0]
	B=filter(lambda e: e==A,L)
	print(A,len(list(B)))
	return repetidoslacrimosa(U[1:],L)
	


def probalacrimosa(U,D):
	X=isinstance(U, int)
	A=X*100
	proba=A/D
	return proba

A=lacrimosa(Rolon)
#print('El caracter menos repetido de este fragmento de rolon es: ')
#print (mr)
print(' Y su probabilidad de salir entre el resto de caracteres es de: ')
print(A ,"%")
"""


"""
<Monads>

--Hole in my soul apocalyptica--  20 pts

There's a hole in my heart, in my life, in my way
And it's filled with regret and all I did, to push you away
If there's still a place in your life, in your heart for me
I would do anything, so don't ask me to leave

I've got a hole in my soul where you use to be
You're the thorn in my heart and you're killing me
I wish I could go back and do it all differently
I wish that I'd treated you differently
'Cause now there's a hole in my soul where you use to be

El fragmento anterior es un canción del grupo apocalyptica

Usando Monads obtenga la letra 
que menos se repite de todo el fragmento y obtenga la probabilidad de sacar dicha
letra.

Nota: Pueden ayudarse de funciones recursivas y compresiones de lista. 

"""
print('')
print(' M O N A D S  S O U L ')
L = ("There's a hole in my heart, in my life, in my way"
"And it's filled with regret and all I did, to push you away"
"If there's still a place in your life, in your heart for me"
"I would do anything, so don't ask me to leave"
"I've got a hole in my soul where you use to be"
"You're the thorn in my heart and you're killing me"
"I wish I could go back and do it all differently"
"I wish that I'd treated you differently"
"'Cause now there's a hole in my soul where you use to be")
#separadas por caracter
Z = map(lambda a: str(a),L)
Y = list(Z)
print(Y)
def revisar(let,la,lb,lc,ld,le,lf,lg,lh,li,lj,lk,ll,lm,ln,lo,lp,lq,lr,ls,lt,lu,lv,lw,lx,ly,lz,s):
    if 0 != len(let):
        if ((let[0]) =='a'or (let[0]) =='A'):
            la = la + 1
            s = s + 1
        if ((let[0]) =='b'or (let[0]) =='B'):
            lb = lb + 1
            s = s + 1
        if ((let[0]) =='c'or (let[0]) =='C'):
            lc = lc + 1
            s = s + 1
        if ((let[0]) =='d'or (let[0]) =='D'):
            ld = ld + 1
            s = s + 1
        if ((let[0]) =='e'or (let[0]) =='E' ):
            le = le + 1
            s = s + 1
        if ((let[0]) =='f'or (let[0]) =='F'):
            lf = lf + 1
            s = s + 1
        if ((let[0]) =='g'or (let[0]) =='G'):
            lg = lg + 1
            s = s + 1
        if ((let[0]) =='h'or (let[0]) =='H'):
            lh = lh + 1
            s = s + 1
        if ((let[0]) =='i'or (let[0]) =='i'):
            li = li + 1
            s = s + 1
        if ((let[0]) =='j'or (let[0]) =='J'):
            lj = lj + 1
            s = s + 1
        if ((let[0]) =='k'or (let[0]) =='K'):
            lk = lk + 1
            s = s + 1
        if ((let[0]) =='l'or (let[0]) =='L'):
            ll = ll + 1
            s = s + 1
        if ((let[0]) =='m'or (let[0]) =='M'):
            lm = lm + 1
            s = s + 1
        if ((let[0]) =='n'or (let[0]) =='N'):
            ln = ln + 1
            s = s + 1
        if ((let[0]) =='o'or (let[0]) =='O'):
            lo = lo + 1
            s = s + 1
        if ((let[0]) =='P'or (let[0]) =='P'):
            lp = lp + 1
            s = s + 1
        if ((let[0]) =='q'or (let[0]) =='Q'):
            lq = lq + 1
            s = s + 1
        if ((let[0]) =='r'or (let[0]) =='R'):
            lr = lr + 1
            s = s + 1
        if ((let[0]) =='s'or (let[0]) =='S'):
            ls = ls + 1
            s = s + 1
        if ((let[0]) =='t'or (let[0]) =='T'):
            lt = lt + 1
            s = s + 1
        if ((let[0]) =='u'or (let[0]) =='U'):
            lu = lu + 1
            s = s + 1
        if ((let[0]) =='V'or (let[0]) =='V'):
            lv = lv + 1
            s = s + 1
        if ((let[0]) =='w'or (let[0]) =='w'):
            lw = lw + 1
            s = s + 1
        if ((let[0]) =='x'or (let[0]) =='X'):
            lx = lx + 1
            s = s + 1
        if ((let[0]) =='y'or (let[0]) =='Y'):
            ly = ly + 1
            s = s + 1
        if ((let[0]) =='z'or (let[0]) =='Z'):
            lz = lz + 1
            s = s + 1
            
        print(s)
        revisar(let[1:],la,lb,lc,ld,le,lf,lg,lh,li,lj,lk,ll,lm,ln,lo,lp,lq,lr,ls,lt,lu,lv,lw,lx,ly,lz,s)
    return  s

revisar(Y,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
print(revisar(Y,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0))

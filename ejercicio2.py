print ("Ejercicio 1:Suma impares")

def parte1(n):
    print ("Parte 1.")
    impar=0
    for i in range(0,n):
        if ( i%2 ==1):#Para saber si el numero es impar
            impar=impar + i#sumatoria de impares.
    print(impar)

def parte2(min,max):
    print ("Parte 2.")
    impar=0
    for i in range(min,max):
        if ( i%2 ==1):#Para saber si el numero es impar
            impar=impar + i
    print(impar)

    
parte1(6)
numero= int(input("Ingresa un número para suma de impares: ")) 
parte1(numero)

parte2(6,30)
minimo= int(input("Ingresa un número para variable min: ")) 
maximo= int(input("Ingresa un número para variable max: ")) 
parte2(minimo,maximo)
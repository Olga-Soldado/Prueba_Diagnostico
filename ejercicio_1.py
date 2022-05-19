print ("Ejercicio 1:Solo pares")

def parte1(n):
    print ("Parte 1.")
    cantidad=n
    par=0
    for i in range(0,30):
        if par <n: #condicional para que solo muestre la cantidad requeirda.
            if ( i%2 ==0):#Para saber si el numero es par
                print (i)
                par=par + 1

def parte2(n):
    print ("Parte 2.") 
    cantidad=n
    par=0
    for i in range(1,30):#se modifica para que comience el bucle en 1 cambie el resultado.
        if par <n: #condicional para que solo muestre la cantidad requeirda.
            if ( i%2 ==0):#Para saber si el numero es par
                print (i)
                par=par + 1

parte1(4)
parte2(4)
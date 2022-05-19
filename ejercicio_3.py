print ("Ejercicio 1:Serie Fibbonacci")

def parte1(n):
    a=0#primer numero de la serie
    b=1#segundo numero de la serie ,se supone que es 1**2 pero como se sabe 1 x 1 =1.
    for i in range(n):
        fibbo = a + b#aqui se suman los 2 anteriores se tomaria en este caso 0 +1=1 fibbo tendria el valor de 1
        a=b #a tomaria el valor de b que en esta ocacion es 1
        b= fibbo #b toamria el valor actual de fiboo que en este caso es 1
    return (a)#se retorna en cada ejecucion de la funcion el valor actual de b 

print("Solucion 1:")
#ciclo para ir iterando los numeros de la secuencia.
for j in range (7):
    print (parte1(j))


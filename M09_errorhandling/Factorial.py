def factorial(numero):
    if(numero <= 1):
        return numero
    
    resultado = numero*(numero-1)
    numero -= 1 
    while(numero>1):
        resultado = resultado *(numero-1)
        numero = numero-1
    return resultado


print("el factorial de 3 es",factorial(3))#6
print("el factorial de 4 es",factorial(4))#24
print("el factorial de 5 es",factorial(5))#24
print("el factorial de 6 es",factorial(6))#24
print("el factorial de 7 es",factorial(7))#24

def Factoriales(lista):
    lista2 = []
    for i in lista:
        lista2.append(factorial(i))
        print(lista2)

Factoriales([1,2,3,4,5,6,7])
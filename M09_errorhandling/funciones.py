class funciones:
    def __init__(self, lista_numeros):
        if (type(lista_numeros) != list):
            self.lista = []
            raise ValueError('Se ha creado una lista vacía. Se esperaba una lista de núemeros enteros')  
        else:
            self.lista = lista_numeros

    def comprobar_primo(self, n):
        if(n>1):
            for div in range(2, n):
                if n % div == 0:
                    return False  
            return True    
        else:
            return False

    def moda(self):
        repetidos={}
        lista = self.lista
        lista.sort()
        for num in lista:
            if(num not in repetidos):
                repetidos[lista.count(num)]=num 
        lista.count(num)
        repe= max(repetidos.keys())

        numero = (repetidos.get(repe))

        repetidos.clear()
        repetidos = [numero,repe]
        #repetidos["numero"] = numero
        #repetidos["repeticiones"] = repe#repeticiones

        return(repetidos)

    def convertir(self, grados, unidad, unidad_destino):
        if (unidad == "celsius"):
            if (unidad_destino == "celsius"):
                unidad_destino = grados
            elif (unidad_destino == "farenheit"):
                unidad_destino = (grados * 9 / 5) + 32
            elif (unidad_destino == "kelvin"):
                unidad_destino = grados + 273.15
            else:
                print("Parámetro de Destino incorrecto")
        elif (unidad == "farenheit"):
            if (unidad_destino == "celsius"):
                unidad_destino = (grados - 32) * 5 / 9
            elif (unidad_destino == "farenheit"):
                unidad_destino = grados
            elif (unidad_destino == "kelvin"):
                unidad_destino = ((grados - 32) * 5 / 9) + 273.15
            else:
                print("Parámetro de Destino incorrecto")
        elif (unidad == "kelvin"):
            if (unidad_destino == "celsius"):
                unidad_destino = grados - 273.15
                unidad_destino = ((grados - 273.15) * 9 / 5) + 32
            elif (unidad_destino == "kelvin"):
                unidad_destino = grados
            else:
                print("Parámetro de Destino incorrecto")
        else:
            print("Parámetro de Origen incorrecto")
        return unidad_destino

    def factorial(self,numero):
        if(type(numero) != int):
            return "El numero debe ser un entero"
        if(numero < 0):
            return "El numero debe ser positivo"
        if (numero > 1):
            numero = numero * self.factorial(numero - 1)
        return numero

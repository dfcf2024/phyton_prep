class Herramientas:
    def __init__(self, lista_numeros):
        self.lista = lista_numeros

    def verifica_primo(self):
        resultados = []  # Creamos una lista para almacenar los resultados
        for num in self.lista:
            # Verificamos si el número es primo
            es_primo = self.es_primo(num)
            resultados.append(es_primo)  # Agregamos el resultado a la lista de resultados
        # Iteramos sobre cada número en la lista original y su resultado correspondiente
        for num, resultado in zip(self.lista, resultados):
            if resultado:
                print(f"{num} es un número primo.")
            else:
                print(f"{num} no es un número primo.")

    def es_primo(self, num):
        if num > 1:
            # Verificamos si el número es divisible por algún otro número
            for i in range(2, num):
                if num % i == 0:
                    return False
            return True
        else:
            return False
        

        
    
    def valor_modal(self, lista_numeros):
        frecuencia_numeros = {}
        for numero in lista_numeros:
            if numero in frecuencia_numeros:
                frecuencia_numeros[numero] += 1
            else:
                frecuencia_numeros[numero] = 1
        
        max_frecuencia = max(frecuencia_numeros.values())
        numero_mas_repetido = [numero for numero, frecuencia in frecuencia_numeros.items() if frecuencia == max_frecuencia]
    
        print(f"El número(s) que más se repite(n) es/son {numero_mas_repetido}, y se repite {max_frecuencia} veces.")

        

    def conversion_grados(self, origen, destino):
        for num in self.lista:
            valor_destino = None
            if origen == 'celsius':
                if destino == 'celsius':
                    valor_destino = num
                elif destino == 'farenheit':
                    valor_destino = (num * 9 / 5) + 32
                elif destino == 'kelvin':
                    valor_destino = num + 273.15
                else:
                    print('Parámetro de Destino incorrecto')
            elif origen == 'farenheit':
                if destino == 'celsius':
                    valor_destino = (num - 32) * 5 / 9
                elif destino == 'farenheit':
                    valor_destino = num
                elif destino == 'kelvin':
                    valor_destino = ((num - 32) * 5 / 9) + 273.15
                else:
                    print('Parámetro de Destino incorrecto')
            elif origen == 'kelvin':
                if destino == 'celsius':
                    valor_destino = num - 273.15
                elif destino == 'farenheit':
                    valor_destino = ((num - 273.15) * 9 / 5) + 32
                elif destino == 'kelvin':
                    valor_destino = num
                else:
                    print('Parámetro de Destino incorrecto')
            else:
                print('Parámetro de Origen incorrecto')
            print(f"{num} grados {origen} son {valor_destino} grados {destino}")


    def factorial(self, numero):
        if type(numero) != int:
            return 'El numero debe ser un entero'
        if numero < 0:
            return 'El numero debe ser positivo'
        if numero > 1:
            numero = numero * self.factorial(numero - 1)
        return numero

    def calcular_factoriales(self):
        for num in self.lista:
            print(f"El factorial de {num} es {self.factorial(num)}")


  
        

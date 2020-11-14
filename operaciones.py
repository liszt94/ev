
import json
class operaciones():
    def ejercicio_uno(self):
        try:
            for x in range(1, 100):
                if (x % 2 == 0):
                    print("numero:", x, "buzz")

                if (x % 3 == 0):
                    print("numero:", x, "fizz")

                if (x % 2 != 0 and x % 3 != 0):
                    print("numero:", x, "fizzbuzz")

        except Exception as e:
            print("error en ejercicio_uno: ", e)

    def ejercicio_dos(self,string):
        repetidos = {}
        try:
            for char in string:

                if char in repetidos:

                    repetidos[char] += 1
                else:

                    repetidos[char] = 1
            for key, value in repetidos.items():
                if value > 1:
                    print("Letra repetida:",key, end=" ")
            print()
        except Exception as e:
            print("Error al encontrar elementos duplicados: ", e)


    def ejercicio_tres(self,string):
        try:
            print("Original: ", string)
            data_dict = json.loads(string)
            print("Diccionario: ", data_dict)
        except Exception as e:
            print("Error al convertir el string a dict: ", e)


    def ejercicio_cuatro(self,lista):
        items_repetidos = []
        i = 0
        j = 1

        try:
            list_aux = lista[:]
            for x in range(i, len(lista)):
                for y in range(j, len(lista)):

                    if (lista[x] == lista[y]):
                        items_repetidos.append(lista[x])

                        list_aux.remove(lista[x])

                j = j + 1
            print("Lista modificada: ", list_aux)
        except Exception as e:
            print("error al eliminar elementos 1repetidos de la lista: ", e)






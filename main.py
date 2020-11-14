# This is a sample Python script.

from operaciones import operaciones




# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    obj_operaciones = operaciones()

    string_dos = "zapato"
    string_tres = '{"nombre" : "Monica", "Edad" : 20, "cel" : 3452661}'
    lista = [88, 34, 13, 88, 1, 2, 81, 15, 77, 13, 50]

    obj_operaciones.ejercicio_uno()
    obj_operaciones.ejercicio_dos(string_dos)
    obj_operaciones.ejercicio_tres(string_tres)
    obj_operaciones.ejercicio_cuatro(lista)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

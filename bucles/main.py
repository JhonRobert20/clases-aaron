compras = {"Aaron": 8, "Jhon": 5, "Ruben": 4 }


def muestra_lista_compra(lista_compra):
    for nombre, dinero in lista_compra.items():
        print("Hoy {} tuvo un gasto de {} ".format(nombre,dinero) )    


muestra_lista_compra(compras)


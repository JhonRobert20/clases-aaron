compras = {"Aaron": 8, "Jhon": 5, "Ruben": 4 }

archive = open("texto2.txt","w")

for name, dinero in compras.items():
    add_text= "el usuario {} tiene un gasto {} \n".format(name,dinero)

    archive.write(add_text)


archive = open("texto.txt")

for line in archive:
    name, spent = line.split(",")

    print("{} a efectuado este gasto {}".format(name,spent))


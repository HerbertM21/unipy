if __name__ == "_main_":
    
    archivo=open("Clase01/adn.txt")
    for elem in archivo:
        miCad=elem.rstrip("\n")
        lista=miCad.split(" ")

    cad1 = lista[0]
    cad2 = lista[1]
    
    print(f"Mis cadenas son: {cad1} y {cad2}")
    
    tamano = len(cad2)
    subcadenaFinal = " "
    for i in range(tamano): 
        for j in range(i+1):
            if(cad1.count(cad2[j:tamano+j-i]) != 0 and subcadenaFinal==" "):
                subcadenaFinal=cad2[j:tamano+j-i]
    print("la mayor subcadena final es",subcadenaFinal)
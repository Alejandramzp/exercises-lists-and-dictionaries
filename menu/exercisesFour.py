from logica.exercisesFour import loteria,formato_fecha

def designFourList():
    numero= int(input("Cuales son los numeros ganadores de la loteria?: "))
    print(loteria(numero))
    
def designFourDict():
    fecha=input("Cual es la fecha? ejemplo: dd/mm/aa, day/moth/year, 01/01/2024")
    print (formato_fecha(fecha))
    return 0
    
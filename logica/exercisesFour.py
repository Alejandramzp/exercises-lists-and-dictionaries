import json 

#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva,
#los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
def leer_archivo(path):
    with open(f"databases/{path}", "r") as file:
        data = file.read()
        converList = json.loads(data)
        return converList

def escribir_archivo(data, path):
    with open(f"databases/{path}", "wb+") as file:
        convertirJson = json.dumps(data, indent=4).encode("utf-8")
        file.write(convertirJson)
        file.close

def loteria(numero):
    data = leer_archivo("exercisesFourList.json")
    data.append(numero)
    escribir_archivo(data, "exercisesFourList.json")
    return data
#Escribir un programa que pregunte una fecha en formato `dd/mm/aaaa` y muestre por pantalla 
# la misma fecha en formato `dd de <mes> de aaaa` donde `<mes>` es el nombre del mes.
def formato_fecha(fecha):
    lista = fecha.split("/")
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    datos = leer_archivo("exercisesFourDict.json")
    formato =  {
        "dia": lista[0],
        "mes": meses[int(lista[1]) -1],
        "anio": lista[2],
        "mensaje": f"{lista[0]} de {meses[int(lista[1]) -1]} de {lista[2]}"
    }
    datos.append(formato)
    escribir_archivo(datos, "exercisesFourDict.json")
    return formato.get("mensaje")
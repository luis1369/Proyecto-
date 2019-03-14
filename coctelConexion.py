import requests
#import json

def buscarBebidaNombre(bebida):
    url = 'http://www.thecocktaildb.com/api/json/v1/1/search.php?s=' + bebida
    response = requests.get(url)

    if response.status_code == 200:
        response_json = response.json()  # Diccionario con elemento de una lista
        idDrink = response_json['drinks'] # Elemento de la lista que es un diccionario

        #idDrink = idDrink[0].get("idDrink"), idDrink[0].get("strDrink") # Tupla

        i = 0 # variable de control para obtener los nombres de los resultados a buscar
        nombreBebidas = [] # almaceno en una lista los nombres de los resultados a buscar
        infoBebidas = [] # almaceno todos los elementos de todas las bebidas
        for clave in idDrink:
            clave = idDrink[i].get("strDrink") # imprimo los nombres de los resultados
            nombreBebidas.append(clave)
            clave = idDrink[i]
            infoBebidas.append(clave)
            i+=1

        return infoBebidas, nombreBebidas

        print("Bebidas encontradas:")
        print(nombreBebidas)
        bebidaCompleta = input(f"Selecciona la bebida del 1 al {len(nombreBebidas)}: ")
        #print(infoBebidas) #imprimo todos los elementos de la lista establecida

        #asignamos el valor de bebid


        print("Tu bebida es: ")

        #sirve para concatenar la info de la bebida selccionada
        bebidaElegida = ""
        for clave, valor  in infoBebidas[int(bebidaCompleta)-1].items():
            if valor != "" and valor != None and valor != " ":
                print(f"{clave} -> {valor}")



        print(bebidaElegida)

        #imprimo toda la info de la bebida seleccionada
        #print(infoBebidas[int(bebidaCompleta)-1].values())

        # Imprimo todos los elementos de la cosulta
        #print(response_json)
        # Imprimo el primero elemento de todos los obtenidos
        #print(idDrink)
        # Imprimo el tipo de dato
        print(type(idDrink))
        """     
        response_json = json.loads(response.text)
        idDrink = response_json['idDrink']
        print(idDrink)
        """
    #print(response.text)

def buscarBebidaIngrediente(ingrediente):
    url = 'http://www.thecocktaildb.com/api/json/v1/1/search.php?s=' + ingrediente
    response = requests.get(url)

    if response.status_code == 200:
        response_json = response.json()  # Diccionario con elemento de una lista
        idDrink = response_json['drinks']  # Elemento de la lista que es un diccionario

        # idDrink = idDrink[0].get("idDrink"), idDrink[0].get("strDrink") # Tupla

        i = 0  # variable de control para obtener los nombres de los resultados a buscar
        nombreBebidas = []  # almaceno en una lista los nombres de los resultados a buscar
        infoBebidas = []  # almaceno todos los elementos de todas las bebidas
        for clave in idDrink:
            clave = idDrink[i].get("strDrink")  # imprimo los nombres de los resultados
            nombreBebidas.append(clave)
            clave = idDrink[i]
            infoBebidas.append(clave)
            i += 1

        print("Bebidas encontradas: ")
        print(nombreBebidas)
        bebidaCompleta = input(f"Selecciona la bebida del 1 al {len(nombreBebidas)}: ")
        # print(infoBebidas) #imprimo todos los elementos de la lista establecida

        # asignamos el valor de bebid

        print("Tu bebida es: ")

        # sirve para concatenar la info de la bebida selccionada
        bebidaElegida = ""
        for clave, valor in infoBebidas[int(bebidaCompleta) - 1].items():
            if valor != "" and valor != None and valor != " ":
                print(f"{clave} -> {valor}")

        print(bebidaElegida)

        # imprimo toda la info de la bebida seleccionada
        # print(infoBebidas[int(bebidaCompleta)-1].values())

        # Imprimo todos los elementos de la cosulta
        # print(response_json)
        # Imprimo el primero elemento de todos los obtenidos
        # print(idDrink)
        # Imprimo el tipo de dato
        print(type(idDrink))


if __name__ == '__main__':
    n = input("Nombre de la bebida: ")
    buscarBebidaNombre(n)

    #nn = input("Nombre del Ingrediente:" )
    #buscarBebidaIngrediente(nn)
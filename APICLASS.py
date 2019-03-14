import requests
import APISERVICE
import DBSERVICE

class buscarNombre(APISERVICE):
    def buscarNombre(self, drinkName):
        url = 'http://www.thecocktaildb.com/api/json/v1/1/search.php?s=' + drinkName
        response = requests.get(url)

        if response.status_code == 200:
            response_json = response.json()  # Diccionario con elemento de una lista
            idDrink = response_json['drinks']  # Elemento de la lista que es un diccionario

            i = 0  # variable de control para obtener los nombres de los resultados a buscar
            nombreBebidas = []  # almaceno en una lista los nombres de los resultados a buscar
            infoBebidas = []  # almaceno todos los elementos de todas las bebidas
            for clave in idDrink:
                clave = idDrink[i].get("strDrink")  # imprimo los nombres de los resultados
                nombreBebidas.append(clave)
                clave = idDrink[i]
                infoBebidas.append(clave)
                i += 1

            return nombreBebidas, infoBebidas


    def buscarIngrediente(self, ingredientName):
        url = 'http://www.thecocktaildb.com/api/json/v1/1/search.php?s=' + ingredientName
        response = requests.get(url)



class guardarBebida(DBSERVICE):
    def guardarBebida(self, drink):
        pass
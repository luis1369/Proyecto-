import requests
import APISERVICE
import DBSERVICE

class buscarNombre(APISERVICE):
    def buscarNombre(self, drinkName):
        url = 'http://www.thecocktaildb.com/api/json/v1/1/search.php?s=' + drinkName
        response = requests.get(url)

        if response.status_code == 200:
            response_json = response.json()  # Diccionario
            idDrink = response_json['drinks']

            idDrink = idDrink[0]

            print(response_json)
            print(idDrink)

    def buscarIngrediente(self, ingredientName):
        url = 'http://www.thecocktaildb.com/api/json/v1/1/search.php?i=' + ingredientName
        response = requests.get(url)

        if response.status_code == 200:
            response_json = response.json()  # Diccionario
            idDrink = response_json['drinks']

            idDrink = idDrink[0]

            print(response_json)
            print(idDrink)

class guardarBebida(DBSERVICE):
    def guardarBebida(self, drink):
        pass
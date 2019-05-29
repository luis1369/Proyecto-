import unittest
import sqlite3
import os
from Bebida import bebida
from unittest.mock import patch
from unittest.mock import MagicMock
from APICLASS import DB
from APICLASS import APIBebida

#Pruebas Unitarias
class TestAPICLASS(unittest.TestCase):
    #Prueba Unitaria en donde se conecta a la API TheCocktailDB
    @patch('requests.get')
    def test_buscarNombre(self, mock_get):
        test_cases = (
            ("Vodka", ['Bebida Long vodka numero 0', 'Bebida Vodka Fizz numero 1', 'Bebida Coffee-Vodka numero 2', 'Bebida Vodka Martini numero 3', 'Bebida Vodka Russian numero 4', 'Bebida Vodka And Tonic numero 5'], lambda: {"drinks": [{"strDrink": "Long vodka"}, {"strDrink": "Vodka Fizz"}, {"strDrink": "Coffee-Vodka"}, {"strDrink": "Vodka Martini"}, {"strDrink": "Vodka Russian"}, {"strDrink": "Vodka And Tonic"}]}),
            ("Beer", ['Bebida Zambeer numero 0', 'Bebida Campari Beer numero 1', 'Bebida California Root Beer numero 2'], lambda: {"drinks": [{"strDrink": "Zambeer"}, {"strDrink": "Campari Beer"}, {"strDrink": "California Root Beer"}]}),
            ("Tequila", ['Bebida Tequila Fizz numero 0', 'Bebida Tequila Sour numero 1', 'Bebida Tequila Sunrise numero 2', 'Bebida Tequila Slammer numero 3', 'Bebida Tequila Surprise numero 4'], lambda: {"drinks": [{"strDrink": "Tequila Fizz"}, {"strDrink": "Tequila Sour"}, {"strDrink": "Tequila Sunrise"}, {"strDrink": "Tequila Slammer"}, {"strDrink": "Tequila Surprise"}]})
        )

        buscar = APIBebida()

        for entrada,esperado,funcion in test_cases:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json = funcion

            salida_real = buscar.buscarNombre(entrada)
            self.assertEqual(salida_real, esperado)


#Pruebas de Integracion
class TestAPICLASSI(unittest.TestCase):
    #Crear la base y darle valores
    def setUp(self):
        self.con = sqlite3.connect("TestEl_Fieston.db")
        cur = self.con.cursor()
        self.db = DB('TestEl_Fieston.db')
        cur.execute('''CREATE TABLE IF NOT EXISTS favoritos
            (id Integer,
            nombre Text,
            tags Text,
            categoria Text,
            alcohol Text,
            vaso Text,
            instrucciones Text,
            imagen Text,
            ingredientes Text,
            medidas Text,
            bienElectrico Integer)
            ''')

        self.db.guardarBebida(bebida(14978, "Rum Punch", None, "Punch / Party Drink", "Alcoholic", "Punch bowl", "Mix all ingredients in a punch bowl and serve.", "https://www.thecocktaildb.com/images/media/drink/wyrsxu1441554538.jpg", "Rum, Ginger ale, Fruit punch, Orange juice, Ice, , , , , , , , , , ,", "mikey bottle , large bottle , 355 ml frozen , 355 ml frozen , crushed ,  ,  ,  ,  ,  , , , , , ,", 7))
        self.db.guardarBebida(bebida(13621, "Tequila Sunrise", "IBA,ContemporaryClassic", "Cocktail", "Alcoholic", "Highball glass", "Pour the tequila and orange juice into glass over ice. Add the grenadine, which will sink to the bottom. Stir gently to create the sunrise effect. Garnish and serve.", "https://www.thecocktaildb.com/images/media/drink/quqyqp1480879103.jpg", "Tequila, Orange juice, Grenadine, , , , , , , , , , , , , ", "2 measures , , , , , , , , , , , , , , , ", 7))
        self.db.guardarBebida(bebida(11000, "Mojito", "IBA,ContemporaryClassic,Alcoholic,USA", "Cocktail", "Alcoholic", "Highball glass", "Muddle mint leaves with sugar and lime juice. Add a splash of soda water and fill the glass with cracked ice. Pour the rum and top with soda water. Garnish and serve with straw.", "https://www.thecocktaildb.com/images/media/drink/rxtqps1478251029.jpg", "Light rum, Lime, Sugar, Mint, Soda water, , , , , , , , , , , ", "2-3 oz , Juice of 1 , 2 tsp , 2-4 , , , , , , , , , , , , ", 10))
        self.db.guardarBebida(bebida(12770, "Iced Coffee", None, "Coffee / Tea", "Non alcoholic", "Coffee mug", "Mix together until coffee and sugar is dissolved. Add milk. Shake well. Using a blender or milk shake maker produces a very foamy drink. Serve in coffee mug.", "https://www.thecocktaildb.com/images/media/drink/ytprxy1454513855.jpg", "Coffee, Sugar, Water, Milk, , , , , , , , , , , , ", "1/4 cup instant , 1/4 cup , 1/4 cup hot , 4 cups cold ,  ,  ,  ,  ,  , , , , , , , ", 7))

    #Elimino la base de datos
    def tearDown(self):
        self.con.close()
        self.db.con.close()
        os.remove("TestEl_Fieston.db")

    #Actualizo una bebida
    def testActualizar(self):
        self.db.actualizarBebida("Rum Punch", 7)
        nombre = "Rum Punch"
        salida_esperada = self.con.execute("select * from favoritos where nombre = ('{}')".format(nombre))
        cursor = salida_esperada.fetchone()
        r = []
        for row in cursor:
            r.append(row)

        salida_esperada3 = bebida(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10])
        real = bebida(14978, "Rum Punch", None, "Punch / Party Drink", "Alcoholic", "Punch bowl", "Mix all ingredients in a punch bowl and serve.", "https://www.thecocktaildb.com/images/media/drink/wyrsxu1441554538.jpg", "Rum, Ginger ale, Fruit punch, Orange juice, Ice, , , , , , , , , , ,", "mikey bottle , large bottle , 355 ml frozen , 355 ml frozen , crushed ,  ,  ,  ,  ,  , , , , , ,", 7)
        sal = (salida_esperada3.bienElectrico, salida_esperada3.nombre)
        re = (real.bienElectrico, real.nombre)
        self.assertEqual(sal, re)

    #Elimino una bebida
    def testBorrar(self):
        self.db.borrarBebida("Rum Punch")
        nombre = "Rum Punch"
        borrado = self.con.execute("SELECT * FROM favoritos where nombre = ('{}')".format(nombre))
        cursor = borrado.fetchone()
        self.assertIsNone(cursor)

    #Agrego una bebida
    def testAgregar(self):
        self.db.guardarBebida(bebida(13621, "Tequila Sunrise", "IBA,ContemporaryClassic", "Cocktail", "Alcoholic", "Highball glass", "Pour the tequila and orange juice into glass over ice. Add the grenadine, which will sink to the bottom. Stir gently to create the sunrise effect. Garnish and serve.", "https://www.thecocktaildb.com/images/media/drink/quqyqp1480879103.jpg", "Tequila, Orange juice, Grenadine, , , , , , , , , , , , , ", "2 measures , , , , , , , , , , , , , , , ", 7))
        real = bebida(13621, "Tequila Sunrise", "IBA,ContemporaryClassic", "Cocktail", "Alcoholic", "Highball glass", "Pour the tequila and orange juice into glass over ice. Add the grenadine, which will sink to the bottom. Stir gently to create the sunrise effect. Garnish and serve.", "https://www.thecocktaildb.com/images/media/drink/quqyqp1480879103.jpg", "Tequila, Orange juice, Grenadine, , , , , , , , , , , , , ", "2 measures , , , , , , , , , , , , , , , ", 7)
        nombre = "Tequila Sunrise"
        salida_esperada = self.con.execute("select * from favoritos where nombre = ('{}')".format(nombre))
        cursor = salida_esperada.fetchone()
        r = []
        for row in cursor:
            r.append(row)

        salida_esperada2 = bebida(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10])
        salida = (salida_esperada2.id, salida_esperada2.nombre, salida_esperada2.tags, salida_esperada2.categoria, salida_esperada2.alcohol, salida_esperada2.vaso, salida_esperada2.instrucciones, salida_esperada2.imagen, salida_esperada2.ingredientes, salida_esperada2.medidas, salida_esperada2.bienElectrico)
        vreal = (real.id, real.nombre, real.tags, real.categoria, real.alcohol, real.vaso, real.instrucciones, real.imagen, real.ingredientes, real.medidas, real.bienElectrico)
        self.assertEqual(salida, vreal)

    #Muestro las bebidas
    def testMostrarT(self):
        salida_esperada = [bebida(14978, "Rum Punch", "None", "Punch / Party Drink", "Alcoholic", "Punch bowl", "Mix all ingredients in a punch bowl and serve.", "https://www.thecocktaildb.com/images/media/drink/wyrsxu1441554538.jpg", "Rum, Ginger ale, Fruit punch, Orange juice, Ice, , , , , , , , , , ,", "mikey bottle , large bottle , 355 ml frozen , 355 ml frozen , crushed ,  ,  ,  ,  ,  , , , , , ,", 7),
                    bebida(13621, "Tequila Sunrise", "IBA,ContemporaryClassic", "Cocktail", "Alcoholic", "Highball glass", "Pour the tequila and orange juice into glass over ice. Add the grenadine, which will sink to the bottom. Stir gently to create the sunrise effect. Garnish and serve.", "https://www.thecocktaildb.com/images/media/drink/quqyqp1480879103.jpg", "Tequila, Orange juice, Grenadine, , , , , , , , , , , , , ", "2 measures , , , , , , , , , , , , , , , ", 7),
                    bebida(11000, "Mojito", "IBA,ContemporaryClassic,Alcoholic,USA", "Cocktail", "Alcoholic", "Highball glass", "Muddle mint leaves with sugar and lime juice. Add a splash of soda water and fill the glass with cracked ice. Pour the rum and top with soda water. Garnish and serve with straw.", "https://www.thecocktaildb.com/images/media/drink/rxtqps1478251029.jpg", "Light rum, Lime, Sugar, Mint, Soda water, , , , , , , , , , , ", "2-3 oz , Juice of 1 , 2 tsp , 2-4 , , , , , , , , , , , , ", 10),
                    bebida(12770, "Iced Coffee", "None", "Coffee / Tea", "Non alcoholic", "Coffee mug", "Mix together until coffee and sugar is dissolved. Add milk. Shake well. Using a blender or milk shake maker produces a very foamy drink. Serve in coffee mug.", "https://www.thecocktaildb.com/images/media/drink/ytprxy1454513855.jpg", "Coffee, Sugar, Water, Milk, , , , , , , , , , , , ", "1/4 cup instant , 1/4 cup , 1/4 cup hot , 4 cups cold ,  ,  ,  ,  ,  , , , , , , , ", 7)]
        a = self.db.mostrarBebidas()
        self.assertEqual(salida_esperada[0], a[0])
        i=0
        for x in salida_esperada:
            self.assertEqual(salida_esperada[i], a[i])
            i+=1

    #Busco una bebida conectandome a la API TheCocktailDB
    def testEncontrarB(self):
        self.api = APIBebida()
        nombre = "Rum"
        salida_esperada = ['Bebida Rum Sour numero 0', 'Bebida Rum Toddy numero 1', 'Bebida Rum Punch numero 2', 'Bebida Cherry Rum numero 3', 'Bebida Rum Cooler numero 4', 'Bebida Rum Runner numero 5', 'Bebida Rum Cobbler numero 6', 'Bebida Rum Milk Punch numero 7', 'Bebida Rum Screwdriver numero 8', 'Bebida Rum Old-fashioned numero 9']
        real = self.api.buscarNombre(nombre)
        self.assertEqual(salida_esperada, real)

    #Busco una bebida conectandome a la API TheCocktailDB y lo seleccione
    def testCreateBebida(self):
        self.api = APIBebida()
        nombre = "Rum"
        numero = 2
        salida_esperada = bebida(14978, "Rum Punch", None, "Punch / Party Drink", "Alcoholic", "Punch bowl", "Mix all ingredients in a punch bowl and serve.", "https://www.thecocktaildb.com/images/media/drink/wyrsxu1441554538.jpg", "Rum, Ginger ale, Fruit punch, Orange juice, Ice, , , , , , , , , , ,", "mikey bottle , large bottle , 355 ml frozen , 355 ml frozen , crushed ,  ,  ,  ,  ,  , , , , , ,", 7)
        real = self.api.getBebida(numero, nombre)
        self.assertEqual(type(salida_esperada), type(real))
        self.assertEqual(salida_esperada.id, int(real.id))

if __name__ == '__main__':
    unittest.main()

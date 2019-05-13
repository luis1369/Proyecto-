import unittest
import sqlite3
import os
from Bebida import bebida
from unittest.mock import patch
from unittest.mock import MagicMock
from APICLASS import *
#from unittest import TestCase
#TestCase.maxDiff = None
from types import *

#Pruebas Unitarias
'''class TestAPICLASS(unittest.TestCase):
    #pruebas unitarias
    @patch('requests.get')
    def test_buscarNombre(self, mock_get):
        test_cases = ((['Bebida Mojito numero 0', 'Bebida Mojito #3 numero 1']),)

        buscar = APIBebida()

        for entrada,esperado in test_cases:
            mock_get.return_value.status_code = 200
            #mock_get.return_value.json = myfunc


    def myfunc(self):
        pass'''

#Pruebas de integracion para la base de datos
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

        self.db.guardarBebida(bebida(12370, "Tequila Sour", "None", "Ordinary Drink", "Alcoholic", "Whiskey sour glass", "Shake tequila, juice of lemon, and powdered sugar with ice and strain into a whiskey sour glass. Add the half-slice of lemon, top with the cherry, and serve.", "https://www.thecocktaildb.com/images/media/drink/ek0mlq1504820601.jpg", "Tequila, Lemon, Powdered sugar, Lemon, Cherry, , , , , , , , , , , ", "2 oz , Juice of 1/2 , 1 tsp , 1/2 slice , 1 ,  ,  ,  ,  ,  , , , , , , ", 10))
        self.db.guardarBebida(bebida(13621, "Tequila Sunrise", "IBA,ContemporaryClassic", "Cocktail", "Alcoholic", "Highball glass", "Pour the tequila and orange juice into glass over ice. Add the grenadine, which will sink to the bottom. Stir gently to create the sunrise effect. Garnish and serve.", "https://www.thecocktaildb.com/images/media/drink/quqyqp1480879103.jpg", "Tequila, Orange juice, Grenadine, , , , , , , , , , , , , ", "2 measures , , , , , , , , , , , , , , , ", 7))
        self.db.guardarBebida(bebida(11000, "Mojito", "IBA,ContemporaryClassic,Alcoholic,USA", "Cocktail", "Alcoholic", "Highball glass", "Muddle mint leaves with sugar and lime juice. Add a splash of soda water and fill the glass with cracked ice. Pour the rum and top with soda water. Garnish and serve with straw.", "https://www.thecocktaildb.com/images/media/drink/rxtqps1478251029.jpg", "Light rum, Lime, Sugar, Mint, Soda water, , , , , , , , , , , ", "2-3 oz , Juice of 1 , 2 tsp , 2-4 , , , , , , , , , , , , ", 10))
        self.db.guardarBebida(bebida(12770, "Iced Coffee", "None", "Coffee / Tea", "Non alcoholic", "Coffee mug", "Mix together until coffee and sugar is dissolved. Add milk. Shake well. Using a blender or milk shake maker produces a very foamy drink. Serve in coffee mug.", "https://www.thecocktaildb.com/images/media/drink/ytprxy1454513855.jpg", "Coffee, Sugar, Water, Milk, , , , , , , , , , , , ", "1/4 cup instant , 1/4 cup , 1/4 cup hot , 4 cups cold ,  ,  ,  ,  ,  , , , , , , , ", 7))
        self.db.guardarBebida(bebida(11007, "Margarita", "IBA,ContemporaryClassic", "Ordinary Drink", "Alcoholic", "Cocktail glass", "Rub the rim of the glass with the lime slice to make the salt stick to it. Take care to moisten only the outer rim and sprinkle the salt on it. The salt should present to the lips of the imbiber and never mix into the cocktail. Shake the other ingredients with ice, then carefully pour into the glass.", "https://www.thecocktaildb.com/images/media/drink/wpxpvu1439905379.jpg", "Tequila, Triple sec, Lime juice, Salt, , , , , , , , , , , , ", "1 1/2 oz , 1/2 oz , 1 oz , , , , , , , , , , , , , ", 9))

    #Elimino la base de datos
    def tearDown(self):
        self.con.close()
        self.db.con.close()
        os.remove("TestEl_Fieston.db")

    #Actualizo una bebida
    def testUpdate(self):
        self.db.actualizarBebida("Mojito", 8)
        nombre = "Mojito"
        #salida_esperada = self.con.execute("select bienElectrico, nombre from favoritos where nombre = ('{}')".format(nombre))
        salida_esperada = self.con.execute("select * from favoritos where nombre = ('{}')".format(nombre))
        cursor = salida_esperada.fetchone()
        l = []
        for row in cursor:
            l.append(row)

        salida_esperada3 = bebida(l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7], l[8], l[9], l[10])
        #salida_esperada2 = bebida(salida_esperada)
        real = bebida(11000, "Mojito", "IBA,ContemporaryClassic,Alcoholic,USA", "Cocktail", "Alcoholic", "Highball glass", "Muddle mint leaves with sugar and lime juice. Add a splash of soda water and fill the glass with cracked ice. Pour the rum and top with soda water. Garnish and serve with straw.", "https://www.thecocktaildb.com/images/media/drink/rxtqps1478251029.jpg", "Light rum, Lime, Sugar, Mint, Soda water, , , , , , , , , , , ", "2-3 oz , Juice of 1 , 2 tsp , 2-4 , , , , , , , , , , , , ", 8)
        sal = (salida_esperada3.bienElectrico, salida_esperada3.nombre)
        re = (real.bienElectrico, real.nombre)
        self.assertEqual(sal, re)

    #Elimino una bebida
    def testDelete(self):
        self.db.borrarBebida("Mojito")
        nombre = "Mojito"
        borrado = self.con.execute("SELECT * FROM favoritos where nombre = ('{}')".format(nombre))
        cursor = borrado.fetchone()
        #print(type(cursor))
        self.assertIsNone(cursor)

    #Agrego una bebida
    def testAdd(self):
        self.db.guardarBebida(bebida(11000, "Mojito", "IBA,ContemporaryClassic,Alcoholic,USA", "Cocktail", "Alcoholic", "Highball glass", "Muddle mint leaves with sugar and lime juice. Add a splash of soda water and fill the glass with cracked ice. Pour the rum and top with soda water. Garnish and serve with straw.", "https://www.thecocktaildb.com/images/media/drink/rxtqps1478251029.jpg", "Light rum, Lime, Sugar, Mint, Soda water, , , , , , , , , , , ", "2-3 oz , Juice of 1 , 2 tsp , 2-4 , , , , , , , , , , , , ", 10))
        real = bebida(11000, "Mojito", "IBA,ContemporaryClassic,Alcoholic,USA", "Cocktail", "Alcoholic", "Highball glass", "Muddle mint leaves with sugar and lime juice. Add a splash of soda water and fill the glass with cracked ice. Pour the rum and top with soda water. Garnish and serve with straw.", "https://www.thecocktaildb.com/images/media/drink/rxtqps1478251029.jpg", "Light rum, Lime, Sugar, Mint, Soda water, , , , , , , , , , , ", "2-3 oz , Juice of 1 , 2 tsp , 2-4 , , , , , , , , , , , , ", 10)
        nombre = "Mojito"
        salida_esperada = self.con.execute("select * from favoritos where nombre = ('{}')".format(nombre))
        cursor = salida_esperada.fetchone()
        l = []
        for row in cursor:
            l.append(row)

        salida_esperada2 = bebida(l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7], l[8], l[9], l[10])
        salida = (salida_esperada2.id, salida_esperada2.nombre, salida_esperada2.tags, salida_esperada2.categoria, salida_esperada2.alcohol, salida_esperada2.vaso, salida_esperada2.instrucciones, salida_esperada2.imagen, salida_esperada2.ingredientes, salida_esperada2.medidas, salida_esperada2.bienElectrico)
        vreal = (real.id, real.nombre, real.tags, real.categoria, real.alcohol, real.vaso, real.instrucciones, real.imagen, real.ingredientes, real.medidas, real.bienElectrico)
        self.assertEqual(salida, vreal)

    #Muestro las bebidas
    def testShowAll(self):
        entrada = [bebida(12370, "Tequila Sour", "None", "Ordinary Drink", "Alcoholic", "Whiskey sour glass", "Shake tequila, juice of lemon, and powdered sugar with ice and strain into a whiskey sour glass. Add the half-slice of lemon, top with the cherry, and serve.", "https://www.thecocktaildb.com/images/media/drink/ek0mlq1504820601.jpg", "Tequila, Lemon, Powdered sugar, Lemon, Cherry, , , , , , , , , , , ", "2 oz , Juice of 1/2 , 1 tsp , 1/2 slice , 1 ,  ,  ,  ,  ,  , , , , , , ", 10),
                bebida(13621, "Tequila Sunrise", "IBA,ContemporaryClassic", "Cocktail", "Alcoholic", "Highball glass", "Pour the tequila and orange juice into glass over ice. Add the grenadine, which will sink to the bottom. Stir gently to create the sunrise effect. Garnish and serve.", "https://www.thecocktaildb.com/images/media/drink/quqyqp1480879103.jpg", "Tequila, Orange juice, Grenadine, , , , , , , , , , , , , ", "2 measures , , , , , , , , , , , , , , , ", 7),
                bebida(11000, "Mojito", "IBA,ContemporaryClassic,Alcoholic,USA", "Cocktail", "Alcoholic", "Highball glass", "Muddle mint leaves with sugar and lime juice. Add a splash of soda water and fill the glass with cracked ice. Pour the rum and top with soda water. Garnish and serve with straw.", "https://www.thecocktaildb.com/images/media/drink/rxtqps1478251029.jpg", "Light rum, Lime, Sugar, Mint, Soda water, , , , , , , , , , , ", "2-3 oz , Juice of 1 , 2 tsp , 2-4 , , , , , , , , , , , , ", 10),
                bebida(12770, "Iced Coffee", "None", "Coffee / Tea", "Non alcoholic", "Coffee mug", "Mix together until coffee and sugar is dissolved. Add milk. Shake well. Using a blender or milk shake maker produces a very foamy drink. Serve in coffee mug.", "https://www.thecocktaildb.com/images/media/drink/ytprxy1454513855.jpg", "Coffee, Sugar, Water, Milk, , , , , , , , , , , , ", "1/4 cup instant , 1/4 cup , 1/4 cup hot , 4 cups cold ,  ,  ,  ,  ,  , , , , , , , ", 7),
                bebida(11007, "Margarita", "IBA,ContemporaryClassic", "Ordinary Drink", "Alcoholic", "Cocktail glass", "Rub the rim of the glass with the lime slice to make the salt stick to it. Take care to moisten only the outer rim and sprinkle the salt on it. The salt should present to the lips of the imbiber and never mix into the cocktail. Shake the other ingredients with ice, then carefully pour into the glass.", "https://www.thecocktaildb.com/images/media/drink/wpxpvu1439905379.jpg", "Tequila, Triple sec, Lime juice, Salt, , , , , , , , , , , , ", "1 1/2 oz , 1/2 oz , 1 oz , , , , , , , , , , , , , ", 9)]

        salida_esperada = [bebida(12370, "Tequila Sour", "None", "Ordinary Drink", "Alcoholic", "Whiskey sour glass", "Shake tequila, juice of lemon, and powdered sugar with ice and strain into a whiskey sour glass. Add the half-slice of lemon, top with the cherry, and serve.", "https://www.thecocktaildb.com/images/media/drink/ek0mlq1504820601.jpg", "Tequila, Lemon, Powdered sugar, Lemon, Cherry, , , , , , , , , , , ", "2 oz , Juice of 1/2 , 1 tsp , 1/2 slice , 1 ,  ,  ,  ,  ,  , , , , , , ", 10),
                bebida(13621, "Tequila Sunrise", "IBA,ContemporaryClassic", "Cocktail", "Alcoholic", "Highball glass", "Pour the tequila and orange juice into glass over ice. Add the grenadine, which will sink to the bottom. Stir gently to create the sunrise effect. Garnish and serve.", "https://www.thecocktaildb.com/images/media/drink/quqyqp1480879103.jpg", "Tequila, Orange juice, Grenadine, , , , , , , , , , , , , ", "2 measures , , , , , , , , , , , , , , , ", 7),
                bebida(11000, "Mojito", "IBA,ContemporaryClassic,Alcoholic,USA", "Cocktail", "Alcoholic", "Highball glass", "Muddle mint leaves with sugar and lime juice. Add a splash of soda water and fill the glass with cracked ice. Pour the rum and top with soda water. Garnish and serve with straw.", "https://www.thecocktaildb.com/images/media/drink/rxtqps1478251029.jpg", "Light rum, Lime, Sugar, Mint, Soda water, , , , , , , , , , , ", "2-3 oz , Juice of 1 , 2 tsp , 2-4 , , , , , , , , , , , , ", 10),
                bebida(12770, "Iced Coffee", "None", "Coffee / Tea", "Non alcoholic", "Coffee mug", "Mix together until coffee and sugar is dissolved. Add milk. Shake well. Using a blender or milk shake maker produces a very foamy drink. Serve in coffee mug.", "https://www.thecocktaildb.com/images/media/drink/ytprxy1454513855.jpg", "Coffee, Sugar, Water, Milk, , , , , , , , , , , , ", "1/4 cup instant , 1/4 cup , 1/4 cup hot , 4 cups cold ,  ,  ,  ,  ,  , , , , , , , ", 7),
                bebida(11007, "Margarita", "IBA,ContemporaryClassic", "Ordinary Drink", "Alcoholic", "Cocktail glass", "Rub the rim of the glass with the lime slice to make the salt stick to it. Take care to moisten only the outer rim and sprinkle the salt on it. The salt should present to the lips of the imbiber and never mix into the cocktail. Shake the other ingredients with ice, then carefully pour into the glass.", "https://www.thecocktaildb.com/images/media/drink/wpxpvu1439905379.jpg", "Tequila, Triple sec, Lime juice, Salt, , , , , , , , , , , , ", "1 1/2 oz , 1/2 oz , 1 oz , , , , , , , , , , , , , ", 9)]

        '''dbMock = MagicMock()
        dbMock.mostrar.return_value = entrada'''

        salida = (salida_esperada[0], salida_esperada[1], salida_esperada[2], salida_esperada[3], salida_esperada[4])
        real = (entrada[0], entrada[1], entrada[2], entrada[3], entrada[4])

        real2 = self.db.mostrarBebidas()

        #salida = (salida_esperada[0].id, salida_esperada[0].nombre, salida_esperada[0].tags, salida_esperada[0].categoria, salida_esperada[0].alcohol, salida_esperada[0].vaso, salida_esperada[0].instrucciones, salida_esperada[0].imagen, salida_esperada[0].ingredientes, salida_esperada[0].medidas, salida_esperada[0].bienElectrico)
        #real = (entrada[0].id, entrada[0].nombre, entrada[0].tags, entrada[0].categoria, entrada[0].alcohol, entrada[0].vaso, entrada[0].instrucciones, entrada[0].imagen, entrada[0].ingredientes, entrada[0].medidas, entrada[0].bienElectrico)

        #print(entrada[3])
        #print(salida_esperada[3])
        #real = self.db.mostrarBebidas()
        


        self.assertEqual(salida_esperada, real2)

if __name__ == '__main__':
    unittest.main()
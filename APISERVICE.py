from abc import ABC, abstractmethod

class APISERVICE(ABC):
    @abstractmethod
    def buscarNombre(self, drinkName):
        # Regresa un objeto tipo dirnk :)
        pass

    @abstractmethod
    def buscarIngrediente(self, ingredientName):
        # Regresa un objeto tipo ingredient :)
        pass
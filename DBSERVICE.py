from abc import ABC, abstractmethod

class DBSERVICE(ABC):
    @abstractmethod
    def guardarBebida(self, drink):
        # Guarda la bebida
        pass
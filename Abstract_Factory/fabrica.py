from abc import ABC, abstractmethod


class Fabrica(ABC):  # AbstractFactory

    @abstractmethod
    def crear_televisor(self):
        pass

    @abstractmethod
    def crear_celular(self):
        pass

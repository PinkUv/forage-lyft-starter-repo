from abc import ABC, abstractmethod

def Serviceable(ABC):
    @abstractmethod
    def needs_service(self): pass
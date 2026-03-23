class Plato:
    def __init__(self, id: int, nombre: str, descripcion: str, categoria: str, precio: float, stock: int) -> None:
        self.id: int = id
        self.nombre: str = nombre
        self.descripcion: str = descripcion
        self.categoria: str = categoria
        self.precio: float = precio
        self.stock: int = stock
        self.vendidos: int = 0

    def actualizar_stock(self, cantidad: int) -> None:
        self.stock += cantidad

class Menu:
    def __init__(self)->None:
        self.platos = []

    def agregar_plato(self,plato)->None:
        self.platos.append(plato)

    def eliminar_plato(self,id_plato:int)->None:
        self.platos =[p for p in self.platos if p.id != id_plato]


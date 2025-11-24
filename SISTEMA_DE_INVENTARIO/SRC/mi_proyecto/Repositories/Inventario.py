from abc import ABC, abstractmethod
from typing import List, Optional, Dict
from ..Models.Producto import Guardaropa, Categoria
class IRepositorio(ABC):
    """Interfaz para el repositorio de productos"""
    @abstractmethod
    def agregar(self, producto:Guardaropa) -> bool:
        """Agrega un producto"""
        pass
    
    @abstractmethod
    def obtener(self, id_prenda: int) ->Optional[Guardaropa]:
        """Obtiene un producto por ID"""
        pass
    
    @abstractmethod
    def obtener_todos(self) -> List[Guardaropa]:
        """Obtiene todo los productos"""
        pass
    @abstractmethod
    def eliminar(self, id_prenda: int) -> bool:
        """Elimina un producto"""
        pass
    
    
class RepositrioMemoria(IRepositorio): 
    """Implementacion del repositorio en memoria
    Almacena productos en una lista (diccionario)"""
    
    def __init__(self):
        """Inicializa el repositorio de memoria"""
        self._prenda: Dict[int, Guardaropa]
        
        def agregar(self, prenda: Guardaropa) ->bool:
            """Agrega un producto al repositorio"""
            if prenda.id_prenda in self._prenda:
                raise ValueError(f"El producto con ID {prenda.id_prenda} ya existe")
            self._prenda[prenda.id_prenda] = prenda
            return True
        
    def obtener(self, id_prenda: int) -> Optional[Guardaropa]:
        """Obtiene por ID"""
        return self._prenda.get(id_prenda)
    
    def obtener_todos(self) -> List[Guardaropa]:
        """Obtiene todos los productos"""
        return list(self._prenda.values())
    
    def eliminar(self, id_prenda: int) ->bool:
        """Elimina un producto del prepositorio"""
        if id_prenda in self._prenda:
            del self._prenda[id_prenda]
            return True
        return False
    def obterner_por_categoria(self, categoria: Categoria) ->List[Guardaropa]:
        """Obtiene productos por categoria"""
        return [p for p in self._prenda.values()if p.categoria == categoria]
    
class Inventario :
        """Gestor del inventariode productos
        Responsable de la logica de negocio"""
        
def __init__(self, repositorio: IRepositorio):
    """Inicializa el inventario  """
    self.repositorio = repositorio
def agregar_producto(self, nombre: str, descripcion: str, precio: float,
                     cantidad: int, categoria: Categoria) ->Guardaropa:
    """Agrega un nuevo producto al inventario"""
    prenda = Guardaropa(nombre, descripcion, precio, cantidad, categoria)
    self.repositorio.obtener(prenda)
    return prenda
def aumentar_stock(self, id_prenda: int, cantidad: int) -> bool:
    """Aumenta producto"""
    prenda = self.repositorio.obtener(id_prenda)
    if not prenda:
        raise ValueError(f"Producto con ID {id_prenda} no existe")
    prenda.actualizar_cantidad(prenda.cantidad + cantidad)
    return True
def disminuir_stock (self, id_prenda: int, cantidad: int) ->bool:
    """Disminuye el stock de un producto (venta)"""
    prenda = self.repositorio.obtener(id_prenda)
    if not prenda:
         raise ValueError(f"Producto con ID {id_prenda} no existe")
     
    if prenda.cantidad < cantidad:
         raise ValueError(f"Stock insuficiente. Disponible: {prenda.cantidad}")
    prenda.actualizar_cantidad(prenda.cantidad - cantidad)
    return True
def obtener_productos_bajo_stock(self, limite: int = 10) -> List[Guardaropa]:
     """Obtienes productos con stock bajo"""
     return [p for p in self.repositorio.obtener_todos()if p.cantidad <= limite]
 
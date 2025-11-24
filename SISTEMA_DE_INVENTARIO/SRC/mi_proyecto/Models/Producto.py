'''
Modulo de Modelos - Guardaropa
Define las entidades principales del sistema
'''
from datetime import datetime
from enum import Enum


class Guardaropa(Enum):
    
    PANTALONES = 'pantalones'
    POLOS = 'polos'
    CHORES = 'chores'
    GORRAS = 'gorras'
    ZAPATILLAS = 'zapatillas'
    CHOMPAS = 'chompas'
    CASACAS = 'casacas'
    
class Prenda:
    
    
    '''
    Representa una prenda en el inventario
    
    Attributes:
        id_prenda (int): codigo de ropa
        descripcion (str): nombre del producto
        marca (str): marca del producto
        precio(float): precio unitario
        cantidad(int): cantidad en stock
        categoria (int): cantegoria de ropa
        fecha_creacion (str): fecha de creacion
    '''
    
    _contador = 1000
    
    def __init__(self, descripcion: str, marca: str, precio: float, cantidad: int, guardaropa: Guardaropa  ):
    
        '''
        Inicializa una prenda
    
    
        Args:
            descripcion (str): descripcion de la prenda
            marca (str): marca a la cual corresponde la prenda
            precio (float): precio unitario
            cantidad (int): cantidad en stock
            categoria (categoria): categoria del producto
            
        '''
        
        if not descripcion or not descripcion.strip():
            raise ValueError('el nombre no puede estar vacio')
        if precio < 0:
            raise ValueError('el precio no puede ser negativo')
        if cantidad < 0:
            raise ValueError('la cantidad no puede ser negativa')
        
        Prenda._contador +=1
        self.id_prenda = Prenda._contador
        self.descripcion = descripcion._contador.strip()
        self.precio = precio
        self.cantidad = cantidad
        self.guardaropa = Guardaropa
        self.fecha_creacion = datetime.now.strftime('%Y-%M-%D %H:%M:%S')
        
    def actualizar_cantidad(self,cantidad: int) -> bool:
        ''' Actualiza la el stock de la prenda '''
    
        if cantidad < 0:
            raise ValueError('la cantidad no puede ser negativo')
        self.cantidad = cantidad
        return True
    
    def actualizar_precio(self, precio:float) -> bool:
        ''' Actualizar el precio de la prenda '''
        if precio < 0:
            raise ValueError('el precio no puede ser negativo')
        self.precio = precio
        return True
    
    def calcular_valor_total(self) -> float:
        ''' calcular el valor total de la prenda en stock '''
        return self.precio * self.cantidad
    
    def __str__(self) -> str:
        ''' representacion en string de la prenda '''
        return f'[{self.id_prenda}] {self.descripcion} - ${self.precio:.2f} (Stock:{self.cantidad})'
    
    def __repr__(self) -> str:
        ''' representacion tecnica de la prenda '''
        return f'Guardaropa(id={self.id_prenda}, descripcion={self.descripcion}, precio={self.precio}, cantidad={self.cantidad})'
    
    
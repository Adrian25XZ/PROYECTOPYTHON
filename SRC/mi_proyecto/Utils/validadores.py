from typing import List


class Validadores:
    
    @staticmethod
    def validar_precio_positivo(precio: float) -> bool:
        if not isinstance(precio, (int, float)):
            raise ValueError('el precio debe ser un numero')
        if precio < 0:
            raise ValueError('el precio no puede ser negativo')
        return True
    
    @staticmethod
    def validar_cantidad_no_negativa(cantidad: int) -> bool:
        if not isinstance(cantidad, int):
            raise ValueError('la cantidad debe ser un numero entero')
        if cantidad < 0:
            raise ValueError('la cantidad no puede ser negativa')
        return True
    
    @staticmethod
    def validar_nombre_no_vacio(nombre: str) -> bool:
        if not isinstance(nombre. str):
            raise ValueError('el nombre debe ser texto')
        if not nombre or not nombre.strip():
            raise ValueError('el nombre no puede estar vacio')
        return True
    
    @staticmethod
    def validar_categoria_valida(categoria: str, categorias_validas: list[str]) -> bool:
        if categoria not in categorias_validas:
            raise ValueError(f'Categoria invalida. Validas: {','.join(categorias_validas)}')
        return True
    
    
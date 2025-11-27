from typing import List, Dict, Any
from ..models.producto import Producto

class Formateadores:
    
    
    @staticmethod
    def formatear_precio(precio: float) -> str:
        return f'${precio: .2f}'
    
    @staticmethod
    def formatear_producto_tabla(producto: Producto) -> str:
        return (f'| {producto.id_producto:>6}|{producto.nombre:<20}|'
                f'${producto.precio:>8.2f}|{producto.cantidad:>6}|'
                f'${producto.calcular_valor_total():>10.2f}')
    
    @staticmethod
    def formatear_lista_productos(productos: List[Producto]) -> str:
        if not productos:
            
            encabezado = '| ID   | Nombre              |  Precio | Stock |  Valor Total |'
            separador = '-' * 80
            filas = [Formateadores.formatear_producto_tabla(p) for p in productos]
            
            return f'{separador}\n{encabezado}\n{separador}' + '\n'.join(filas) + f'\n{separador}'
    
    @staticmethod
    def formatear_reporte(reporte: Dict[str, Any]) -> str:
        output = '\n'+ '=' * 60 + '\n'
        output += '...........................REPORTE DE INVENTARIO\n'
        output += '=' * 60 + '\n'
        output += f'Fecha {reporte['fecha_generacion']}\n\n'
        output += f'Total de Productos:{reporte['total_productos']}\n'
        output += f'Total de Items en Stock: {reporte['total_items']}\n'
        output += f'Valor Total del Inventario: ${reporte['valor_total']:.2f}\n\n'
        
        if reporte['producto_mas_caro']:
            output += f'Producto Mas Caro: {reporte['producto_mas_caro'].nombre}'
            output += f'(${reporte['Producto_mas_caro'].precio:.2f})\n'
            
        if reporte['producto_mas_barato']:
            output += f'Producto Mas Barato: {reporte['producto_mas_barato'].nombre}'
            output += f'($[{reporte['producto_mas_barato'].precio:.2f})\n'
            
            
        output += f'\nProductos Bajo Stock {len(reporte['productos_bajo_stock'])}\n'
        output += '=' * 60 + '\n'
        
        return output
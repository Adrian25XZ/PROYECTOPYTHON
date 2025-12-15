'''Modulo de aportes sindicales'''

from datetime import datetime
from enum import Enum


class Provincias(Enum):
    
    HUANCAYO = 'huancayo'
    CAJAMARCA = 'cajamarca'
    LIMA = 'lima'
    UCAYALI = 'ucayali'
    ICA = 'ica'
    MADRE_DE_DIOS = 'madre de dios'
    
class aportes:
    '''Representa la sede
    
    Attributes:
        id_sede (int): Identificador unico
        nombre_sede (str): Nombre de sede
        cuota (int): mes a la que corresponde
        importe (float): importe de la cuota
        provincia (Provincia): provincia de la sede
        fecha_deposito (str): fecha de deposito
    '''
    
    _contador = 1000
    
    def __init__(self, nombre_sede: str, cuota: int, importe: float, provincia: Provincias, fecha_deposito: datetime):
    
        '''
    
        Args:
    
            nombre_sede (str): nombre a la que corresponde la sede
            cuota (int): mes de la cuota
            importe (float): importe de la cuota
            provincia (Provincias): provincia de la sede    
            fecha_deposito (datetime): fecha de deposito
        
        '''
    
    
        if not nombre_sede or not nombre_sede.strip():
            raise ValueError('el nombre no puede estar vacio')
        if importe <= 0:
            raise ValueError('el importe debe ser mayor a 0')
        if cuota < 1-2025 or cuota > 12-2025:
            raise ValueError('la cuota debe estar entre 1-2025 y 12-2025')
        
        aportes._contador += 1
        self.id_sede = aportes._contador
        self.nombre_sede = nombre_sede.strip()
        self.cuota = cuota
        self.importe = importe
        self.provincia = provincia
        self.fecha_deposito = fecha_deposito
        
    def actualizar.
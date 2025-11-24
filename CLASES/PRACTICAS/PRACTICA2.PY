
# FUNCION DICIONARIO DE VUELOS

def crear_vuelos():
    """
    """
    vuelos=[
            
        {"codigo": "SP101","destino": "cusco","precio": 200.45,"disponible": 5},
        {"codigo": "SP102","destino": "arequipa","precio": 180.45,"disponible": 5},
        {"codigo": "SP103","destino": "iquitos","precio": 320.45,"disponible": 5},
        {"codigo": "SP104","destino": "piura","precio": 220.45,"disponible": 5},
        {"codigo": "SP105","destino": "trujillo","precio": 150.45,"disponible": 5}
    ]

    return(vuelos)
#BUSCAR VUELOS

def buscar_vuelo(lista_vuelos, codigo):

    for vuelo in lista_vuelos:
        if vuelo['codigo'].upper() == codigo.upper():
            return(vuelo)
    return None

#CALCULAR PRECIO DEL VUELO

def calcular_precio_total(precio_base, pasajeros, precio_extra):

    sub_total = pasajeros*precio_base
    total_equipaje = precio_extra*50
    total_general= sub_total+total_equipaje

    return(sub_total,total_equipaje,total_general)

#GENERAR BOURDING PASS

def generar_pass(vuelo, pasajeros, total_general):
    
    

#PROGRAMA PRINCIPAL

def main():





#PUNTO DE ENTRADA

if __name__ == "__main__":
    main()
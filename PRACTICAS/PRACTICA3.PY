

#FUNCION DICIONARIO MENU
def lista_menu():
    
    menu=[
        
        {"codigo":"A001","producto": "cafe","precio": 5},
        {"codigo":"A002","producto": "te","precio": 2},
        {"codigo":"A003","producto": "jugo","precio": 7},
        {"codigo":"A004","producto": "empanada","precio": 2.50},
        {"codigo":"A005","producto": "torta","precio": 4.50},
        
    ]
    return menu

#FUNCION BUSCAR PRODUCTO

def buscar_producto(menu_productos, codigo):
    
    for producto in menu_productos:
        if producto ['codigo'].upper() == codigo.upper():

#FUNCION MOSTRAR MENU

def mostrar_menu(menu_productos):
    
    print("\n" "="*40)
    print("       RESTAURANTE EL POWER SHOT           ")
    print("="*40)
    print(f"{'Codigo':<7} | {'Producto':<10} | {'precio':<5}")
    print("="*40)
    
    for i, item in enumerate(menu_productos,1):
        print(f"{i<4} | {item['codigo']} | {item['producto']} | {item['precio']:.2f}")
        print("="*40)
        
        
# FUNCION TOMAR PEDIDO
def tomar_pedido(producto, cantidad,):
    
    pedido = print(input("INGRESE EL PRODUCTO QUE DESEA CONSUMIR :")).strip()
    
    
    

#PROGRAMA PRINCIPAL

def main():
    
    
    

#PUNTO DE ENTRADA

if __mane__ == "__main__":
    main()
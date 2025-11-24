#FUNCION CREAR CATALOGO

def crear_catalogo():

    """
    crear catalogo de electrodomesticos

    return:
        list: lista de diccionario con electrodomesticos

    """


    catalogo=[
        {"nombre":"refrigeradora","potencia":150,"horas_dia":24},
        {"nombre":"televisor","potencia":100,"horas_dia":5},
        {"nombre":"lavadora","potencia":500,"horas_dia":2},
        {"nombre":"computadora","potencia":200,"horas_dia":8},
        {"nombre":"microondas","potencia":1000,"horas_dia":0.05}
    ]
    return catalogo

#
#FUNCION CALCULAR COSTO KW HORA
#

def calcular_consumo_kwh(potencia, horas_dia, dias=30):
    """
    calcular el costo por kw de un electrodomestico
    
    arg:

        potencia (int): potencia en watts
        horas_dia (float): horas de uso diario
        dias (int): dias del mes (defaul: 30)
    """

    consumo=(potencia*horas_dia*dias)/1000

    return round(consumo,2)


#
# FUNCION : APLICAR TARIFA X KW
#

def calcular_costo(consumo_kwh, tarifa=6.12):

    costo=round(consumo_kwh*tarifa,2)
    return round(consumo_kwh,costo,)

#
#FUNCION REPORTE DE CONSUMO MENSUAL
#

def reporte(lista_electrodomesticos):
    """
    generar reporte de consumo electrico
    """
    print("\n" "-"*75)
    print("         REPORTE DE CONSUMO ELECTRICO MENSUAL            ")
    print("-"*75)
    print(f"{'N°':<4}|{'Electrodomestico':<18}|{'Potencia':<10}|{'Kwh':<8}|{'Costos S/'}")
    print("-"*75)
    consumo_total = 0
    costo_total = 0

    for i, item in enumerate(lista_electrodomesticos,1):
        print(f"{i:<4}|{item['nombre']:<18}|{item['potencia']}w{'':<6} | "
            f"{item['consumo_kw']:<8}| S/{item['costo']:.2f}")
        
        consumo_total += item['consumo_kw']
        costo_total += item['costo']

    print("-"*75)
    print(f"{'TOTAL MENSUAL:':<35} |{consumo_total:<8.2f} | {costo_total:.2f} S/{"" <5}")
    print("-"*75)


#
#PROGRAMA PRINCIPAL
#
def main():
    
    """
    Funcion principal del gestor de tareas.
    """
    print("="*75)
    print("=   CALCULADORA DE CONSUMO ELECTRICO FAMILIAR             ")
    print("="*75)

    #CREAR CATALOGO
    catalogo=crear_catalogo()

    #MOSTRAR CATALOGO
    print("\n ELECTRODOMESTICOS REGISTRADOS:")
    for i, aparato in enumerate(catalogo,1):
        print(f" {i}. {aparato['nombre']:<18} - {aparato['potencia']}w "
            f"- {aparato['horas_dia']}h/dia")
        
    #CALCULAR CONSUMO
    lista_consumos = []
    
    for i, aparato in catalogo:
        consumo_kwh = calcular_consumo_kwh(
            aparato['potencia'],
            aparato['horas_dia']
        )
    _, costo = calcular_costo(consumo_kwh)
    item = {
            "nombre": aparato['nombre'],
            "potencia": aparato ['potencia'],
            "consumo_kwh": consumo_kwh,
            "costo": costo
    }
    lista_consumos.append(item)
        
    #GENERAR REPORTE
        
    reporte(lista_consumos)
        
    #ESTADISTICA ADICIONA
    
    consumos = [item['consumo_kwh'] for item in lista_consumos ]
    mayor_consumo = max(consumos)
    menor_consumo = min(consumos)
    
    #ENCONTRAR ELECTRODOMESTICOS CON MAYOR CONSUMO
    for item in lista_consumos:
        if item['consumo_kwh'] == mayor_consumo:
            print(f"\n mayor consumo: {item['nombre']}({mayor_consumo}kwh)") 
        if item['conusmo_kwh'] == menor_consumo:
            print(f"\n menos consumo: {item['nombre']}({menor_consumo}kwh)")

#
#PUNTO DE ENTRADA 
#
if __name__ == "__main__":
    main()
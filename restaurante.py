def calcular_descuento(monto):
    if monto >= 200000:
        descuento = monto * 0.15
    elif monto >= 50000:
        descuento = monto * 0.02
    elif monto >= 20000:
        descuento = monto * 0.015
    else:
        descuento = 0
    return descuento

def imprimir_factura(nombre_cliente, monto_compra):
    descuento = calcular_descuento(monto_compra)
    total_a_pagar = monto_compra - descuento
    
    print("\n--- FACTURA DE COBRO ---")
    print(f"Nombre del cliente: {nombre_cliente}")
    print(f"Monto de la compra: ${monto_compra:,.2f}")
    print(f"Valor del descuento: ${descuento:,.2f}")
    print(f"Total a pagar: ${total_a_pagar:,.2f}")
    print("-------------------------")
    print("¡Gracias por su compra!")

def main():
    nombre_cliente = input("Ingrese su nombre: ")
    monto_compra = float(input("Ingrese el monto de la compra: $"))
    
    imprimir_factura(nombre_cliente, monto_compra)

if __name__ == "__main__":
    main()
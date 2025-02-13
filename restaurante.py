def calcularDescuento(valorCompra):
    if valorCompra >= 200000:
        descuento = valorCompra * 0.15
    elif valorCompra >= 50000:
        descuento = valorCompra * 0.02
    elif valorCompra >= 20000:
        descuento = valorCompra * 0.015
    else:
        descuento = 0
    return descuento

def imprimirFactura(nombreCliente, valorDeCompra):
    descuento = calcularDescuento(valorDeCompra)
    totalPagar = valorDeCompra - descuento
    
    print("\n--- FACTURA DE COBRO ---")
    print(f"Nombre del cliente: {nombreCliente}")
    print(f"Monto de la compra: ${valorDeCompra:,.2f}")
    print(f"Valor del descuento: ${descuento:,.2f}")
    print(f"Total a pagar: ${totalPagar:,.2f}")
    print("-------------------------")
    print("¡Gracias por su compra!")

def main():
    nombreCliente = input("Ingrese su nombre: ")
    valorDeCompra = float(input("Ingrese el monto de la compra: $"))
    
    imprimirFactura(nombreCliente, valorDeCompra)

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()

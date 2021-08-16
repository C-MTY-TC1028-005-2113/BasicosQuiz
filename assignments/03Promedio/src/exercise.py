def main():
    #escribe tu código abajo de esta línea
    # importar el módulo math para tener las funciones disponibles
    import math

    # 1º Leer los datos de entrada: a, b, c
    a = int( input("Ingresa el coeficiente a: ") )
    b = int( input("Ingresa el coeficiente b: ") )
    c = int( input("Ingresa el coeficiente c: ") )

    # 2º Calcular las 2 raices usando la formula general
    # Sergio - añadir los (  ) / (  )
    x1 = (  -b + math.sqrt( b ** 2 - 4 * a * c)  )  /  ( 2 * a )
    x2 = (  -b - math.sqrt( b ** 2 - 4 * a * c)  )  /  ( 2 * a )

    # 3º Desplegar las 2 raices
    print("Raiz positiva es :", x1)
    print("Raiz negativa es :", x2)


if __name__ == '__main__':
    main()

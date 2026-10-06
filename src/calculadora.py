def calcular(numero1, numero2, operacion):
    respuesta = 0
    match operacion:
        case '+':
            # Operación suma
            respuesta = numero1 + numero2
        case '-':
            # Operación resta
            respuesta = numero1 - numero2
        case '*':
            # Operación multiplicación
            respuesta = numero1 * numero2
        case '/':
            # Operación división
            respuesta = numero1 / numero2

        case '**':
            # Operación potencia
            respuesta = numero1 ** numero2
        case '//':
            # Operación división entera
            respuesta = numero1 // numero2
        case '%':
            # Operación módulo
            respuesta = numero1 % numero2
        case '√':
            # Operación raíz cuadrada
            respuesta = numero1 ** 0.5
        case 'c':
            # Operación cubo
            respuesta = numero1 ** 3
        case '√3':
            # Operación raíz cúbica
            respuesta = numero1 ** (1/3)
        case _:
            raise ValueError("Operación inválida.")

    return respuesta

if __name__ == '__main__':
    # Lectura del valor de 2 variables enteras por consola:
    print("Ingrese el número 1")
    numero1 = int(input())
    print("Ingrese el número 2")
    numero2 = int(input())
    
    print("Ingrese la operación (+, -, *, /, **, //, %)")
    operacion = input()
    
    resultado = calcular(numero1, numero2, operacion)
    print("La respuesta es " + str(resultado))

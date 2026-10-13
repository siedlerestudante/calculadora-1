def calculadora():
    numero1= float(input("digite o primeiro número: "))
    operacao = input("""digite:
    '+' para adição 
    '-' para subtração
    'x' para multiplicação
    '/' para divisão 
    '*' para potencia
    """)
    numero2 = float(input("digite o segundo numero: "))
    
    if operacao == "+":
        resultado = numero1 + numero2

    elif operacao == "-":
        resultado = numero1 - numero2

    elif operacao == "x":
        resultado = numero1 * numero2

    elif operacao == "/":
        if numero2 == 0:
            resultado = "equação impossivel"
        elif numero1 == 0 and numero2 == 0:
            resultado = "equação impossivel"
        else:
            resultado = numero1 / numero2

    elif operacao == "*":
        resultado = numero1 ** numero2

    else: 
        resultado = "operação invalida"

    print(" ")
    print(f"O Resultado é {resultado}")
    return resultado


def continuar_conta(numero1):

    print(f"o primeiro numero é: {numero1}")

    operacao = input("""digite:
        '+' para adição 
        '-' para subtração
        'x' para multiplicação
        '/' para divisão 
        '*' para potencia
        """)
    
    numero2 = float(input("digite o segundo numero: "))
        
    if operacao == "+":
            resultado = numero1 + numero2
    
    elif operacao == "-":
            resultado = numero1 - numero2
    
    elif operacao == "x":
            resultado = numero1 * numero2
    
    elif operacao == "/":
        if numero2 == 0:
                resultado = "equação impossivel"
        elif numero1 == 0 and numero2 == 0:
                resultado = "equação impossivel"
        else:
                resultado = numero1 / numero2
    
    elif operacao == "*":
            resultado = numero1 ** numero2
    
    else: 
            resultado = "operação invalida"

    print(resultado)
    return resultado



print("...Iniciando a Calculadora...")
resultado_anterior = calculadora()
print(" ")


proximo_passo = 0

while proximo_passo != 3:

    continuar = int(input("""Digite:
    1 -> Para continuar a conta( com o resultado da conta anterior como 1° número)
    2 -> Para reiniciar a calculadora 
    3 -> Para fechar a calculadora
    Fazer ação """))

    proximo_passo += continuar

    if proximo_passo == 1:
        resultado_anterior = continuar_conta(resultado_anterior)
        proximo_passo = 0

    elif proximo_passo == 2:
        resultado_anterior = calculadora()
        proximo_passo = 0

    elif proximo_passo == 3:
        print("...Fechando a Calculadora...")
        break

    else: print("Respota com erro, tente novamente")
    proximo_passo = 0

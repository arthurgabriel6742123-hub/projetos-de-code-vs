print("=== Calculadora ===")
print("Operações disponíveis: +, -, * e /")

try:
    numero1 = float(input("Digite o primeiro número: "))
    operacao = input("Digite a operação (+, -, *, /): ").strip()
    numero2 = float(input("Digite o segundo número: "))

    if operacao == "+":
        resultado = numero1 + numero2
    elif operacao == "-":
        resultado = numero1 - numero2
    elif operacao == "*":
        resultado = numero1 * numero2
    elif operacao == "/":
        if numero2 == 0:
            print("Erro: não é possível dividir por zero.")
            raise SystemExit(1)
        resultado = numero1 / numero2
    else:
        print("Erro: operação inválida.")
        raise SystemExit(1)

    print(f"Resultado: {resultado:g}")
except ValueError:
    print("Erro: digite números válidos.")
    raise SystemExit(1)

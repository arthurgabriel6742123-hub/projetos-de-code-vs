print("=== Super Calculadora ===")

try:
    primeiro_numero = float(input("Digite o primeiro número: "))
    resultado = primeiro_numero
    quantidade = 1

    while quantidade < 9:
        operacao = input("Qual é a operação? (+, -, *, /): ").strip()
        if operacao not in ("+", "-", "*", "/"):
            print("Operação inválida. Escolha +, -, * ou /.")
            continue

        segundo_numero = float(input("Digite o próximo número: "))

        if operacao == "+":
            resultado += segundo_numero
        elif operacao == "-":
            resultado -= segundo_numero
        elif operacao == "*":
            resultado *= segundo_numero
        elif operacao == "/":
            if segundo_numero == 0:
                print("Não é possível dividir por zero.")
                continue
            resultado /= segundo_numero

        quantidade += 1
        print(f"Resultado até agora: {resultado:g}")

        if quantidade == 9:
            print("Você chegou ao limite de 9 números.")
            break

        continuar = input("Deseja botar outro número? (s/n): ").strip().lower()
        if continuar not in ("s", "sim"):
            break

    print(f"Resultado final: {resultado:g}")
except ValueError:
    print("Erro: digite números válidos.")
    raise SystemExit(1)

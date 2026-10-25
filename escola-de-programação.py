alunos = []
materias = []


def cadastrar_aluno():
    nome = input("Nome do aluno: ").strip()
    if not nome:
        print("Nome inválido.")
        return

    curso = input("Curso: ").strip()
    if not curso:
        print("Curso inválido.")
        return

    alunos.append({"nome": nome, "curso": curso})
    print(f"Aluno {nome} cadastrado com sucesso no curso {curso}!")


def listar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    print("\n=== ALUNOS CADASTRADOS ===")
    for indice, aluno in enumerate(alunos, start=1):
        print(f"{indice}. {aluno['nome']} - {aluno['curso']}")


def excluir_aluno():
    if not alunos:
        print("Nenhum aluno cadastrado para excluir.")
        return

    listar_alunos()

    try:
        escolha = int(input("Digite o número do aluno para excluir: "))
    except ValueError:
        print("Digite um número válido.")
        return

    if escolha < 1 or escolha > len(alunos):
        print("Número inválido.")
        return

    aluno_removido = alunos.pop(escolha - 1)
    print(f"Aluno {aluno_removido['nome']} removido com sucesso!")


def cadastrar_materia():
    nome_materia = input("Nome da matéria: ").strip()
    if not nome_materia:
        print("Nome da matéria inválido.")
        return

    materias.append(nome_materia)
    print(f"Matéria {nome_materia} cadastrada com sucesso!")


def listar_materias():
    if not materias:
        print("Nenhuma matéria cadastrada.")
        return

    print("\n=== MATÉRIAS CADASTRADAS ===")
    for indice, materia in enumerate(materias, start=1):
        print(f"{indice}. {materia}")


def excluir_materia():
    if not materias:
        print("Nenhuma matéria cadastrada para excluir.")
        return

    listar_materias()

    try:
        escolha = int(input("Digite o número da matéria para excluir: "))
    except ValueError:
        print("Digite um número válido.")
        return

    if escolha < 1 or escolha > len(materias):
        print("Número inválido.")
        return

    materia_removida = materias.pop(escolha - 1)
    print(f"Matéria {materia_removida} removida com sucesso!")


def menu():
    while True:
        print("\n=== ESCOLA DE PROGRAMAÇÃO ===")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Excluir aluno")
        print("4 - Cadastrar matéria")
        print("5 - Listar matérias")
        print("6 - Excluir matéria")
        print("7 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            excluir_aluno()
        elif opcao == "4":
            cadastrar_materia()
        elif opcao == "5":
            listar_materias()
        elif opcao == "6":
            excluir_materia()
        elif opcao == "7":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


menu()


usuarios = []

def cadastrar():
    nome = input("Nome: ")
    email = input("E-mail: ")
    senha = input("Senha: ")

    usuario = {
        "nome": nome,
        "email": email,
        "senha": senha
    }

    usuarios.append(usuario)
    print("Cadastro realizado com sucesso!")


def listar():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        for u in usuarios:
            print(f"Nome: {u['nome']} | E-mail: {u['email']}")


def excluir_cadastro():
    if not usuarios:
        print("Nenhum usuário cadastrado para excluir.")
        return

    email = input("Digite o e-mail do usuário que deseja excluir: ")

    for usuario in usuarios:
        if usuario["email"] == email:
            usuarios.remove(usuario)
            print(f"Usuário com e-mail {email} foi excluído com sucesso!")
            return

    print("Usuário não encontrado.")


while True:
    print("\n=== MENU ===")
    print("1 - Cadastrar")
    print("2 - Listar usuários")
    print("3 - Excluir cadastro")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        excluir_cadastro()
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")

                 
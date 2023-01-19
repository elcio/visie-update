pessoas = [
    {
        'nome': 'João',
        'idade': 20,
        'email': 'joao@hotmail.com',
        'skills': {'Python', 'Django', 'Flask'},
    },
    {
        'nome': 'Maria',
        'idade': 25,
        'email': 'maria@gmail.com',
        'skills': {'PHP', 'WordPress', 'HTML'},
    },
]


def menu():
    """Exibe o menu e solicita uma opção ao usuário."""
    print("""O que deseja fazer?
    1 - Listar pessoas
    2 - Adicionar pessoa
    3 - Excluir pessoa
    4 - Sair
    """)
    opcao = input('Digite a opção desejada: ')
    if opcao == '1':
        listar_pessoas()
    elif opcao == '2':
        adicionar_pessoa()
    elif opcao == '3':
        excluir_pessoa()
    elif opcao == '4':
        exit()


def listar_pessoas():
    """Exibe as pessoas cadastradas."""
    for pessoa in pessoas:
        print('=' * 60)
        print(f"Nome: {pessoa['nome']}")
        print(f"Idade: {pessoa['idade']}")
        print(f"E-mail: {pessoa['email']}")
        print(f"Skills: {pessoa['skills']}")
    print('=' * 60)


def adicionar_pessoa():
    """Adiciona uma pessoa ao cadastro."""
    nome = recebe_dado('Nome: ')
    idade = recebe_numero('Idade: ')
    email = recebe_email('E-mail: ')
    skills = recebe_set('Skills: ')
    pessoa = {
        'nome': nome,
        'idade': idade,
        'email': email,
        'skills': skills,
    }
    pessoas.append(pessoa)


def recebe_set(prompt):
    """Recebe um conjunto de valores separados por vírgula."""
    valor = ''
    while not valor.strip():
        valor = recebe_dado(prompt)
    return set(map(str.strip, valor.split(',')))


def recebe_numero(prompt):
    """Recebe um número inteiro."""
    valor = ''
    while not valor.isdigit():
        valor = recebe_dado(prompt)
    return valor


def recebe_email(prompt):
    """Recebe um e-mail válido."""
    valor = ''
    while '@' not in valor.strip():
        valor = recebe_dado(prompt)
    return valor


def recebe_dado(prompt):
    """Recebe um dado do usuário."""
    valor = ''
    while not valor.strip():
        valor = input(prompt)
    return valor


def excluir_pessoa():
    """Exclui uma pessoa do cadastro."""
    global pessoas
    email = recebe_email('E-mail da pessoa a excluir: ')
    novo_pessoas = []
    for pessoa in pessoas:
        if pessoa['email'] != email:
            novo_pessoas.append(pessoa)
    pessoas = novo_pessoas


def main():
    """Loop principal."""
    while True:
        menu()


if __name__ == "__main__":
    main()


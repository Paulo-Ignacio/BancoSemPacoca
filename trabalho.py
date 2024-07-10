# Dicionário para armazenar usuários
usuarios = {}

# Dicionário para armazenar contas correntes
contas = {}

def validar_cpf():
    while True:
        cpf = input('Digite o seu CPF: ')

        # Tratamento de entrada
        cpf = cpf.replace(' ', '')
        cpf = cpf.replace('.', '')
        cpf = cpf.replace('-', '')

        # Checa se o CPF inserido é uma sequência de 11 digitos decimais
        if cpf.isdecimal() and len(cpf) == 11:
            return cpf
        else:
            print('-----------------------------')
            print('|ERRO: Digite um CPF válido!|')
            print('-----------------------------')

def cadastrar_usuario(nome, cpf):
    if cpf in usuarios:
        print("Usuário já cadastrado.")
    else:
        usuarios[cpf] = {"nome": nome, "cpf": cpf}
        contas[cpf] = {"saldo": 0.0, "extrato": []}
        print(f"Usuário {nome} cadastrado com sucesso.")

def depositar(cpf, valor):
    if cpf in contas:
        contas[cpf]["saldo"] += valor
        contas[cpf]["extrato"].append(f"Depósito: +R${valor:.2f}")
    else:
        print("Usuário não encontrado.")

def sacar(cpf, valor):
    if cpf in contas:
        if valor > contas[cpf]["saldo"]:
            print("Saldo insuficiente.")
        else:
            contas[cpf]["saldo"] -= valor
            contas[cpf]["extrato"].append(f"Saque: -R${valor:.2f}")
            print("-------------------------")
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
            print("-------------------------")
    else:
        print("Usuário não encontrado.")

def transferir(cpf_origem, cpf_destino, valor):
    if cpf_origem in contas and cpf_destino in contas:
        if valor > contas[cpf_origem]["saldo"]:
            print("Saldo insuficiente para transferência.")
        else:
            contas[cpf_origem]["saldo"] -= valor
            contas[cpf_destino]["saldo"] += valor
            contas[cpf_origem]["extrato"].append(f"Transferência enviada: -R${valor:.2f} para {usuarios[cpf_destino]['nome']}")
            contas[cpf_destino]["extrato"].append(f"Transferência recebida: +R${valor:.2f} de {usuarios[cpf_origem]['nome']}")
    else:
        print("Usuário de origem ou destino não encontrado.")

def gerar_extrato(cpf):
    if cpf in contas:
        print(f"Extrato da conta de {usuarios[cpf]['nome']} (CPF: {usuarios[cpf]['cpf']}):")
        for item in contas[cpf]["extrato"]:
            print(item)
        print(f"Saldo atual: R${contas[cpf]['saldo']:.2f}")
    else:
        print("Usuário não encontrado.")

def editar_usuario(cpf):
    if cpf in usuarios:
        novo_nome = input("Digite o novo nome: ").strip()
        usuarios[cpf]['nome'] = novo_nome
        print(f"Dados do usuário {cpf} atualizados para: {usuarios[cpf]}")
    else:
        print("Usuário não encontrado.")

# Adicione a função fechar_conta aqui
# Adicione a função consultar_saldo aqui

print(
"""
------------------
|SISTEMA DE BANCO|
------------------
* Opção 1: Cadastrar usuário;
* Opção 2: Depositar;
* Opção 3: Sacar;
* Opção 4: Transferir;
* Opção 5: Gerar extrato;
* Opção 6: Editar usuário;
* Opção 7: Sair.
""")

while True:
    opcao = input('Selecione uma opção para prosseguir: ')

    if opcao in '1234567': # Se a opção for válida

        if opcao == '1':
            nome = input("Digite o nome do usuário: ")
            cpf = validar_cpf()
            cadastrar_usuario(nome, cpf)
        elif opcao == '2':
            cpf = validar_cpf()
            valor = float(input("Digite o valor a ser depositado: R$ "))
            depositar(cpf, valor)
        elif opcao == '3':
            cpf = validar_cpf()
            valor = float(input("Digite o valor a ser sacado: R$ "))
            sacar(cpf, valor)
        elif opcao == '4':
            print("---TRANSFERÊNCIA---")
            cpf_origem = validar_cpf()
            cpf_destino = validar_cpf()
            valor = float(input("Digite o valor a ser transferido: R$ "))
            transferir(cpf_origem, cpf_destino, valor)
        elif opcao == '5':
            cpf = validar_cpf()
            gerar_extrato(cpf)
        elif opcao == '6':
            cpf = validar_cpf()
            editar_usuario(cpf)
        elif opcao == '7':
            break  # Sair do programa

        print(
        """
------------------
|SISTEMA DE BANCO|
------------------
* Opção 1: Cadastrar usuário;
* Opção 2: Depositar;
* Opção 3: Sacar;
* Opção 4: Transferir;
* Opção 5: Gerar extrato;
* Opção 6: Editar usuário;
* Opção 7: Sair.
        """)

    else:
        print('-----------------------------------')
        print('|ERRO: Selecione uma opção válida!|')
        print('-----------------------------------')
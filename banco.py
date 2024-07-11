# Dicionário para armazenar usuários
usuarios = {}
usuarios["12345678900"] = {"nome": "João", "cpf": "12345678900"}

# Dicionário para armazenar contas correntes
contas = {}
contas["12345678900"] = {"saldo": 300.0, "extrato": []}

def validar_cpf():
    while True:
        cpf = input('Digite o seu CPF: ')

        # Tratamento de entrada
        cpf = cpf.replace(' ', '')
        cpf = cpf.replace('.', '')
        cpf = cpf.replace('-', '')

        # Checa se o CPF inserido é uma sequência de 11 digitos decimais; 
        # se sim, retorna o CPF para seguir com o programa, caso contrário, emite um erro reinicia o laço While.
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

def fechar_conta(conta):
    while True:
        i = int(input("""Tem certeza que deseja deletar a conta?
                
            1 - SIM
            2 - NÃO
                """))
        if i == 1:
            if conta in usuarios:
                usuarios.pop(conta)
                contas.pop(conta)
                print(f"\nA conta de número {conta} foi apagada com sucesso!")
                break
            else:
                print("Usuário não encontrado.")
                break
        elif i == 2:
            break
        else:
            print("Digite uma opção válida.")

def consultar_saldo(conta):
    while True:
        if conta in contas:
            saldo = contas[conta]["saldo"]
            print(f"\nA conta possui saldo {saldo:.2f}")
            break
        else:
            print("\nUsuário não encontrado. ")
            break
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
* Opção 7: Deletar conta;
* Opção 8: Checar Saldo;
* Opção 9: Sair.

""")

while True:
    opcao = input('Selecione uma opção para proseguir: ')

    if opcao in '123456789': # Se a opção for válida

        if opcao == '1':
            pass # Cadastrar Usuário (Grupo 4)
        elif opcao == '2':
            pass # Depositar (Grupo 4)
        elif opcao == '3':
            pass # Sacar (Grupo 1)
        elif opcao == '4':
            pass # Transferir (Grupo 1)
        elif opcao == '5':
            pass # Gerar extrato (Grupo 3)
        elif opcao == '6':
            pass # Editar usuário (Grupo 3)
        elif opcao == '9':
            break # Sair
        elif opcao == '8':
            while True:
                checarsaldo = input("\nDigite o número da conta para checar o saldo, ou digite 0 para cancelar! ")
                if checarsaldo == '0':
                    break
                else:
                    consultar_saldo(checarsaldo)
        elif opcao == '7':
            while True:
                fecharconta = input("\nDigite o número da conta que deseja que seja cancelada, ou digite 0 para sair! ")
                if fecharconta == '0':
                    break
                else:
                    fechar_conta(fecharconta)
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

"""
# Cadastro de usuários (exemplo)
cadastrar_usuario("João", "12345678900")
cadastrar_usuario("Maria", "09876543211")

# Realizar algumas operações (exemplo)
depositar("12345678900", 1000.0)
sacar("12345678900", 200.0)
transferir("12345678900", "09876543211", 300.0)

# Gerar extratos (exemplo)
gerar_extrato("12345678900")
print()
gerar_extrato("09876543211")
"""

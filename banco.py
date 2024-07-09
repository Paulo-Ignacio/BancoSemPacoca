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
            print("-------------------------")
            print(f" saque de {valor} realizado com sucesso!")
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
    opcao = input('Selecione uma opção para proseguir: ')

    if opcao in '1234567': # Se a opção for válida

        if opcao == '1':
            pass # Cadastrar Usuário (Grupo 4)
        elif opcao == '2':
            pass # Depositar (Grupo 4)
        elif opcao == '3':
            cpf =validar_cpf()
            opcoes =["1", "2", "3", "4", "5", "6", "7", "8"]
            while True:
                print("-------------------------------------------")
                print(  
                        """ opções de saque:
                            1. 10         5. 200
                            2. 20         6. 400
                            3. 50         7. Outro
                            4. 100        8. Voltar Menu principal
                        """)
                print("-------------------------------------------")

                opcao = input("digite a OPÇÃO de acordo com o valor desejado: ")
                if opcao in opcoes: 
                        
                    if opcao == "1":
                        sacar(cpf, 10)
                        break
                    elif opcao == "2":
                        sacar(cpf, 20)
                        break
                    elif opcao == "3":
                        sacar(cpf, 50)
                        break
                    elif opcao == "4":
                        sacar(cpf, 100)
                        break
                    elif opcao == "5":
                        sacar(cpf, 200)
                        break
                    elif opcao == "6":
                        sacar(cpf, 400)
                        break
                    elif opcao == "7":
                        valor = int(input("digite o valor saque desejado: "))
                        sacar(cpf, valor)
                        break
                    elif opcao == "8":
                        break
                else:    
                    print('|ERRO: opção inválida!  Digite uma OPÇÃO correspondente ao valor de saque!|')
        elif opcao == '4':
            print("TRANSFERÊNCIA")
            print("---CPF DE ORIGEM---")
            cpf_origem = validar_cpf()
            print("---CPF DE DESTINO---")   
            cpf_destino = validar_cpf()
            print("---VALOR DA TRANFERÊNCIA---")
            
            while True:
                try:
                    valor = float(input("Digite o valor da transferência:R$ "))
                    if valor <= 0:
                        print("---Valor muito baixo. Digite um valor válido.---")
                    else:
                        break
                except ValueError:
                    print("Atenção! Valor inválido. Digite um valor valido." )

            transferir(cpf_origem, cpf_destino, valor)
            print("!!!Transferência concluida com sucesso!!!")
        elif opcao == '5':
            pass # Gerar extrato (Grupo 3)
        elif opcao == '6':
            pass # Editar usuário (Grupo 3)
        elif opcao == '7':
            break # Sair

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

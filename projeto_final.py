def adicionar_tarefa(lista_de_tarefas, tarefa):
    '''Adiciona uma noa tarefa à lista'''
    lista_de_tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso! ☻")
    print("\n")
    return lista_de_tarefas

def listar_tarefas(lista_de_tarefas):
    '''Exibe a lista de tarefas'''
    print("\n")
    print("♦" * 50)
    print(f"{' ' * 17}LISTA DE TAREFAS{' ' * 17}")
    print("♦" * 50)
    n = 1
    for tarefa in lista_de_tarefas:
        print(f"{n} - {tarefa}")
        n += 1
        print("-" * 50)
    print("\n")

def deletar_tarefa(lista_de_tarefas, tarefa):
    '''Exclui uma tarefa selecionada'''
    lista_de_tarefas.pop((tarefa - 1))
    return lista_de_tarefas

def exibir_menu():
    '''Exibe as funções da lista para selecionar'''
    print("• ESCOLHA UMA OPÇÃO •\n"
        "1 - Inserir nova taraefa\n" 
        "2 - Listar\n"
        "3 - Deletar tarefa\n"      
        "4 - Apagar todas as tarefas\n"
        "5 - Sair"
         )
    print("-" * 50)

def deletar_todas_as_tarefas(lista_de_tarefas):
    '''Deleta TODAS as tarefas'''
    lista_de_tarefas.clear()
    print("Todas as tarefas foram deletadas com sucesso!")
    print("\n")
    return lista_de_tarefas
    
# Inicialização de variáveis
lista_de_tarefas = []
continuar = True

# Cabeçalho do programa
print('♥' * 50)
print(f"{' ' * 10}-Essa é sua Lista de Tarefas-{' ' * 10}")
print('♥' * 50)

# Loop principal
while continuar:
    exibir_menu()
    opcao = input('=> insira o que deseja fazer: ')
    
    if opcao == "1":
        print("\n")
        tarefa = input('=> insira uma nova tarefa: ')
        lista_de_tarefas = adicionar_tarefa(lista_de_tarefas, tarefa)
    elif opcao == "2":
        listar_tarefas(lista_de_tarefas)
    elif opcao == "3":
        # A validação verifica se o valor é numerico, menor ou igual a 0 ou maior que o limite da lista
        tarefa = input('=> insira o número da tarefa que deseja deletar: ')
        if not tarefa.isnumeric():
            print("Número inválido, tente novamente.")
        elif int(tarefa) > len(lista_de_tarefas):
            print("Número inválido, tente novamente.")
        elif int(tarefa) <= 0:
            print("Número inválido, tente novamente.")
        else: 
            deletar_tarefa(lista_de_tarefas, int(tarefa))
            print("Tarefa deletada com sucesso!")
    elif opcao == "4":
        confirmacao = input("Tem certeza que deseja apagar TODAS as tarefas? (s/n): ").lower()
        if confirmacao == 's':
            lista_de_tarefas = deletar_todas_as_tarefas(lista_de_tarefas)
        print('\n')
    elif opcao == "5": 
         continuar = False
    else:
        print("Opção inválida! Por favor, tente novamente.")
    print("\n")


tarefas = []

def mostrar_Tarefas():

    if len(tarefas) == 0:
        print (' Nenhuma tarefa foi registrada')

    else:

        print (" Lista de tarefas: ")
        for i, tarefa in enumerate(tarefas):
            print (f"{i + 1} - {tarefa}")

def adicionar_tarefa():

    tarefa = input("Adicionar nova tarefa:")
    tarefas.append(tarefa)
    print ("Tarefa adicionada com sucesso")

def remover_tarefa():

    mostrar_Tarefas()

    try:
        numero = int(input("Digite o número da tarefa que deseja remover: "))
        if 1 <= numero <= len(tarefas):
            tarefas.pop(numero -1)
            print ("Tarefa removida com sucesso!")

        else:

            print ("Numéro inválido!")     

    except:
        print ("Digite um número válido")

def menu():

    while True:   #Vai criar um loop infinito até eu escolher a opcao 4 que dará um break no sistema

        print("======= MENU =======")
        print("1 - Ver tarefas ")
        print("2 - Adicionar tarefas")
        print("3- Remover tarefas")
        print("4 - Sair")

        opcao = int(input( ("Escolha uma opcão: ")))

        if opcao == 1:

            mostrar_Tarefas()

        elif opcao == 2:

            adicionar_tarefa()

        elif opcao == 3:

            remover_tarefa()

        elif opcao == 4:

            break

        else:

            print ("Opcão inválida, tente novamente")

menu()





    
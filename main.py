import json
import os


def load_tasks():
    try:
        with open('tasks.json', 'r') as arquivo:
            return json.load(arquivo)
    except:
        return []


def save_tasks(tarefas):
    with open('tasks.json', 'w') as arquivo:
        json.dump(tarefas, arquivo, indent=4)


tarefas = load_tasks()


def add_task(tarefas):
    print('Adicionando tarefa')
    print('-' * 20)
    task = input('Digite sua tarefa: ').capitalize()
    tarefas.append(task)
    save_tasks(tarefas)
    print(f'\nTarefa "{task}" adicionada!')
    input('\nPressione ENTER para continuar...')


def list_task(tarefas):
    if not tarefas:
        print('Sua lista de tarefas está vazia!')
    else:
        print('Lista de Tarefas')
        print('-' * 20)
        for i, t in enumerate(tarefas, start=1):
            print(f'{i} - {t}')


def remove_task(tarefas):
    list_task(tarefas)
    if not tarefas:
        return
    print('\nRemovendo tarefa')
    print('-' * 20)
    num = int(input('\nDigite o numero da tarefa: '))
    if 1 <= num <= len(tarefas):
        tarefa_removida = tarefas[num-1]
        tarefas.remove(tarefas[num-1])
        save_tasks(tarefas)
        print(f'\nTarefa "{tarefa_removida}" removida!')
        input('\nPressione ENTER para continuar...')
    else:
        print('\nEssa tarefa não existe!')
        input('\nPressione ENTER para continuar...')


while True:
    os.system('cls')
    print('[1] - Adicionar nova tarefa')
    print('[2] - Listar tarefas')
    print('[3] - Remover uma tarefa')
    print('[4] - Sair\n')
    escolha = int(input('Digite a sua escolha: '))

    match escolha:
        case 1:
            os.system('cls')
            add_task(tarefas)
        case 2:
            os.system('cls')
            list_task(tarefas)
            input('\nPressione ENTER para continuar...')
            os.system('cls')
        case 3:
            os.system('cls')
            remove_task(tarefas)
        case 4:
            break

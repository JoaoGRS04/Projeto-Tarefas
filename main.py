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


def add_task(tarefas):
    print('Adicionando tarefa')
    print('-' * 20)
    task = input('Digite sua tarefa: ').capitalize()
    tarefas.append(task)
    save_tasks(tarefas)
    print(f'\nTarefa "{task}" adicionada!')
    input('\nPressione ENTER para continuar...')
    os.system('cls')


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
    num = int(input('\nDigite o numero da tarefa: '))
    if 1 <= num <= len(tarefas):
        tarefa_removida = tarefas[num-1]
        tarefas.remove(tarefas[num-1])
        save_tasks(tarefas)
        print(f'\nTarefa "{tarefa_removida}" removida!')
        input('\nPressione ENTER para continuar...')
        os.system('cls')
    else:
        print('Essa tarefa não existe')
        input('\nPressione ENTER para continuar...')
        os.system('cls')

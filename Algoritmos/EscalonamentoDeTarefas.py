def escalonarTarefas(tarefas):
    sortedTarefas = sorted(tarefas, key=lambda x: x[1])
    
    tarefas = []
    ultimo = -float('inf')  
    
    for tarefa in sortedTarefas:
        inicio, fim = tarefa
        if inicio >= ultimo:  
            tarefas.append(tarefa)
            ultimo = fim 
    
    return tarefas

if __name__ == "__main__":
    tarefas = [
        (1, 4), (3, 5), (0, 6),
        (5, 7), (8, 9), (5, 9)
    ]

    print(f"\nTarefas selecionadas (início, fim): {escalonarTarefas(tarefas)}\n")

from os import system as sys
from rich.console import Console
from rich.table import Table
from rich.text import Text

console = Console()

sys("clear")

"""
algoritmo de Round-Robin.
* FIFO (First-In-First-Out)


"""


def round_robin(tasks, quantum):
    """
    :param tasks: Lista de tuplas (nome_da_tarefa, tempo_de_execução).
    :param quantum: Tempo máximo que cada tarefa pode executar por vez.
    """

    # Criação da fila de tarefas
    queue = tasks[:]
    time_elapsed = 0  # Tempo total decorrido

    console.rule("[bold blue]Simulação do Algoritmo Round-Robin[/bold blue]")

    while queue:
        # Pega a primeira tarefa da fila
        task_name, task_time = queue.pop(0)

        if task_time <= quantum:
            # A tarefa pode ser concluída nesse quantum
            time_elapsed += task_time
            console.print(
                f"[green]✔ Tarefa `{task_name}` concluída após {time_elapsed} unidades de tempo.[/green]"
            )
        else:
            # A tarefa não pode ser concluída, volta para o fim da fila
            time_elapsed += quantum
            console.print(
                f"""
                [yellow]⏳ Tarefa `{task_name}` executou por {quantum} unidades de tempo.
                Restam {task_time - quantum} unidades.[/yellow]
                """
            )
            queue.append((task_name, task_time - quantum))

    console.rule("[bold green]Todas as tarefas foram concluídas[/bold green]")


# Entrada do usuário
def main():
    console.rule("[bold cyan]Algoritmo de Round-Robin[/bold cyan]")

    n = int(console.input("[bold]Digite o número de tarefas: [/bold]"))

    tasks = []
    for i in range(n):
        task_name = console.input(f"[bold]Digite o nome da tarefa {i + 1}: [/bold]")
        task_time = int(
            console.input(
                f"[bold]Digite o tempo de execução necessário para `{task_name}`: [/bold]"
            )
        )
        tasks.append((task_name, task_time))

    quantum = int(
        console.input("\n[bold]Digite o quantum (tempo máximo por tarefa): [/bold]")
    )

    # Exibe a tabela com as informações das tarefas
    table = Table(title="Tarefas Iniciais")
    table.add_column("Tarefa", justify="left", style="cyan", no_wrap=True)
    table.add_column("Tempo de Execução", justify="center", style="magenta")

    for task_name, task_time in tasks:
        table.add_row(task_name, str(task_time))

    console.print(table)

    # Executar o algoritmo Round-Robin
    round_robin(tasks, quantum)


if __name__ == "__main__":
    main()

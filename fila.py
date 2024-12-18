from collections import deque
from rich.console import Console
from rich.table import Table


from os import system as sys

sys("clear")

"""
Deque é uma estrutura de dados que combina as características de pilhas e filas.
Ele permite adicionar e remover elementos de ambos os lados da estrutura.

Sistema de gerenciamento de impressoras.
Esse sistema organiza documentos enviados para impressão em uma fila.
A impressora processa os documentos na ordem em que foram adicionados à fila (FIFO).
"""


class FilaDeImpressao:
    def __init__(self):
        self.fila = deque()
        self.console = Console()  # Console para saída estilizada

    def adicionar_documento(self, documento):
        """
        Adiciona um documento à fila de impressão.
        """
        self.fila.append(documento)
        self.console.print(
            f"[green]Documento '{documento['nome']}' adicionado à fila![/green]"
        )

    def processar_documento(self):
        """
        Processa o próximo documento da fila.
        """
        if self.esta_vazia():
            self.console.print("[red]Nenhum documento na fila para processar.[/red]")
            return None
        documento = self.fila.popleft()
        self.console.print(
            f"[cyan]Processando documento: {documento['nome']} "
            f"(Páginas: {documento['paginas']})[/cyan]"
        )
        return documento

    def cancelar_documento(self, nome_documento):
        """
        Cancela um documento específico pelo nome.
        """
        for documento in list(self.fila):
            if documento["nome"] == nome_documento:
                self.fila.remove(documento)
                self.console.print(
                    f"[yellow]Documento '{nome_documento}' foi cancelado![/yellow]"
                )
                return True
        self.console.print(
            f"[red]Documento '{nome_documento}' não encontrado na fila.[/red]"
        )
        return False

    def visualizar_fila(self):
        """
        Exibe o estado atual da fila de impressão.
        """
        if self.esta_vazia():
            self.console.print("[bold red]A fila está vazia.[/bold red]")
        else:
            table = Table(title="Fila de Impressão", title_style="bold magenta")
            table.add_column("Posição", justify="center", style="bold cyan")
            table.add_column("Nome do Documento", justify="center", style="bold green")
            table.add_column("Páginas", justify="center", style="bold yellow")

            for i, documento in enumerate(self.fila, start=1):
                table.add_row(str(i), documento["nome"], str(documento["paginas"]))

            self.console.print(table)

    def esta_vazia(self):
        """
        Retorna True se a fila estiver vazia.
        """
        return len(self.fila) == 0


# Criando e manipulando a fila de impressão
fila_impressao = FilaDeImpressao()

# Adicionando documentos
fila_impressao.adicionar_documento({"nome": "Relatório Anual", "paginas": 10})
fila_impressao.adicionar_documento({"nome": "Currículo", "paginas": 2})
fila_impressao.adicionar_documento({"nome": "Projeto Final", "paginas": 25})

# Visualizando a fila
fila_impressao.console.print(
    "\n[bold magenta]--- Visualizando a fila de impressão ---[/bold magenta]"
)
fila_impressao.visualizar_fila()

# Processando o primeiro documento
fila_impressao.console.print(
    "\n[bold magenta]--- Processando documentos ---[/bold magenta]"
)
fila_impressao.processar_documento()

# Visualizando a fila após o processamento
fila_impressao.console.print(
    "\n[bold magenta]--- Visualizando a fila após o processamento ---[/bold magenta]"
)
fila_impressao.visualizar_fila()

# Cancelando um documento específico
fila_impressao.console.print(
    "\n[bold magenta]--- Cancelando um documento específico ---[/bold magenta]"
)
fila_impressao.cancelar_documento("Currículo")

# Visualizando a fila após o cancelamento
fila_impressao.console.print(
    "\n[bold magenta]--- Visualizando a fila após o cancelamento ---[/bold magenta]"
)
fila_impressao.visualizar_fila()

# Processando documentos restantes
fila_impressao.console.print(
    "\n[bold magenta]--- Processando documentos restantes ---[/bold magenta]"
)
while not fila_impressao.esta_vazia():
    fila_impressao.processar_documento()

# Visualizando a fila após concluir todos os processos
fila_impressao.console.print(
    "\n[bold magenta]--- Visualizando a fila após concluir todos os processos ---[/bold magenta]"
)
fila_impressao.visualizar_fila()

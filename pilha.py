from rich.console import Console
from rich.table import Table

from os import system as sys

sys('clear')

class Navegador:
    def __init__(self):
        self.pilha_anteriores = []  # Páginas visitadas anteriormente
        self.pilha_futuros = []  # Páginas futuras
        self.pagina_atual = None  # Página atual
        self.console = Console()  # Instância do console para saída estilizada

    def visitar_pagina(self, pagina):
        """
        Visita uma nova página, adicionando à pilha de páginas anteriores
        e limpando a pilha de páginas futuras.
        """
        if self.pagina_atual == pagina:
            self.console.print(f"[yellow]Você já está na página: {pagina}[/yellow]")
            return

        if self.pagina_atual is not None:
            self.pilha_anteriores.append(self.pagina_atual)
        self.pagina_atual = pagina
        self.pilha_futuros.clear()  # Limpa as páginas futuras ao visitar uma nova página
        self.console.print(f"[green]Visitando: {pagina}[/green]")

    def voltar(self):
        """
        Volta para a página anterior, movendo a página atual para a pilha de futuros.
        """
        if not self.pilha_anteriores:
            self.console.print("[red]Não há páginas anteriores para voltar.[/red]")
            return

        self.pilha_futuros.append(self.pagina_atual)
        self.pagina_atual = self.pilha_anteriores.pop()
        self.console.print(f"[blue]Voltando para: {self.pagina_atual}[/blue]")

    def avancar(self):
        """
        Avança para a próxima página, movendo a página atual para a pilha de anteriores.
        """
        if not self.pilha_futuros:
            self.console.print("[red]Não há páginas futuras para avançar.[/red]")
            return

        self.pilha_anteriores.append(self.pagina_atual)
        self.pagina_atual = self.pilha_futuros.pop()
        self.console.print(f"[cyan]Avançando para: {self.pagina_atual}[/cyan]")

    def exibir_estado(self):
        """
        Exibe o estado atual do navegador, incluindo a página atual,
        as páginas anteriores e as páginas futuras.
        """
        table = Table(title="Estado do Navegador", title_style="bold magenta")
        table.add_column("Categoria", justify="center", style="bold cyan")
        table.add_column("Páginas", justify="center", style="bold yellow")

        # Adiciona as informações ao estado
        table.add_row("Página Atual", self.pagina_atual or "[red]Nenhuma[/red]")
        table.add_row(
            "Páginas Anteriores", ", ".join(self.pilha_anteriores) or "Nenhuma"
        )
        table.add_row("Páginas Futuras", ", ".join(self.pilha_futuros) or "Nenhuma")

        self.console.print(table)

    def exibir_historico_completo(self):
        """
        Exibe um histórico completo das páginas visitadas,
        combinando as pilhas de anteriores, a página atual e os futuros.
        """
        historico = self.pilha_anteriores + [self.pagina_atual] + self.pilha_futuros
        self.console.print("\n[bold green]Histórico Completo:[/bold green]")
        for i, pagina in enumerate(historico, 1):
            if pagina == self.pagina_atual:
                self.console.print(f"[bold cyan]{i}. {pagina} (Atual)[/bold cyan]")
            else:
                self.console.print(f"[yellow]{i}. {pagina}[/yellow]")


# Instância do navegador
navegador = Navegador()

# Simulação do uso do navegador
navegador.visitar_pagina("google.com")
navegador.visitar_pagina("wikipedia.org")
navegador.visitar_pagina("openai.com")

navegador.exibir_estado()

navegador.voltar()
navegador.voltar()

navegador.exibir_estado()

navegador.avancar()

navegador.exibir_estado()

navegador.visitar_pagina("github.com")

navegador.exibir_estado()

navegador.exibir_historico_completo()

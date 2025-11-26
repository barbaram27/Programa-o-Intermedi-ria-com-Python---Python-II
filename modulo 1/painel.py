"""
Módulo de painel usando rich.panel.

Oferece funções que exibem textos dentro de painéis estilizados.
"""

from rich.console import Console
from rich.panel import Panel

console = Console()

def _ler_arquivo(texto: str, isArquivo: bool) -> str:
    """Lê o arquivo se necessário."""
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            return f.read()
    return texto


def painel_simples(texto: str, isArquivo: bool = False) -> None:
    """Exibe o texto em um painel simples."""
    full = _ler_arquivo(texto, isArquivo)
    console.print(Panel(full, title="Painel Simples"))


def painel_estiloso(texto: str, isArquivo: bool = False) -> None:
    """Exibe o texto com bordas e estilo."""
    full = _ler_arquivo(texto, isArquivo)
    console.print(
        Panel(
            full,
            title="[bold magenta]Painel Estiloso[/]",
            border_style="blue",
            expand=True,
        )
    )

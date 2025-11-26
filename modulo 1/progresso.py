"""
Módulo de progresso usando rich.progress.

Inclui barras de progresso que exibem o texto junto.
"""

from rich.console import Console
from rich.progress import Progress
import time

console = Console()

def _ler_arquivo(texto: str, isArquivo: bool) -> str:
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            return f.read()
    return texto


def progresso_lento(texto: str, isArquivo: bool = False) -> None:
    """Mostra uma barra de progresso lenta com o texto ao final."""
    full = _ler_arquivo(texto, isArquivo)

    with Progress() as progress:
        task = progress.add_task("Processando...", total=50)
        for _ in range(50):
            time.sleep(0.02)
            progress.update(task, advance=1)

    console.print(full)


def progresso_com_texto(texto: str, isArquivo: bool = False) -> None:
    """Mostra o texto dentro da descrição da barra enquanto carrega."""
    full = _ler_arquivo(texto, isArquivo)

    with Progress() as progress:
        task = progress.add_task(full[:30] + "...", total=30)
        for _ in range(30):
            time.sleep(0.03)
            progress.update(task, advance=1)


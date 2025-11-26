"""
Módulo de estilos usando rich.

Altera cor, negrito, itálico e aplica formatação Markdown.
"""

from rich.console import Console
from rich.markdown import Markdown

console = Console()

def _ler_arquivo(texto: str, isArquivo: bool) -> str:
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            return f.read()
    return texto


def estilo_colorido(texto: str, isArquivo: bool = False) -> None:
    """Exibe o texto com cor roxa e negrito."""
    full = _ler_arquivo(texto, isArquivo)
    console.print(f"[bold purple]{full}[/]")


def estilo_markdown(texto: str, isArquivo: bool = False) -> None:
    """Renderiza o texto como Markdown."""
    full = _ler_arquivo(texto, isArquivo)
    md = Markdown(full)
    console.print(md)

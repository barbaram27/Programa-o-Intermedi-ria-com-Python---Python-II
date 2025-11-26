"""
Módulo de layout usando rich.layout.

Cada função recebe (texto: str, isArquivo: bool) e imprime
o conteúdo com layouts diferentes.
"""

from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel

console = Console()

def _ler_arquivo(texto: str, isArquivo: bool) -> str:
    """Lê o arquivo se isArquivo for True."""
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            return f.read()
    return texto


def layout_duas_colunas(texto: str, isArquivo: bool = False) -> None:
    """Divide o texto em duas colunas."""
    full = _ler_arquivo(texto, isArquivo)
    meio = len(full) // 2
    left = full[:meio]
    right = full[meio:]

    layout = Layout()
    layout.split_row(
        Layout(Panel(left, title="Coluna 1")),
        Layout(Panel(right, title="Coluna 2")),
    )

    console.print(layout)


def layout_três_blocos(texto: str, isArquivo: bool = False) -> None:
    """Divide o texto em três blocos verticais."""
    full = _ler_arquivo(texto, isArquivo)

    partes = [p.strip() for p in full.split("\n\n") if p.strip()][:3]

    layout = Layout()
    layout.split_column(
        Layout(Panel(partes[0] if len(partes) > 0 else "(vazio)", title="Bloco 1")),
        Layout(Panel(partes[1] if len(partes) > 1 else "(vazio)", title="Bloco 2")),
        Layout(Panel(partes[2] if len(partes) > 2 else "(vazio)", title="Bloco 3")),
    )

    console.print(layout)

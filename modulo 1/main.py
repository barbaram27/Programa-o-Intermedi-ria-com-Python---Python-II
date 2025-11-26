"""
Programa principal com argparse.

Executa funções dos módulos do pacote personalizador.
"""

import argparse
from personalizador import layout, painel, progresso, estilo

# Mapeamento de módulos
MODULOS = {
    "layout": layout,
    "painel": painel,
    "progresso": progresso,
    "estilo": estilo
}

# Mapeamento de funções por módulo
FUNCOES = {
    "layout": {
        "layout_duas_colunas": layout.layout_duas_colunas,
        "layout_três_blocos": layout.layout_três_blocos
    },
    "painel": {
        "painel_simples": painel.painel_simples,
        "painel_estiloso": painel.painel_estiloso
    },
    "progresso": {
        "progresso_lento": progresso.progresso_lento,
        "progresso_com_texto": progresso.progresso_com_texto
    },
    "estilo": {
        "estilo_colorido": estilo.estilo_colorido,
        "estilo_markdown": estilo.estilo_markdown
    }
}


def main():
    parser = argparse.ArgumentParser(
        description="Imprime textos formatados usando o pacote personalizador."
    )

    parser.add_argument(
        "texto",
        help="Texto a ser exibido OU caminho para arquivo."
    )

    parser.add_argument(
        "-a", "--arquivo",
        action="store_true",
        help="Indica que o argumento é um arquivo."
    )

    parser.add_argument(
        "-m", "--modulo",
        choices=MODULOS.keys(),
        required=True,
        help=f"Escolha um módulo: {list(MODULOS.keys())}"
    )

    parser.add_argument(
        "-f", "--funcao",
        required=True,
        help="Nome da função dentro do módulo escolhido."
    )

    args = parser.parse_args()

    if args.funcao not in FUNCOES[args.modulo]:
        raise ValueError(f"Função inválida! Disponíveis: {list(FUNCOES[args.modulo])}")

    func = FUNCOES[args.modulo][args.funcao]
    func(args.texto, args.arquivo)


if __name__ == "__main__":
    main()

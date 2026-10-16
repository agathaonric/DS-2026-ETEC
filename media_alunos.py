def calcular_media(notas):
    """Calcula a média aritmética das notas de um aluno."""
    if not notas:
        return 0.0
    return sum(notas) / len(notas)


def verificar_status(media, media_minima=6.0):
    """Verifica se o aluno foi aprovado ou reprovado com base na média."""
    if media >= media_minima:
        return "Aprovado"
    else:
        return "Reprovado"


def gerar_relatorio(nome_aluno, notas):
    """Procedimento para exibir o relatório de desempenho do aluno."""
    media = calcular_media(notas)
    status = verificar_status(media)

    print("=" * 35)
    print("      RELATÓRIO DE DESEMPENHO      ")
    print("=" * 35)
    print(f"Aluno: {nome_aluno}")
    print(f"Notas: {', '.join(map(str, notas))}")
    print(f"Média Final: {media:.2f}")
    print(f"Situação: {status}")
    print("=" * 35 + "\n")


# Exemplo de uso do sistema com múltiplos alunos
alunos = {
    "Ana Silva": [7.5, 8.0, 6.5],
    "Carlos Souza": [4.0, 5.5, 6.0],
    "Mariana Costa": [9.0, 8.5, 9.5],
}

for nome, notas in alunos.items():
    gerar_relatorio(nome, notas)
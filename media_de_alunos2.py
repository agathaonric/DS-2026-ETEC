class Aluno:

  def __init__(self, matricula, nome, notas, pesos=None):
    self.matricula = matricula
    self.nome = nome
    self.pesos = pesos
    # Validação de domínio logo na inicialização
    self.notas = self._validar_e_filtrar_notas(notas)

  def _validar_e_filtrar_notas(self, notas):
    """Garante que as notas sejam numéricas e estejam entre 0 e 10."""
    notas_validadas = []
    for nota in notas:
      if not isinstance(nota, (int, float)):
        raise TypeError(f"Nota inválida (tipo não numérico): {nota}")
      if not (0.0 <= nota <= 10.0):
        raise ValueError(
            f"Nota inválida ({nota}). Deve estar entre 0.0 e 10.0."
        )
      notas_validadas.append(nota)
    return notas_validadas

  def calcular_media(self):
    """Calcula média aritmética ou ponderada sem duplicar código."""
    if not self.notas:
      return 0.0

    if self.pesos:
      if len(self.pesos) != len(self.notas):
        raise ValueError(
            "A quantidade de pesos deve ser igual à quantidade de notas."
        )
      soma_ponderada = sum(n * p for n, p in zip(self.notas, self.pesos))
      soma_pesos = sum(self.pesos)
      return soma_ponderada / soma_pesos
    else:
      return sum(self.notas) / len(self.notas)

  def verificar_status(self):
    """Define a situação acadêmica considerando também a recuperação."""
    media = self.calcular_media()
    if media >= 6.0:
      return "Aprovado"
    elif 4.0 <= media < 6.0:
      return "Recuperação"
    else:
      return "Reprovado"

  def gerar_dados_relatorio(self):
    """Retorna um dicionário com os dados.

    Isola a lógica de negócio da apresentação (I/O).
    """
    media = self.calcular_media()
    return {
        "matricula": self.matricula,
        "nome": self.nome,
        "notas": self.notas,
        "media_final": round(media, 2),
        "status": self.verificar_status(),
    }


def exibir_relatorio_terminal(dados_relatorio):
    """Camada de apresentação isolada (I/O).

    Pode ser substituída por envio de e-mail, PDF ou API.
    """
    print("=" * 45)
    print("         RELATÓRIO DE DESEMPENHOS ESCOLAR        ")
    print("=" * 45)
    print(f"Matrícula : {dados_relatorio['matricula']}")
    print(f"Aluno     : {dados_relatorio['nome']}")
    print(f"Notas     : {dados_relatorio['notas']}")
    print(f"Média     : {dados_relatorio['media_final']}")
    print(f"Situação  : {dados_relatorio['status']}")
    print("=" * 45 + "\n")


# Exemplo de uso seguro do sistema:
try:
  # Aluno com notas ponderadas (ex: pesos 1, 1 e 2)
  aluno1 = Aluno(
      matricula="2026001",
      nome="Ana Silva",
      notas=[7.5, 8.0, 6.5],
      pesos=[1, 1, 2],
  )
  dados = aluno1.gerar_dados_relatorio()
  exibir_relatorio_terminal(dados)

  # Testando validação de erro (descomente para testar a exceção)
  # aluno_erro = Aluno("2026002", "Carlos Souza", [12.0, 5.0])

except (ValueError, TypeError) as erro:
  print(f"[ERRO DE SISTEMA]: {erro}")
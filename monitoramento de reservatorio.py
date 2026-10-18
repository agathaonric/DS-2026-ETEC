from colorama import Fore, Style, init

init()

niveis_reservatorio = [
    {"nivel": 1, "situacao": "Muito baixo (crítico)", "cor": Fore.RED},
    {"nivel": 2, "situacao": "Baixo", "cor": Fore.YELLOW},
    {"nivel": 3, "situacao": "Médio", "cor": Fore.GREEN},
    {"nivel": 4, "situacao": "Alto", "cor": Fore.CYAN},
    {"nivel": 5, "situacao": "Muito alto (alerta)", "cor": Fore.BLUE},]


def exibir_alerta(dados_nivel):
  cor = dados_nivel["cor"]
  nivel = dados_nivel["nivel"]
  situacao = dados_nivel["situacao"]

  # Exibe a mensagem formatada com a cor específica
  print(f"{cor}Nível {nivel} - Situação: {situacao}")

  print(Style.RESET_ALL, end="")


def simular_monitoramento():
  print("=" * 50)
  print("MONITORAMENTO DO RESERVATÓRIO DE ÁGUA - SIMULAÇÃO")
  print("=" * 50)

  for item in niveis_reservatorio:
    exibir_alerta(item)


if __name__ == "__main__":
  simular_monitoramento()
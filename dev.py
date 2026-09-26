excelente = 0
bom = 0
ruim = 0
TOTAL_ENTREVISTADOS = 5

print(f"--- Início da Pesquisa de Atendimento ({TOTAL_ENTREVISTADOS} entrevistados) ---")

for i in range(1, TOTAL_ENTREVISTADOS + 1):
    print(f"\nEntrevistado nº {i}:")
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    
    print("Opiniões sobre o atendimento:")
    print("1: EXCELENTE")
    print("2: BOM")
    print("3: RUIM")
    
    # Validação da entrada (só sai daqui quando for 1, 2 ou 3)
    while True:
        opiniao = input("Digite o número da sua opinião (1, 2 ou 3): ")
        if opiniao in ['1', '2', '3']:
            break
        print("Opção inválida! Por favor, digite 1, 2 ou 3.")

    # ATENÇÃO À INDENTAÇÃO: Este 'if' fica fora do 'while' (mesma margem do 'while')
    if opiniao == '1':
        excelente += 1
    elif opiniao == '2':
        bom += 1
    elif opiniao == '3':
        ruim += 1

# Exibição dos resultados (fora do ciclo 'for')
print("\n" + "="*30)
print("       RESULTADO DA PESQUISA     ")
print("="*30)
print(f"a) Quantidade de respostas 'EXCELENTE': {excelente}")
print(f"b) Quantidade de respostas 'RUIM': {ruim}")
print(f"Total de respostas 'BOM': {bom}")  
print("="*30)

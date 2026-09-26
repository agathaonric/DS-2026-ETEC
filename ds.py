valor= float(input("Digite o valor da compra (R$)"))
if valor <200.00: 
    porcentagem_desconto= 5
elif 200.00 <= valor < 300.00:
    porcentagem_desconto = 10
else:
    porcentagem_desconto= 15
valor_desconto = valor * (porcentagem_desconto / 100)
valor_final = valor - valor_desconto
print(f"\n--- Resumo do Desconto ---")
print(f"Porcentagem de desconto aplicada: {porcentagem_desconto}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor total a ser pago: R$ {valor_final:.2f}")
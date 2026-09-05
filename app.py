Nome=input("Fale o nome do Eletrodoméstico:")
print ("Tudo bem, seu aparelho é:", Nome ) 
Potencia= float (input ("Okay, agora preciso saber da potência do seu eletrodoméstico (em Watts):"))
print ("Certo,", Potencia, "W")
Horas= float (input ("Agora, digite o tempo médio de uso por dia (em horas):"))
print ("Maravilha,", Horas, "h")
print("\n--- Calculando... ---\n")
Consumo_Mensal = (Potencia * Horas * 30) / 1000
valor_kwh = 0.75
custo_estimado = Consumo_Mensal * valor_kwh
print("\n" + "="*30)
print(f"Nome: {Nome}")
print(f"Consumo estimado: {Consumo_Mensal:.1f} kWh/mês")
print(f"Custo estimado: R$ {custo_estimado:.2f}/mês")
print("="*30)








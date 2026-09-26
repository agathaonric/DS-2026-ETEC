nome= input("Diga em qual categoria seu imóvel se encaixa a seguir (comercial, casa ou apartamento): ")
print ("Seu imóvel é do tipo", nome)
consumo= float(input("Preciso saber do seu consumo de água por mês (em 𝑚 3, apenas números decimais):"))
if nome == "comercial" :  
     print("Tarifa comercial aplicada – consulte o plano corporativo.")
elif nome == "apartamento"  and consumo < 10:
 print("Consumo econômico – excelente controle de água!")
elif nome == "apartamento" or "casa" and consumo <= 25:
   print("Consumo moderado – dentro do padrão residencial.")
else:
 print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")



     

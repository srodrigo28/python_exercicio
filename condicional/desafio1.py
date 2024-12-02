registroKM = float(input("Km registrado? "))
valor_multa_km = 30
if registroKM > 80:
    print("Parabéns multa a caminho")
    multa = (registroKM - 80) * valor_multa_km
    print(f"Valor da multa é R$ {multa:.2f}")
else:
    print("parabéns você respeita as leis de transito!")
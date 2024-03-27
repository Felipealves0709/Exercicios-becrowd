tempo = int(input("Tempo gastop: "))
velocidade_media = int(input("digite a velocidade media durante a viagem Km/h: "))

distancia = tempo * velocidade_media

litros_gastos = distancia/12
print(f"{litros_gastos:.3f} litros")


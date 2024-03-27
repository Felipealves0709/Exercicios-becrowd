valor = float(input("Digite o valor: "))
cedulas =0
valorCedulaAtual=100
valorAserAntregue = valor
while True:
    if valorCedulaAtual <= valorAserAntregue:
        cedulas +=1
        valorAserAntregue -= valorCedulaAtual
    else:
        print("%d cedula(s) de R$ %5.2f" % (cedulas,valorCedulaAtual))
        if valorAserAntregue == 0:
            break
        if valorCedulaAtual == 100:
            valorCedulaAtual =50
        elif valorCedulaAtual ==50:
            valorCedulaAtual =20
        elif  valorCedulaAtual == 20:
            valorCedulaAtual = 10
        elif valorCedulaAtual ==10:
            valorCedulaAtual = 5
        elif valorCedulaAtual == 5:
            valorCedulaAtual =2
        cedulas=0
        
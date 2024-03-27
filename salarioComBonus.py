vendedor = input("Digite o nome do vendedor: ")
salaraioFixo = float(input("Digite o salário fixo: "))

total_vendas = float(input("Digite o total de vendas: "))

comissao = total_vendas * 0.15

salario_total = comissao + salaraioFixo

print(f"Total = R${salario_total:.2f}")
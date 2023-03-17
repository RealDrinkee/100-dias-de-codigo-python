print("Bem-vindo(a) à calculadora de gorjeta!")

contaTotal = float(input("Qual foi o valor total da conta? R$"))
gorjeta = int(input("Qual a porcentagem de gorjeta que você deseja dar? 10, 12 ou 15? "))
numeroPessoas = int(input("Quantas pessoas vão dividir a conta? "))

gorjetaEmPercentual = gorjeta / 100
valorTotalGorjeta = contaTotal * gorjetaEmPercentual
valorTotalConta = contaTotal + valorTotalGorjeta
valorPorPessoa = valorTotalConta / numeroPessoas
valorFinal = round(valorPorPessoa, 2)

print("Cada pessoa deve pagar: R${}".format(valorFinal))
print("Locadora de Veiculos")
dias=int(input("Quantos dias alugados? "))
km=float(input("Quantos Km rodados? "))

diaria = 60
kmrodado = 0.15

print("O total a pagar é de R$ {:.2f}".format((dias*diaria)+(km*kmrodado)))

print("Escolha seu desconto:")
print("1 - 5%"
      "\n2 - 10%"
      "\n3 - 15%"
      "\n4 - 20%")
opcao = int(input("Digite a opção desejada: "))
valor = float(input("Digite o valor do produto: "))

if opcao == 1:
            opcao = 5
elif opcao == 2:    
            opcao = 10
elif opcao == 3:    
            opcao = 15
elif opcao == 4:    
            opcao = 20
else:
    print("Opção inválida")
    exit()

desconto = opcao * valor / 100
valor_final = valor - desconto
print(f"O valor do desconto é de R$ {desconto:.2f} e o valor final é de R${valor_final:.2f}")

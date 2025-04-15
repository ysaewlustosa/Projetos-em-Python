# Exercicio 1 - Posição da primeira e última letra A de uma string
# Este programa solicita ao usuário que insira uma frase e, em seguida, exibe a posição da primeira e última letra da frase.    
Frase = str(input("Digite uma frase: ")).upper().strip()

print("A letra A {} aparece na frase. " .format(Frase.count('A')))
print("A primeira letra A aparece na posição {}" .format(Frase.find('A')+1))
print("A última letra A aparece na posição {}" .format(Frase.rfind('A')+1))

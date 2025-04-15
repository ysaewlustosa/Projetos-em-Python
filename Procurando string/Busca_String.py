# Este programa verifica se o nome do usuário contém a palavra "Silva".
# O programa solicita ao usuário que insira seu nome completo e, em seguida, verifica se a palavra "Silva" está presente no nome.

nome = str(input("Digite seu nome completo: "))



if 'Silva' in nome: 
    print(f"Seu nome tem 'Silva'")
else:
    print(f"Seu nome não tem 'Silva'")

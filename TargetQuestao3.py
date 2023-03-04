numeroEscolhido = int(input("Digite seu número aqui: "))

n1 = 0
n2 = 1

while n1 < numeroEscolhido:
    n1, n2 = n2, n2 + n1

print(n1 == numeroEscolhido)
if n1 != numeroEscolhido:
    print(f"O número {numeroEscolhido} não pertence à Sequência de Fibonacci.")
else:
    print(f"O número{numeroEscolhido} pertence à Sequência de Fibonacci.")
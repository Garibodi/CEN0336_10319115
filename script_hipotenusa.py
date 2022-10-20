#aceita as variaveis do triangulo
# a = input("Digite o valor do lado 1: ")
# b = input("Digite o valor do lado 2: ")

import sys
a = sys.argv[1]
b = sys.argv[2]

#checa se é um número menor que 500 e se realmente é um número, se não cumprir estas condições pede ao usuário para recomeçar
def dados():
    global a, b
    try:
        if int(a) > 500 or int(b) > 500: 
            print("Digite números até no máximo 500. Tente novamente")
            a = input("Digite o valor do lado 1: ")
            b = input("Digite o valor do lado 2: ")
            dados()
    except:
        print("Você digitou algo que não um número, tente novamente")
        a = int(input("Digite o valor do lado 1: "))
        b = int(input("Digite o valor do lado 2: "))
        dados()
dados()

#imprime o valor do quadrado da hipotenusa
a = int(a)
b = int(b)
y = (a **2 + b**2)**(1/2)
print("O quadrado da hipotenusa para o triangulo retângulo com lados a=", a, "e b=", b, "é", y)

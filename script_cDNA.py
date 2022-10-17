#aceita o input do usuário sobre a sequência e os números de interesse

import sys
print(sys.argv)
seq = sys.argv[1]
n1 = sys.argv[2]
n2 = sys.argv[3]
n3 = sys.argv[4]
n4 = sys.argv[5]
lenght = len(seq[0: ])

#diz o tamanho da string
print("tamanho da string é", lenght, "caracteres")

def testes(): #testa se os formatos estão certos e se os números são menores que a sequência
    global seq, n1, n2, n3, n4, lenght
    try:
        seq = str(seq)
        n1 = int(n1)
        n2 = int(n2)
        n3 = int(n3)
        n4 = int(n4)

    except:
        if type(seq) == int:
            print("Sua sequência não está correta")
        elif type(n1) != int or n1 > seq:
            print("Sequência certa, porém n1 não é um número")
        elif type(n2) != int:
            print("Sequência certa, porém n2 não é um número")
        elif type(n3) != int:
            print("Sequência certa, porém n3 não é um número")
        elif type(n4) != int:
            print("Sequência certa, porém n4 não é um número")        
testes()




def check(a):
    if a < lenght:
        print("Intervalos ok!")
    elif a > lenght: #testa se os números não são maiores que a string
        print("Deu ruim, ", a, "é muito grande")
      
            
check(n1)
check(n2)
check(n3)
check(n4)

#pega o intervalo n1:n2 e n3:n4, printa cada um
seq1 = seq[n1 -1 :n2 -1]
seq2 = seq[n3 -1 :n4 -1 ]
print("As sequências são: ", seq1, " e ", seq2)

#conferir se inicia com o códon de inicio, ATG.
if "ATG" in seq1[0: ]:
    print("A sequência 1 começa com ATG")
    beg = 1
else:
    print("A sequência 1 não começa com ATG")
    beg = 0

#conferir se termina com o códon de termino, TAG, TAA, TGA.
if "TAG" or "TAA" or "TGA" in seq2[ :n4]:
    print("A sequência 2 termina com stop codon")
    end = 1
else:
    print("A sequência 2 não termina com stop codon")
    end = 0

def concatena() :  #, concatena e printa o resultado   
    global beg, end, seq1, seq2, seq3
    if (beg and end) == 1:
        seq3 = seq1 + seq2
        print("Sequência resultante é: ", seq3)
    elif beg == 0:
        print("Sequência 1 não deu certo")
    elif end == 0:
        print("Sequência 2 deu Não deu certo")
if (beg and end) == 1:
    concatena()











#crie um script de python com o nome script_cDNA.py que realize as seguintes operações: 

#1. Aceitar cinco argumentos da linha de comentos (use o modulo sys). O primeiro argumento é uma sequência de DNA (veja abaixo), os outros quatro argumentos são números inteiros. Os números inteiros correspondem a os números n1, n2, n3 e n4 como são mostrados na figura de acima, nessa ordem específica.

#2. O script tem que conferir que o usuário passou os dados de tipo correto, i.e., o primeiro um 'string' e os restantes, números inteiros (lembre das funcões int e isdigit). Além disso, tem que conferir que nenhum dos inteiros seja maior que o tamanho da sequência de DNA.

#3. O script tem que extrair a sequência da CDS 1, e conferir se inicia com o códon de inicio, ATG.

#4. O script tem que extrair a sequência da CDS 2, e conferir se termina com um dos códons de parada, TAG, TAA ou TGA.

#5. Caso o ponto 3 e 4 sejam verdadeiros, imprimir na tela a sequencia que resulta da juntar (concatenar) as CDS 1 e CDS 2.

#Seu script tem que ter comentários (linhas que iniciam com #) indicando o que está fazendo cada bloco de código!

#Seu script tem que ser carregado (ADD/COMMIT/PUSH) no seu repositório para a prova.

#CGTCGTCGCCGCCGCCGCCATGTCGGGAGGTGGTGTGATCCGTGGCCCGACGAAAAAAAAAAAAAGCGGGGAACAACGACTGCCGCATCTACGTGTAAAAAAACGAAAAAAAAAAAAAAAAAAAA

#E as coordenadas:

#n1: 20

#n2: 49

#n3: 66

#n4: 98

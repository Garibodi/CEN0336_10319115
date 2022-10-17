#crie um script de python com o nome script_cDNA.py que realize as seguintes operações: 

#1. Aceitar cinco argumentos da linha de comentos (use o modulo sys). O primeiro argumento é uma sequência de DNA (veja abaixo), os outros quatro argumentos são números inteiros. Os números inteiros correspondem a os números n1, n2, n3 e n4 como são mostrados na figura de acima, nessa ordem específica.

#2. O script tem que conferir que o usuário passou os dados de tipo correto, i.e., o primeiro um 'string' e os restantes, números inteiros (lembre das funcões int e isdigit). Além disso, tem que conferir que nenhum dos inteiros seja maior que o tamanho da sequência de DNA.

#3. O script tem que extrair a sequência da CDS 1, e conferir se inicia com o códon de inicio, ATG.

#4. O script tem que extrair a sequência da CDS 2, e conferir se termina com um dos códons de parada, TAG, TAA ou TGA.

#5. Caso o ponto 3 e 4 sejam verdadeiros, imprimir na tela a sequencia que resulta da juntar (concatenar) as CDS 1 e CDS 2.

#Seu script tem que ter comentários (linhas que iniciam com #) indicando o que está fazendo cada bloco de código!

#CGTCGTCGCCGCCGCCGCCATGTCGGGAGGTGGTGTGATCCGTGGCCCGACGAAAAAAAAAAAAAGCGGGGAACAACGACTGCCGCATCTACGTGTAAAAAAACGAAAAAAAAAAAAAAAAAAAA
#E as coordenadas:
#n1: 20
#n2: 49
#n3: 66
#n4: 98

#aceita os dados via terminal usando sys
# import sys
# print(sys.argv)
# seq = sys.argv[1]
# n1 = sys.argv[2]
# n2 = sys.argv[3]
# n3 = sys.argv[4]
# n4 = sys.argv[5]
# lenght = len(seq[0: ])

#or

#aceita os dados via input
# seq = input("Sequência: ")
# n1 = input("1o Número: ")
# n2 = input("2o Número: ")
# n3 = input("3o Número: ")
# n4 = input("4o Número: ")
# lenght = len(seq[0: ])

# or

#aceita os dados no script
seq = "CGTCGTCGCCGCCGCCGCCATGTCGGGAGGTGGTGTGATCCGTGGCCCGACGAAAAAAAAAAAAAGCGGGGAACAACGACTGCCGCATCTACGTGTAAAAAAACGAAAAAAAAAAAAAAAAAAAA"
n1 = "20"
n2 = "49"
n3 = "66"
n4 = "98"
lenght = len(seq[0: ])

#variáveis validadas no formato certo
dna = str(seq)
pri = int(n1)
seg = int(n2)
ter = int(n3)
qua = int(n4)
seq1 = dna[pri -1 : seg ]
seq2 = dna[ter  : qua ]

#conferir se digitou o tipo certo de dados indicando qual foi o possível erro
def checkdados():
        global dna, pri, seg, ter, qua
        if (seq.isalpha() == True) :
                print("Sequência Ok")
                if (n1.isdigit() ==True) and int(n1) < lenght:
                        print("número 1 ok")
                        if (n2.isdigit() ==True) and int(n2) < lenght:
                                print("número 2 ok")
                                if (n3.isdigit() ==True) and int(n3) < lenght:
                                        print("número 3 ok")
                                        if (n4.isdigit() ==True) and int(n4) < lenght:
                                                print("número 4 ok")
                                                return True #retorna True se todos os dados estão corretos
        else:
                return False #retorna falso caso contrário


#confere se a sequência Começa com ATG e termina com TAG, TAA ou TGA, indicando qual delas pode estar errada
def checkseq():
        if seq1.startswith("ATG") and seq2.endswith("TAG" or "TAA" or "TGA"):
                print("Sequência começa com ATG e termina com códons de parada")
                return True
        elif seq1.startswith("ATG") == False:
                print("A sequência 1 NÃO começa com ATG")
                return False
        elif seq2.endswith("TAG" or "TAA" or "TGA") == False:
                print("A sequência 2 NÃO termina com Códon de parada")
                return False 


  
#se os dados estão corretos, e a sequência começa e termina com os codons certos, concatena as duas ou imprime uma mensagem de erro
if checkdados() == True:
        print("As sequências são: ", seq1, " e ", seq2)
        if checkseq() == True: 
                print(seq1 + seq2, "É a sequência final")
        else:
                print("Não foi possível concatenar")
        













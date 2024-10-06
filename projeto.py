n=1
cont=1
l=[]
d={}

while n!=0 and cont<=50:                                                                  
    print("Para inserir um dado, aperte 1")
    print("Para imprimir todos os dados, aperte 2")
    print("Para imprimir trecho de dados, aperte 3")
    print("Para buscar um dado, aperte 4")
    print("Para finalizar o código, aperte 0")
    n=int(input("insira o codigo do menu "))
    cont+=1
    buscador=0

    if n==1:
        print("voce pode inserir o nome de um ator/atriz de novela, o ano de nascimento e qual a altura")
        d["nome"]=str(input("qual o nome do ator/atriz de novela? "))
        d["ano"]=int(input("qual o ano de nascimento do ator/atriz de novela? "))
        d["altura"]=float(input("qual a altura do ator/atriz de novela? (pode ser float)"))
        l.append(d.copy())

    if n==2:
        for i in range(len(l)):
            print(l[i]["nome"], l[i]["ano"], l[i]["altura"])

    if n==3:
        print("**PS: a posicao na lista começa com 1, e nao com 0. Entao o primeiro item selecionado considere na posicao numero 1**")
        c=int(input("o trecho que voce quer imprimir comeca em qual posicao? "))
        f=int(input("o trecho que voce quer imprimir termina em qual posicao? "))
        print(l[c-1:f])
        
    if n==4:
        b=str(input("digite nome se voce quiser pesquisar pelo nome, digite ano se voce quiser pesquisar pelo ano e digite altura se quiser buscar pela altura: "))
        print("**PS: a posicao na lista começa com 1, e nao com 0. Entao o primeiro item selecionado considere na posicao numero 1**")
        if b=="nome":
            p=str(input("qual o nome do ator/atriz de novela? "))
            for j in range(len(l)):
                if l[j]["nome"]==p:
                    print(f"o ator/atriz {p} está na {j+1} posicao")
                    buscador+=1
            

        if b=="ano":                                                                 
            p=int(input("qual o ano de nascimento? "))
            for j in range(len(l)):
                if l[j]["ano"]==p:
                    print(f"o ator/atriz que nasceu em {p} está na {j+1} posicao")
                    buscador+=1
            

        if b=="altura":
            p=float(input("qual a altura do ator/atriz de novela? "))
            for j in range(len(l)):
                if l[j]["altura"]==p:
                    print(f"o ator/atriz com altura {p} está na {j+1} posicao")
                    buscador+=1

        if buscador==0:
            print("Elemento não encontrada")





# p=input("qual o nome da fruta? ")
# for j in range(len(l)):
#     if l[j]["quantidade"]==p:
#         print(f"a fruta com quantidade {p} está na {j} posicao")

print("acabou o codigo")
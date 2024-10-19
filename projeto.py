


                                                    #se na primeira execução no Visual Studio Code aparecer um erro no começo, ignore. Na parte inferior erro o código vai estar funcionando ou execute o código outra vez. Obrigado



confirmar=0
n=1
cont=1
l=[{"nome": "Caio Castro", "ano": 1989, "altura": 1.75},    #lista já ta com 5 itens para ajudar o usuário a usar rapidamente o código
    {"nome": "Antonio Fagundes", "ano": 1949, "altura": 1.81}, 
    {"nome": "Adriana Esteves", "ano": 1969, "altura": 1.63}, 
    {"nome": "Fernanda Montenegro", "ano": 1929, "altura": 1.64}, 
    {"nome": "Giovanna Antonelli", "ano": 1976, "altura": 1.68}]
d={}


print("\n====================ATORES/ATRIZES DE NOVELA | INSERIR, IMPRIMIR, BUSCAR====================\n")   #começo do menu


while n!=0 and cont<=46:
    
    print("==== MENU ====\n")
    print("PARA INSERIR UM NOVO DADO, APERTE -> 1 <-\n")
    print("PARA IMPRIMIR TODA A LISTA, APERTE -> 2 <-\n")
    print("PARA IMPRIMIR SOMENTE UM TRECHO DA LISTA, APERTE -> 3 <-\n")
    print("PARA BUSCAR UM ATOR/ATRIZ, APERTE -> 4 <-\n")
    print("PARA SABER QUANTOS ITENS JÁ TEM NA LISTA, APERTE -> 5 <-\n")
    print("PARA SAIR, APERTE -> 0 <-\n")
    n=int(input("Por favor, insira o número desejado, tendo em base o Menu acima: "))   #aqui irá inserir o número do menu que o usuário quer

    if confirmar==0:    #na primeira vez que o código foi executado (confirmar vai estar em 0), vai avisar que o código já tem 5 atores/atrizes para rápida utilização
        print("\nPor ajudar a rapidez de execução do código, já foram adicionados 5 atores/atrizes automáticamente, você poderá adicionar mais, se desejar.\n")

    print("\n========================================\n")   #final do menu
    buscador=0
    confirmar+=1

    if n==1 and cont<46:
        print("INSERIR ATOR/ATRIZ DE NOVELA\n")
        d["nome"]=str(input("Qual o Nome do ator/atriz de novela? -> "))    #nessa linha e nas 2 seguintes o usuário vai colocar os dados dos dicionários
        d["ano"]=int(input("\nQual o Ano de Nascimento do ator/atriz de novela? -> "))
        d["altura"]=float(input("\nQual a Altura do ator/atriz de novela? (pode ser número float) -> "))
        l.append(d.copy())  #o dicionário vai ser colocado no final da lista
        cont+=1 #o contador vai ser adicionado o valor 1, o código acaba quando chegar ao 46, então a lista vai ter no máximo 50 posições já que já tem 5 posições pré completadas por padrão
    elif n==1 and cont>=46:
        print("Já chegou no limite máximo de 50 posições na lista\n")   #aqui avisando se a lista já está cheia

    if n==2:
        print("=====A SEGUIR TODA A LISTA ATUAL=====\n")
        for i in range(len(l)): #aqui vai passar por cada posição da lista
            print(f"\nNome: {l[i]['nome']}, Ano de Nascimento: {l[i]['ano']}, Altura: {l[i]['altura']}\n") #aqui vai imprimir cada dicionário

    if n==3:
        print("\n**PS: A lista começa com a posição 1, e não com 0**\n")
        c=int(input("\nO trecho que você quer imprimir Começa em qual posição? -> "))
        f=int(input("\nO trecho que você quer imprimir Termina em qual posição? -> "))
        for i in range(f-c+1):  #vai ser feito o FOR a quantidade de vezes entre o final e o inicial indicado pelo usuário, ou seja, se vai do 2 ao 4 então vai ser feito 3 vezes (2, 3 e 4)
            print(f"\nNome: {l[c+i-1]['nome']}, Ano de Nascimento: {l[c+i-1]['ano']} e Altura: {l[c+i-1]['altura']}\n") #vai ser printado os dicionários um por um, desde o começo, adicionando valor 1 a cada vez que o FOR IN foi rodado, dessa forma para passar para o próximo dicionário


                
    if n==4:
        print("=====BUSCAR ATOR/ATRIZ DE NOVELA=====\n")    #pequeno menu para ajudar o usuário a como fazer a busca
        print("PARA BUSCAR PELO NOME DO ATOR/ATRIZ, DIGITE -> nome <-\n")
        print("PARA BUSCAR PELO ANO DE NASCIMENTO DO ATOR/ATRIZ, DIGITE -> ano <-\n")
        print("PARA BUSCAR PELA ALTURA DO ATOR/ATRIZ, DIGITE -> altura <-\n")
        b=str(input())  #aqui vai ser inserido se o usuário quer buscar pelo nome, ano ou altura. Essa variável vai servir para usar nos IF a seguir
        print("\n**PS: A lista começa com a posição 1, e não com 0**\n")
        if b=="nome":   #esse IF funciona se o usuário quiser buscar pelo nome do ator/atriz
            p=str(input("Qual o nome do ator/atriz de novela? -> "))    #aqui vai colocar o nome da pessoa
            for j in range(len(l)): #agora vai colocar cada posição da lista, um por um
                if l[j]["nome"]==p: #nessa linha, vai ver se o que o usuário inseriu anteriormente para fazer a busca, for igual ao valor que está sendo analisado, no caso somente os nomes
                    print(f"\no ator/atriz {p} está na {j+1} posição")  #aqui vai ser imprimido o nome do ator, que foi inserido pelo usuário, e a posição
                    buscador+=1 #aqui vai ser adicionado valor 1 a variável buscador, serve para saber se o elemento foi encontrado. Se não foi encontrado então vai ser 0 e vai cair no IF destinado a caso isso aconteça
                    

        if b=="ano":    #mesma lógica da busca por nomes
            p=int(input("Qual o ano de nascimento? -> "))
            for j in range(len(l)):
                if l[j]["ano"]==p:
                    print(f"\no ator/atriz que nasceu em {p} está na {j+1} posição")
                    buscador+=1
                    

        if b=="altura": #mesma lógica da busca por nomes e anos de nascimentos
            p=float(input("Qual a altura do ator/atriz de novela? -> "))
            for j in range(len(l)):
                if l[j]["altura"]==p:
                    print(f"\no ator/atriz que possui a altura {p} está na {j+1} posição")
                    buscador+=1

        if buscador==0: #se o buscador foi 0 significa que não caiu em nenhum IF anteriores, então não foi encontrado o item desejado
            print("\nElemento não encontrado")    #aviso falando que o valor não foi encontrado

    if n==5:
        print(f"A lista atualmente tem {len(l)} itens.\n")
            
    if confirmar>=1 and n!=0: #esse IF serve para saber se o usuário quer continuar, só vai ser mostrado a partir da segunda alimentação do código por causa do confirmar>1 (o confirmar só aumenta depois da primeria execução do código)
        continuar=str(input("\nDESEJA CONTINUAR? SE SIM, DIGITE -> y <-; SE NÃO QUISER, DIGITE QUALQUER TECLA "))   #esse mini menu serve também por causa que o menu inicial é muito grande, então as vezes o resultado ficava muito para cima do terminal e poderia fazer com que o usuário achasse que o resultado não tinha sido mostrado
        if continuar=="y":  #nesse caso, só vai continuar executando o código se for digitado y, se for digitado qualquer outra coisa vai ser a mesma coisa que digitar 0 no menu inicial
            print()
        else:
            print()
            n=0


print("=== O código foi finalizado ===\n")  #aviso final que fala que o código foi finalizado por completo
print("Obrigado pela utilização!\n")  #agradecendo ao usuário por ter usado o código até o final
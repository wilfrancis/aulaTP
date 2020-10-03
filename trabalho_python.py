#-------------------------- Tiago Moraes =>23541920 ----------------------------
#-------------------------- William Francisco =>23541865------------------------
categorias = ["Informática","Móveis"]
margemLucro = [1.50,1.60]

produtosInformatica = []
produtosMoveis = []

precosInformatica = []
precosMoveis = []

carrinho = []
precoCarrinho = []
codigoProduto = []

cond_cadastro = True

while cond_cadastro:

    print("Qual a categoria?")
    print(" 1 - Informática")
    print(" 2 - Móveis")
    opcao1 = int(input("Opção: "))

    if opcao1 == 1:
       produtosInformatica.append (input("Digite o nome do produto da categoria Informática: "))
       precosInformatica.append (float(input("Digite o valor: ")))

    else:
        opcao1 == 2
        produtosMoveis.append (input("Digite o nome do produto da categoria Móveis: "))
        precosMoveis.append (float(input("Digite o valor: ")))
    
    cond_cadastro = input('Deseja continuar o cadastro (s/n)? ') == 's'

print("Cadastro finalizado com sucesso.")
print("------------------------------------------")
print("Recalculando preços com margem de lucro...")
import locale

a = 0
for i in precosInformatica:
    precoVendaInfo = i * margemLucro[0]
    precosInformatica.pop(a)
    precosInformatica.insert(a, precoVendaInfo)
    print("[ Categoria",categorias[0],']', produtosInformatica[a], "- valor recalculado R$:",locale.format("%1.2f",precoVendaInfo),)
    a = a + 1
    
b = 0
for i in precosMoveis:
    precoVendaMoveis = i * margemLucro[1]
    precosMoveis.pop(b)
    precosMoveis.insert(b, precoVendaMoveis)
    print("[ Categoria",categorias[1],']', produtosMoveis[b], "- valor recalculado R$:",locale.format("%1.2f",precoVendaMoveis),)
    b = b + 1

print("------------------------------------------")
print("Iniciando vendas...")
cond_venda = True

while cond_venda:

    valorMaximo = float(input("Qual valor máximo de pesquisa em reais? "))
    print("Qual a categoria da pesquisa?")
    print(" 1 - Informática")
    print(" 2 - Móveis")
    opcao2 = int(input("Opção: "))

    if opcao2 == 1:
        for i in range(len(precosInformatica)):
            if precosInformatica[i] <= valorMaximo:
                print("[",i,"]", produtosInformatica[i], "- valor:",locale.format("%1.2f",precosInformatica[i]),)
        codigoProduto = int(input("Digite o código do produto para adicionar no carrinho: "))
        carrinho.append(produtosInformatica[codigoProduto])
        precoCarrinho.append(precosInformatica[codigoProduto])

    elif opcao2 == 2:
        for i in range(len(precosMoveis)):
            if precosMoveis[i] <= valorMaximo:
                print("[",i,"]", produtosMoveis[i], " - valor: ",locale.format("%1.2f",precosMoveis[i]),)
        codigoProduto = int(input("Digite o código do produto para adicionar no carrinho: " ))
        carrinho.append(produtosMoveis[i])
        precoCarrinho.append(precosMoveis[i])

    cond_venda = input('Deseja continuar comprando (s/n)? ') == 's'

print("------------------------------------------")
print("Listando produtos no carrinho:")
for i in range(len(carrinho)):
    print("[",i,"]",carrinho[i], "- valor R$:",locale.format("%1.2f",precoCarrinho[i]),)
              
print("Remover não funcionado, só o total.")
remover = input("Para remover um produto digite o código, caso contrário digite FIM: ")

while remover != "FIM" and remover != "fim":

    #tentativa de remover:
    #for i in range(len(carrinho)):
        #if remover != str(i):
            #carrinho.remove(carrinho[i])
            #print("Produto ",carrinho[i]," removido")
    #for i in range(len(precoCarrinho)):
        #if remover != int(i):
            #precoCarrinho.remove(precoCarrinho[i])            
    #for i in range(int(codigoProduto)):
        #if remover != str(i):
            #codigoProduto.remove(codigoProduto[i])
            
    remover = input("Para remover um produto digite o código, caso contrário digite FIM: ")

precoTotal = 0              
for i in range(len(precoCarrinho)):
    precoTotal = precoTotal + precoCarrinho[i]
print("Total da compra: ",locale.format("%1.2f",precoTotal),)
            


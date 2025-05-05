from functools import reduce
import time
import logging
from datetime import time, timedelta
import os
import csv
import re
import datetime

def functionArgsAndKWargs(*args, **kwargs):
    print('args:', args)
    print('kwargs:', kwargs)
functionArgsAndKWargs(1,2,3, "willian",nome='Will', idade=20) 

def soma_total(*args):
 resultado = sum(args)
 print(resultado)
soma_total(1,2,3,4,5) 

def mostrar_dados(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")
mostrar_dados(nome="Will", linguagem="Python", nivel="avançado")        

def processar_dados(*args):
    quantidade = len(args)
    valor_max = max(args)
    print('Quantidade de argumentos', quantidade)
    print('Maior Valor', valor_max)
processar_dados(20,50,10)

def lambdas():
    soma = lambda x, y : x + y
    print('Valor da soma é:' , soma(2,5))
lambdas()

def map_lambdas():
    numeros = [1,2,3,4]
    pares = list(map(lambda x : x * 4, numeros))
    print("Numeros * 4",pares)
map_lambdas()

def filter_num():
 num = [1,2,3,4,5,6]
 resultado = list(filter(lambda x : x % 2 == 0, num))
 print("numeros pares dentro da lista", resultado)
filter_num()  

def reduce_lambdas():
    lista = [1,2,3,4,5,6,7,8]
    produtos = reduce(lambda x, y : x * y, lista)
reduce_lambdas()    
    
def desafio():
    lista = [1,2,3,4,5,6,7,8,9,10,11,12,14]
    dobrar = list(map(lambda x : x * 2, lista))
    filtar_valor = list(filter(lambda x : x > 10, dobrar))
    top_valores = reduce(lambda x, y : x + y, filtar_valor)

desafio()    

def lista():
    lista = [1,2,3,4,5,6]
    lista.append(22)
    lista.remove(1)
    lista.sort()
    print(lista)
lista()    

def dicionarios():
    dicionario = {'nome': 'willian', 'idade': 20}
    dicionario['cidade'] = 'São Paulo' # Adicionar item
    del dicionario['idade']
    print(dicionario)
dicionarios()    

def meu_set():
    set_list = {1,2,3,4,5,6,7}
    print(set_list)
    set_list.add(2)
    print(set_list)
    set_list.remove(5)
    print(set_list)
    set_list = set_list.union({7,8})
    print(set_list)
meu_set()    

def iterator():
    list = [1,2,3,4]
    iterator = iter(list)
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
iterator()    

def quadrados(n):
    for i in range(n):
        yield i * i

gen = quadrados(5)
for num in gen:
    print(num) 
quadrados(5)    

def quadrado_perfect():
    quadrados = [x * x for x in range(5)]
    print(quadrados)
quadrado_perfect()    

def timer(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f'função executadaa em {end_time - start_time} segundos')
    return wrapper
    
@timer
def funcao():
    
    time.sleep(2)
 

def facil (*args, **kwargs):
    resultado = sum(args)
    print('Valor total da conta', resultado)
    print('kwargs:' , kwargs)
facil(1,2,2,3,44,52, nome = "Willian", idade = 20)    

def multiplo_de_tres():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    resultado = list(filter(lambda x : x % 3 == 0, numeros))
    print('Resultado é:', resultado)
multiplo_de_tres()    

def calcular_fatorial():
    lista = [1,2,3,4,5]
    resultado = reduce(lambda x, y : x * y, lista)
    return 'resultado', resultado
calcular_fatorial()    

def listar_produtos():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] # Lista
    resultado = list(filter(lambda x : x % 2 != 0, lista)) # Números impares
    dobrar_valor = list(map(lambda x : x * 2, resultado))
    fatorial = reduce(lambda x, y : x * y, resultado)
    print('--------LAMBDA--------')
    print('Números Impares', resultado)
    print('Dobro dos números', dobrar_valor)
    logging.info('Fatorial', fatorial)
listar_produtos()   

def carrinho_de_compras(*args, **kwargs):
    quantidade_carrinho = sum(args)
    for chave, valor in kwargs.items():
      print(chave, valor)
    print('Quantidade no carrinho', quantidade_carrinho)
carrinho_de_compras(10, 20, 30, fruta=0.1, bebida=0.2)

def carrinho_de_compras(*args, **kwargs):
    # Total bruto: soma de todos os preços
    total_bruto = sum(args)
    
    # Dicionário para armazenar preços por categoria
    precos_por_categoria = {categoria: [] for categoria in kwargs.keys()}
    
    # Distribuindo preços nas categorias
    for i, preco in enumerate(args):
        categoria = list(kwargs.keys())[i % len(kwargs)]  # Distribui os preços nas categorias
        precos_por_categoria[categoria].append(preco)
    
    # Calculando total com descontos por categoria
    total_com_desconto = 0
    for categoria, precos in precos_por_categoria.items():
        subtotal = sum(precos)
        desconto = kwargs[categoria]
        total_com_desconto += subtotal * (1 - desconto)  # Aplica o desconto

    # Exibindo os resultados
    print(f"Total bruto: R$ {total_bruto}")
    print(f"Total com descontos: R$ {total_com_desconto}")
carrinho_de_compras(10, 20, 30, fruta=0.1, bebida=0.2)

def filtar_e_dobrar():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    pares = list(filter(lambda x : x % 2 == 0, numeros))
    dobrar = list(map(lambda x : x * 2, pares))
    print('Números pares', pares)
    print('Dobrando os pares', dobrar)
filtar_e_dobrar()    

def soma_dos_quadrados():
    numeros = [1, 2, 3, 4, 5]
    quadrados = list(map(lambda x: x ** 2, numeros))
    resultado = reduce(lambda x, y: x + y, quadrados)
    print('Soma dos quadrados:', resultado)
soma_dos_quadrados()

def media_nota():
    notas = [35, 78, 90, 40, 67, 45, 89, 100]
    media = list(map(lambda x : x > 50, notas))
    total = list(map(lambda y : y / 6, notas))
    print(total)

media_nota()    

def dobrar():
    lista = [1,2,3,4]
    resultado = len(lista)
    print('Quantidade de números', resultado)
    dobrar_num = list(map(lambda x : x * 2, lista))
    print(dobrar_num)
dobrar()    

def elevar():
    num = [2,4,6,8]
    lista = list(filter(lambda x : x > 5, num))
    total = list(map(lambda y : y ** 2, lista))
    print('Números esperado:', total)
elevar()    

def media():
    nota = [45, 67, 89, 90, 32, 76]
    aprovados= list(filter(lambda x : x > 60, nota))
    media_aprovados = sum(aprovados) / len(aprovados)
    print(media_aprovados)
media()    

def multiplos():
    lista = [1,2,3,4,5,6,7,8,9,10]
    filtrar = list(filter(lambda x : x % 3 == 0, lista))
    somar_fatorial = reduce(lambda x, y : x + y, filtrar)
    print('Múltiplos de três', filtrar)
    print(f'Soma de: {filtrar} é = {somar_fatorial}')
multiplos()     

def relatorio_de_faturamento():
    produtosDicionario = [
        {"nome": "Camisa", "preco": 50, "quantidade": 4},
        {"nome": "Calça", "preco": 120, "quantidade": 8},
        {"nome": "Tênis", "preco": 250, "quantidade": 2},
        {"nome": "Boné", "preco": 30, "quantidade": 10},
    ]
    filtrar_produto = list(filter(lambda produto: produto['quantidade'] > 1, produtosDicionario))
    mapear = list(map(lambda x: {"nome": x["nome"], "total": x["preco"] * x["quantidade"]}, filtrar_produto))
    faturamento_total = reduce(lambda valor, total: valor + total["total"], mapear, 0)
    
    print('Relatório de Faturamento')
    for item in mapear:
        print(f'{item["nome"]}: R$ {item["total"]:.2f}')
        
    print(f"\nFaturamento total: R$ {faturamento_total:.2f}")

relatorio_de_faturamento()

def relatorio_lucro():
    produtos = [
        {"nome": "Camisa", "custo": 25, "venda": 55, "quantidade": 10},
        {"nome": "Calça", "custo": 70, "venda": 120, "quantidade": 5},
        {"nome": "Tênis", "custo": 180, "venda": 250, "quantidade": 3},
        {"nome": "Boné", "custo": 15, "venda": 30, "quantidade": 20},
    ]
    
    # 1. Filtrando produtos com lucro por unidade > 20
    filtrar_produto = list(filter(lambda produto: (produto['venda'] - produto['custo']) > 20, produtos))
    
    # 2. Calculando lucro total por produto
    mapear = list(map(lambda prod: {"nome": prod["nome"], "total": (prod["venda"] - prod["custo"]) * prod["quantidade"]}, filtrar_produto))
    
    # 3. Calculando lucro total geral
    total = reduce(lambda valor, total: valor + total['total'], mapear, 0)
    
    # 4. Imprimindo o relatório
    print('Relatório de Lucros:')
    for item in mapear:
        print(f'{item["nome"]}: R${item["total"]:.2f}')
    
    print(f'\nFaturamento total: R${total:.2f}')

# Chamada da função
relatorio_lucro()

def relatorio_lucro_categoria():

    produtos = [
        {"nome": "Camisa", "custo": 25, "venda": 55, "quantidade": 10, "categoria": "Roupas"},
        {"nome": "Calça", "custo": 70, "venda": 120, "quantidade": 5, "categoria": "Roupas"},
        {"nome": "Tênis", "custo": 180, "venda": 250, "quantidade": 3, "categoria": "Calçados"},
        {"nome": "Boné", "custo": 15, "venda": 30, "quantidade": 20, "categoria": "Acessórios"},
    ]

    # Corrigindo o map
    lucros = list(map(lambda prod: {
        "categoria": prod["categoria"],
        "lucro": (prod["venda"] - prod["custo"]) * prod["quantidade"]
    }, produtos))

    # Corrigindo o loop e variáveis
    lucro_por_categoria = {}
    for item in lucros:
        cat = item["categoria"]
        lucro = item["lucro"]
        lucro_por_categoria[cat] = lucro_por_categoria.get(cat, 0) + lucro

    print("Relatório de Lucro por Categoria")
    for categoria, lucro in lucro_por_categoria.items():
        print(f"{categoria}: R${lucro:.2f}")
        
    with open("lucro_por_categoria.csv", mode="w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["Categoria", "Lucro (R$)"])
        for categoria, lucro in lucro_por_categoria.items():
            escritor.writerow([categoria, f"{lucro:.2f}"])

    print("\nArquivo 'lucro_por_categoria.csv' gerado com sucesso")
relatorio_lucro_categoria()

def numeros_negativos():
    numeros = [-5, 3, -1, 7, -9, 0]
    negativos = list(filter(lambda x : x < 0, numeros))
    print(negativos)
    # Saída esperada: [-5, -1, -9]
numeros_negativos()    

def nomes_com_menos_de_cinco_letras():
    nomes = ['carro', 'sol', 'avião', 'lua']
    cinco_a_menos = list(filter(lambda five : len(five) < 5, nomes))
    print(cinco_a_menos)
nomes_com_menos_de_cinco_letras()

def pares():
    entrada = [1, 2, 3, 4, 5, 6]
    resultado = list(filter(lambda pares : pares % 2 == 0, entrada))
    dobrar = list(map(lambda x : x * 2, resultado))
    print(dobrar)
pares()    

def fatorial_dos_impares():
    entrada = [1, 2, 3, 4, 5]
    impares = list(filter(lambda impar : impar % 2 != 0, entrada))
    fatorial = reduce(lambda x, y : x * y, impares)
    print(f'Os valores impares são: {impares} é o fatorial é:{fatorial}')
fatorial_dos_impares()    

def aumentar_numeros():
    numeros = [3, 8, 12, 5, 10]
    novo = list(filter(lambda x : x < 10, numeros))
    mapear = list(map(lambda y : y + 5, novo))
    print('Antiga lista', numeros)
    print('Nova Lista', mapear)
aumentar_numeros()    

def lucro_acima():
# Dicionario Produtos
    produtos = [
    {"nome": "Camisa", "custo": 30, "venda": 90},  # lucro = 60
    {"nome": "Tênis", "custo": 120, "venda": 180}, # lucro = 60
    {"nome": "Boné", "custo": 15, "venda": 40},     # lucro = 25
]
    
    lucrativo = list(filter(lambda prod : (prod['venda'] - prod['custo']) > 50, produtos))
    print('\n')
    for produto in lucrativo:
        lucro = produto['venda'] - produto['custo']
        print(f"{produto['nome']} - Lucro R${lucro}")
lucro_acima()

def lucro_acima_com_map():
    # Dicionário de Produtos
    produtos = [
        {"nome": "Camisa", "custo": 30, "venda": 90},  # lucro = 60
        {"nome": "Tênis", "custo": 120, "venda": 180}, # lucro = 60
        {"nome": "Boné", "custo": 15, "venda": 40},    # lucro = 25
    ]
    
    lucro = list(filter(lambda valor: (valor['venda'] - valor['custo']) > 50, produtos))
    lucro_produtos = list(map(lambda prod: f"{prod['nome']} - Lucro R${prod['venda'] - prod['custo']}", lucro))
    
    for item in lucro_produtos:
        print(item)
lucro_acima_com_map()

def dobrar_numeros():
    numeros = [1, 2, 3, 4, 5]
    lista = list(map(lambda x : x * 2, numeros))
    print(lista)
dobrar_numeros()

def celsius_para_fahrenheit():
    celsius = [0, 10, 20, 30]
    conversao = list(map(lambda x : (x * 1.8 ) + 32, celsius))
    print(f'Fahrenheit {conversao}')
celsius_para_fahrenheit()

def quadrado():
    numeros = [2, 3, 4, 5]
    total = list(map(lambda y : y ** 2, numeros))
    print(total)
quadrado()    

def nomes():
    nomes_completos = ["Ana Silva", "João Pedro", "Maria Souza"]
    listar = list(map(lambda x : x.split()[0], nomes_completos))
    print(listar)
nomes()    

def formatar_texto():
    produtos = [
    {"nome": "Camisa", "preco": 50},
    {"nome": "Calça", "preco": 100},
    {"nome": "Tênis", "preco": 200},
    ]
    
    listar = list(map(lambda produto : f"O produto {produto['nome']} custa R${produto['preco']}", produtos))
    
    for nova_lista in listar:
        print(nova_lista)
formatar_texto()         

def teste():
  lista = [1,2,3,4,5]
  status = list(filter(lambda x : x % 2 == 0, lista))
  print(status)
teste()

def datetime_teste():
    agora = datetime.datetime.now()
    agora_str = agora.strftime("%d/%m/%Y") 
    datas = re.findall(r"\d{2}/\d{2}/\d{4}", agora_str)
    print(agora)
    print(datas)
datetime_teste()

def system_404():
    system = os.environ
    print(system['HOME'])
    print(os.getcwd()) # Localizar a pasta onde você tá
    
system_404()    

def horario():
    from datetime import datetime
    
    agora = datetime.now()
    print("Horário atual:", agora.strftime("%H:%M:%S"))

horario()    

def atrasar():
    import time
    print('Esperando')
 #   time.sleep(3)
    print('Pronto')
atrasar()

def mostrar_data():
    from datetime import datetime
    
    hoje = datetime.today()
    print('Data de hoje', hoje.strftime("%d/%m/%Y"))
mostrar_data()

def natal():
    from datetime import datetime
    
    hoje = datetime.today()
    natal = datetime(hoje.year,12, 25)
    faltam = (natal - hoje).days
    print(f'Faltam {faltam} dias para o natal')
natal()

def horario_antes_ou_depois():
    from datetime import datetime
    
    agora = datetime.now()
    if agora.hour < 12:
        print('Antes do meio dia')
    else:
        print('Depois do meio dia')
        
horario_antes_ou_depois()

def cronometro():
    import time
    
    print('Contagem regressiva')
    for i in range(5,0, -1):
        print(i)
       # time.sleep(1)
    print('Tempo acabou')    
cronometro()

def cronometro_simples():
    for i in range(1, 11, +1):
        print(i)
        
cronometro_simples()

def cronometro_usuario():
    import time
    cronometro: int = int(input('Digite um valor INT'))
    for i in range(0,cronometro, +1):
        time.sleep(1)
        print(i)
cronometro_usuario()

def calcular_min():
    import time
    
    inicio = time.time()
    total = 0
    
    for i in range(1, 1_000_001):
        total += 1
        
    fim = time.time()
    print(f"Resultado da soma: {total}")
    print(f"Tempo de execução: {fim - inicio:.5f} segundos")
calcular_min()

def calcular_idade():
    from datetime import datetime
    from calendar import monthrange

    nascimento_str = input('Digite sua data de nascimento (ddmmaaaa): ')
    nascimento = datetime.strptime(nascimento_str, "%d%m%Y")
    hoje = datetime.today()

    # Total de dias vividos
    dias_totais = (hoje - nascimento).days
    anos_aproximado = dias_totais / 365

    # Cálculo de idade exata
    anos = hoje.year - nascimento.year
    meses = hoje.month - nascimento.month
    dias = hoje.day - nascimento.day

    if dias < 0:
        meses -= 1
        # Corrigindo mês anterior se mês atual for janeiro
        mes_anterior = hoje.month - 1 if hoje.month > 1 else 12
        ano_para_mes = hoje.year if hoje.month > 1 else hoje.year - 1
        dias += monthrange(ano_para_mes, mes_anterior)[1]

    if meses < 0:
        anos -= 1
        meses += 12

    print(f'Você tem {anos} anos, {meses} meses e {dias} dias.')
    print(f'Total de dias vividos: {dias_totais}')
    print(f'Idade aproximada em anos (dividindo dias por 365): {anos_aproximado:.0f} anos')

calcular_idade()


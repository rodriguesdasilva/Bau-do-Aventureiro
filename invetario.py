import json
import os
from time import sleep


ARQUIVO = 'inventario.json'
loja = []

def menu_principal():
    print(f'''
    .___________________________________________.
    | ::::::::::  BAÚ DO AVENTUREIRO :::::::::::|
    |___________________________________________|
    |                                           |
    |  [1] => Adicionar Novo Tesouro.           |
    |  [2] => Consultar Inventário.             |
    |  [3] => Filtrar por Categoria.            |
    |  [4] => Avaliar Fortuna Total.            |
    |  [5] => Descartar Item.                   |
    |                                           |
    |  [0] => Fechar Mochila.                   |
    |___________________________________________|
          
    ''')
    
def carregar_inventario():
    if not os.path.exists(ARQUIVO):
        return []
    try:   
        with open(ARQUIVO, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print('Erro ao carregar o arquivo')
        return []

def salvar_item(loja):
    try:
        with open(ARQUIVO, 'w', encoding='utf-8') as f:
            json.dump(loja, f, indent=4, ensure_ascii=False)
    except IOError:
        print("Erro ao salvar os dados.")

def cadastrar_item(loja):
    print('\n==============| Cadastrar Item |=================')
    try:
        categoria = input('Nome da categoria: ').lower().strip()
        nome = input('Nome do item: ').lower().strip()
        preco = float(input('Preço em Ouro: '))
        novo_item = {
            'categoria': categoria,
            'nome': nome,
            'preco': preco,
        }

        loja.append(novo_item)
        salvar_item(loja)
        print('\n' + '='*47)
        print(f'O item [{nome}] foi cadastrado com sucesso ✅!')
        print('='*47)
    except ValueError:
        print("Erro: O preço deve ser um número.")

def listar_item(loja):
    if not loja:
        print('\nNenhum item cadastrado!')
        return
        
    print('\n|=================================== Inventário ======================================|')
    for i, item in enumerate(loja):
        print(f'#{i+1} => Categoria: [{item["categoria"]}] | Nome: [{item["nome"]}] | Preço: {item["preco"]:.2f}g')
    print('='*86)

def buscar_categoria(loja):
    if not loja:
        print('Inventário Vazio!')
        return
    
    buscar = input('Digite o nome da categoria: ').lower().strip()
    
    print(f'\n--- Resultados para "{buscar}" ---')
    print('='*40)
    for i, item in enumerate(loja):
        if item['categoria'] == buscar:
            print(f'#{i+1} => {item["nome"]} - Preço: {item["preco"]}g')
        else:
            print('Nenhum item encontrado nesta categoria.')
    print('='*40)

def calcular_valor(loja):
    if not loja:
        print('Nenhum item no inventário para calcular valor ❌.')
        return
    
    valor_total = 0
    
    for item in loja:
        valor_total += item['preco']

    print('-'*55)   
    print(f'Patrimônio total do jogador: {valor_total:,.2f} moedas de ouro.')
    print('-'*55)

def remover_item(loja):
    if not loja:
        print('Nenhum item para remover.')
        return

    listar_item(loja)
    try:
        index = int(input('Digite o número (#) do item que deseja excluir: ')) - 1
        if 0 <= index < len(loja):
            removido = loja.pop(index)
            salvar_item(loja)
            print('-'*40)
            print(f"O item '{removido['nome']}' foi removido com sucesso ✅.")
            print('-'*40)
        else:
            print('Número Inválido.')
    except ValueError:
        print('Por favor, digite um número válido ❌.')

dados = carregar_inventario()

while True:

    menu_principal()

    op = input('Digite sua opção: ')

    if op == '1':
        cadastrar_item(dados)
    elif op == '2':
        listar_item(dados)
    elif op == '3':
        buscar_categoria(dados)
    elif op == '4':
        calcular_valor(dados)
    elif op == '5':
        remover_item(dados)
    elif op == '0':
        sleep(0.)
        print('Saindo do Sistema...')
        sleep(0.5)
        print('Saindo do Sistema..')
        sleep(0.5)
        print('Saindo do Sistema.')
        sleep(0.5)
        print('Saindo do Sistema...')
        sleep(2)
        print('Até mais!')
        break
    else:
        print('Opção inválida, tente novamente.')
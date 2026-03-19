Baú do Aventureiro: Sistema de Inventário em Python

O Baú do Aventureiro é uma aplicação de linha de comando (CLI) temática voltada para jogadores de RPG ou entusiastas que desejam gerenciar itens de um inventário. O sistema permite o cadastro de tesouros, filtragem por categorias e o cálculo automático da fortuna total acumulada, salvando todos os dados localmente para que não sejam perdidos ao fechar o programa.

Funcionalidades
Adicionar Novo Tesouro: Registra o nome, a categoria e o preço (em ouro) de um item.

Consultar Inventário: Lista todos os itens guardados com seus respectivos índices.

Filtrar por Categoria: Busca rápida para visualizar apenas itens de uma classe específica (ex: "armas" ou "poções").

Avaliar Fortuna Total: Soma o valor de todos os itens e exibe o patrimônio total do jogador.

Descartar Item: Remove um item específico do inventário através do seu número de identificação.

Persistência de Dados: Utiliza um arquivo .json para salvar e carregar as informações automaticamente.

Passo a Passo do Funcionamento
O código foi estruturado de forma modular. Abaixo, explico a lógica por trás de cada etapa:

1. Inicialização e Persistência (JSON)
Ao iniciar, o sistema executa a função carregar_inventario(). Ela verifica se o arquivo inventario.json existe. Se sim, carrega os dados; se não, cria uma lista vazia. Isso garante que seus itens "sobrevam" ao fechamento do console.

2. O Fluxo de Controle (Loop While)
O programa roda dentro de um loop infinito (while True) que só é interrompido quando o usuário escolhe a opção 0. A cada ciclo, o menu_principal() é exibido e a entrada do usuário direciona para a função correspondente.

3. Cadastro e Tratamento de Erros
Na função cadastrar_item(), utilizamos um bloco try-except. Isso é vital para evitar que o programa "quebre" caso o usuário digite letras no campo de preço, onde o sistema espera um número real (float).

4. Lógica de Filtragem e Busca
A função buscar_categoria() percorre a lista de dicionários e compara a entrada do usuário com a chave categoria. Se houver correspondência, o item é exibido na tela.

5. Remoção Dinâmica
Para remover um item, o sistema primeiro lista o inventário para que o usuário veja o índice (#). Ao escolher um número, o método .pop(index) remove o elemento exato da lista, e a função salvar_item() atualiza o arquivo JSON instantaneamente.

💻 Tecnologias Utilizadas
Python 3

Biblioteca json: Para armazenamento de dados.

Biblioteca os: Para verificação de existência de arquivos no sistema.

Bibliotec

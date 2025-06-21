# Biblioteca Pandas: Uma das ferramentas mais populares para a análise e manipulação de dados em python
# Principais recursos:
    # DataFrame: Estrutura de dados tabular (como uma planilha do Excel) que permite armazenar e manipular dados de forma eficiente.
    # Series: Estrutura unidimensional (como uma coluna em um DataFrame) que armazena dados de um único tipo.
    # Leitura e escrita de dados: Suporte para diversos formatos como CSV, Excel, SQL, JSON, HTML, etc.
    # Limpeza e preparação de dados: Funções para lidar com valores ausentes, duplicatas, filtragem e transformação de dados.
    # Análise estatística: Cálculos como média, mediana, desvio padrão, correlação, etc.
    # Visualização de dados: Integração com bibliotecas como Matplotlib e Seaborn para gerar gráficos.
    # Agregação e agrupamento: Operações como groupby, pivot_table e merge para resumir e combinar dados.

# df = pd.read_csv("winemag-data-130k-v2.csv") -> read_csv: Ler arquivos do Google Drive
# df.head() -> lêmos as 5 primeiras linhas do DataFrame
# df.tail() -> lêmos as 5 últimas linhas do DataFrame
# df.sample(5) -> exibe uma amostra aleatória do DataFrame ( no caso, n = 5)
# df.shape -> mostrar as dimensões do DataFrame (no nosso caso, 14 colunas e 129.971 linhas?)
# df.describe() -> retorna:
    # count: número de observações daquela variável
    # mean: valor médio dessa variável
    # std: desvio padrão da variável
    # min: valor mínimo registrado
    # 25%: valor que separa o primeiro quartil
    # 50%: valor que separa o segundo quartil
    # 75%: valor que separa o terceiro quartil
    # max: valor máximo registrado

# O método df.columns em pandas (onde df é um DataFrame) retorna os nomes das colunas do DataFrame como um Index object 
# (uma estrutura semelhante a uma lista, mas com funcionalidades adicionais).
# 1.Mostra os nomes das colunas 2.Permite renomear colunas 3.Pode ser usado para selecionar, filtrar ou modificar colunas
# df.info() -> permite extrair informações como: quantidade de colunas, quantidade de linhas não nulas e o tipo de dado de cada uma.
# df['country'] -> "fatia" o DataFrame por coluna ( nesse caso, por country/país)

# Série é uma estrutura de dados unidimensional (como uma lista ou array) fornecida pela biblioteca pandas. 
    # 1.Pode ser homogênea ou heterogênea (mas geralmente homogênea).
    # 2.Possui rótulos (índices) personalizáveis (não apenas 0, 1, 2...).
    # 3.Suporta operações vetorizadas (como NumPy).
    # 4.Métodos integrados para limpeza e análise de dados (ex.: mean(), isna()).
# Ela é similar a uma coluna em uma tabela do Excel,e pode armazenar dados de qualquer tipo(números, strings, booleanos, etc.).
# DataFrame nada mais é que um conjunto de Series juntas
# Quando quisermos selecionar mais de uma coluna de um dataset, a estratégia é criar um dataset novo com as colunas desejadas.
# Para fazer isso precisamos passar os nomes das colunas, entre aspas, entre DOIS colchetes
    # df_novo = df[['country','variety]]
    # df_novo2 = df[['country','variety','province', 'region_1',]]
# Separação e seleção de linhas -> métodos .loc e .iloc
    # df_novo2.iloc[5] #linha 5
# A única diferença entre .loc e .iloc é que com o iloc é passado a posição numérica da linha desejada.
# Já no .loc devemos passar o rótulo da linha e não a usa posição
# o rótulo seria essa primeira coluna que fica a esquerda da tabela com os números em negrito)
# Nesse caso, como as linhas estão ordenadas o loc e o iloc fazem a mesma coisa. 
# Mas nos casos em que o rótulo não coincide com a posição devemos nos atentar a qual usar.
# Podemos filtrar também dessa forma -> df[(condicao_desejada)]
    # Ex: df_novo = df[df['country'] == 'France']  #filtrando quando df['country'] for igual a 'France'
# df_group = df[['country','points','price']]
# df_group = df_group.groupby('country').mean()
# Se quisermos ordenar os valores:
    # df_group.sort_values(by='points', ascending=True) -> ascending=True: crescente, asceding=False: decrescente
# Dados Nulos (ou Faltantes):
    # Dados faltantes são dados não registrados, ou seja, uma determinada célula do dataframe que não possui nenhum dado lá dentro. 
    # Saiba que é comum que os dados nulos sejam chamados de "NaN" (Not a Number) no dataframe.
    # df.isnull() -> mostrará se cada linha possui algum valor nulo
    # df.isnull().sum() -> soma e retorna a quantidade de valores nulos para cada coluna 
    # df.dropna() -> ela remove todas as linhas que possuem algum valor nulo
    # de forma similar, df.duplicated().sum() -> soma e retorna a quant. de linhas duplicadas
    # df = df.drop_duplicates()
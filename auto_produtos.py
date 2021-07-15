# > EXEMPLO MERCADO LIVRE

# - Obtendo produtos do Mercado Livre a partir de uma busca realizada

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

#Declara uma variável para Pandas
lista_produtos = []

#URL BASE
url_base = 'https://lista.mercadolivre.com.br/'

#Imprimir questão para o usuário com input
produto_desejado = input('Qual produto você deseja?')


#1º requisição por padrão de busca. Exemplo final mi-band-5

requisicao = requests.get(url_base + produto_desejado + '#D[A:' + produto_desejado +']')


#2º Converte este conteúdo em BS, dentro de uma variável
site = bs(requisicao.text, 'html.parser')

#Variável para o produto desejado
produto_desejado = site.findAll('div', attrs={'class': 'andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default'})

#FOR
for especificacao in produto_desejado:
    #Titulo
    titulo = especificacao.find('h2', attrs={'class': 'ui-search-item__title'})
    print('Título do Produto: ', titulo.text)
    #Link
    link = especificacao.find('a', attrs={'class': 'ui-search-item__group__element ui-search-link'})
    print('Link do produto: ', link['href'])
    #Preço
    simbolo = especificacao.find('span', attrs={'class': 'price-tag-symbol'})  
    real = especificacao.find('span', attrs={'class': 'price-tag-fraction'})  
    centavo = especificacao.find('span', attrs={'class': 'price-tag-cents'})
    
    if (centavo):
        lista_produtos.append([titulo.text, link['href'], (simbolo.text + real.text + ',' + centavo.text)])
        print('Valor: ', simbolo.text + real.text + ',' + centavo.text)
    else:
        lista_produtos.append([titulo.text, link['href'], (simbolo.text + real.text + ',00')])
        print('Valor: ', simbolo.text + real.text + ',00', '')
    
    print()
        

#Armazenando em lista
tabela_produtos = pd.DataFrame(lista_produtos, columns=['Produto', 'Link', 'Valor'])

#7º Salva em CSV
tabela_produtos.to_csv('ML-Base de Dados_bicicleta.csv', index=True)
tabela_produtos.to_excel('ML-Base de Dados_bicicleta.xlsx', index=False)    
    










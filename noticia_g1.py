#Import
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

#INSTRUÇÕES
#1ºFaz uma requisição
#2º Converte este conteúdo em BS, dentro de uma variável
#3º Dentro da variável faz a pesquisa que deseja
#4º FOR para buscar todas as noticias
#5º Converte em formato texto com .text
#6º Transforma em DataFrame
#7º Salva em CSV


#Para criar a tabela Pandas, cria vazio para armazenar todo o conteúdo depois no FOR
lista_noticias = []

#---------------------------------------
#1ºFaz uma requisição
requisicao = requests.get('https://g1.globo.com/')

conteudo = requisicao.content


#---------------------------------------
#2º Converte este conteúdo em BS, dentro de uma variável
site = bs(conteudo, 'html.parser')


#---------------------------------------
#3º Dentro da variável faz a pesquisa que deseja
#HTML da notícia
todas_noticias = site.findAll('div', attrs={'class': 'feed-post-body'})


#---------------------------------------
#4º FOR para buscar todas as noticias
for noticia in todas_noticias:
    #Título da notícia
    titulo = noticia.find('a', attrs={'class': 'feed-post-link gui-color-primary gui-color-hover'})

    #titulo: imprima ele em formato de texto
    print(titulo.text)

    #Pode acessar o titulo como se fosse um dicionário, pegando o link da noticia
    print(titulo['href'])


    #Subtitulo da notícia
    subtitulo = noticia.find('div', attrs={'class': 'feed-post-body-resumo'})

    #titulo: imprima ele em formato de texto


    #Se o subtitulo existir imprima ele
    #Armazenamento da lista de noticias, add titulo, link e subtitulo
    if (subtitulo):
        lista_noticias.append([titulo.text, subtitulo.text, titulo['href'] ])
        print(subtitulo.text)
    else:
        lista_noticias.append([titulo.text, '', titulo['href'] ])    

#pd = Panda que transforma em DataFrame
noticias_dataframe = pd.DataFrame(lista_noticias, columns=['Titulo', 'Subtitulo', 'Link'])

#7º Salva em CSV
noticias_dataframe.to_csv('Base de Daos.csv', index=True)
noticias_dataframe.to_excel('Base de Dados.xlsx', index=False)

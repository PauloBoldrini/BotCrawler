import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import pandas as pd

#Options
options = Options()
#Headless = realiza o processo sem abrir o navegador na maquina
options.add_argument('--headless')
options.add_argument('window-size=400,800')

#Selenium
navegador = webdriver.Chrome(options=options)
navegador.get('https://www.airbnb.com')


#Serve para aguardar a página ser criada pelo cliente para que então possa puxar o HTML
sleep(2)


#Primeira parte: LOCALIZAÇÃO
#Encontrar elementos
local_input = navegador.find_element_by_tag_name('input')
#Procure palavras chaves
local_input.send_keys('Florianopolis')
#Enter
local_input.submit()


#Segunda parte: ENCONTRE UM LUGAR PARA FICAR
sleep(0.5)
#Em button com tag filha chamada img
primeira_opcao = navegador.find_element_by_css_selector('button > img')
primeira_opcao.click()


#Terceira parte: CALENDÁRIO
# -1 = procura o último elemento
sleep(0.5)
proximo = navegador.find_elements_by_tag_name('button')[-1]
proximo.click()


#Quarta parte: adicionar pessoas
sleep(0.5)
pessoas = navegador.find_elements_by_css_selector('button > span > svg > path[d="m2 16h28m-14-14v28"]')[0]
pessoas.click()
sleep(1)
pessoas.click()


#Quinta parte: Pesquisar
sleep(1)
pesquisar = navegador.find_elements_by_tag_name('button')[-1]
pesquisar.click()




#Page_source traz o html da página
sleep(4)
site = BeautifulSoup(navegador.page_source, 'html.parser')

dados_hospedagens = []

#Primeiro apartamento
hospedagens = site.findAll('div', attrs={'itemprop': 'itemListElement'})

for hospedagem in hospedagens:

    #print(hospedagem.prettify())

    #Descrição
    hospedagem_descricao = hospedagem.find('meta', attrs={'itemprop': 'name'})
    hospedagem_descricao = hospedagem_descricao['content']
    #url
    hospedagem_url = hospedagem.find('meta', attrs={'itemprop': 'url'})
    hospedagem_url = hospedagem_url['content']
    #Detalhes
    hospedagem_detalhes = hospedagem.find('div', attrs={'style': 'margin-bottom: 2px;' }).findAll('li')

    #Preço
    preco = hospedagem.findAll('span')[-3].text


    #Juntar as duas LI
    #hospedagem_detalhes = hospedagem_detalhes[0].text + hospedagem_detalhes[1].text
    hospedagem_detalhes = ''.join([detalhe.text for detalhe in hospedagem_detalhes])

    #Entre [] para tirar o HTML
    print('Descrição:', hospedagem_descricao)
    print('Link:', hospedagem_url)
    print('Detalhes da hospedagem: ', hospedagem_detalhes)
    print('Preço: ', preco)
    print()

    dados_hospedagens.append([hospedagem_descricao, hospedagem_url, hospedagem_detalhes, preco])

dados = pd.DataFrame(dados_hospedagens, columns=['Descrição', 'Link', 'Detalhes', 'Preço'])
dados.to_csv('hospedagens_airbnb.csv', index=False)
dados.to_excel('hospedagens_airbnb.xlsx', index=False)

import urllib.request


#Site 1
content = urllib.request.urlopen("https://www.melhorcambio.com/cotacao/compra/euro/sao-paulo")
#read retorna o HTML do site
content = str(content) #converte o resultado em string
find = '<span>R$</span>' #irá procurar o texto próximo do find
posicao = int(content.index(find) + len(find)) #retorna o indice da string que passo como parametro
#Qual o parametro?  imput type= "hidden" value="'. Onde retorna a posição deste conteudo  que esta na string
#LEN(find) = irá listar o conteúdo recebido da String
dolar = content [posicao : posicao + 4] #Pega a sub String de content, ou seja, todo o conteúdo do site
# A partir do valor informado até posição + 4


#Site 2
content = urllib.request.urlopen("https://www.sdasd.com")
content = str(content)
find = '<imput type= "hidden" value="' 
posicao = int(content.index(find) + len(find)) 
euro = content [posicao : posicao + 4] 


#Site 3
content = urllib.request.urlopen("https://www.sdasd.com")
content = str(content)
find = 'xima">' 
posicao = int(content.index(find) + len(find)) 
maxima = content [posicao : posicao + 2] 

find = 'nima">' 
posicao = int(content.index(find) + len(find)) 
minima= content [posicao : posicao + 2] 





#Imprimir valores no console
print("Dolar: " + dolar)
print("Euro: " + euro)
print("Temperatura Máxima: " + maxima)
print("Temperatura Mínima: " + minima)

from  lib.scrapy_dadosAbertos import DadosAbertos

listJson = DadosAbertos()

ldeputados = {}
for lista in listJson.deputados():
    nome    =  lista['nome']
    partido =  lista['siglaPartido']
    ldeputados[nome] = partido

for partido in sorted(ldeputados.values()):
    for nome in ldeputados:
        if partido == ldeputados[nome]:
            print("Nome: {0}, Partido: {1}".format(nome,partido))

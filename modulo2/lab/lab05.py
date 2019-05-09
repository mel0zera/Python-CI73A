from  lib.scrapy_dadosAbertos import DadosAbertos

listJson = DadosAbertos()

for org in listJson.orgaos():
    id   = org['id']
    nome = org['nome']
    print(id,nome.upper())

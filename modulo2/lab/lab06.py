from  lib.scrapy_dadosAbertos import DadosAbertos

listJson = DadosAbertos()

for comissao in  listJson.orgaos_membros('5973'):
    print(comissao['nome'])

from  lib.scrapy_dadosAbertos import DadosAbertos

listJson = DadosAbertos()

deputado = listJson.deputado_id('73437')
nome = deputado['nomeCivil']

despesas = listJson.deputado_despesas('73437')
for despesa in despesas:
    print("{2}, {3}, {0}/{1}, R$ {4}".format(despesa['mes'],despesa['ano'],nome,despesa['tipoDespesa'],despesa['valorDocumento']))

from  lib.scrapy_dadosAbertos import DadosAbertos

list_dep = DadosAbertos()

num = len(list_dep.deputados())

print("Numero de deputados:", num)

from  lib.scrapy_dadosAbertos import DadosAbertos

list_dep = DadosAbertos()

print(len(list_dep.deputados()))


for dep in list_dep.deputados():    
    id   = dep['id']
    nome = dep['nome']

    infodep = list_dep.deputado_id(id)
    
    mascara = "Id: {0}\n Nome: {1}\n Data de Nascimento: {2}\n Estado de Nascimento: {3}\n Email: {4}\n Sigla do Partido: {5}\n #-------------------------------------------------"

    print(mascara.format( 
                         id,
                         nome,
                         infodep['dataNascimento'],
                         infodep['ufNascimento'],
                         infodep['ultimoStatus']['gabinete']['email'],
                         infodep['ultimoStatus']['siglaPartido']
                         ))

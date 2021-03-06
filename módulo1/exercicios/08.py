from  lib.scrapy_table import Scrapy_Table


url_populacao   = "https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Brasil_por_popula%C3%A7%C3%A3o"
url_homicidio   = "https://pt.wikipedia.org/wiki/Lista_de_cidades_por_taxa_de_homic%C3%ADdios"
url_fecundidade = "https://pt.wikipedia.org/wiki/Lista_de_unidades_federativas_do_Brasil_por_taxa_de_fecundidade"


wiki_populacao   = Scrapy_Table(url_populacao)
wiki_homicidio   = Scrapy_Table(url_homicidio)
wiki_fecundidade = Scrapy_Table(url_fecundidade)


tables_populacao   = wiki_populacao.get_tables(0)
tables_homicidio   = wiki_homicidio.get_tables(1)
tables_fecundidade = wiki_fecundidade.get_tables(1)

tot = 0

for linha in tables_populacao[1:]:
  
  pop = linha[4]
  nome = linha[2]
  est = linha[3]
  pop1 = int(pop)
  if est == "Minas Gerais" or est == "Rio de Janeiro" or est == "São Paulo" or est == "Espírito Santo":
    tot = tot + pop1

print(tot)

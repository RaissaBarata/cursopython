trabalho_terca = False
trabalho_quinta = False

"""
confirmando os dois trabalhos: TV 50' + sorvete
confirmando apenas 1: TV 32' + sorvete
nenhum confirmado: fica em casa
"""

tv_50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta
mais_saudavel = not sorvete

print(
    "Tv50={} Tv32={} Sorvete={} saudavel{}".format(tv_50, tv_32, sorvete, mais_saudavel)
)

def stampaDizionario(diz):
    for key,value in diz.items():
         print("la chiave è ..."+key)
         print("Il valore è..."+str(value))
def totaleOre(totale):
    somma=0
    for key,value in dizionario.items():
        somma+=value
    print(somma)
def cattedraPiena(cattPiena):
    i=0
    for key,value in dizionario.items():
        if value==18:
             i+=1
    print(i)
def oreAllocate(diz,prof,ore):
   diz[prof]=ore
dizionario = {"rossi":18,"bianchi":16,"verdi":6}
print(dizionario)
oreAllocate(dizionario,"rossi",6)
stampaDizionario(dizionario)




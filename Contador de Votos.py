#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      aula14
#
# Created:     25/09/2019
# Copyright:   (c) aula14 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

Va=0
Vb=0
Vc=0
otros=0
voto=str(input("Por favor, digite su voto "))
while voto !="x":
    if voto=="A":
        Va=Va+1
    elif voto=="B":
        Vb=Vb+1
    elif voto=="C":
        Vc=Vc+1
    else:
        otros=otros+1
    voto=(str(Input("Por favor digite el siguiente Voto"))) #jajaxd
total=Va+Vb+Vc+otros
pa=Va/total*100
pb=Vb/total*100
pc=Vc/total*100
print("la cantidd de votos son ",total,)
print("la cantidad de votos para el candidato A  son ",Va,"y su porcentaje es de ",round(pa))
print("la cantidad de votos para el candidato A  son ",Vb,"y su porcentaje es de ",round(pb))
print("la cantidad de votos para el candidato A  son ",Vc,"y su porcentaje es de ",round(pc))

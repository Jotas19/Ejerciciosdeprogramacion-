#aprobador
nota=float(input("por favor digite su nota"))
nombre=str(input("por favor digite su nombre"))
if nota>=3.0:
    print("el estudiante ",nombre," con ",nota," aprobó la materia")
elif nota<=3.0:
    print("el estudiante ",nombre," con ",nota," reprobó la materia")
else:
    print("la nota introducida es incorrecta o no válida")
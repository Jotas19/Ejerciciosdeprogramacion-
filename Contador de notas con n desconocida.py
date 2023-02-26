#En python xd
ContE=float
ContM=float
ContB=float
ContE==0
ContB==0
ContM==0
Estudiante=int(input("Por favor ingrese su código"))
while Estudiante!=0:
    nota=float(input("Por favor ingrese su nota"))
    Centinela=str(input("Ha terminado de escribir su nota ?"))
    if Centinela=="Si" or Centinela=="sI" or Centinela=="SI" or Centinela=="si":
     print("Notas malas ",ContM," Notas Buenas ",ContB," Notas excelentes",ContE,)
    elif Centinela=="No" or Centinela=="nO" or Centinela=="NO" or Centinela=="no":
        if nota>=1.0 and nota<=2.9:
            ContM=ContM+1
        if nota>=3.0 and nota<=3.0:
            ContB=ContB+1
        if nota>=4.0 and nota<=5.0:
            ContE=ContE+1




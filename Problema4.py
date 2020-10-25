numar=eval(input("Dati un numar:"))
suma=0
produs=1
nr=1
while nr<=numar:
    suma+=nr
    produs*=nr
    nr+=1

print("Suma este",suma)
print("Produsul este",produs)
print("Media aritmetica este",(suma/numar))
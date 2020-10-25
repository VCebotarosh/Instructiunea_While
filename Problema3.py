numar=0
suma_pare=0
while ((numar%3!=0)or(numar%2==0)):
    numar=eval(input("Dati un numar: "))
    if numar%2==0:
        suma_pare+=numar
        
print("Suma numerelor pare este egala cu ",suma_pare)
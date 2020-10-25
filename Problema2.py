luna=1
temperaturi_pozitive=0
temperaturi_negative=0
suma_pozitiva=0
suma_negativa=0
while luna<=12:
    temperatura=eval(input("Dati temperatura medie a fiecarei luni:\n"))
    if temperatura>=0:
        temperaturi_pozitive+=1
        suma_pozitiva+=temperatura
    elif temperatura<0:
        temperaturi_negative+=1
        suma_negativa+=temperatura
    luna+=1

print("Media temperaturilor pozitive este",round((suma_pozitiva/temperaturi_pozitive),2))    
print("Media temperaturilor negative este",round((suma_negativa/temperaturi_negative),2))    
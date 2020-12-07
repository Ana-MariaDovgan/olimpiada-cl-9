<<Sa se scrie un program care citeste un numar de ani si calculeaza numarul de luni,zile si ore corespunzatoare. Se considera ca un an are 365 
zile.>>
n = int(input("dati numarul de ani: "))
print("In",n,"ani sunt", n * 12,"luni")
print("In",n,"ani sunt", n * 52,"saptamani")
print("In",n,"ani sunt", n * 365,"zile")
print("In",n,"ani sunt", n * 365 * 24,"ore")

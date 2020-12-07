<<La o ferma avicola sunt x pasari. Jumatate din acestea sunt gaini. Numarul ratelor constituie un sfert din numarul gainilor. Celelalte sunt 
gaste. Scrieti un program care citeste de la tastatura numarul total de pasari si afiseaza numarul de gaini, rate si gaste.>> 

n=int(input("numarul total de pasari: "))
g=n//2
r=g//4
gs=n-g-r
print("numarul de gaini este: ",g)
print("numarul de rate este: ",r)
print("numarul de gaste este: ",gs)

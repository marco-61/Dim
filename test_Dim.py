from Dim import Dim
A=Dim(float,10,30,[x *3.3 for x in range(10,31)])  # crea un array di 20 float con indici che vanno da 10,30
B=Dim(int, 3,-3,data=[1,2,3,4,5,6,7])  # crea un array di 7 interi con indici misti invertiti e gli assegna dei valori.

#Esempio di matrice
M=Dim(Dim,1,2)  # crea la base della matrice
M[1]=A
M[2]=B
M[1][10]=5.67 #setta il primo indice dell’array A
M[2][-3]=45 #setta il primo indice dell’array B
S=M[2][-2]  # ritorna il valore dell’indice -2 della secondo array
#Potete creare matrici miste ma non dimensioni miste ogni dimensione può avere un solo tipo
#  stampa i valori stile stile freebasic
for x in range(A.LBound(),A.UBound()):  print(A[x])
# stampa I valori stile python
for x in A: print(x,end=' ')
print(len(A)) # ritorna il numero di elementi in a
print(f"somma dell'array B={sum(B)}") # somma il valore degli elementi e ne ritorna il totale
# La classe è ben documentata e un buono studio per le classi contenitore.

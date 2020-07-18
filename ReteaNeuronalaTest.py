import math

linSablon, colSablon=5, 5
iesiri=10

NI=linSablon*colSablon
NO=iesiri
NH=int((NI+NO)/2)
        
#Intrari
x=[0 for i in range(NI)]
#Ponderi intre startul de intrare si stratul ascuns
w1=[[0 for i in range(NI)] for j in range(NH)]
#Ponderi intre stratul ascuns si stratul de iesire
w2=[[0 for i in range(NH)] for j in range(NO)]
#Activarile pentru neuronii din stratul ascuns
yH=[0 for i in range(NH)]
#Activarile pentru neuronii din stratul de iesire
yO=[0 for i in range(NO)]


"""Se pun datele din fisierul de sabloane in matricea de intrari."""
with open("sabloane test.txt", "r") as fisierSabloane:
    stringFisier=fisierSabloane.read()
    sablon=stringFisier.split("\n\n")
    sablon.pop(1)
    pixel="".join(sablon[0].split("\n"))
    for i in range(linSablon*colSablon):
        x[i]=int(pixel[i])

"""Initializam ponderile dintre stratul de intrare si stratul ascuns,
si ponderile dintre stratul ascuns si stratul de iesire cu valorile rezultate dupa antrenament."""
with open("ponderi.txt", "r") as fisierPonderi:
    stringFisier=fisierPonderi.read()
    straturiPonderi=stringFisier.split("\n")
    pondere=straturiPonderi[0].split()
    for i in range(NH):
        for j in range(NI):
            w1[i][j]=float(pondere[i*NI+j])
    pondere=straturiPonderi[1].split()
    for i in range(NO):
        for j in range(NH):
            w2[i][j]=float(pondere[i*NH+j])

for i in range(NH):
    a=0
    for j in range(NI):
        a+=x[j]*w1[i][j]
    yH[i]=1/(1+math.exp(-a))
for i in range(NO):
    a=0
    for j in range(NH):
        a+=yH[j]*w2[i][j]
    yO[i]=1/(1+math.exp(-a))
    
         
print("Cifra 0: "+str(yO[0]))
print("Cifra 1: "+str(yO[1]))
print("Cifra 2: "+str(yO[2]))
print("Cifra 3: "+str(yO[3]))
print("Cifra 4: "+str(yO[4]))
print("Cifra 5: "+str(yO[5]))
print("Cifra 6: "+str(yO[6]))
print("Cifra 7: "+str(yO[7]))
print("Cifra 8: "+str(yO[8]))
print("Cifra 9: "+str(yO[9]))

max=0
for i in range(NO):
    if yO[i]>max:
        max=yO[i]
        indiceIesire=i

print()
if max>=0.7:
    print("Cifra este: "+str(indiceIesire))
else:
    print("Cifra introdusa este neclara. Reteaua neuronala necesita mai multa antrenare...")
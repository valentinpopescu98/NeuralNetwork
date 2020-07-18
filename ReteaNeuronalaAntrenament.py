import random, math

linSablon, colSablon=5, 5
iesiri=10

NI=linSablon*colSablon
NO=iesiri
NH=int((NI+NO)/2)

"""Creeaza fisierele daca nu exista."""
fisierSabloane=open("sabloane antrenament.txt", "a")
fisierSabloane.close()
fisierPonderi=open("ponderi.txt", "a")
fisierPonderi.close()

"""Se numara sabloanele."""
nrSabloane=-1
with open("sabloane antrenament.txt", "r") as fisierSabloane:
    date=fisierSabloane.read()
    sablon=date.split("\n\n")
    for i in enumerate(sablon):
        nrSabloane+=1    
        
#Intrari
x=[[0 for i in range(NI)] for j in range(nrSabloane)]
#Iesiri
y=[[0 for i in range(NO)] for j in range(nrSabloane)]
#Ponderi intre startul de intrare si stratul ascuns
w1=[[0 for i in range(NI)] for j in range(NH)]
#Ponderi intre stratul ascuns si stratul de iesire
w2=[[0 for i in range(NH)] for j in range(NO)]
#Activarile pentru neuronii din stratul ascuns
yH=[0 for i in range(NH)]
#Activarile pentru neuronii din stratul de iesire
yO=[0 for i in range(NO)]
#Derivatele pentru neuronii din stratul ascuns
deltaH=[0 for i in range(NH)]
#Derivatele pentru neuronii din stratul de iesire
deltaO=[0 for i in range(NO)]
#Erorile pentru fiecare sablon in parte
eSablon=[0 for i in range(nrSabloane)]
#Limita de eroare totala sub care reteaua va converge
eLimita=0.0001
#Initializarea numarului epocilor
epoca=0

"""Se pun datele din fisierul de sabloane in matricea de intrari, respectiv in vectorul de iesiri."""
with open("sabloane antrenament.txt", "r") as fisierSabloane:
    stringFisier=fisierSabloane.read()
    sablon=stringFisier.split("\n\n")
    sablon.pop(nrSabloane)
    for i in range(nrSabloane):
        pixel="".join(sablon[i].split("\n"))
        for j in range(linSablon*colSablon):
            x[i][j]=int(pixel[j])
        for j in range(iesiri):
            y[i][j]=int(pixel[linSablon*colSablon+j])

"""Initializam ponderile dintre stratul de intrare si stratul ascuns cu valori aleatoare."""
for i in range(NH):
    for j in range(NI):
        w1[i][j]=float(random.uniform(-0.5, 0.5))

"""Initializam ponderile dintre stratul ascuns si stratul de iesire cu valori aleatoare."""        
for i in range(NO):
    for j in range(NH):
        w2[i][j]=float(random.uniform(-0.5, 0.5))

"""Functie care salveaza ponderile actuale intr-un fisier text ponderi.txt pe hard disk."""
def salveazaPonderi():
    fisierPonderi=open("ponderi.txt", "w")
    for i in range(NH):
        for j in range(NI):
            fisierPonderi.write(str(w1[i][j])+" ")
    fisierPonderi.write("\n")
    for i in range(NO):
        for j in range(NH):
            fisierPonderi.write(str(w2[i][j])+" ")
    fisierPonderi.write("\n")
    fisierPonderi.close()
       
    
"""Algoritmul back-propagation."""
while(1):
    for ex in range(nrSabloane):
        for i in range(NH):
            a=0
            for j in range(NI):
                a+=x[ex][j]*w1[i][j]
            yH[i]=1/(1+math.exp(-a))
        for i in range(NO):
            a=0
            for j in range(NH):
                a+=yH[j]*w2[i][j]
            yO[i]=1/(1+math.exp(-a))
        
        eSablon[ex]=0
        for i in range(NO):
            eSablon[ex]+=0.5*(yO[i]-y[ex][i])**2
        for i in range(NO):
            deltaO[i]=(yO[i]-y[ex][i])*(1-yO[i])*yO[i]
        for i in range(NO):
            for j in range(NH):
                w2[i][j]-=yH[j]*deltaO[i]
        for i in range(NH):
            sumaPond=0
            for j in range(NO):
                sumaPond+=w2[j][i]*deltaO[j]
            deltaH[i]=sumaPond*(1-yH[i])*yH[i]
        for i in range(NH):
            for j in range(NI):
                w1[i][j]-=x[ex][j]*deltaH[i]
    epoca+=1
    #Suma erorii tuturor sabloanelor
    eTotala=0
    for i in range(nrSabloane):
        eTotala+=eSablon[i]
    print("Epoca "+str(epoca)+", eroare: "+str(eTotala))
    if eTotala<=eLimita:
        break


salveazaPonderi()
print("A convers...")
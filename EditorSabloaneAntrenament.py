import tkinter as tk
root = tk.Tk()

frameSablonText=tk.Frame(root)
frameSablonText.grid(row=0, padx=10, pady=10)

frameSablon = tk.Frame(root)
frameSablon.grid(row=1)

frameIesiriText=tk.Frame(root)
frameIesiriText.grid(row=2, padx=10, pady=10)

frameIesiri = tk.Frame(root)
frameIesiri.grid(row=3)

frameButoane = tk.Frame(root)
frameButoane.grid(row=4, padx=10, pady=(50, 0))

frameNumarareSabloane = tk.Frame(root)
frameNumarareSabloane.grid(row=5, padx=10, pady=10)

linSablon, colSablon=5, 5
iesiri=10
butonIntrare= []
butonIesire= []

"""Creeaza fisierul daca nu exista."""
fisierSabloane=open("sabloane antrenament.txt", "a")
fisierSabloane.close()

"""Se numara sabloanele."""
nrSabloane=-1
with open("sabloane antrenament.txt", "r") as fisierSabloane:
    date=fisierSabloane.read()
    sablon=date.split("\n\n")
    for i in enumerate(sablon):
        nrSabloane+=1  

"""Functie toggle la oricate butoane se aleg in acelasi timp."""
def toggleButonIntrare(i, j):
    if butonIntrare[i*colSablon+j].config("bg")[-1] == "SystemButtonFace":
        #ON
        butonIntrare[i*colSablon+j].config(bg="grey", relief="sunken")
    else:
        #OFF
        butonIntrare[i*colSablon+j].config(bg="SystemButtonFace", relief="raised")

"""Functie toggle la un singur buton la un moment dat."""
def selectButonIesire(iIesiri):
    #OFF la toate
    for i in range(iesiri):
        butonIesire[i].config(bg="SystemButtonFace", relief="raised")
    if butonIesire[iIesiri].config("bg")[-1] == "SystemButtonFace":
        #ON
        butonIesire[iIesiri].config(bg="grey", relief="sunken")
        
"""Functie care scrie starea butoanelor intr-un fisier text sabloane antrenament.txt pe hard disk.
   Functia permite adaugarea a noi modele in acelasi fisier."""
def scrie():
    fisierSabloane=open("sabloane antrenament.txt", "a")
    contorEndl=0
    for i in range(linSablon*colSablon):
        if butonIntrare[i].config("bg")[-1]=="grey":
            #ON
            fisierSabloane.write("1")
        else:
            #OFF
            fisierSabloane.write("0")
        contorEndl+=1
        if contorEndl%colSablon==0:
            fisierSabloane.write("\n")
    for i in range(iesiri):
        if butonIesire[i].config("bg")[-1]=="grey":
            #ON
            fisierSabloane.write("1")
        else:
            #OFF
            fisierSabloane.write("0")        
    fisierSabloane.write("\n\n")
    fisierSabloane.close()

"""Functie care repune butoanele la starea initiala."""  
def revenire():
    for i in range(linSablon*colSablon):
        butonIntrare[i].config(bg="SystemButtonFace", relief="raised")
    for i in range(iesiri):
        butonIesire[i].config(bg="SystemButtonFace", relief="raised")

"""Functie care manipuleaza functia 'scrie' adaugand urmatoarele restrictii:
    1. Nu se permite salvarea unui sablon fara a alege o iesire.
    2. Nu se permite salvarea aceluiasi sablon de 2 ori"""
def salveaza():
    patternMatrice=""
    patternIesiri=""
    patternIesiriGol=""
    contorEndl=0
    #Creeaza sablonul de proba.
    for i in range(linSablon*colSablon):
        if butonIntrare[i].config("bg")[-1]=="grey":
            #ON
            patternMatrice+="1"
        else:
            #OFF
            patternMatrice+="0"
        contorEndl+=1
        if contorEndl%colSablon==0:
            patternMatrice+="\n"
    #Creeaza vectorul de iesiri dorite de proba.
    for i in range(iesiri):
        patternIesiriGol+="0"
        if butonIesire[i].config("bg")[-1]=="grey":
            #ON
            patternIesiri+="1"
        else:
            #OFF
            patternIesiri+="0"
    """Se compara vectorul de iesiri, apoi matricea de pixeli sablon daca respecta conditiile,
    iar daca le respecta se va face scrierea propriu-zisa in fisier."""
    with open("sabloane antrenament.txt", "r") as fisierSabloane:
        if patternIesiri==patternIesiriGol:
            tk.messagebox.showerror("Nicio intrare", "Nu ati ales niciun element pe vectorul de iesiri dorite!")
        else:
            if patternMatrice in fisierSabloane.read():
                tk.messagebox.showwarning("Model existent", "Acest model exista deja in baza de date!")
            else:
                scrie()
                tk.messagebox.showinfo("Sablon salvat", "Sablonul selectat s-a salvat in baza de date!")


"""Afiseaza un label pentru identificarea matricii de pixeli a sablonului."""
text=tk.Label(frameSablonText, text="Configurare sablon:")
text.grid()

"""Iteratie care afiseaza matricea de pixeli sablon si ii aplica functionalitatea de apasare."""
for i in range(linSablon):
    for j in range(colSablon):
        butonIntrare.append(tk.Button(frameSablon, command=lambda i=i, j=j: toggleButonIntrare(i, j)))
        butonIntrare[(i)*colSablon+j].grid(row=i, column=j)


"""Afiseaza un label pentru identificarea vectorului de iesiri dorite."""
text=tk.Label(frameIesiriText, text="Configurare iesiri dorite:")
text.grid()

"""Iteratie care afiseaza vectorul de iesiri dorite si ii aplica functionalitatea de apasare."""
for i in range(iesiri):
    butonIesire.append(tk.Button(frameIesiri, command=lambda i=i: selectButonIesire(i)))
    butonIesire[i].grid(row=linSablon, column=i, padx=2)



"""Buton care face legatura cu functia salveaza."""
save=tk.Button(frameButoane, text="SAVE", command=salveaza)
save.grid(row=0, column=0, padx=5)

"""Buton care face legatura cu functia revenire."""
clear=tk.Button(frameButoane, text="CLEAR", command=revenire)
clear.grid(row=0, column=1, padx=5)

"""Buton care inchide programul."""
quitBtn=tk.Button(frameButoane, text="QUIT", command=root.destroy)
quitBtn.grid(row=0, column=2, padx=5)



text=tk.Label(frameNumarareSabloane, text="Numarul curent de sabloane: "+str(nrSabloane))
text.grid()

root.mainloop()
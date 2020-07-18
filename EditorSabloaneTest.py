import tkinter as tk
root = tk.Tk()

frameSablonText=tk.Frame(root)
frameSablonText.grid(row=0, padx=10, pady=10)

frameSablon = tk.Frame(root)
frameSablon.grid(row=1)

frameButoane = tk.Frame(root)
frameButoane.grid(row=2, padx=10, pady=(50, 20))

linSablon, colSablon=5, 5
iesiri=10
butonIntrare= []

"""Creeaza fisierul daca nu exista."""
fisierSabloane=open("sabloane test.txt", "a")
fisierSabloane.close()

"""Functie toggle la oricate butoane se aleg in acelasi timp."""
def toggleButonIntrare(i, j):
    if butonIntrare[i*colSablon+j].config("bg")[-1] == "SystemButtonFace":
        #ON0
        butonIntrare[i*colSablon+j].config(bg="grey", relief="sunken")
    else:
        #OFF
        butonIntrare[i*colSablon+j].config(bg="SystemButtonFace", relief="raised")
        
"""Functie care scrie starea butoanelor intr-un fisier text sabloane.txt pe hard disk.
   Functia permite adaugarea a noi modele in acelasi fisier."""
def scrie():
    fisierSabloane=open("sabloane test.txt", "w")
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
    fisierSabloane.write("\n")
    fisierSabloane.close()

"""Functie care repune butoanele la starea initiala."""  
def revenire():
    for i in range(linSablon*colSablon):
        butonIntrare[i].config(bg="SystemButtonFace", relief="raised")

"""Functie care manipuleaza functia 'scrie' adaugand urmatoarea restrictie: nu se permite salvarea aceluiasi sablon de 2 ori"""
def salveaza():
    patternMatrice=""
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
    """Se compara vectorul de iesiri, apoi matricea de pixeli sablon daca respecta conditiile,
    iar daca le respecta se va face scrierea propriu-zisa in fisier."""
    with open("sabloane test.txt", "r") as fisierSabloane:
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


"""Buton care face legatura cu functia salveaza."""
save=tk.Button(frameButoane, text="SAVE", command=salveaza)
save.grid(row=0, column=0, padx=5)

"""Buton care face legatura cu functia revenire."""
clear=tk.Button(frameButoane, text="CLEAR", command=revenire)
clear.grid(row=0, column=1, padx=5)

"""Buton care inchide programul."""
quitBtn=tk.Button(frameButoane, text="QUIT", command=root.destroy)
quitBtn.grid(row=0, column=2, padx=5)


root.mainloop()
from tkinter import *

fenetre = Tk()
fenetre.title("Organisation de Repas")
fenetre.state("zoomed")
fenetre.configure(bg="#f4f1f1")

nom_var = StringVar()
prenom_var = StringVar()
categorie_var = StringVar()
categorie_var.set("Entrée")

compteur_entree = IntVar()
compteur_entree.set(0)

compteur_plat = IntVar()
compteur_plat.set(0)

compteur_dessert = IntVar()
compteur_dessert.set(0)

compteur_boisson = IntVar()
compteur_boisson.set(0)

etat_repas = StringVar()
etat_repas.set("État du repas : Aucun participant")

def mettre_a_jour_etat():
    entree = compteur_entree.get()
    plat = compteur_plat.get()
    dessert = compteur_dessert.get()
    boisson = compteur_boisson.get()

    valeurs = [entree, plat, dessert, boisson]
    maximum = max(valeurs)
    minimum = min(valeurs)

    if maximum == 0:
        etat_repas.set("État du repas : Aucun participant")
        label_etat.config(fg="black")
    elif maximum - minimum <= 1:
        etat_repas.set("État du repas : Équilibré")
        label_etat.config(fg="green")
    elif maximum - minimum <= 3:
        etat_repas.set("État du repas : À surveiller")
        label_etat.config(fg="orange")
    else:
        etat_repas.set("État du repas : Déséquilibré")
        label_etat.config(fg="red")

def ajouter_participant():
    nom = nom_var.get()
    prenom = prenom_var.get()
    categorie = categorie_var.get()

    if nom != "" and prenom != "":
        if categorie == "Entrée":
            compteur_entree.set(compteur_entree.get() + 1)
        elif categorie == "Plat":
            compteur_plat.set(compteur_plat.get() + 1)
        elif categorie == "Dessert":
            compteur_dessert.set(compteur_dessert.get() + 1)
        elif categorie == "Boisson":
            compteur_boisson.set(compteur_boisson.get() + 1)

        nom_var.set("")
        prenom_var.set("")
        categorie_var.set("Entrée")

        mettre_a_jour_etat()

def effacer():
    nom_var.set("")
    prenom_var.set("")
    categorie_var.set("Entrée")

cadre = Frame(fenetre, bg="#f4f1f1")
cadre.place(relx=0.5, rely=0.5, anchor="center")

Label(
    cadre,
    text="Organisation de Repas",
    font=("Arial", 22, "bold"),
    bg="#f4f1f1"
).grid(row=0, column=0, columnspan=2, pady=20)

Label(
    cadre,
    text="Nom :",
    font=("Arial", 14),
    bg="#f4f1f1"
).grid(row=1, column=0, sticky="e", padx=10, pady=8)

Entry(
    cadre,
    textvariable=nom_var,
    font=("Arial", 14),
    width=25
).grid(row=1, column=1, padx=10, pady=8)

Label(
    cadre,
    text="Prénom :",
    font=("Arial", 14),
    bg="#f4f1f1"
).grid(row=2, column=0, sticky="e", padx=10, pady=8)

Entry(
    cadre,
    textvariable=prenom_var,
    font=("Arial", 14),
    width=25
).grid(row=2, column=1, padx=10, pady=8)

Label(
    cadre,
    text="Catégorie :",
    font=("Arial", 14),
    bg="#f4f1f1"
).grid(row=3, column=0, sticky="ne", padx=10, pady=8)

cadre_radio = Frame(cadre, bg="#f4f1f1")
cadre_radio.grid(row=3, column=1, sticky="w", padx=10, pady=8)

Radiobutton(cadre_radio, text="Entrée", variable=categorie_var, value="Entrée",
            font=("Arial", 13), bg="#f4f1f1").grid(row=0, column=0, sticky="w")
Radiobutton(cadre_radio, text="Plat", variable=categorie_var, value="Plat",
            font=("Arial", 13), bg="#f4f1f1").grid(row=1, column=0, sticky="w")
Radiobutton(cadre_radio, text="Dessert", variable=categorie_var, value="Dessert",
            font=("Arial", 13), bg="#f4f1f1").grid(row=2, column=0, sticky="w")
Radiobutton(cadre_radio, text="Boisson", variable=categorie_var, value="Boisson",
            font=("Arial", 13), bg="#f4f1f1").grid(row=3, column=0, sticky="w")

Button(
    cadre,
    text="Valider",
    font=("Arial", 14),
    bg="black",
    fg="white",
    width=12,
    command=ajouter_participant
).grid(row=4, column=0, pady=20)

Button(
    cadre,
    text="Effacer",
    font=("Arial", 14),
    bg="black",
    fg="white",
    width=12,
    command=effacer
).grid(row=4, column=1, pady=20)

Label(
    cadre,
    text="Répartition actuelle",
    font=("Arial", 18, "bold"),
    bg="#f4f1f1"
).grid(row=5, column=0, columnspan=2, pady=(20, 10))

Label(cadre, text="Entrée :", font=("Arial", 14), bg="#f4f1f1").grid(row=6, column=0, sticky="e", padx=10, pady=5)
Label(cadre, textvariable=compteur_entree, font=("Arial", 14), bg="#f4f1f1", fg="blue").grid(row=6, column=1, sticky="w", padx=10, pady=5)

Label(cadre, text="Plat :", font=("Arial", 14), bg="#f4f1f1").grid(row=7, column=0, sticky="e", padx=10, pady=5)
Label(cadre, textvariable=compteur_plat, font=("Arial", 14), bg="#f4f1f1", fg="blue").grid(row=7, column=1, sticky="w", padx=10, pady=5)

Label(cadre, text="Dessert :", font=("Arial", 14), bg="#f4f1f1").grid(row=8, column=0, sticky="e", padx=10, pady=5)
Label(cadre, textvariable=compteur_dessert, font=("Arial", 14), bg="#f4f1f1", fg="blue").grid(row=8, column=1, sticky="w", padx=10, pady=5)

Label(cadre, text="Boisson :", font=("Arial", 14), bg="#f4f1f1").grid(row=9, column=0, sticky="e", padx=10, pady=5)
Label(cadre, textvariable=compteur_boisson, font=("Arial", 14), bg="#f4f1f1", fg="blue").grid(row=9, column=1, sticky="w", padx=10, pady=5)

label_etat = Label(
    cadre,
    textvariable=etat_repas,
    font=("Arial", 16, "bold"),
    bg="#f4f1f1"
)
label_etat.grid(row=10, column=0, columnspan=2, pady=25)

fenetre.mainloop()

# Organisateur de repas collectifs

**Application de bureau en Python et Tkinter pour suivre la répartition des contributions lors d'un repas collectif.**

Ce projet a été réalisé dans un cadre pédagogique autour de la conception d'une interface graphique et des interactions entre les actions utilisateur, les données internes et les retours visuels. Il répond à un cas d'usage simple : organiser un repas de promotion où chaque personne choisit d'apporter une **entrée**, un **plat**, un **dessert** ou une **boisson**.

## Fonctionnalités

- **Saisie d'un participant** : champs `Nom` et `Prénom` ; la validation exige que les deux soient renseignés.
- **Sélection d'une contribution** : boutons radio pour les quatre catégories (entrée, plat, dessert, boisson).
- **Comptage par catégorie** : le bouton **Valider** incrémente le compteur correspondant à la catégorie choisie.
- **Suivi de la répartition** : les quatre compteurs sont visibles dans l'interface et se mettent à jour après chaque validation.
- **Indicateur d'équilibre** : l'application compare les compteurs et affiche un état global avec un code couleur.
- **Effacement du formulaire** : le bouton **Effacer** vide les champs de saisie et rétablit la catégorie « Entrée », sans modifier les compteurs.

> **Périmètre actuel :** le programme mémorise les nombres de contributions par catégorie pendant son exécution, mais ne conserve **pas** les noms et prénoms dans une liste, une base de données ou un fichier. Les compteurs sont réinitialisés à chaque nouveau lancement.

## Logique de l'indicateur

L'application calcule l'écart entre le compteur le plus élevé et le plus faible :

```python
ecart = max(compteurs) - min(compteurs)
```

| Situation | État affiché | Couleur |
| --- | --- | --- |
| Tous les compteurs sont à zéro | Aucun participant | Noir |
| Écart de 0 ou 1 | Équilibré | Vert |
| Écart de 2 ou 3 | À surveiller | Orange |
| Écart de 4 ou plus | Déséquilibré | Rouge |

**Exemple :** pour 3 entrées, 2 plats, 1 dessert et 2 boissons, l'écart est `3 - 1 = 2` : l'état affiché est **« À surveiller »**.

Ces seuils mesurent uniquement la **répartition numérique** des contributions ; ils ne déterminent pas les quantités alimentaires nécessaires.

## Technologies

- **Python 3** pour la logique de l'application ;
- **Tkinter**, bibliothèque d'interface graphique fournie avec la plupart des installations de Python ;
- **Widgets Tkinter** : `Entry`, `Radiobutton`, `Button`, `Label` ;
- **Variables d'interface** : `StringVar` et `IntVar` pour lier les données aux éléments affichés.

Aucune bibliothèque tierce n'est utilisée dans le code.

## Installation et utilisation

1. Installer **Python 3** avec Tkinter (généralement inclus sous Windows).
2. Cloner le dépôt ou télécharger ses fichiers.
3. Ouvrir un terminal dans le dossier du projet.
4. Lancer :

   ```powershell
   python organisation-repas.py
   ```

5. Dans la fenêtre :
   - saisir un nom et un prénom ;
   - choisir une catégorie ;
   - cliquer sur **Valider** pour mettre à jour les compteurs ;
   - consulter l'indicateur d'équilibre.

**Compatibilité :** le programme utilise `fenetre.state("zoomed")` pour maximiser la fenêtre, ce qui est adapté à Windows. Ce comportement peut demander une adaptation sur certains autres systèmes.

## Structure du dépôt

```text
meal-planning-organizer/
├── organisation-repas.py
├── README.md
├── .gitignore
└── docs/
    └── Projet-Organisation-de-Repas.pdf
```

Le [rapport de conception](docs/Projet-Organisation-de-Repas.pdf) détaille le noyau fonctionnel, les interactions prévues, les états du système et la maquette de l'interface graphique.

## Organisation du code

- `ajouter_participant()` : vérifie les champs, incrémente le compteur de la catégorie choisie, remet le formulaire à zéro et actualise l'état.
- `mettre_a_jour_etat()` : calcule l'écart entre les quatre compteurs et choisit le texte et la couleur de l'indicateur.
- `effacer()` : réinitialise uniquement les champs du formulaire et la catégorie sélectionnée.
- La suite du fichier construit l'interface Tkinter et lance la boucle d'événements (`mainloop`).

## Limites et pistes d'amélioration

Le programme est un **prototype local**. Voici quelques fonctionnalités envisageables pour une version ultérieure (non implémentées actuellement) :

- conserver une véritable liste de participants, avec modification ou suppression ;
- empêcher les inscriptions en double ;
- enregistrer et recharger les données ;
- exporter la répartition sous forme de tableau ;
- adapter la fenêtre et son affichage à différents systèmes.

---

*Projet pédagogique — interface graphique et programmation événementielle en Python.*

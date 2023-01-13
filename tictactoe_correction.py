grille = {
    1:[None, None, None],
    2:[None, None, None],
    3:[None, None, None]
        }

# for cle in dico:
#     for elt in dico[cle]:
#         print("|", elt, "|" , end="")
#     print("\n")

# //////////////// debut affichage de la griller
def afficher_grille(grille):
    """ la fonction doit afficher la grille à chaque coup

    Args:
        grille (_type_): doit afficher la grille à chaque coup
    """

    for cle in grille:
        for elt in grille[cle]:
            print("|", elt, "|" , end="")
        print("\n") # gére l'espace
    return grille





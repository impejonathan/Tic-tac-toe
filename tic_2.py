grille = {
    1:[None, None, None],
    2:[None, None, None],
    3:[None, None, None]
        }

# for cle in dico:
#     for elt in dico[cle]:
#         print("|", elt, "|" , end="")
#     print("\n")


# //////////////// debut affichage de la griller  ////////////////
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

# afficher_grille(grille)

#/////////// jouer le coup  ////////////////

# coup = input("coup:",[],[])

# valeur_user = input("coup:",grille,[],[])

     
# ////////////  2eme partie fonction  jouer_coup
def jouer_coup(grille,coup,i,j):
    
    """cette fonction joue le coup dans le dictionnaire

    Args:
        coup (_type_): coup a jouer x ou o
        i (_type_): que dico viser
        j (_type_): la position dans le dico

    Returns:
        _type_: _description_
    """
    # var_coup_jouer = input("jouer son coup " )
    
    if grille[i][j-1]==None:
        grille[i][j-1]=coup
    else:
        print("coup deja jouer")
        
    # print(var_coup_jouer)        
    return afficher_grille (grille)
    

    
    
    
    
    
# /////////////// fin test de la grille  ////////////////
def test_gagne(grille):
    """on test si la grille et gagnante 

    Args:
        grille (_type_): recupére la grille 

    Returns:
        _type_: dit comment le joueur à gagner 
    """
    for i in range(1,4):
        if grille[i][0]== grille[i][1]== grille[i][2] and grille[i][2]!=None:
            print("c'est gagnant par linge")

    for j in range(3):
        if grille[1][j]==grille[2][j]==grille[3][j] and grille[3][j]!=None:
            print("c'est gagnant par colone")

    if (grille[1][0]==grille[2][1]==grille[3][2] and grille[3][2]!=None) or (grille[1][2]==grille[2][1]==grille[3][0] and grille[3][2]!=None):
        print("c'est gagnant par diagonale")
    return False


terminer = False
joureur ="j"

while not terminer:
    # afficher_grille(grille)
    coup_X=" X "
    coup_O = "O"
    # coup=input("jouer forme X ou O:  ")
    coup_line= int(input('position ligne:  '))
    if coup_line > 3:
        print("le chiffre doit etre entre 1 et 3")
    coup_colonne= int(input('position collone:  '))
    if coup_colonne > 3:
        print("le chiffre doit etre entre 1 et 3 ")
    jouer_coup(grille,coup_X,coup_line,coup_colonne)
    
    test_gagne(grille)
    
    



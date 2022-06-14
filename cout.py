# Fonction de coût
from array import array

def f(entrees,parametres) -> array:
    return [0.8, 0.2, 0.1] 

# Cout
def Cout(entrees : array,
         sorties_desirees : array,
         parametres : array) -> float:

    sorties_produites = f(entrees,parametres)
    cout = 0
    for j in range(len(sorties_desirees)):
        cout= cout+ (sorties_desirees[j]-sorties_produites[j])**2
    return cout    

# Transcode 
#   - de la représentation en caractère
#   - vers du mumérique (0,1)
def Transcode(image : array) -> array:
    lignes, colonnes = len(image), len(image[0])
    image_numerique = [[0]*lignes for _ in range(colonnes)]
    l = 0
    for ligne in image:
        c = 0
        for caractere in ligne:
            if caractere == ' ':
                v = 0
            else:
                v = 1     
            image_numerique[l][c] = v;
            c= c+1
        l= l+1    
    return image_numerique;        

# Affiche une image ligne à ligne
def affiche_image(etiquette : str, 
                  image : array):
    print(etiquette)
    for ligne in image:
        print("    ", ligne)
    
# affiche un texte sousligné    
def affiche_ligne(texte : str) ->None:
    ligne = "";
    for c in texte:
        ligne = ligne + "="
    print ("")    
    print (ligne)   
    print(texte)
    print(ligne)   
    print ("")

# Images lisibles ("+" ou "-")  
c1= Transcode([
        #01234
        "  |  ", # 0
        "  |  ", # 1
        "  |  ", # 2 
        "  |  ", # 3 
        "  |  "  # 4
    ])

c2= Transcode([
        ".-.  ",
        "| |  ",
        "  |  ",
        "  |  ",
        "  +--"
    ])

c3= Transcode([
        "----.",
        "    |",
        "  --+",
        "    |",
        "----."
    ])

affiche_ligne("Fonction de coût")
print("Images à reconnaitre:")
affiche_image('1', c1)
affiche_image('2', c2)
affiche_image('3', c3)

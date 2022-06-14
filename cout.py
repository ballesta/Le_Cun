# Fonction de cout
from array import array

def f(entrees,parametres) -> array:
    return [0.8, 0.2, 0.1] 

def Cout(entrees,sorties_desirees,parametres):
    sorties_produites = f(entrees,parametres)
    cout = 0
    for j in range(len(sorties_desirees)):
        cout= cout+ (sorties_desirees[j]-sorties_produites[j])**2
    return cout    

def Transcode(image) -> array:
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

def affiche_image(etiquette : str, 
                  image : array):
    print(etiquette)
    for ligne in image:
        print(ligne)
    
def affiche(texte : str) ->None:
    print(texte)
    for c in texte:
        print ('=',end='')
    print ('\n')   

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

affiche("Fonction de cout")
print("Images à reconnaitre")
affiche_image('1', c1)
affiche_image('2', c2)
affiche_image('3', c3)

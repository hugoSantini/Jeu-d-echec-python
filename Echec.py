ligne = [8,7,6,5,4,3,2,1]

colonne = ['a','b','c','d','e','f','g','h']

plateauCase = [
    'a8','b8','c8','d8','e8','f8','g8','h8',
    'a7','b7','c7','d7','e7','f7','g7','h7',
    'a6','b6','c6','d6','e6','f6','g6','h6',
    'a5','b5','c5','d5','e5','f5','g5','h5',
    'a4','b4','c4','d4','e4','f4','g4','h4',
    'a3','b3','c3','d3','e3','f3','g3','h3',
    'a2','b2','c2','d2','e2','f2','g2','h2',
    'a1','b1','c1','d1','e1','f1','g1','h1'
    ]

plateauCaseToCoord = {
    'a8' : [1,8] ,'b8' : [2,8] ,'c8' : [3,8] ,'d8' : [4,8] ,'e8' : [5,8] ,'f8' : [6,8] ,'g8' : [7,8] ,'h8' : [8,8] ,
    'a7' : [1,7] ,'b7' : [2,7] ,'c7' : [3,7] ,'d7' : [4,7] ,'e7' : [5,7] ,'f7' : [6,7] ,'g7' : [7,7] ,'h7' : [8,7] ,
    'a6' : [1,6] ,'b6' : [2,6] ,'c6' : [3,6] ,'d6' : [4,6] ,'e6' : [5,6] ,'f6' : [6,6] ,'g6' : [7,6] ,'h6' : [8,6] ,
    'a5' : [1,5] ,'b5' : [2,5] ,'c5' : [3,5] ,'d5' : [4,5] ,'e5' : [5,5] ,'f5' : [6,5] ,'g5' : [7,5] ,'h5' : [8,5] ,
    'a4' : [1,4] ,'b4' : [2,4] ,'c4' : [3,4] ,'d4' : [4,4] ,'e4' : [5,4] ,'f4' : [6,4] ,'g4' : [7,4] ,'h4' : [8,4] ,
    'a3' : [1,3] ,'b3' : [2,3] ,'c3' : [3,3] ,'d3' : [4,3] ,'e3' : [5,3] ,'f3' : [6,3] ,'g3' : [7,3] ,'h3' : [8,3] ,
    'a2' : [1,2] ,'b2' : [2,2] ,'c2' : [3,2] ,'d2' : [4,2] ,'e2' : [5,2] ,'f2' : [6,2] ,'g2' : [7,2] ,'h2' : [8,2] ,
    'a1' : [1,1] ,'b1' : [2,1] ,'c1' : [3,1] ,'d1' : [4,1] ,'e1' : [5,1] ,'f1' : [6,1] ,'g1' : [7,1] ,'h1' : [8,1]
}

plateauCoord = [
    [1,8],[2,8],[3,8],[4,8],[5,8],[6,8],[7,8],[8,8],
    [1,7],[2,7],[3,7],[4,7],[5,7],[6,7],[7,7],[8,7],
    [1,6],[2,6],[3,6],[4,6],[5,6],[6,6],[7,6],[8,6],
    [1,5],[2,5],[3,5],[4,5],[5,5],[6,5],[7,5],[8,5],
    [1,4],[2,4],[3,4],[4,4],[5,4],[6,4],[7,4],[8,4],
    [1,3],[2,3],[3,3],[4,3],[5,3],[6,3],[7,3],[8,3],
    [1,2],[2,2],[3,2],[4,2],[5,2],[6,2],[7,2],[8,2],
    [1,1],[2,1],[3,1],[4,1],[5,1],[6,1],[7,1],[8,1],
]

pieces = {
    'a8' : ['Tour','Noir'],'b8' : ['Cavalier','Noir'],'c8' : ['Fou','Noir'],'d8' : ['Dame','Noir'],'e8' : ['Roi','Noir'],'f8' : ['Fou','Noir'],'g8' : ['Cavalier','Noir'],'h8' : ['Tour','Noir'],
    'a7' : ['Pion','Noir'],'b7' : ['Pion','Noir'],'c7' : ['Pion','Noir'],'d7' : ['Pion','Noir'],'e7' : ['Pion','Noir'],'f7' : ['Pion','Noir'],'g7' : ['Pion','Noir'],'h7' : ['Pion','Noir'],
    'a6' : ['null','null'],'b6' : ['null','null'],'c6' : ['null','null'],'d6' : ['null','null'],'e6' : ['null','null'],'f6' : ['null','null'],'g6' : ['null','null'],'h6' : ['null','null'],
    'a5' : ['null','null'],'b5' : ['null','null'],'c5' : ['null','null'],'d5' : ['null','null'],'e5' : ['null','null'],'f5' : ['null','null'],'g5' : ['null','null'],'h5' : ['null','null'],
    'a4' : ['null','null'],'b4' : ['null','null'],'c4' : ['null','null'],'d4' : ['null','null'],'e4' : ['null','null'],'f4' : ['null','null'],'g4' : ['null','null'],'h4' : ['null','null'],
    'a3' : ['null','null'],'b3' : ['null','null'],'c3' : ['null','null'],'d3' : ['null','null'],'e3' : ['Pion','Pion'],'f3' : ['null','null'],'g3' : ['null','null'],'h3' : ['null','null'],
    'a2' : ['Pion','Blanc'],'b2' : ['Pion','Blanc'],'c2' : ['Pion','Blanc'],'d2' : ['Pion','Blanc'],'e2' : ['null','null'],'f2' : ['Pion','Blanc'],'g2' : ['Pion','Blanc'],'h2' : ['Pion','Blanc'],
    'a1' : ['Tour','Blanc'],'b1' : ['Cavalier','Blanc'],'c1' : ['Fou','Blanc'],'d1' : ['Dame','Blanc'],'e1' : ['Roi','Blanc'],'f1' : ['Fou','Blanc'],'g1' : ['Cavalier','Blanc'],'h1' : ['Tour','Blanc']
    }
class couleur :
    gris = '\033[1;37;40m'
    noir = '\033[1;30;39m'
    rouge = '\033[1;31;40m'

strligne=['8 ','7 ','6 ','5 ','4 ','3 ','2 ','1 ','+ a b c d e f g h ']

vecteurs = {
    'tour' : [[1,0],[0,1],[-1,0],[0,-1]],
    'fou' : [[1,1],[1,-1],[-1,1],[-1,-1]],
    'roi' : [[1,1],[1,-1],[-1,1],[-1,-1],[1,0],[0,1],[-1,0],[0,-1]],
    'dame' : [[1,1],[1,-1],[-1,1],[-1,-1],[1,0],[0,1],[-1,0],[0,-1]],
    'cavalier' : [[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1]],
    'pionNmange' : [[-1,-1],[1,-1]],
    'pionNdouble' : [[0,-2]],
    'pionNsimple' : [[0,-1]],
    'pionBmange' : [[1,1],[-1,1]],
    'pionBdouble' : [[0,2]],
    'pionBsimple' : [[0,1]]
}
def strligneReset ():
    '''
    Permet de reset le tableau 'strligne'
    '''
    strligne = ['\033[1;31;40m8 ','\033[1;31;40m7 ','\033[1;31;40m6 ','\033[1;31;40m5 ','\033[1;31;40m4 ','\033[1;31;40m3 ','\033[1;31;40m2 ','\033[1;31;40m1 ','\033[1;31;40m+ a b c d e f g h \033[7;37;40m']
    return strligne

def getColor(case):
    '''
    Argument :
        Case : "a-h|1-8"
    Return : Couleur de la case
    '''
    return pieces[case][1]

def printerDamier(strligne):
    '''
    Argument :
        strligne : Tableau du même nom
    Affiche le tableau, ligne par ligne.
    '''
    strDamier = ''
    for i in range (0,9):
        strDamier += strligne[i]+'\n'
    return strDamier

def outCase(case):
    '''
    Argument :
        Case : "a-h|1-8"
    Return : La première lettre du nom de la pièce dans la couleur de cette dernière
    '''
    color = getColor(case)
    if pieces[case][0][0] != 'n' and color == 'Blanc':
        x = couleur.gris + pieces[case][0][0] + ' ' + couleur.rouge
    elif pieces[case][0][0] != 'n' and color == 'Noir':
        x = couleur.noir + pieces[case][0][0] + ' ' + couleur.rouge
    else :
        x = '- '
    return x

def affichage():
    '''
    Fonction général qui affiche le damier et les pièces
    '''
    strligne = strligneReset()
    for i in range (0,8):
        iChar = ligne[i]
        for j in range (0,8):
            jChar = colonne[j]
            strCase = str(jChar) + str(iChar)
            strligne[i] += outCase(strCase)
    return printerDamier(strligne)
#Module "Jeu" :

from random import *

def movePiece(caseDepart,caseArrivée):
    '''
    Fonction permetant de déplacer une piece sur l'echequier.
    Argument : caseDepart ("a-h|1-8")
               caseArrivée ("a-h|1-8")
    '''
    global pieces
    pieces[caseArrivée][0] = pieces[caseDepart][0]
    pieces[caseArrivée][1] = pieces[caseDepart][1]
    pieces[caseDepart][0] = 'null'
    pieces[caseDepart][1] = 'null'

def getCaseFromCoord (coord):
    '''
    Fonction qui donne la case en fonction d'une coordonnée.
    Argument : coord ([1-8;1-8])
    Return : case ("a-h|1-8")
    '''
    return plateauCase[plateauCoord.index(coord)]

def newCoord(oldCoord, vecteur):
    return [oldCoord[0]+vecteur[0],oldCoord[1]+vecteur[1]]

def presence(case):
    '''
    Fonction testant la présence ou non du piece sur un case donné.
    '''
    if case not in pieces :
        return 2
    if pieces[case][0][0] != 'n':
        return 1
    return 0
def analyseTour(case,couleur):
    '''
    Argument
        case : Forme lettreChiffre (ex : a2, h5...)
        couleur : Couleur de la piece a jouer('Blanc'|'Noir')
    Return : La table des cases d'arrivé possible pour la pièces initiale
    '''
    tabAnalyseTour = []
    coordIni = plateauCaseToCoord[case]
    for vecteur in vecteurs['tour']:
        coordVec = newCoord(coordIni,vecteur)
        if coordVec in plateauCoord:
            while coordVec in plateauCoord and presence(getCaseFromCoord(coordVec)) == 0 :
                tabAnalyseTour.append(getCaseFromCoord(coordVec))
                coordVec = newCoord(coordVec,vecteur)
            if coordVec in plateauCoord and presence(getCaseFromCoord(coordVec)) == 1:
                if getColor(getCaseFromCoord(coordVec)) != couleur:
                    tabAnalyseTour.append(getCaseFromCoord(coordVec))
    return tabAnalyseTour

def analyseFou(case,couleur):
    '''
    Argument
        case : Forme lettreChiffre (ex : a2, h5...)
        couleur : Couleur de la piece a jouer('Blanc'|'Noir')
    Return : La table des cases d'arrivé possible pour la pièces initiale
    '''
    tabAnalyseFou = []
    coordIni = plateauCaseToCoord[case]
    for vecteur in vecteurs['fou']:
        coordVec = newCoord(coordIni,vecteur)
        if coordVec in plateauCoord:
            while coordVec in plateauCoord and presence(getCaseFromCoord(coordVec)) == 0 :
                tabAnalyseFou.append(getCaseFromCoord(coordVec))
                coordVec = newCoord(coordVec,vecteur)
            if coordVec in plateauCoord and presence(getCaseFromCoord(coordVec)) == 1:
                if getColor(getCaseFromCoord(coordVec)) != couleur:
                    tabAnalyseFou.append(getCaseFromCoord(coordVec))
    return tabAnalyseFou


def analyseDame(case,couleur):
    '''
    Argument
        case : Forme lettreChiffre (ex : a2, h5...)
        couleur : Couleur de la piece a jouer('Blanc'|'Noir')
    Return : La table des cases d'arrivé possible pour la pièces initiale
    '''
    tabAnalyseDame = []
    coordIni = plateauCaseToCoord[case]
    for vecteur in vecteurs['dame']:
        coordVec = newCoord(coordIni,vecteur)
        if coordVec in plateauCoord:
            while coordVec in plateauCoord and presence(getCaseFromCoord(coordVec)) == 0 :
                tabAnalyseDame.append(getCaseFromCoord(coordVec))
                coordVec = newCoord(coordVec,vecteur)
            if coordVec in plateauCoord and presence(getCaseFromCoord(coordVec)) == 1:
                if getColor(getCaseFromCoord(coordVec)) != couleur:
                    tabAnalyseDame.append(getCaseFromCoord(coordVec))
    return tabAnalyseDame


def analyseRoi(case,couleur):
    '''
    Argument
        case : Forme lettreChiffre (ex : a2, h5...)
        couleur : Couleur de la piece a jouer('Blanc'|'Noir')
    Return : La table des cases d'arrivé possible pour la pièces initiale
    '''
    tabAnalyseRoi = []
    coordIni = plateauCaseToCoord[case]
    for vecteur in vecteurs['roi']:
        coordVec = newCoord(coordIni,vecteur)
        if coordVec in plateauCoord and presence(getCaseFromCoord(coordVec)) == 0 :
            tabAnalyseRoi.append(getCaseFromCoord(coordVec))
        if newCoord(coordVec,vecteur) in plateauCoord and presence(getCaseFromCoord(newCoord(coordVec,vecteur))) == 1:
                if getColor(getCaseFromCoord(coordVec)) != couleur:
                    tabAnalyseRoi.append(getCaseFromCoord(coordVec))
    return tabAnalyseRoi


def analysePion(case,couleur):
    '''
    Argument
        case : Forme lettreChiffre (ex : a2, h5...)
        couleur : Couleur de la piece a jouer('Blanc'|'Noir')
    Return : La table des cases d'arrivé possible pour la pièces initiale
    '''

    tabAnalysePion = []
    coordIni = plateauCaseToCoord[case]
    if couleur == 'Noir':

        coordVec = newCoord(coordIni,vecteurs['pionNdouble'][0])
        if case[1] == '7' and presence(getCaseFromCoord(coordVec)) == 0:
            tabAnalysePion.append(getCaseFromCoord(coordVec))

        coordVec = newCoord(coordIni,vecteurs['pionNsimple'][0])
        if coordVec in plateauCoord and presence(getCaseFromCoord(coordVec)) == 0:
            tabAnalysePion.append(getCaseFromCoord(coordVec))

        for vecteur in vecteurs['pionNmange']:
            coordVec = newCoord(coordIni,vecteur)
            if coordVec in plateauCoord and presence(getCaseFromCoord(coordVec)) == 1:
                if getColor(getCaseFromCoord(coordVec)) != couleur:
                    tabAnalysePion.append(getCaseFromCoord(coordVec))

    if couleur == 'Blanc':
        coordVec = newCoord(coordIni,vecteurs['pionBdouble'][0])
        if case[1] == '2' and presence(getCaseFromCoord(coordVec)) == 0:
            tabAnalysePion.append(getCaseFromCoord(coordVec))

        coordVec = newCoord(coordIni,vecteurs['pionBsimple'][0])
        if coordVec in plateauCoord and presence(getCaseFromCoord(coordVec)) == 0:
            tabAnalysePion.append(getCaseFromCoord(coordVec))

        for vecteur in vecteurs['pionBmange']:
            coordVec = newCoord(coordIni,vecteur)
            if coordVec in plateauCoord and presence(getCaseFromCoord(coordVec)) == 1:
                if getColor(getCaseFromCoord(coordVec)) != couleur:
                    tabAnalysePion.append(getCaseFromCoord(coordVec))

    return tabAnalysePion


def analyseCavalier(case,couleur):
    '''
    Argument
        case : Forme lettreChiffre (ex : a2, h5...)
        couleur : Couleur de la piece a jouer('Blanc'|'Noir')
    Return : La table des cases d'arrivé possible pour la pièces initiale
    '''
    tabAnalyseCavalier = []
    coordIni = plateauCaseToCoord[case]
    for vecteur in vecteurs['cavalier']:
        coordVec = newCoord(coordIni,vecteur)
        if coordVec in plateauCoord and presence(getCaseFromCoord(coordVec)) == 0 :
            tabAnalyseCavalier.append(getCaseFromCoord(coordVec))
        if newCoord(coordVec,vecteur) in plateauCoord and presence(getCaseFromCoord(newCoord(coordVec,vecteur))) == 1:
                if getColor(getCaseFromCoord(coordVec)) != couleur:
                    tabAnalyseCavalier.append(getCaseFromCoord(coordVec))
    return tabAnalyseCavalier

def getType(case):
    '''
    Argument :
        Case : Case ciblé
    Return : Le type de piece sur la case demandé
    '''
    return pieces[case][0]

def possibleMoves(typePiece,case,couleurPiece):
    '''
    Retourne le tableaux de la fonction d'analyse de la fonction correspondante.
    '''
    if typePiece == 'Fou':
        return analyseFou(case,couleurPiece)
    elif typePiece == 'Tour':
        return analyseTour(case,couleurPiece)
    elif typePiece == 'Dame':
        return analyseDame(case,couleurPiece)
    elif typePiece == 'Roi':
        return analyseRoi(case,couleurPiece)
    elif typePiece == 'Cavalier':
        return analyseCavalier(case,couleurPiece)
    elif typePiece == 'Pion':
        return analysePion(case,couleurPiece)

def gameTurn(turnNumber,colorPlayer, colorBot):
    '''
    Fonction général qui initialise un tour de jeu :
    Argument :
        turnNumber = Numéro du tour (if : Pair = Noir de joué | else | Impair = Blanc de joué)
        colorPlayer : Couleur jouer par l'humain('Blanc'|'Noir')
        colorBot : Couleur jouer par le bot('Blanc'|'Noir')
    Return : True si il n'y a plus qu'un roi sur le plateau.

    '''
    countRoi = 0
    for case in plateauCase:
        if pieces[case][0] == 'Roi':
            countRoi += 1
    if countRoi == 1:
        for case in plateauCase:
            if pieces[case][0] == 'Roi':
                couleurWin = pieces[case][1]
                print ("\n\n\n\n\n\nLes "+ couleurWin + "s ont gagné")
                return False

    if turnNumber % 2 == 0 :
        colorToPlay = 'Blanc'
    else :
        colorToPlay = 'Noir'
    if colorPlayer == colorToPlay :
        humanTurn(colorPlayer)
    else :
        botTurn(colorBot)
    return True

def humanTurn(colorPlayer):
    '''
    Déroule les instructions et fonctions à éxécuter pour le tour de l'"humain"
    '''
    stringAff = "La case du pion de départ : \n" + affichage()+ '\n'
    caseDep = input(stringAff)
    while caseDep not in plateauCase:
        caseDep = input('Veuillez re-rentrer la case de départ : \n' + affichage())
    piece = getType(caseDep)
    moves = possibleMoves(piece,caseDep,colorPlayer)
    print(moves)
    while (moves == [] or moves == None) or ((moves == [] or moves == None) and caseDep not in plateauCase and piece != 'null' and moves != [] and pieces[caseDep][1] != colorPlayer):
        print('inboucle')
        caseDep = input('Veuillez re-rentrer la case de départ : \n' + affichage())
        if caseDep in plateauCase:
            piece = getType(caseDep)
            moves = possibleMoves(piece,caseDep,colorPlayer)
    caseArv = input(affichage() + 'Sur quel case voulez-vous déplacé la piece en '+ caseDep +': ' + str(moves) + ' ')
    while caseArv not in moves:
        caseArv = input("Sur quel case voulez-vous déplacer la pièce: " + str(moves))
        if caseArv == 'Stop':
            humanTurn(colorPlayer)
    movePiece(caseDep,caseArv)

def botTurn(colorBot):
    '''
    Déroule les instructions et fonctions à éxécuter pour le tour du bot
    '''
    listeCasePiece = []
    for i in plateauCase:
        if pieces[i][1] == colorBot:
            listeCasePiece.append(i)
    case = listeCasePiece[randint(0,len(listeCasePiece)-1)]
    piece = getType(case)
    tabDeplacement = possibleMoves(piece,case,colorBot)
    print(tabDeplacement)
    while tabDeplacement == []:
        case = listeCasePiece[randint(0,len(listeCasePiece)-1)]
        piece = getType(case)
        tabDeplacement = possibleMoves(piece,case,colorBot)
    depChoice = tabDeplacement[randint(0,len(tabDeplacement)-1)]
    movePiece(case,depChoice)
    print(affichage()+'Le bot a déplacé '+case+' en '+depChoice)

def resetBoard():
    '''
    Return : Le tableau 'pieces' avec les pieces à leur positions de initiale.
    '''
    global pieces
    pieces = {
        'a8' : ['Tour','Noir'],'b8' : ['Cavalier','Noir'],'c8' : ['Fou','Noir'],'d8' : ['Dame','Noir'],'e8' : ['Roi','Noir'],'f8' : ['Fou','Noir'],'g8' : ['Cavalier','Noir'],'h8' : ['Tour','Noir'],
        'a7' : ['Pion','Noir'],'b7' : ['Pion','Noir'],'c7' : ['Pion','Noir'],'d7' : ['Pion','Noir'],'e7' : ['Pion','Noir'],'f7' : ['Pion','Noir'],'g7' : ['Pion','Noir'],'h7' : ['Pion','Noir'],
        'a6' : ['null','null'],'b6' : ['null','null'],'c6' : ['null','null'],'d6' : ['null','null'],'e6' : ['null','null'],'f6' : ['null','null'],'g6' : ['null','null'],'h6' : ['null','null'],
        'a5' : ['null','null'],'b5' : ['null','null'],'c5' : ['null','null'],'d5' : ['null','null'],'e5' : ['null','null'],'f5' : ['null','null'],'g5' : ['null','null'],'h5' : ['null','null'],
        'a4' : ['null','null'],'b4' : ['null','null'],'c4' : ['null','null'],'d4' : ['null','null'],'e4' : ['null','null'],'f4' : ['null','null'],'g4' : ['null','null'],'h4' : ['null','null'],
        'a3' : ['null','null'],'b3' : ['null','null'],'c3' : ['null','null'],'d3' : ['null','null'],'e3' : ['null','null'],'f3' : ['null','null'],'g3' : ['null','null'],'h3' : ['null','null'],
        'a2' : ['Pion','Blanc'],'b2' : ['Pion','Blanc'],'c2' : ['Pion','Blanc'],'d2' : ['Pion','Blanc'],'e2' : ['Pion','Blanc'],'f2' : ['Pion','Blanc'],'g2' : ['Pion','Blanc'],'h2' : ['Pion','Blanc'],
        'a1' : ['Tour','Blanc'],'b1' : ['Cavalier','Blanc'],'c1' : ['Fou','Blanc'],'d1' : ['Dame','Blanc'],'e1' : ['Roi','Blanc'],'f1' : ['Fou','Blanc'],'g1' : ['Cavalier','Blanc'],'h1' : ['Tour','Blanc']
    }
    return pieces

def selectColor():
    '''
    Demande au joueur la couleur qu'il veut jouer
    '''
    colorPlayer = input("Quel couleur voulez-vous jouez ? ('Blanc'/'Noir') : ")
    while colorPlayer != 'Blanc' and colorPlayer != 'Noir':
        colorPlayer = input("Veuillez re-rentré votre couleur ('Blanc'/'Noir') : ")
    if colorPlayer == 'Blanc':
        colorBot = 'Noir'
    else :
        colorBot = 'Blanc'
    return colorPlayer,colorBot

def lauchGame():
    '''
    Fonction général qui lance le jeu
    '''
    pieces = resetBoard()
    colorPlayer, colorBot = selectColor()
    print('Vous avez choisi la couleur', colorPlayer)
    turnNumber = 1
    fin = True
    while fin:
        turnNumber += 1
        fin = gameTurn(turnNumber, colorPlayer, colorBot)


lauchGame()

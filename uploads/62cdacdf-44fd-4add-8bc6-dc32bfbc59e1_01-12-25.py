""" 01-12-25

"""
from arbres_binaires import *

D = {1: 'r',
     2: 'a', 3: 'b',
     4: 'c', 5: 'd', 6: 'e', 7:'f',
     9: 'h', 10: 'i', 11: 'j', 12: 'k',
     22: 'm'}


def parcours_largeur(N):
    res = []
    file = [N]
    while file != []:
        N1 = file.pop()
        res.append(N1.v)
        if N1.fg != None:
            file.insert(0, N1.fg)
        if N1.fd != None:
            file.insert(0, N1.fd)
    return res


""" Afficher m à partir de r """
r = Noeud('r')
r.insere_g('a')
r.insere_d('b')
r.fg.insere_g('c')
r.fg.insere_d('d')
r.fd.insere_g('e')
r.fd.insere_d('f')
r.fg.fg.insere_d('h')
r.fg.fd.insere_g('i')
r.fg.fd.insere_d('j')
r.fd.fg.insere_g('k')
r.fg.fd.fd.insere_g('m')
print(parcours_largeur(r))

r1 = r.copie()
print(parcours_largeur(r1))
# r.arbre_schema()


""" b) """
def complete(N):
    N1 = N.copie()
    h = N.hauteur()
    file = [(N1, 1)]

    while file != []:
        noeud, profondeur = file.pop()
        if profondeur < h:
            if noeud.fg != None:
                file.insert(0, (noeud.fg, profondeur + 1))
            else:
                noeud.fg = Noeud('None')
                file.insert(0, (noeud.fg, profondeur + 1))
            if noeud.fd != None:
                file.insert(0, (noeud.fd, profondeur + 1))
            else:
                noeud.fd = Noeud('None')
                file.insert(0, (noeud.fd, profondeur + 1))
    return N1
N1 = complete(r)
# N1.arbre_schema()

def descendant(i, r):
    while i > r:
        i = i // 2
        if i == r:
            return True
    return False

for i in range(56):
    print(i, descendant(i, 6))


def coherence_cles(dic):
    r = min(dic.keys())
    for cle in dic:
        if cle != r and not cle // 2 in dic:
            return False
    return True

print(coherence_cles({1: 1, 2: 1, 5: 1}))

def racine(dic):
    dic1 = {}
    r = min(dic)
    for cle in dic:
        dic1[cle] = Noeud(dic[cle])
    for cle in dic:
        if cle%2 == 0 and cle != r:
            dic1[cle // 2].insere_g(dic1[cle].v)
            dic1[cle] = dic1[cle // 2].fg
        elif cle != r:
            dic1[cle // 2].insere_d(dic1[cle].v)
            dic1[cle] = dic1[cle // 2].fd
    return dic1[r]
d = {1: 'a', 2: 'b', 5: 'c'}
r1 = racine(d)
# r1.arbre_schema()

def prefixe(N):
    if N != None:
        print(N.v)
        prefixe(N.fg)
        prefixe(N.fd)

prefixe(r)

def infixe(N):
    if N != None:
        infixe(N.fg)
        print(N.v)
        infixe(N.fd)
print('**************')

infixe(r)

def suffixe(N):
    if N != None:
        suffixe(N.fg)
        suffixe(N.fd)
        print(N.v)

print('**************')

suffixe(r)




""" pour demain écrire les trois codes pour renvoyer une liste :
    en variable globale
    en paramètre """










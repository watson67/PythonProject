

#Question 1

def est_pair(n):
    if n % 2 == 0:
        return True
    else :
        return False

def affichage_chaine(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    if l1>l2:
        print(s1)
    elif(l2>l1):
        print(s2)
    else:
        print(s1)
        print(s2)


def fibonnacci_reccursive(n):
    if n==0:
        return 0
    elif n == 1 :
        return 1
    else :
        return fibonnacci_reccursive(n-1) + fibonnacci_reccursive(n-2)

def fibonnacci(n):
    a=0
    c=0
    b=1
    for i in range(2,n+1):
        c=a+b
        a=b
        b=c
    return c

def nom(string):
    string_final=[]
    count = 0
    for i in range(0,len(string)):
        if i == 0 and string[i].islower():
            string_final.append(string[i].upper())
            count +=1

        elif string[i].isupper():
            string_final.append(string[i].lower())
            count +=1
        
        else:
           string_final.append(string[i]) 
    s="".join(string_final)
    if s == string :
        print("Aucune ligne modifiée")
    else : 
        print(s)
        print("Il y a ", count, " caractères modifiés")

import numpy as np

def recherche(liste, n):
    if n in liste:
        print("Le nombre n se trouve ", liste.count(n) , " fois dans la liste")
        index = np.where(liste==n)
        print("les index sont : ", index)
    else:
        print("Ne se trouve pas dans la liste")

lst=[1,2,3,4,2,5,8]
recherche(lst,2)
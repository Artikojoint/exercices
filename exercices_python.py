#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Exercice 1
def diviseurs(n):
    div = [1]
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            div.append(int(i))
            if n/i != i:
                div.append(int(n/i))
    return div

diviseurs(1864864548684682)

def nombres_parfaits(n):
    np = []
    for i in range(1,n+1):
        if sum(diviseurs(i)) == i:
            np.append(i)
    return np

nombres_parfaits(100000)

def nombres_amicaux(n):
    na = []
    nb = []
    for i in range(1,n+1):
        if i not in nb:
            ami = sum(diviseurs(i))
            if sum(diviseurs(ami)) == i and i!=ami:
                na.append(str(i)+" et "+str(ami))
                nb.append(i)
                nb.append(ami)
    return na

nombres_amicaux(100000)

# Exercice 2

def premier(n):
    if n in [0,1]:
        return False
    if len(diviseurs(n))==1:
        return True
    else:
        return False

premier(7)

def chanceux(n):
    ch=[]
    for i in range(2,n+1):
        chance = True
        for k in range(0,i-1):
            if chance:
                calc = i + k**2 + k
                if not(premier(calc)):
                    chance = False
        if chance:
            ch.append(i)
    return ch

chanceux(1000)

# Exercice 3

def entier(n):
    if n-int(n)==0:
        return True
    else:
        return False
    
entier(3.00001)

def taxi(n):
    tn = []
    for i in range(2,n+1):
        couples = []
        for k in range(1,int((i/2)**(1/3))+1):
            for m in range(k,int(i**(1/3))+1):
                if k**3 + m**3 == i and k!=m and k not in couples and m not in couples:
                    couples.append(k)
                    couples.append(m)
        if len(couples) >=4:
            print (i,couples)
            tn.append(i)
    return tn
            
def taxicab(N):
    n=int(N**(1/3))
    liste = []
    for i in range(1,n+1):
        a=i**3
        for j in range(i+1,n+1):
            s=a+j**3
            if s<=N:
                for k in range(i+1,n+1):
                    b=k**3
                    for l in range(k+1,n+1):
                        if s==b+l**3:
                            liste.append([s,[i,j],[k,l]])
    return liste


taxi(25000)
taxicab(1000000)


# Exercice 4

def conway(n):
    suite = ["1"]
    for i in range(1,n+1):
        terme_pre = str(suite[i-1])
        combo = 1
        terme = terme_pre[0]
        terme_suiv = ""
        # terme_suivant = str(terme)
        for k in range(1,len(terme_pre)):
            if terme_pre[k]==terme:
                combo += 1
            else:
                for c in range(combo):
                    terme_suiv += terme
                terme = terme_pre[k]
                combo = 1
        suite.append(terme_suiv)
    return suite

#def suivant_conway(n):
#    mot = str(n)
#    mot_suivant = ""
#    i = 0
#    while i < len(mot):
#        j=l
        # à continuer
        

#conway(5)
                    
                
            
        
        
        
                


















            
            





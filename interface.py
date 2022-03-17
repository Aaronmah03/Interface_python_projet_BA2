import turtle as t
import tkinter as tk
import numpy as np
import math as m
'''
#ATTENTION TJRS RETIRER LES 'XY' DE LA PREMIERE LIGNE DU CSV
import matplotlib.pyplot as plt
import numpy as np
x,y= np.loadtxt('cercle_carre.csv', delimiter=',', unpack=True)
plt.plot(x,y, marker='.',markersize=1)
plt.title('Vérification du CSV')
plt.show()

liste=['cercle_carre','coo_cp','coo_test','CP_1!TRAIT_400','trois_lignes']
t.write('Les fichiers disponibles sont; \n cercle_carre \n coo_cp \n coo_test \n CP_1!TRAIT_400 \n trois_lignes')
nom=t.textinput('Tracage','choisis ta forme')
while nom not in liste and not nom=='STOP':
    t.up()
    t.goto(-100,-100)
    t.down()
    t.write('Le fichier que vous rechercher n\'existe pas \n Veillez à l\'orthographe du nom du fichier')
    nom = t.textinput('Tracage', 'choisis ta forme')
'''
from tkinter import *

import tkinter as tk
from tkinter import ttk

# Dico Lettres
list_lettres = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
list_formes = ['Cercle','Triangle','Carré','Pentagone','Hexagone']
list_bonus = ['Polytech','carapils','cara_5000','Pendu','Stickman de Vitruve']



def enhaut(a):
    neg=0
    if a=='B' or a=='H':
        neg=1
    else :
        neg=-1
    return neg
def cote(a):
    if a=='V':
        neg=1
    else :
        neg=1
    return neg
def B(a):
    if a=='B_1':
        pas=100
    return pas
def recentrerxC(a):
    if a=='C':
        b=150
    elif a=='E'or a=='U' or a=='V'or a=='W':
        b=150
    elif a=='A':
        b=0
    elif a=='I':
        b=20
    elif a=='X':
        b=-80
    elif a=='G' :
        b=100
    elif a=='H'or a=='Q' :
        b=130
    elif a=='J':
        b=190
    elif a=='K' or a=='L':
        b=190
    elif a=='O' or a=='S' :
        b=80
    elif a=='R':
        b=130
    else:
        b=0
    return b
def recentreryC(a):
    if a=='C':
        b=80
    elif a=='D':
        b=130
    elif a=='G' or a=='S':
        b=120
    elif a=='J'or a=='U' or a=='V' or a=='W' or a=='X' or a=='Y' or a=='Z' or a=='I':
        b=250
    elif a=='Q':
        b=20
    else:
        b=0
    return b
# New window
def newWindow(name,a,liste):
    newwin = Toplevel(root)
    newwin.title(name)
    newwin.geometry("1000x600")
    exit(newwin)
    a(newwin,liste)
def Newwin(name):
    newwin = Toplevel(root)
    newwin.title(name)
    newwin.geometry("1000x600")
    exit(newwin)
# exit button
def buttons(place,liste):
    x = 100
    y = 100
    for i in range(len(liste)):

        button = ttk.Button(
            place,
            text= liste[i],
            command= lambda i=liste[i] : ouverture(i)
        )

        button.pack(
            ipadx=5,
            ipady=5,
            expand=True
        )
        button.place(x=x,y=y)
        x += 100
        if x == 700 :
            x = 100
            y += 100
def distance(p_1,p_2):
    z=m.sqrt((float(p_2[0])-float(p_1[0]))**2+(float(p_2[1])-float(p_1[1]))**2)
    return z
 ## créer la matrice
def ouverture(a):
    x, y = np.loadtxt('csv_projet/'+a+'.csv', delimiter=',', unpack=True)  ## créer la matrice
    x_1 = []
    y_1 = []
    x_y = x_1
    for i in range(len(x)):
        a = str(x[i])
        x_1.append(a)
    for j in range(len(y)):
        b = str(y[j])
        y_1.append(b)
    for c in range(len(x_1)):
        x_y[c] = (x_1[c], y_1[c], '0')
    l = []
    for i in range(len(x_y) - 1):
        l.append(distance(x_y[i], x_y[i + 1]))
    somme = 0
    for i in range(len(l)):
        somme += l[i]
    moyenne = somme / len(l)
    e = []  # listes des pts a rajouté
    pt_dist = []  # listes des pts ou il y un plus grandes distances
    for i in range(len(x_y) - 1):
        if distance(x_y[i], x_y[i + 1]) > moyenne+1:
            f = (x_y[i][0], x_y[i][1], '1')
            g = (x_y[i + 1][0], x_y[i + 1][1], '1')
            e.append(f)
            e.append(g)
            pt_dist.append(x_y[i])
    for r in range(len(pt_dist)):
        k = x_y.index(pt_dist[r])
        x_y.insert(k + 1, e[0])
        e.remove(e[0])
        x_y.insert(k + 2, e[0])
        e.remove(e[0])
    x_y1 = []
    pos_x = float(x_y[0][0])
    pos_y = float(x_y[0][1])
    for k in range(len(x_y)):
        pos_modifx = float(x_y[k][0])
        pos_modify = float(x_y[k][1])
        pos_corrx = pos_modifx - pos_x
        pos_corry = -(pos_modify - pos_y) - 200
        x_y1.append((str(pos_corrx), str(pos_corry), x_y[k][2]))
    t.hideturtle()
    t.up()
    t.goto(-320, 300)
    t.down()
    t.write('Plotter en train de dessiner', font=("Simplified Arabic Fixed", 11, "bold"))
    t.up()
    t.goto(-320, 260)
    t.down()
    t.color('red')
    t.write('Plotter rétracté', font=("Simplified Arabic Fixed", 11, "bold"))
    t.up()
    t.shape('circle')
    t.up()
    t.goto(float(x_y1[0][0]), float(x_y1[0][1]))
    t.showturtle()
    for i in range(len(x_y1)):
        if x_y1[i][2] == '0':
            t.color('black')
            t.speed(0)
            t.down()
            t.goto(float(x_y1[i][0]), float(x_y1[i][1]))
        if x_y1[i][2] == '1':
            t.up()
            t.speed(1)
            t.goto(float(x_y1[i][0]), float(x_y1[i][1]))
            t.color('red')
    t.done()
def exit(place):
    exit_button = ttk.Button(
        place,
        text='Exit',
        command=lambda: place.quit()
    )

    exit_button.pack(
        ipadx=5,
        ipady=5,
        expand=True
    )
    exit_button.place(x=800, y=500)
def tracemot(i):
    somme=0
    figure=[]
    for m in i:
        if somme > 0:
            x, y = np.loadtxt('csv_projet/' + m + '.csv', delimiter=',', unpack=True)  ## créer la matrice
            x_1 = []
            y_1 = []
            x_y = x_1
            for i in range(len(x)):
                a = str(x[i])
                x_1.append(a)
            for j in range(len(y)):
                b = str(y[j])
                y_1.append(b)
            for c in range(len(x_1)):
                x_y[c] = (x_1[c], y_1[c], '0')
            l = []
            for i in range(len(x_y) - 1):
                l.append(distance(x_y[i], x_y[i + 1]))
            some = 0
            for i in range(len(l)):
                some += l[i]
            moyenne = some / len(l)
            e = []  # listes des pts a rajouté
            pt_dist = []  # listes des pts ou il y un plus grandes distances
            for i in range(len(x_y) - 1):
                if distance(x_y[i], x_y[i + 1]) > moyenne + 5:
                    f = (x_y[i][0], x_y[i][1], '1')
                    g = (x_y[i + 1][0], x_y[i + 1][1], '1')
                    e.append(f)
                    e.append(g)
                    pt_dist.append(x_y[i])
            for r in range(len(pt_dist)):
                k = x_y.index(pt_dist[r])
                x_y.insert(k + 1, e[0])
                e.remove(e[0])
                x_y.insert(k + 2, e[0])
                e.remove(e[0])
            pos_x = float(x_y[0][0])
            pos_y = float(x_y[0][1])
            x_y1 = []
            for k in range(len(x_y)):
                pos_modifx = float(x_y[k][0])
                pos_modify = float(x_y[k][1])
                pos_corrx = cote(m) * pos_modifx - pos_x + (somme) * 250 + recentrerxC(m)
                pos_corry = enhaut(m) * (pos_modify - pos_y) - 200 + recentreryC(m)
                x_y1.append((str(pos_corrx), str(pos_corry), x_y[k][2]))
            x_y1.insert(0, (x_y1[0][0], x_y1[0][1], '1'))
            x_y1.append((x_y1[len(x_y1) - 1][0], x_y1[len(x_y1) - 1][1], '1'))
            for i in range(len(x_y1)):
                figure.append((x_y1[i][0], x_y1[i][1], x_y1[i][2]))
            long = len(figure)
            somme += 1

        if somme == 0:
            x, y = np.loadtxt('csv_projet/' + m + '.csv', delimiter=',', unpack=True)  ## créer la matrice
            x_1 = []
            y_1 = []
            x_y = x_1
            for i in range(len(x)):
                a = str(x[i])
                x_1.append(a)
            for j in range(len(y)):
                b = str(y[j])
                y_1.append(b)
            for c in range(len(x_1)):
                x_y[c] = (x_1[c], y_1[c], '0')
            l = []
            for i in range(len(x_y) - 1):
                l.append(distance(x_y[i], x_y[i + 1]))

            some = 0
            for i in range(len(l)):
                some += l[i]
            moyenne = some / len(l)
            e = []  # listes des pts a rajouté
            pt_dist = []  # listes des pts ou il y un plus grandes distances
            for i in range(len(x_y) - 1):
                if distance(x_y[i], x_y[i + 1]) > moyenne + 5:
                    f = (x_y[i][0], x_y[i][1], '1')
                    g = (x_y[i + 1][0], x_y[i + 1][1], '1')
                    e.append(f)
                    e.append(g)
                    pt_dist.append(x_y[i])
            for r in range(len(pt_dist)):
                k = x_y.index(pt_dist[r])
                x_y.insert(k + 1, e[0])
                e.remove(e[0])
                x_y.insert(k + 2, e[0])
                e.remove(e[0])
            pos_x = float(x_y[0][0])
            pos_y = float(x_y[0][1])
            x_y11 = []
            for k in range(len(x_y)):
                pos_modifx = float(x_y[k][0])
                pos_modify = float(x_y[k][1])
                pos_corrx = cote(m) * pos_modifx - pos_x + recentrerxC(m)
                pos_corry = enhaut(m) * (pos_modify - pos_y) - 200 + recentreryC(m)
                x_y11.append((str(pos_corrx), str(pos_corry), x_y[k][2]))
            x_y11.append((x_y11[len(x_y11) - 1][0], x_y11[len(x_y11) - 1][1], '1'))
            somme += 1
            for i in range(len(x_y11)):
                figure.append((x_y11[i][0], x_y11[i][1], x_y11[i][2]))
    figures = []
    for i in range(len(figure)):
        bouge = float(figure[i][0]) - somme * 100
        figures.append((str(bouge), figure[i][1], figure[i][2]))
    t.hideturtle()
    t.up()
    t.goto(-300,300)
    t.down()
    t.write('Plotter qui trace', font=("Simplified Arabic Fixed", 11, "bold"))
    t.up()
    t.goto(-300,260)
    t.down()
    t.color('red')
    t.write('Plotter rétracté',font=("Simplified Arabic Fixed", 11, "bold"))
    t.up()

    t.shape('circle')
    t.goto(float(figures[0][0]), float(figures[0][1]))
    t.showturtle()
    for i in range(len(figures)):
        if figures[i][2] == '0':
            t.color('black')
            t.speed(0)
            t.down()
            t.goto(float(figures[i][0]), float(figures[i][1]))
        if figures[i][2] == '1':
            t.up()
            t.speed(1)
            t.goto(float(figures[i][0]), float(figures[i][1]))
            t.color('red')
    t.done()
'''
Main code
'''


# root window
root = tk.Tk()
root.geometry('1000x600')
root.title('Interface pour dicter les formes')

exit(root)

liste=[]
def mot(a):
    def Take_input():
        INPUT = inputtxt.get("1.0", "end-1c")
        tracemot(INPUT)
        liste.append(INPUT)
    f = Label(a, text="Taper le mot en Majuscule et envoyé")
    inputtxt = Text(a, height = 2,width = 25,)
    Display = Button(a, height = 2,width = 20,text ="Envoyé",command =lambda:Take_input())
    ex=exit(a)

    f.pack()
    inputtxt.pack()
    Display.pack()

# bouton lettre

letter_button =ttk.Button(root,text='Lettres',command = lambda: newWindow('Lettres',buttons,list_lettres))
letter_button.pack(ipadx=3,ipady=3,expand=True)
letter_button.place(x=200, y=300)

# bouton shape

shape_button =ttk.Button(root,text='Formes',command = lambda: newWindow('Formes',buttons,list_formes))
shape_button.pack(ipadx=0,ipady=0,expand=True)
shape_button.place(x=400, y=300)

# bouton bonus

bonus_button =ttk.Button(root,text='Formes complexes',command = lambda: newWindow('Styleyyy',buttons,list_bonus))
bonus_button.pack(ipadx=0,ipady=0,expand=True)
bonus_button.place(x=600, y=300)

def change(nom):
    new = tk.Tk()
    new.geometry('1000x600')
    new.title(nom)
    mot(new)


#bouton mots
word_button=ttk.Button(root,text='Mot',command= lambda: change('MOTS'))
word_button.pack(ipadx=0,ipady=0,expand=True)
word_button.place(x=800, y=300)



root.mainloop()





from random import *

as1=[1,'as_de_pique',11,0]
as2=[2,'as_de_trefle',11,0]
as3=[3,'as_de_coeur',11,0]
as4=[4,'as_de_carreau',11,0]
de1=[5,'deux_de_pique',2,0]
de2=[6,'deux_de_trefle',2,0]
de3=[7,'deux_de_coeur',2,0]
de4=[8,'deux_de_carreau',2,0]
t1=[9,'trois_de_pique',3,0]
t2=[10,'trois_de_trefle',3,0]
t3=[11,'trois_de_coeur',3,0]
t4=[12,'trois_de_carreau',3,0]
q1=[13,'quatre_de_pique',4,0]
q2=[14,'quatre_de_trefle',4,0]
q3=[15,'quatre_de_coeur',4,0]
q4=[16,'quatre_de_carreau',4,0]
c1=[17,'cinq_de_pique',5,0]
c2=[18,'cinq_de_trefle',5,0]
c3=[19,'cinq_de_coeur',5,0]
c4=[20,'cinq_de_carreau',5,0]
s1=[21,'six_de_pique',6,0]
s2=[22,'six_de_trefle',6,0]
s3=[23,'six_de_coeur',6,0]
s4=[24,'six_de_carreau',6,0]
se1=[25,'sept_de_pique',7,0]
se2=[26,'sept_de_trefle',7,0]
se3=[27,'sept_de_coeur',7,0]
se4=[28,'sept_de_carreau',7,0]
h1=[29,'huit_de_pique',8,0]
h2=[30,'huit_de_trefle',8,0]
h3=[31,'huit_de_coeur',8,0]
h4=[32,'huit_de_carreau',8,0]
n1=[33,'neuf_de_pique',9,0]
n2=[34,'neuf_de_trefle',9,0]
n3=[35,'neuf_de_coeur',9,0]
n4=[36,'neuf_de_carreau',9,0]
d1=[37,'dix_de_pique',10,0]
d2=[38,'dix_de_trefle',10,0]
d3=[39,'dix_de_coeur',10,0]
d4=[40,'dix_de_carreau',10,0]
v1=[41,'valet_de_pique',10,0]
v2=[42,'valet_de_trefle',10,0]
v3=[43,'valet_de_coeur',10,0]
v4=[44,'valet_de_carreau',10,0]
r1=[45,'dame_de_pique',10,0]
r2=[46,'dame_de_trefle',10,0]
r3=[47,'dame_de_coeur',10,0]
r4=[48,'dame_de_carreau',10,0]
ro1=[49,'roi_de_pique',10,0]
ro2=[50,'roi_de_trefle',10,0]
ro3=[51,'roi_de_coeur',10,0]
ro4=[52,'roi_de_carreau',10,0]

deck=[as1,as2,as3,as4,d1,d2,d3,d4,t1,t2,t3,t4,q1,q2,q3,q4,c1,c2,c3,c4,s1,s2,s3,s4,se1,se2,se3,se4,h1,h2,h3,h4,n1,n2,n3,n4,d1,d2,d3,d4,v1,v2,v3,v4,r1,r2,r3,r4,ro1,ro2,ro3,ro4]

def	create_player(b):
	print "bonjour a vous", b
	return b

def	choix_carte(d_joueur):
        while 1:
	    rand = randrange(1,52)
            if deck[rand][3] == 0:
                break
        deck[rand][3]=1
	i=0
	while 1:
		if d_joueur[i] == 0:
			d_joueur[i] = deck[rand]
                        d_joueur
                        return d_joueur
		else:
			i+=1	
	
def	tour_joueur(joueur1,d_joueur):
	tab_action=[[0,"passer"],[1,"carte ! "]]
        while 1:
            i = 0
            total = 0
            print "Que voulez vous faire ?\n"
	    print "Tapez 0 pour passer votre tour \nTapez 1 pour demander une carte"
	    action = input()
            if action == 1:
		print "vous avez choisi de ",tab_action[action]
                d_joueur = choix_carte(d_joueur)
                while d_joueur[i]!= 0:
		    print d_joueur[i][1]
                    total += d_joueur[i][2]
                    i+=1
                print "point total : ", total
	    else:
                i = 0
                while d_joueur[i]!= 0:
                 total += d_joueur[i][2]
                 i+=1
        	return total

def     tour_bank(d_bank):
    i = 0
    total = i
    while d_bank[i] != 0:
        total += d_bank[i][2]
        i += 1
    if total < 17:
      d_bank= choix_carte(d_bank)
      print "la banque recupere la carte suivante : ", d_bank[i][2], " avec une valeur de ",d_bank[i][2]
      total += d_bank[i][2]
    if total < 17:
        tour_bank(d_bank)
    return total

def     init_bank(d_bank):
    d_bank= choix_carte(d_bank)
    print "la banque recupere la carte suivante : ", d_bank[0][1], " avec une valeur de ",d_bank[0][2]
    return d_bank

def     init_joueur(d_joueur):
    d_joueur =  choix_carte(d_joueur)
    print "le croupier vous donne la carte", d_joueur[0][1],"avec une valeur de ",d_joueur[0][2],"\n" 
    return d_joueur
        
def main(a):
	if a == 1:
		joueur1 = create_player(raw_input("quel est votre nom joueur1 ? \n"))
		d_joueur = [0,0,0,0,0,0,0,0]
                d_bank = [0,0,0,0,0,0,0,0]
	else:
		print "dont fuck with me and pick a number betwen 1 and 1"
              	main(input("combien de joueur ?\n"))
	while 1:
                init_joueur(d_joueur)
                init_bank(d_bank)
                #print deck
		d_joueur = tour_joueur(joueur1,d_joueur)
                d_bank = tour_bank(d_bank)
                if d_joueur - d_bank > 0:
                    print "Vous avez gagne "
                else:
                   print "domage la banque gagne avec ", d_bank , "points contre", d_joueur
	        break
	return 0
main(input("combien de joueur ?\n"))

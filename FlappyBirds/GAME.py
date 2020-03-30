'''
Created on 31 gen 2020

@author: ruben
'''
import pygame 
import random
import math


pygame.init()

sfondo = pygame.image.load('img/sfondo.png')
uccello = pygame.image.load('img/uccello.png')
base = pygame.image.load('img/base.png')
gameover = pygame.image.load('img/gameover.png')
tubo_giu = pygame.image.load('img/tubo.png')
tubo_su = pygame.transform.flip(tubo_giu, False, True)

SCHERMO = pygame.display.set_mode((288, 512))
FPS = 60
VEL_AVANZ = 3
FONT = pygame.font.SysFont('Comic Sans MS', 15, bold=True)


class ValoriLivello(object):
    def __init__(self, tubiSuperati):
        self.__distanza_tubi = 250
        self.__distanza_tubi_iniziale = 250
        self.tubiSuperati = tubiSuperati
        self.xTubiIniziale = 450
        self.livelloDiGioco = 1
        self.__punti = 0
        self.tolleranza = 5
        self.distanzax = 500
        self.distanzaxIniziale = 500
        self.vel_avanz = 1
        self.vel_avanzIniziale = 1 
        self.uccello_vely = 0.2
        
    def aggiornaValori(self):
        if self.__distanza_tubi > 180:
            self.__distanza_tubi = self.__distanza_tubi_iniziale - self.tubiSuperati * 1 
        if self.tubiSuperati / 2 > self.livelloDiGioco:
            self.livelloDiGioco += 1 
            
        if self.tolleranza > 0:
            self.tolleranza = self.tolleranza - self.livelloDiGioco
        if self.tolleranza < 0:
            self.tolleranza = 0   
        
        self.distanzax = self.distanzaxIniziale - self.tubiSuperati*5   #distanza tra ogni sequenza di tubi     
        if self.distanzax < 270:
            self.distanzax = 270
            
        self.vel_avanz = self.vel_avanzIniziale + self.tubiSuperati   #velocita di avanzamento
        if self.vel_avanz > 15:
            self.vel_avanz = 15
            
        self.uccello_vely = self.livelloDiGioco * 0.2 
        '''
        if self.livelloDiGioco == 3:    
            self.uccello_vely = 0.4
        elif self.livelloDiGioco == 6:
            self.uccello_vely = 0.6
        '''    
        self.__punti = self.tubiSuperati * self.livelloDiGioco
        print(str(self.distanzax), " distanzax")
        print(str(self.vel_avanz), " velocita")
    def getLivelloDiGioco(self):
        return self.livelloDiGioco
    
    def getDistanzaTubi(self):
        return self.__distanza_tubi
    def get_vel_avanz(self):
        return self.tubiSuperati*4
    def setTubiSuperati(self, tubi):
        self.tubiSuperati = tubi
    def getPunti(self):
        return self.__punti
        


class livelli_classe:
    def __init__(self, live):
        self.live = live
        '''
        dis = self.dis
        self.tolleranza
        self.grav
        '''
    def getx(self, live):
        self.x = (700 /math.sqrt(live))
        return self.x
    
        
        
        
class tubi_classe:
    def __init__(self, live):
        #print(livello.getx(live))
        self.x = valiv.distanzax #Dictionary
        self.y = random.randint(-75,150)
        
    def avanza_e_disegna(self):
        self.x -= VEL_AVANZ
        SCHERMO.blit(tubo_giu, (self.x,self.y+valiv.getDistanzaTubi()))  #Dictionary
        SCHERMO.blit(tubo_su, (self.x,self.y-valiv.getDistanzaTubi()))  #Dictionary 
               
    def collisione(self, uccello, uccellox, uccelloy):
        tolleranza = valiv.livelloDiGioco    #Dictionary
        uccello_lato_dx = uccellox+uccello.get_width()-tolleranza
        uccello_lato_sx = uccellox+tolleranza
        tubi_lato_dx = self.x + tubo_giu.get_width()
        tubi_lato_sx = self.x 
        uccello_lato_su = uccelloy+tolleranza
        uccello_lato_giu = uccelloy+uccello.get_height()-tolleranza
        tubi_lato_su = self.y+90
        tubi_lato_giu = self.y+10+valiv.getDistanzaTubi()   #Dictionary
        #if uccello_lato_dx > tubi_lato_sx and uccello_lato_sx < tubi_lato_dx:
            #if uccello_lato_su < tubi_lato_su or uccello_lato_giu > tubi_lato_giu:
                #hai_perso()
                
    def fra_i_tubi(self, uccello, uccellox):
        tolleranza = valiv.livelloDiGioco   #Dictionary
        uccello_lato_dx = uccellox+uccello.get_width()-tolleranza
        uccello_lato_sx = uccellox+tolleranza
        tubi_lato_dx = self.x + tubo_giu.get_width()
        tubi_lato_sx = self.x 
        if uccello_lato_dx > tubi_lato_sx and uccello_lato_sx < tubi_lato_dx:
            return True
        
def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)
      
def disegna_oggetti():
    SCHERMO.blit(sfondo, (0,0))
    for t in tubi:
        t.avanza_e_disegna()
    SCHERMO.blit(uccello, (uccellox, uccelloy))
    SCHERMO.blit(base, (basex, 400))
    
    punti_render = FONT.render('score ' + str(valiv.getPunti()), 1, (0,0,0))
    SCHERMO.blit(punti_render, (120,420))
    
    livello_render = FONT.render('liv '+ str(valiv.getLivelloDiGioco()), 1, (0,0,0))
    SCHERMO.blit(livello_render, (5,420))
    
    vely = FONT.render('G: '+ str(valiv.uccello_vely), 1, (0,0,0))
    SCHERMO.blit(vely, (5, 450))
    
    distanzax = FONT.render('distanzaX: '+ str(valiv.distanzax), 1, (0,0,0))
    SCHERMO.blit(distanzax, (5, 480))
    
    vel_avanz = FONT.render('velocita: '+ str(valiv.vel_avanz), 1, (0,0,0))
    SCHERMO.blit(vel_avanz, (5, 430))
def hai_perso():
    print("hai perso") 
    
    SCHERMO.blit(gameover, (50,450))
    aggiorna()
    ricominciamo = False
    while not ricominciamo:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                inizializza()
                ricominciamo = True
            if event.type == pygame.QUIT:
                pygame.quit()      
                  
def inizializza():
    global uccellox, uccelloy, uccello_vely
    global basex
    global tubi
    global tubiSuperati
    global fra_i_tubi 
    global live
    global valiv
    live = 0 #livello del gioco
    global dis #distanza fra i tubi
    uccellox, uccelloy = 60, 150
    uccello_vely = 0
    basex = 0
    tubiSuperati = 0
    fra_i_tubi = False
    tubi = []
    valiv = ValoriLivello(tubiSuperati)
    tubi.append(tubi_classe(live))
    
    
inizializza()

while True:
    #Gestione livelli
    print(valiv.getDistanzaTubi())
    print(valiv.getLivelloDiGioco())
    #Gravity
    velav =  valiv.vel_avanz
    basex -= velav    #Dictionary
    if basex < -45: basex = 0
    uccello_vely += valiv.uccello_vely  #Dictionary
    uccelloy += uccello_vely
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_UP):
            uccello_vely = -6
        if event.type == pygame.QUIT:
            pygame.quit() 
    if tubi[-1].x < 150: tubi.append(tubi_classe(live))
    for t in tubi:
        t.collisione(uccello, uccellox, uccelloy)
        #punteggio
    if not fra_i_tubi:  
        for t in tubi:
            if t.fra_i_tubi(uccello, uccellox):
                fra_i_tubi = True
                break
    if fra_i_tubi:
        fra_i_tubi = False
        for t in tubi:
            if t.fra_i_tubi(uccello, uccellox):
                fra_i_tubi = True
                break
        if not fra_i_tubi:
            tubiSuperati += 1
            #Collisione per terra
    valiv.setTubiSuperati(tubiSuperati)
    
    
    if uccelloy < 0:
        uccelloy = 0
    #Aggiornamente schermo
    disegna_oggetti()
    aggiorna()
    #if uccelloy > 380:
        #hai_perso()
    valiv.aggiornaValori()
     




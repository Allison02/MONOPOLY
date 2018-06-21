echo "# Mono" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/ArianaVillegas/Mono.git
git push -u origin master

import pygame, sys, random

pygame.init()

#Inicio
inicio = pygame.display.set_mode((1100,700))
pygame.display.set_caption("MONOPOLY")
fondo = pygame.image.load("Imagenes/fondo.jpg")
tablero = pygame.transform.scale(pygame.image.load("Imagenes/monopolio.jpg"), (650,650))
banco = 250000

#Botones
color_opciones_1, color_opciones_2, color_ok_1 = (240, 240, 240),(240, 240, 240),(240, 240, 240)
color_text_1, color_text_2, color_textok_1 = (0,0,0),(0,0,0),(0,0,0)
turno = 1
color_turno = (50,60,70)
color = (0, 0, 0)

#Jugador 1
jugador1 = [0,0,True,True,True,True,1500]
propiedades_j1 = []

#Jugador 2
jugador2 = [0,0,True,True,True,True,1500]
propiedades_j2 = []

#Propiedades y tarjetas
prop = [[(815,600),(815,635),"Go", None, None,None],[(745,600),(745,635),"Mediterranean Avenue",60,2,0],
        [(690,600),(690,635),"Community Chest", None, None,None],[(635,600),(635,635),"Baltic Avenue",60,4,0],
        [(585,600),(585,635),"Income Tax", None, 200,0],[(530,600),(530,635),"Reading Railroad",200, 50,0],
        [(480,600),(480,635),"Oriental Avenue",100,6,0],[(430,600),(430,635),"Chance", None, None,None],
        [(375,600),(375,635),"Vermont Avenue",100,6,0],[(325,600),(325,635),"Connecticut Avenue",120,8,0],
        [(270,600),(270,635),"Jail", None, None,None],[(270,535),(230,535),"St. Charles Place",140,10,0],
        [(270,490),(230,490),"Electric Company", 150, 75,0],[(270,430),(230,430),"States Avenue",140,10,0],
        [(270,380),(230,380),"Virginia Avenue",160,12,0],[(270,330),(230,330),"Pennsylvania Railroad", 200, 50,0],
        [(270,275),(230,275),"St. James Place",180,14,0],[(270,225),(230,225),"Community Chest", None, None,None],
        [(270,170),(230,170),"Tennessee Avenue",180,14,0],[(270,120),(230,120),"New York Avenue",200,16,0],
        [(270,65),(230,65),"Free Parking", None, None,None],[(325,65),(325,30),"Kentucky Avenue",220,18,0],
        [(375,65),(375,30),"Chance", None, None,None],[(430,65),(430,30),"Indiana Avenue",220,18,0],
        [(480,65),(480,30),"Illinois Avenue",240,20,0],[(530,65),(530,30),"B & O Railroad", 200, 50,0],
        [(585,65),(585,30),"Atlantic Avenue",260,22,0],[(635,65),(635,30),"Ventor Avenue",260,22,0],
        [(690,65),(690,30),"Water Works", 150, 75,0],[(745,65),(745,30),"Marvin Gardens",280,24,0],
        [(795,65),(795,30),"Go to jail",None, None,None],[(795,120),(835,120),"Pacific Avenue",300,26,0],
        [(795,170),(835,170),"North Carolina Avenue",300,26,0],[(795,225),(835,225),"Community Chest", None, None,None],
        [(795,275),(835,275),"Pennsylvania Avenue",320,28,0],[(795,330),(835,330),"Short Line", 200, 50,0],
        [(795,380),(835,380),"Chance", None, None,None],[(795,430),(835,430),"Park Place",350,35,0],
        [(795,490),(835,490),"Luxury tax", None, None,None],[(795,535),(835,535),"Boardwalk", 400, 50,0]]

Chance = ["Avanza hasta Go.", "Avanza hasta Illinois Avenue.","Recoge $50 del banco.", "Salir de la cárcel gratis.",
          "Avanza 3 espacios.", "Ve a la cárcel.", "Paga $50 al banco.","Avanza a Reading Railroad.", "Avanza a Boardwalk.",
          "Recoge $150 del banco.","Recoge $200 del banco."]

Arca_Comunal=["Avanza hasta Go.", "Recoge $75 del banco.", "Paga $50 al banco.", "Salir de la cárcel gratis.",
              "Ve a la cárcel.", "Recoge $10 del otro jugador.", "Recoge $50 del otro jugador.", "Recoge $25 del banco.",
              "Recoge $100 del banco.", "Paga $50 al otro jugador.", "Recoge $25 del banco."]
tarjetas_num = 0

#Función dados
dados = 0
dados_j2 = 0
posx_dados = 90
posx_dados_j2 = 950

#FUNCIONES--------------------------------------------------------------------------------------------------------------

coordenada = 0
def Pieza(jugador, pos, imagen):
    coordenada = prop[jugador][pos]
    pieza = pygame.image.load(imagen)
    inicio.blit(pieza, coordenada)

fuente_dat = pygame.font.Font(None, 35)
def InfoJugador(n, prop, dinero, pposx):
    fuente_nom = pygame.font.Font(None, 50)
    nom_jug = fuente_nom.render("Jugador " + str(n), 0, color)
    dat1_jug = fuente_dat.render("Propiedades: " + str(len(prop)), 0, color)
    dat2_jug = fuente_dat.render("Dinero: " + str(dinero), 0, color)
    dat3_jug = fuente_dat.render("Dados:", 0, color)
    inicio.blit(nom_jug, (pposx+12, 300))
    inicio.blit(dat1_jug, (pposx, 360))
    inicio.blit(dat2_jug, (pposx, 405))
    inicio.blit(dat3_jug, (pposx, 450))

fuente_acc = pygame.font.Font(None, 27)
def CentrarTexto(texto,ejey):
    titulo_panel = fuente_acc.render(texto, 0, color)
    rectangulo_pregunta = titulo_panel.get_rect()
    rectangulo_pregunta.centerx = inicio.get_rect().centerx
    rectangulo_pregunta.centery = ejey
    inicio.blit(titulo_panel, rectangulo_pregunta)

def Rectangulo():
    pygame.draw.rect(inicio, (180, 150, 100), (400, 275, 300, 150))
    pygame.draw.rect(inicio, (120, 90, 40), (400, 275, 300, 150), 5)

color_ok_1 = (240,240,240)
color_textok_1 = (0,0,0)
def OpcionOK():
    pygame.draw.rect(inicio, color_ok_1, (520, 370, 50, 30))
    boton_ok = fuente_acc.render("OK", 0, color_textok_1)
    inicio.blit(boton_ok, (530, 377))

#-----------------------------------------------------------------------------------------------------------------------

while True:

    # Condiciones_iniciales
    inicio.blit(fondo, (0, 0))
    inicio.blit(tablero, (225, 25))
    Pieza(jugador1[0],0,"Imagenes/barco.png")
    Pieza(jugador2[0],1,"Imagenes/auto.png")
    # Posicion del mouse
    pos_rat = pygame.mouse.get_pos()
    rat_presion = pygame.mouse.get_pressed()
    fuente_dad = pygame.font.Font(None, 120)

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------JUGADOR 1 --------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    # Jugador 1/DATOS

    InfoJugador(1,propiedades_j1,jugador1[6],15)

    if turno == 1:
        color_turno = (50,180,70)
    else:
        color_turno = (50,60,70)
    fuente_turno = pygame.font.SysFont("Arial",40)
    pygame.draw.rect(inicio, color_turno, (25, 140, 175, 70))
    text_turno = fuente_turno.render("TURNO",0,color)
    inicio.blit(text_turno,(43,155))

    #Dados
    if 25 < pos_rat[0] < 25+170 and 600 < pos_rat[1] < 600+45 and turno == 1:
        color_dad = (150, 140, 50)
        if rat_presion[0] == 1 and pygame.event.wait():
            dados = random.randint(1,6) + random.randint(1,6)
            posx_dados = 90
            tarjetas_num = random.randint(0,10)
            if dados > 9:
                posx_dados = 70
        #Posicion del pieza
            if jugador1[0] + dados < 40:
                jugador1[0] += dados
            else:
                jugador1[0] = (jugador1[0] + dados - 39)
                jugador1[6] += 200
            jugador1[2] = True
            jugador1[3] = True
            jugador1[4] = True
            jugador1[5] = True
            turno = 2
    else:
        color_dad = (50, 140, 50)
    dat4_jug = fuente_dad.render(str(dados), 0, color)
    inicio.blit(dat4_jug, (posx_dados, 495))
    pygame.draw.rect(inicio, color_dad, (25, 600, 170, 45))
    nom_dad = fuente_dat.render("Tirar dados", 0, color)
    inicio.blit(nom_dad, (45, 613))
        #Accion de la posicion
    if prop[jugador1[0]][3] != None and jugador1[2] == True:
        if prop[jugador1[0]][5] == 0 and jugador1[6] >= prop[jugador1[0]][3]:
            Rectangulo()
            CentrarTexto("¿Quieres comprar la propiedad: ",310)
            CentrarTexto(prop[jugador1[0]][2] + " ($" + str(prop[jugador1[0]][3]) + ") ?",340)
            # Opciones (Sí o No)
            pygame.draw.rect(inicio, color_opciones_1, (450, 370, 50, 30))
            boton_si = fuente_acc.render("SÍ", 0, color_text_1)
            inicio.blit(boton_si, (467, 377))
            pygame.draw.rect(inicio, color_opciones_2, (600, 370, 50, 30))
            boton_no = fuente_acc.render("NO", 0, color_text_2)
            inicio.blit(boton_no, (614, 377))
            if 450 < pos_rat[0] < 450 + 50 and 370 < pos_rat[1] < 370 + 30:
                color_opciones_1 = (50, 50, 50)
                color_text_1 = (40, 20, 40)
                if rat_presion[0] == 1 and pygame.event.wait():
                    banco += prop[jugador1[0]][3]
                    jugador1[6] -= prop[jugador1[0]][3]
                    prop[jugador1[0]][5] = 1
                    propiedades_j1.append(prop[jugador1[0]][2])
                    jugador1[2] = False
            elif 600 < pos_rat[0] < 600 + 50 and 370 < pos_rat[1] < 370 + 30:
                color_opciones_2 = (50, 50, 50)
                color_text_2 = (40, 20, 40)
                if rat_presion[0] == 1 and pygame.event.wait():
                    jugador1[2] = False
            else:
                color_opciones_1 = (240, 240, 240)
                color_text_1 = (0,0,0)
                color_opciones_2 = (240, 240, 240)
                color_text_2 = (0, 0, 0)
        elif prop[jugador1[0]][5] == 2:
            Rectangulo()
            CentrarTexto("La propiedad le pertenece",310)
            CentrarTexto("al jugador 2, debes pagar: " + str(prop[jugador1[0]][4]), 340)
            # Opciones (Ok)
            OpcionOK()
            if 520 < pos_rat[0] < 520 + 50 and 370 < pos_rat[1] < 370 + 30:
                color_ok_1 = (50, 50, 50)
                color_textok_1 = (40, 20, 40)
                if rat_presion[0] == 1 and pygame.event.wait():
                    jugador1[6] -= prop[jugador1[0]][4]
                    jugador2[6] += prop[jugador1[0]][4]
                    jugador1[2] = False
            else:
                color_ok_1 = (240, 240, 240)
                color_textok_1 = (0,0,0)
        elif prop[jugador1[0]][5] == 1:
            Rectangulo()
            CentrarTexto("Esta propiedad te pertenece",340)
            # Opciones (Ok)
            OpcionOK()
            if 520 < pos_rat[0] < 520 + 50 and 370 < pos_rat[1] < 370 + 30:
                color_ok_1 = (50, 50, 50)
                color_textok_1 = (40, 20, 40)
                if rat_presion[0] == 1 and pygame.event.wait():
                    jugador1[2] = False
            else:
                color_ok_1 = (240, 240, 240)
                color_textok_1 = (0, 0, 0)
        else:
            jugador1[2] = False
    if (prop[jugador1[0]][2] == "Chance" or prop[jugador1[0]][2] == "Community Chest") and jugador1[3] == True:
        Rectangulo()
        #Acción de cerrar la pestaña con "OK"
        if prop[jugador1[0]][2] == "Chance":
            CentrarTexto(Chance[tarjetas_num],340)
            OpcionOK()
            if 520 < pos_rat[0] < 520 + 50 and 370 < pos_rat[1] < 370 + 30:
                color_ok_1 = (50, 50, 50)
                color_textok_1 = (40, 20, 40)
                if rat_presion[0] == 1 and pygame.event.wait():
                    # Acciones de casualidad o Arca comunal
                    if Chance[tarjetas_num] == "Avanza hasta Go.":
                        jugador1[0] = 0
                        jugador1[6] += 200
                    elif Chance[tarjetas_num] == "Avanza hasta Illinois Avenue.":
                        if jugador1[0] >= 24:
                            jugador1[6] += 200
                        jugador1[0] = 24
                    elif Chance[tarjetas_num] == "Recoge $50 del banco.":
                        jugador1[6] += 50
                    elif Chance[tarjetas_num] == "Salir de la cárcel gratis.":
                        jugador1[1] += 1
                    elif Chance[tarjetas_num] == "Avanza 3 espacios.":
                        jugador1[0] += 3
                        jugador1[2] = True
                        jugador1[4] = True
                        jugador1[5] = True
                    elif Chance[tarjetas_num] == "Ve a la cárcel.":
                        jugador1[0] = 30
                    elif Chance[tarjetas_num] == "Paga $50 al banco.":
                        jugador1[6] -= 50
                    elif Chance[tarjetas_num] == "Avanza a Reading Railroad.":
                        jugador1[0] = 5
                        if jugador1[0] >= 5:
                            jugador1[6] += 200
                    elif Chance[tarjetas_num] == "Avanza a Boardwalk.":
                        jugador1[0] = 39
                        if jugador1[0] >= 39:
                            jugador1[6] += 200
                    elif Chance[tarjetas_num] == "Recoge $150 del banco.":
                        jugador1[6] += 150
                    elif Chance[tarjetas_num] == "Recoge $200 del banco.":
                        jugador1[6] += 200
                    jugador1[3] = False
            else:
                color_ok_1 = (240, 240, 240)
        elif prop[jugador1[0]][2] == "Community Chest":
            CentrarTexto(Arca_Comunal[tarjetas_num],340)
            OpcionOK()
            if 520 < pos_rat[0] < 520 + 50 and 370 < pos_rat[1] < 370 + 30:
                color_ok_1 = (50, 50, 50)
                color_textok_1 = (40, 20, 40)
                if rat_presion[0] == 1 and pygame.event.wait():
                    # Acciones de casualidad o Arca comunal
                    if Arca_Comunal[tarjetas_num] == "Avanza hasta Go.":
                        jugador1[0] = 0
                        jugador1[6] += 200
                    elif Arca_Comunal[tarjetas_num] == "Salir de la cárcel gratis.":
                        jugador1[1] += 1
                    elif Arca_Comunal[tarjetas_num] == "Ve a la cárcel.":
                        jugador1[0] = 30
                    elif Arca_Comunal[tarjetas_num] == "Recoge $75 del banco.":
                        jugador1[6] += 75
                    elif Arca_Comunal[tarjetas_num] == "Paga $50 al banco.":
                        jugador1[6] -= 50
                    elif Arca_Comunal[tarjetas_num] == "Recoge $10 del otro jugador.":
                        jugador1[6] += 10
                        jugador2[6] -= 10
                    elif Arca_Comunal[tarjetas_num] == "Recoge $50 del otro jugador.":
                        jugador1[6] += 50
                        jugador2[6] -= 50
                    elif Arca_Comunal[tarjetas_num] == "Recoge $25 del banco.":
                        jugador1[6] += 25
                    elif Arca_Comunal[tarjetas_num] == "Recoge $100 del banco.":
                        jugador1[6] += 100
                    elif Arca_Comunal[tarjetas_num] == "Paga $50 al otro jugador.":
                        jugador1[6] -= 50
                        jugador2[6] += 50
                    jugador1[3] = False
            else:
                color_ok_1 = (240, 240, 240)
                color_textok_1 = (0, 0, 0)
    if (prop[jugador1[0]][2] == "Income Tax" or prop[jugador1[0]][2] == "Luxury tax" or prop[jugador1[0]][2] == "Jail"
        or prop[jugador1[0]][2] == "Free Parking") and jugador1[4] == True:
        Rectangulo()
        # Opciones (Ok)
        OpcionOK()
        if prop[jugador1[0]][2] == "Income Tax":
            CentrarTexto("Income Tax: pierdes $200",340)
            if 520 < pos_rat[0] < 520 + 50 and 370 < pos_rat[1] < 370 + 30:
                color_ok_1 = (50, 50, 50)
                color_textok_1 = (40, 20, 40)
                if rat_presion[0] == 1 and pygame.event.wait():
                    jugador1[6] -= 200
                    jugador1[4] = False
            else:
                color_ok_1 = (240, 240, 240)
                color_textok_1 = (0, 0, 0)
        elif prop[jugador1[0]][2] == "Luxury tax":
            CentrarTexto("Luxury Tax: pierdes $100",340)
            if 520 < pos_rat[0] < 520 + 50 and 370 < pos_rat[1] < 370 + 30:
                color_ok_1 = (50, 50, 50)
                color_textok_1 = (40, 20, 40)
                if rat_presion[0] == 1 and pygame.event.wait():
                    jugador1[6] -= 100
                    jugador1[4] = False
            else:
                color_ok_1 = (240, 240, 240)
                color_textok_1 = (0, 0, 0)
        elif prop[jugador1[0]][2] == "Jail":
            CentrarTexto("Estas de visita en la cárcel",340)
            if 520 < pos_rat[0] < 520 + 50 and 370 < pos_rat[1] < 370 + 30:
                color_ok_1 = (50, 50, 50)
                color_textok_1 = (40, 20, 40)
                if rat_presion[0] == 1 and pygame.event.wait():
                    jugador1[4] = False
            else:
                color_ok_1 = (240, 240, 240)
                color_textok_1 = (0, 0, 0)
        elif prop[jugador1[0]][2] == "Free Parking":
            CentrarTexto("Parada libre",340)
            if 520 < pos_rat[0] < 520 + 50 and 370 < pos_rat[1] < 370 + 30:
                color_ok_1 = (50, 50, 50)
                color_textok_1 = (40, 20, 40)
                if rat_presion[0] == 1 and pygame.event.wait():
                    jugador1[4] = False
            else:
                color_ok_1 = (240, 240, 240)
                color_textok_1 = (0, 0, 0)
    if (prop[jugador1[0]][2] == "Go to jail" or jugador1[0] == 30) and jugador1[5] == True:
        Rectangulo()
        CentrarTexto("Ir a la carcel",300)
        # Opciones ("Tarjeta", "Pagar $50")
        if 490 < pos_rat[0] < 490 + 120 and 320 < pos_rat[1] < 320 + 30:
            color_ok_1 = (50, 50, 50)
            color_textok_1 = (40, 20, 40)
            if rat_presion[0] == 1 and pygame.event.wait() and jugador1[1] > 0:
                jugador1[1] -= 1
                jugador1[0] = 10
                jugador1[5] = False
        else:
            color_ok_1 = (240, 240, 240)
            color_textok_1 = (0, 0, 0)
        pygame.draw.rect(inicio, color_ok_1, (490, 320, 120, 30))
        boton_tarjeta = fuente_acc.render("Usar tarjeta", 0, color_textok_1)
        inicio.blit(boton_tarjeta, (500, 328))

        if 490 < pos_rat[0] < 490 + 120 and 360 < pos_rat[1] < 360 + 30:
            color_ok_1 = (50, 50, 50)
            color_textok_1 = (40, 20, 40)
            if rat_presion[0] == 1 and pygame.event.wait() and jugador1[6]>=50:
                jugador1[6] -= 50
                jugador1[0] = 10
                jugador1[5] = False
        else:
            color_ok_1 = (240, 240, 240)
            color_textok_1 = (0, 0, 0)
        pygame.draw.rect(inicio, color_ok_1, (490, 360, 120, 30))
        boton_pagar = fuente_acc.render("Pagar $50", 0, color_textok_1)
        inicio.blit(boton_pagar, (500, 368))


    #-------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------
    #------------------------------------JUGADOR 2 ---------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------


    # Jugador 2/DATOS

    InfoJugador(2,propiedades_j2,jugador2[6],890)

    if turno == 2:
        color_turno = (50,180,70)
    else:
        color_turno = (50,60,70)
    fuente_turno = pygame.font.SysFont("Arial",40)
    pygame.draw.rect(inicio, color_turno, (895, 140, 175, 70))
    text_turno = fuente_turno.render("TURNO",0,color)
    inicio.blit(text_turno,(913,155))

    # Dados
    if 900 < pos_rat[0] < 900 + 170 and 600 < pos_rat[1] < 600 + 45 and turno == 2:
        color_dad = (150, 140, 50)
        if rat_presion[0] == 1 and pygame.event.wait():
            dados_j2 = random.randint(1,6) + random.randint(1,6)
            posx_dados_j2 = 950
            tarjetas_num = random.randint(0, 10)
            if dados_j2 > 9:
                posx_dados_j2 = 930
            # Posicion del pieza
            if jugador2[0] + dados_j2 < 40:
                jugador2[0] += dados_j2
            else:
                jugador2[0] = (jugador2[0] + dados - 39)
                jugador2[6] += 200
            jugador2[2] = True
            jugador2[3] = True
            jugador2[4] = True
            jugador2[5] = True
            turno = 1
    else:
        color_dad = (50, 140, 50)
    dat4_jug_j2 = fuente_dad.render(str(dados_j2), 0, color)
    inicio.blit(dat4_jug_j2, (posx_dados_j2, 495))
    pygame.draw.rect(inicio, color_dad, (900, 600, 170, 45))
    nom_dad_j2 = fuente_dat.render("Tirar dados", 0, color)
    inicio.blit(nom_dad_j2, (918, 613))
    # Accion de la posicion
    fuente_acc = pygame.font.Font(None, 27)
    if prop[jugador2[0]][3] != None and jugador2[2] == True:
        if prop[jugador2[0]][5] == 0 and jugador2[6] >= prop[jugador2[0]][3]:
            Rectangulo()
            CentrarTexto("¿Quieres comprar la propiedad: ",310)
            CentrarTexto(prop[jugador2[0]][2] + " ($" + str(prop[jugador2[0]][3]) + ") ?",340)
            # Opciones (Sí o No)
            pygame.draw.rect(inicio, color_opciones_1, (450, 370, 50, 30))
            pygame.draw.rect(inicio, color_opciones_2, (600, 370, 50, 30))
            boton_si = fuente_acc.render("SÍ", 0, color_text_1)
            boton_no = fuente_acc.render("NO", 0, color_text_2)
            inicio.blit(boton_si, (467, 377))
            inicio.blit(boton_no, (614, 377))
            if 450 < pos_rat[0] < 450 + 50 and 370 < pos_rat[1] < 370 + 30:
                color_opciones_1 = (50, 50, 50)
                color_text_1 = (40, 20, 40)
                if rat_presion[0] == 1 and pygame.event.wait():
                    jugador2[6] -= prop[jugador2[0]][3]
                    prop[jugador2[0]][5] = 2
                    propiedades_j2.append(prop[jugador2[0]][2])
                    jugador2[2]= False
            elif 600 < pos_rat[0] < 600 + 50 and 370 < pos_rat[1] < 370 + 30:
                color_opciones_2 = (50, 50, 50)
                color_text_2 = (40, 20, 40)
                if rat_presion[0] == 1 and pygame.event.wait():
                    jugador2[2] = False
            else:
                color_opciones_1 = (240, 240, 240)
                color_text_1 = (0, 0, 0)
                color_opciones_2 = (240, 240, 240)
                color_text_2 = (0, 0, 0)
        elif prop[jugador2[0]][5] == 1:
            Rectangulo()
            CentrarTexto("La propiedad le pertenece",310)
            CentrarTexto("al jugador 1, debes pagar: " + str(prop[jugador2[0]][4]),340)
            # Opciones (Ok)
            OpcionOK()
            if 520 < pos_rat[0] < 520 + 50 and 370 < pos_rat[1] < 370 + 30:
                color_ok_1 = (50, 50, 50)
                color_textok_1 = (40, 20, 40)
                if rat_presion[0] == 1 and pygame.event.wait():
                    jugador2[6] -= prop[jugador2[0]][4]
                    jugador1[6] += prop[jugador2[0]][4]
                    jugador2[2] = False
            else:
                color_ok_1 = (240, 240, 240)
                color_textok_1 = (0, 0, 0)
        elif prop[jugador2[0]][5] == 2:
            Rectangulo()
            CentrarTexto("Esta propiedad te pertenece",340)
            # Opciones (Ok)
            OpcionOK()
            if 520 < pos_rat[0] < 520 + 50 and 370 < pos_rat[1] < 370 + 30:
                color_ok_1 = (50, 50, 50)
                color_textok_1 = (40, 20, 40)
                if rat_presion[0] == 1 and pygame.event.wait():
                    jugador2[2] = False
            else:
                color_ok_1 = (240, 240, 240)
                color_textok_1 = (0, 0, 0)
        else:
            jugador2[2] = False
    if (prop[jugador2[0]][2] == "Chance" or prop[jugador2[0]][2] == "Community Chest") and jugador2[3] == True:
        Rectangulo()
        # Acción de cerrar la pestaña con "OK"
        if prop[jugador2[0]][2] == "Chance":
            CentrarTexto(Chance[tarjetas_num],340)
            OpcionOK()
            if 520 < pos_rat[0] < 520 + 50 and 370 < pos_rat[1] < 370 + 30:
                color_ok_1 = (50, 50, 50)
                color_textok_1 = (40, 20, 40)
                if rat_presion[0] == 1 and pygame.event.wait():
                    # Acciones de casualidad o Arca comunal
                    if Chance[tarjetas_num] == "Avanza hasta Go.":
                        jugador2[0] = 0
                        jugador2[6] += 200
                    elif Chance[tarjetas_num] == "Avanza hasta Illinois Avenue.":
                        if jugador2[0] >= 24:
                            jugador2[6] += 200
                        jugador2[0] = 24
                    elif Chance[tarjetas_num] == "Recoge $50 del banco.":
                        jugador2[6] += 50
                    elif Chance[tarjetas_num] == "Salir de la cárcel gratis.":
                        jugador2[1] += 1
                    elif Chance[tarjetas_num] == "Avanza 3 espacios.":
                        jugador2[0] += 3
                        jugador2[2] = True
                        jugador2[4] = True
                        jugador2[5] = True
                    elif Chance[tarjetas_num] == "Ve a la cárcel.":
                        jugador2[0] = 30
                    elif Chance[tarjetas_num] == "Paga $50 al banco.":
                        jugador2[6] -= 50
                    elif Chance[tarjetas_num] == "Avanza a Reading Railroad.":
                        jugador2[0] = 5
                        if jugador2[0] >= 5:
                            jugador2[6] += 200
                    elif Chance[tarjetas_num] == "Avanza a Boardwalk.":
                        jugador2[0] = 39
                        if jugador2[0] >= 39:
                            jugador2[6] += 200
                    elif Chance[tarjetas_num] == "Recoge $150 del banco.":
                        jugador2[6] += 150
                    elif Chance[tarjetas_num] == "Recoge $200 del banco.":
                        jugador2[6] += 200
                    jugador2[3] = False
            else:
                color_ok_1 = (240, 240, 240)
        elif prop[jugador2[0]][2] == "Community Chest":
            CentrarTexto(Arca_Comunal[tarjetas_num],340)
            OpcionOK()
            if 520 < pos_rat[0] < 520 + 50 and 370 < pos_rat[1] < 370 + 30:
                color_ok_1 = (50, 50, 50)
                color_textok_1 = (40, 20, 40)
                if rat_presion[0] == 1 and pygame.event.wait():
                    # Acciones de casualidad o Arca comunal
                    if Arca_Comunal[tarjetas_num] == "Avanza hasta Go.":
                        jugador2[0] = 0
                        jugador2[6] += 200
                    elif Arca_Comunal[tarjetas_num] == "Salir de la cárcel gratis.":
                        jugador2[1] += 1
                    elif Arca_Comunal[tarjetas_num] == "Ve a la cárcel.":
                        jugador2[0] = 30
                    elif Arca_Comunal[tarjetas_num] == "Recoge $75 del banco.":
                        jugador2[6] += 75
                    elif Arca_Comunal[tarjetas_num] == "Paga $50 al banco.":
                        jugador2[6] -= 50
                    elif Arca_Comunal[tarjetas_num] == "Recoge $10 del otro jugador.":
                        jugador2[6] += 10
                        jugador1[6] -= 10
                    elif Arca_Comunal[tarjetas_num] == "Recoge $50 del otro jugador.":
                        jugador2[6] += 50
                        jugador1[6] -= 50
                    elif Arca_Comunal[tarjetas_num] == "Recoge $25 del banco.":
                        jugador2[6] += 25
                    elif Arca_Comunal[tarjetas_num] == "Recoge $100 del banco.":
                        jugador2[6] += 100
                    elif Arca_Comunal[tarjetas_num] == "Paga $50 al otro jugador.":
                        jugador2[6] -= 50
                        jugador1[6] += 50
                    jugador2[3] = False
            else:
                color_ok_1 = (240, 240, 240)
                color_textok_1 = (0, 0, 0)
    if (prop[jugador2[0]][2] == "Income Tax" or prop[jugador2[0]][2] == "Luxury tax" or jugador2[6] == 10
        or prop[jugador2[0]][2] == "Free Parking") and jugador2[4] == True:
        Rectangulo()
        # Opciones (Ok)
        OpcionOK()
        if prop[jugador2[0]][2] == "Income Tax":
            CentrarTexto("Income Tax: pierdes $200",340)
            if 520 < pos_rat[0] < 520 + 50 and 370 < pos_rat[1] < 370 + 30:
                color_ok_1 = (50, 50, 50)
                color_textok_1 = (40, 20, 40)
                if rat_presion[0] == 1 and pygame.event.wait():
                    jugador2[6] -= 200
                    jugador2[4] = False
            else:
                color_ok_1 = (240, 240, 240)
                color_textok_1 = (0, 0, 0)
        elif prop[jugador2[0]][2] == "Luxury tax":
            CentrarTexto("Luxury Tax: pierdes $100",340)
            if 520 < pos_rat[0] < 520 + 50 and 370 < pos_rat[1] < 370 + 30:
                color_ok_1 = (50, 50, 50)
                color_textok_1 = (40, 20, 40)
                if rat_presion[0] == 1 and pygame.event.wait():
                    jugador2[6] -= 100
                    jugador2[4] = False
            else:
                color_ok_1 = (240, 240, 240)
                color_textok_1 = (0, 0, 0)
        elif prop[jugador2[0]][2] == "Jail":
            CentrarTexto("Estas de visita en la cárcel",340)
            if 520 < pos_rat[0] < 520 + 50 and 370 < pos_rat[1] < 370 + 30:
                color_ok_1 = (50, 50, 50)
                color_textok_1 = (40, 20, 40)
                if rat_presion[0] == 1 and pygame.event.wait():
                    jugador2[4] = False
            else:
                color_ok_1 = (240, 240, 240)
                color_textok_1 = (0, 0, 0)
        elif prop[jugador2[0]][2] == "Free Parking":
            CentrarTexto("Parada libre",340)
            if 520 < pos_rat[0] < 520 + 50 and 370 < pos_rat[1] < 370 + 30:
                color_ok_1 = (50, 50, 50)
                color_textok_1 = (40, 20, 40)
                if rat_presion[0] == 1 and pygame.event.wait():
                    jugador2[4] = False
            else:
                color_ok_1 = (240, 240, 240)
                color_textok_1 = (0, 0, 0)
    if jugador2[0] == 30 and jugador2[5] == True:
        Rectangulo()
        CentrarTexto("Ir a la carcel",300)
        # Opciones ("Tarjeta", "Pagar $50")
        if 490 < pos_rat[0] < 490 + 120 and 320 < pos_rat[1] < 320 + 30:
            color_ok_1 = (50, 50, 50)
            color_textok_1 = (40, 20, 40)
            if rat_presion[0] == 1 and pygame.event.wait() and jugador2[1] > 0:
                jugador2[1] -= 1
                jugador2[0] = 10
                jugador2[5] = False
        else:
            color_ok_1 = (240, 240, 240)
            color_textok_1 = (0, 0, 0)
        pygame.draw.rect(inicio, color_ok_1, (490, 320, 120, 30))
        boton_tarjeta = fuente_acc.render("Usar tarjeta", 0, color_textok_1)
        inicio.blit(boton_tarjeta, (500, 328))

        if 490 < pos_rat[0] < 490 + 120 and 360 < pos_rat[1] < 360 + 30:
            color_ok_1 = (50, 50, 50)
            color_textok_1 = (40, 20, 40)
            if rat_presion[0] == 1 and pygame.event.wait() and jugador1[6]>=50:
                jugador2[6] -= 50
                jugador2[0] = 10
                jugador2[5] = False
        else:
            color_ok_1 = (240, 240, 240)
            color_textok_1 = (0, 0, 0)
        pygame.draw.rect(inicio, color_ok_1, (490, 360, 120, 30))
        boton_pagar = fuente_acc.render("Pagar $50", 0, color_textok_1)
        inicio.blit(boton_pagar, (500, 368))

    #------------------------------------------FIN----------------------------------------------------------------------

    # if can_dinero_j2 < 0 or can_dinero_j1 < 0:
    #     jugar = False
    #     final = True

    #-------------------------------------------------------------------------------------------------------------------

    for accion in pygame.event.get():
        if accion.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

# fin = pygame.display.set_mode((1100, 700))
# while True:
#     if can_dinero_j2 < 0 or can_dinero_j1 < 0:
#         fuente_fin = pygame.font.SysFont("Calibri", 90)
#         if can_dinero_j1 < 0:
#             CentrarTexto("EL JUGADOR 2 GANÓ", 300)
#         else:
#             CentrarTexto("EL JUGADOR 1 GANÓ", 300)
#
#     for accion in pygame.event.get():
#         if accion.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#
#     pygame.display.update()
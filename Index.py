import pygame,sys, random, tkinter

pygame.init()

#Propiedades

prop = [[(815,635),"Go", None, None,None],[(745,635),"Mediterranean Avenue",60,2,0],
        [(690,635),"Community Chest", None, None,None],[(635,635),"Baltic Avenue",60,4,0],
        [(585,635),"Income Tax", None, 200,0],[(530,635),"Reading Railroad",200, 50,0],
        [(480,635),"Oriental Avenue",100,6,0],[(430,635),"Chance", None, None,None],
        [(375,635),"Vermont Avenue",100,6,0],[(325,635),"Connecticut Avenue",120,8,0],
        [(270,635),"Jail", None, None,None],[(230,535) ,"St. Charles Place",140,10,0],
        [(230,490),"Electric Company", 150, 75,0],[(230,430),"States Avenue",140,10,0],
        [(230,380),"Virginia Avenue",160,12,0],[(230,330),"Pennsylvania Railroad", 200, 50,0],
        [(230,275),"St. James Place",180,14,0],[(230,225),"Community Chest", None, None,None],
        [(230,170),"Tennessee Avenue",180,14,0],[(230,120),"New York Avenue",200,16,0],
        [(230,65),"Free Parking", None, None,None],[(325,25),"Kentucky Avenue",220,18,0],
        [(375,25),"Chance", None, None,None],[(430,25),"Indiana Avenue",220,18,0],
        [(480,25),"Illinois Avenue",240,20,0],[(530,25),"B &  O Railroad", 200, 50,0],
        [(585,25),"Atlantic Avenue",260,22,0],[(635,25),"Ventor Avenue",260,22,0],
        [(690,25),"Water Works", 150, 75,0],[(745,25),"Marvin Gardens",280,24,0],
        [(795,25),"Go to jail",None, None,None],[(835,120),"Pacific Avenue",300,26,0],
        [(835,170),"North Carolina Avenue",300,26,0],[(835,225),"Community Chest", None, None,None],
        [(835,275),"Pennsylvania Avenue",320,28,0],[(835,330),"Short Line", 200, 50,0],
        [(835,380),"Chance", None, None,None],[(835,430),"Park Place",350,35,0],
        [(835,490),"Luxury tax", None, None,None],[(835,535),"Boardwalk", 400, 50,0]]
nombre = None
costo = None
alquiler = None

def Propiedades(posicion):
    coordenada = prop[posicion][0]
    nombre = prop[posicion][1]
    costo = prop[posicion][2]
    alquiler = prop[posicion][3]
    return coordenada,nombre,costo,alquiler

#Fondo

inicio = pygame.display.set_mode((1100,700))
pygame.display.set_caption("MONOPOLY")

fondo = pygame.image.load("Imagenes/fondo.jpg")
coordenada_f = (0, 0)

tablero = pygame.transform.scale(pygame.image.load("Imagenes/monopolio.jpg"), (650,650))
coordenada_t = (225, 25)

#Piezas

barco = pygame.image.load("Imagenes/barco.png")
coordenada_b = (835,120)

# #Jugador
#
# class jugador():
#     def __init__(self):
#         self.coordenada = (coordenada_b)
#         self.posicion = 0
#         self.n_prop = 0
#         self.turno = 0
#         self.dinero = 1500
#         self.propiedades = []
#
#     #Nombre
#     def Nombre(self,nombre,pos_nom):
#         self.nombre = pygame.font.Font(None, 50)
#         self.texto = self.nombre.render(nombre, 0, (250, 250, 250))
#         inicio.blit(self.texto, pos_nom)
#
#     #Dados
#     def Nom_dados(self,nom_dados,pos_nom_dad):
#         self.texto_1 = self.nombre.render(nom_dados, 0, (250, 250, 250))
#         inicio.blit(self.texto_1, pos_nom_dad)
#
#     def Tirar_dados(self, pos_dad):
#         self.dados = random.randint(1, 4) + random.randint(1, 4)
#         self.texto_2 = self.nombre.render(self.dados, 0, (250, 250, 250))
#         inicio.blit(self.texto_1, pos_dad)
#
#     #Avanzar
#     def Avanzar(self):
#         self.info_prop = Propiedades(self.posicion +self.dados)
#         self.coordenada = self.info_prop(0)
#
#     #Comprar propiedades
#     def Comprar(self,coordenada):
#         self.preguntar = tkinter.Tk()
#         # self.preguntar.title("COMPRAR PROPIEDADES")
#         # self.preguntar.mainloop()
#
# #Actualización

while True:

    #Condiciones_iniciales
    inicio.blit(fondo, coordenada_f)
    inicio.blit(tablero, coordenada_t)
    inicio.blit(barco, coordenada_b)

    for accion in pygame.event.get():
        if accion.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
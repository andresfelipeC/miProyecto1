import turtle

def POSICIONAR():
    """Cambia el onscreenclick para que lea donde posicionar a Karel"""
    global kl
    wn.title("HAGA CLICK DONDE QUIERA INICIAR A KAREL")
    bep.ht()
    kl.ht()
    wn.onscreenclick(FACING)

def FACING(x,y):
    """Recibe unas coordenadas y posiciona a karel en el centro del cuadrante donde estan ubicadas,
    luego activa comandos onkey para determinar su orientacion"""
    x=((25+x)//50)*50
    y=((25+y)//50)*50
    kl.goto(x,y)
    karel.x=x 
    karel.y=y
    kl.st()
    kl.speed(1)
    wn.title("PRESIONE UNA TECLA DE DIRECCION PARA ORIENTAR A KAREL")
    wn.onkey(EJECUTARNORTE,"Up")
    wn.onkey(EJECUTARSUR,"Down")
    wn.onkey(EJECUTAROESTE,"Left")
    wn.onkey(EJECUTARESTE,"Right")

def EJECUTARNORTE():
    """Comienza a ejecutar la programacion compilada con karel orientandose al norte"""
    karel.facing=1
    kl.seth(karel.facing*90)
    karel.execute(ejecucion)
def EJECUTARSUR():
    """Comienza a ejecutar la programacion compilada con karel orientandose al sur"""
    karel.facing=3
    kl.seth(karel.facing*90)
    karel.execute(ejecucion)
def EJECUTAROESTE():
    """Comienza a ejecutar la programacion compilada con karel orientandose al oeste"""
    karel.facing=2
    kl.seth(karel.facing*90)
    karel.execute(ejecucion)
def EJECUTARESTE():
    """Comienza a ejecutar la programacion compilada con karel orientandose al este"""
    karel.facing=0
    kl.seth(karel.facing*90)
    karel.execute(ejecucion)

def exitf():
    """Cambia el onscreenclick para que lea donde posicionar los beepers"""
    global bep
    wn.title("SITUE LOS BEEPERS Y LUEGO PRESIONE ENTER")
    visualk.penup()
    visualk.ht()
    visualk.onclick(None)
    bep.penup()
    bep.color("red")
    bep.shape("circle")
    bep.speed(0)
    wn.onclick(situarbeeper)
    
def situarmuros(x,y):
    """Recibe unas coordenadas y situa muros hasta estas coordenadas, ubicandolos en el centro
    de los cuadrantes, guarda la ubicacion de los muros en una lista"""
    primero=visualk.position()
    visualk.pendown()
    visualk.pencolor("Black")
    visualk.pensize("10")
    x=(x//50)*50+25
    y=(y//50)*50+25
    if (x!=primero[0] or y!=primero[1]) and (x==primero[0] or y==primero[1]):
        visualk.goto(x,y)
        if x!=primero[0]:
            a=(x+primero[0])/2
            muros.append([a, y])
        else:
            a=(y+primero[1])/2
            muros.append([x,a])
    visualk.penup()
    
def iracentro(x,y): 
    """Recibe unas coordenadas y situa la tortuga en el centro del cuadrante"""
    x=(x//50)*50+25
    y=(y//50)*50+25
    visualk.goto(x,y)
    visualk.st()

def situarbeeper(x,y):
    """Recibe unas coordenadas y situa un beeper en la esquina del cuadrante, guarda los beepers
    en un diccionario. Si hay mas de un beeper en la esquina, dibuja el numero de beepers que hay"""
    x=((25+x)//50)*50
    y=((25+y)//50)*50
    bep.goto(x,y)
    bep.st()
    if (x,y) not in list(beepers.keys()):
        beepers[x,y]=[bep.clone()]
    else:
        beepers[x,y].append(bep.clone())
        beepers[x,y][0].pencolor("black")
        beepers[x,y][0].write(len(beepers[x,y]), move=False, align="center", font=("Arial", 7, "bold"))

def tolist(contador,listraw):
    """Recibe una lista de lineas y las almacena en una nueva lista, quitando las cadenas vacias,
    limpiando de espacios y tabulaciones el final de la cadena, almacenando en una sublista los cuerpos
    de los comandos de tipo ITERATE, WHILE, IF, DEFINE (identificados por no tener ; al final y no ser 
    turnoff ni END ni ELSE ni BEGIN)"""
    newlist=[]
    i=0
    while (i)<len(listraw):
        listraw[i]=listraw[i][contador:]
        if len(listraw[i])!=0:
            if listraw[i]=="turnoff":
                for x in reversed(range(len(listraw)-i)):
                    newlist.append(listraw[len(listraw)-1-x])
                return newlist
            else:
                if listraw[i][len(listraw[i])-1]!=";":
                    block=[]
                    while listraw[i][contador:]!="END" and listraw[i][contador:]!="END;":
                        block.append(listraw.pop(i))
                    block.pop(1)
                    block[len(block)-1]+=";"
                    newblock=[block[0]]+tolist(contador+1,block[1:])
                    newlist.append(newblock)
                else:
                    newlist.append(listraw[i])
        i+=1
    return newlist

class Karel:
    def __init__(self,facing=0,x=0,y=0,beepers=0):
        """x, y son las coordenadas. facing: 0 es este, 1 es norte, 2 es oeste, 3 es sur."""
        self.facing=facing
        self.x=x 
        self.y=y 
        self.beepers=beepers
    def __str__(self): 
        """Este metodo permite imprimir en la consola a lo que hace karel"""
        return "Facing: {0}, pos:({1},{2}), beepers:{3}".format(self.facing,self.x,self.y,self.beepers)
    
#     ********FUNCIONES BASICAS**********
    
    def move(self):
        """Mueve a karel 50 unidades, guarda las nuevas coordenadas en self.x, self.y. 
        Es util dado que a veces al pedir las coordenadas de turtle hay problemas con los decimales"""
        if self.facing==0:
            if [self.x+25,self.y] in muros:
                kl.forward(20)
                self.executionerror()
            self.x+=50
        elif self.facing==1:
            if [self.x,25+self.y] in muros:
                kl.forward(20)
                self.executionerror()
            self.y+=50
        elif self.facing==2:
            if [self.x-25,self.y] in muros:
                kl.forward(20)
                self.executionerror()
            self.x-=50
        else:
            if [self.x,self.y-25] in muros:
                kl.forward(20)
                self.executionerror()
            self.y-=50
        kl.forward(50)
    def turnleft(self):
        """Cambia el facing a la izquierda, mueve a karel a la izquierda"""
        if self.facing==3:
            self.facing=0
            kl.seth(self.facing*90)
        else:
            self.facing+=1
            kl.seth(self.facing*90)
    def pickbeeper(self):
        """Si no hay beepers devuelve un error, si hay beepers suma 1 a self.beepers. Borra el numero
        de beepers que estaba escrito antes y si queda mas de un beeper en el lugar escribe el numero
        que queda"""
        if (self.x,self.y) not in list(beepers.keys()):
            self.executionerror()
        elif len(beepers[self.x,self.y])==0:
            self.executionerror()
        beepers[self.x,self.y][0].pencolor("white") 
        beepers[self.x,self.y][0].write(len(beepers[self.x,self.y]),move=False, align="center", font=("Arial", 7, "bold"))
        beepers[self.x,self.y][0].ht()
        beepers[self.x,self.y].pop(0)
        if len(beepers[self.x,self.y])!=0:
            beepers[self.x,self.y][0].pencolor("black")
            beepers[self.x,self.y][0].write(len(beepers[self.x,self.y]),move=False, align="center", font=("Arial", 7, "bold"))
        self.beepers+=1
    def putbeeper(self):
        """Si no tiene beepers karel, devuelve un error. Situa un beeper en la posicion de karel, 
        disminuye 1 a self.beepers"""
        if self.beepers<=0:
            self.executionerror()
        situarbeeper(self.x,self.y)
        self.beepers-=1
        
#     ********EJECUCION**********
    
    def execute(self,listaejecu):
        """Lee cada funcion en una lista y la ejecuta debidamente, busca en un diccionario las
        funciones que no entiende, si no esta en el diccionario levanta error de lexico.
        Imprime en consola el comando ejecutado y el nuevo estado de karel"""
        for i in range(len(listaejecu)):
            print(listaejecu[i])
            if listaejecu[i]!="":
                if listaejecu[i]=="move;":
                    self.move()
                elif listaejecu[i]=="turnleft;":
                    self.turnleft()
                elif listaejecu[i]=="pickbeeper;":
                    self.pickbeeper()
                elif listaejecu[i]=="putbeeper;":
                    self.putbeeper()
                elif listaejecu[i]=="turnoff" or listaejecu[i]=="turnoff":
                    self.turnoff()
                    if listaejecu[i+1]=="\tEND-OF-EXECUTION" and listaejecu[i+2]=="END-OF-PROGRAM":
                        break
                    else:
                        self.lexicerror()
                elif type(listaejecu[i]) is list:
                    if listaejecu[i][0][:7]=="ITERATE":
                        x=listaejecu[i][0].find(" TIMES")
                        a=(listaejecu[i][0][8:x])
                        for q in range(int(a)):
                            self.execute(listaejecu[i][1:])
                    if listaejecu[i][0][:3]=="IF " and listaejecu[i][0][len(listaejecu[i][0])-5:]==" THEN":
                        if listaejecu[i][0][3:len(listaejecu[i][0])-5]=="facing-north":
                            if self.facingnorth():
                                self.execute(listaejecu[i][1:])
                            else: 
                                if len(listaejecu)>(i+1):
                                    if listaejecu[i+1][0]=="ELSE":
                                        self.execute(listaejecu[i+1][1:])
                        if listaejecu[i][0][3:len(listaejecu[i][0])-5]=="not-facing-north":
                            if not self.facingnorth():
                                self.execute(listaejecu[i][1:])
                            else: 
                                if len(listaejecu)>(i+1):
                                    if listaejecu[i+1][0]=="ELSE":
                                        self.execute(listaejecu[i+1][1:])
                        if listaejecu[i][0][3:len(listaejecu[i][0])-5]=="facing-south":
                            if self.facingsouth():
                                self.execute(listaejecu[i][1:])
                            else: 
                                if len(listaejecu)>(i+1):
                                    if listaejecu[i+1][0]=="ELSE":
                                        self.execute(listaejecu[i+1][1:])
                        if listaejecu[i][0][3:len(listaejecu[i][0])-5]=="not-facing-south":
                            if not self.facingsouth():
                                self.execute(listaejecu[i][1:])
                            else: 
                                if len(listaejecu)>(i+1):
                                    if listaejecu[i+1][0]=="ELSE":
                                        self.execute(listaejecu[i+1][1:])
                        if listaejecu[i][0][3:len(listaejecu[i][0])-5]=="facing-west":
                            if self.facingwest():
                                self.execute(listaejecu[i][1:])
                            else: 
                                if len(listaejecu)>(i+1):
                                    if listaejecu[i+1][0]=="ELSE":
                                        self.execute(listaejecu[i+1][1:])
                        if listaejecu[i][0][3:len(listaejecu[i][0])-5]=="not-facing-west":
                            if not self.facingwest():
                                self.execute(listaejecu[i][1:])
                            else: 
                                if len(listaejecu)>(i+1):
                                    if listaejecu[i+1][0]=="ELSE":
                                        self.execute(listaejecu[i+1][1:])
                        if listaejecu[i][0][3:len(listaejecu[i][0])-5]=="facing-east":
                            if self.facingeast():
                                self.execute(listaejecu[i][1:])
                            else: 
                                if len(listaejecu)>(i+1):
                                    if listaejecu[i+1][0]=="ELSE":
                                        self.execute(listaejecu[i+1][1:])
                        if listaejecu[i][0][3:len(listaejecu[i][0])-5]=="not-facing-east":
                            if not self.facingeast():
                                self.execute(listaejecu[i][1:])
                            else: 
                                if len(listaejecu)>(i+1):
                                    if listaejecu[i+1][0]=="ELSE":
                                        self.execute(listaejecu[i+1][1:])
                        if listaejecu[i][0][3:len(listaejecu[i][0])-5]=="next-to-a-beeper":
                            if self.nexttoabeeper():
                                self.execute(listaejecu[i][1:])
                            else:
                                if len(listaejecu)>(i+1):
                                    if listaejecu[i+1][0]=="ELSE":
                                        self.execute(listaejecu[i+1][1:])
                        if listaejecu[i][0][3:len(listaejecu[i][0])-5]=="not-next-to-a-beeper":
                            if not self.nexttoabeeper():
                                self.execute(listaejecu[i][1:])
                            else:
                                if len(listaejecu)>(i+1):
                                    if listaejecu[i+1][0]=="ELSE":
                                        self.execute(listaejecu[i+1][1:])
                        if listaejecu[i][0][3:len(listaejecu[i][0])-5]=="front-is-clear":
                            if self.isclear(0):
                                self.execute(listaejecu[i][1:])
                            else:
                                if len(listaejecu)>(i+1):
                                    if listaejecu[i+1][0]=="ELSE":
                                        self.execute(listaejecu[i+1][1:])
                        if listaejecu[i][0][3:len(listaejecu[i][0])-5]=="front-is-blocked":
                            if not self.isclear(0):
                                self.execute(listaejecu[i][1:])
                            else:
                                if len(listaejecu)>(i+1):
                                    if listaejecu[i+1][0]=="ELSE":
                                        self.execute(listaejecu[i+1][1:])
                        if listaejecu[i][0][3:len(listaejecu[i][0])-5]=="left-is-clear":
                            if self.isclear(1):
                                self.execute(listaejecu[i][1:])
                            else:
                                if len(listaejecu)>(i+1):
                                    if listaejecu[i+1][0]=="ELSE":
                                        self.execute(listaejecu[i+1][1:])
                        if listaejecu[i][0][3:len(listaejecu[i][0])-5]=="left-is-blocked":
                            if not self.isclear(1):
                                self.execute(listaejecu[i][1:])
                            else:
                                if len(listaejecu)>(i+1):
                                    if listaejecu[i+1][0]=="ELSE":
                                        self.execute(listaejecu[i+1][1:])
                        if listaejecu[i][0][3:len(listaejecu[i][0])-5]=="right-is-clear":
                            if self.isclear(-1):
                                self.execute(listaejecu[i][1:])
                            else:
                                if len(listaejecu)>(i+1):
                                    if listaejecu[i+1][0]=="ELSE":
                                        self.execute(listaejecu[i+1][1:])
                        if listaejecu[i][0][3:len(listaejecu[i][0])-5]=="right-is-blocked":
                            if not self.isclear(-1):
                                self.execute(listaejecu[i][1:])
                            else:
                                if len(listaejecu)>(i+1):
                                    if listaejecu[i+1][0]=="ELSE":
                                        self.execute(listaejecu[i+1][1:])
                                        
                    if listaejecu[i][0][:6]=="WHILE " and listaejecu[i][0][len(listaejecu[i][0])-3:]==" DO":
                        if listaejecu[i][0][6:len(listaejecu[i][0])-3]=="facing-north":
                            while self.facingnorth():
                                self.execute(listaejecu[i][1:])
                        if listaejecu[i][0][6:len(listaejecu[i][0])-3]=="not-facing-north":
                            while not self.facingnorth():
                                self.execute(listaejecu[i][1:])
                        if listaejecu[i][0][6:len(listaejecu[i][0])-3]=="facing-south":
                            while self.facingsouth():
                                self.execute(listaejecu[i][1:])
                        if listaejecu[i][0][6:len(listaejecu[i][0])-3]=="not-facing-south":
                            while not self.facingsouth():
                                self.execute(listaejecu[i][1:])
                        if listaejecu[i][0][6:len(listaejecu[i][0])-3]=="facing-west":
                            while self.facingwest():
                                self.execute(listaejecu[i][1:])
                        if listaejecu[i][0][6:len(listaejecu[i][0])-3]=="not-facing-west":
                            while not self.facingwest():
                                self.execute(listaejecu[i][1:])
                        if listaejecu[i][0][6:len(listaejecu[i][0])-3]=="facing-east":
                            while self.facingeast():
                                self.execute(listaejecu[i][1:])
                        if listaejecu[i][0][6:len(listaejecu[i][0])-3]=="not-facing-east":
                            while not self.facingeast():
                                self.execute(listaejecu[i][1:])
                        if listaejecu[i][0][6:len(listaejecu[i][0])-3]=="next-to-a-beeper":
                            while self.nexttoabeeper():
                                self.execute(listaejecu[i][1:])
                        if listaejecu[i][0][6:len(listaejecu[i][0])-3]=="not-next-to-a-beeper":
                            while not self.nexttoabeeper():
                                self.execute(listaejecu[i][1:])
                        if listaejecu[i][0][6:len(listaejecu[i][0])-3]=="front-is-clear":
                            while self.isclear(0):
                                self.execute(listaejecu[i][1:])
                        if listaejecu[i][0][6:len(listaejecu[i][0])-3]=="front-is-blocked":
                            while not self.isclear(0):
                                self.execute(listaejecu[i][1:])
                        if listaejecu[i][0][6:len(listaejecu[i][0])-3]=="left-is-clear":
                            while self.isclear(1):
                                self.execute(listaejecu[i][1:])
                        if listaejecu[i][0][6:len(listaejecu[i][0])-3]=="left-is-blocked":
                            while not self.isclear(1):
                                self.execute(listaejecu[i][1:])
                        if listaejecu[i][0][6:len(listaejecu[i][0])-3]=="right-is-clear":
                            while self.isclear(-1):
                                self.execute(listaejecu[i][1:])
                        if listaejecu[i][0][6:len(listaejecu[i][0])-3]=="right-is-blocked":
                            while not self.isclear(-1):
                                self.execute(listaejecu[i][1:])
                                                
                    elif listaejecu[i][0][:4]=="ELSE":
                        None
                else:
                    try:
                        self.execute(diccionario[listaejecu[i]])
                    except:
                        self.lexicerror()
            wn.ontimer(None,100)  
            print(self)
            
#     ********ERRORES**********
    
    def lexicerror(self):
        """Levanta error de lexico"""
        raise ValueError("Error de lexico")
    def executionerror(self):
        """levanta error de ejecucion"""
        raise ValueError("Error de ejecucion")
    
#     ********PRUEBAS LOGICAS**********
    
    def facingeast(self):
        """Evalua si karel esta orientada al este"""
        if self.facing==0:
            return True
        else:
            return False
    def facingnorth(self):
        """Evalua si karel esta orientada al norte"""
        if self.facing==1:
            return True
        else:
            return False
    def facingwest(self):
        """Evalua si karel esta orientada al oeste"""
        if self.facing==2:
            return True
        else:
            return False
    def facingsouth(self):
        """Evalua si karel esta orientada al sur"""
        if self.facing==3:
            return True
        else:
            return False
    def nexttoabeeper(self):
        """Evalua si karel esta sobre un beeper"""
        if (self.x,self.y) in list(beepers.keys()):
            if len(beepers[self.x,self.y])!=0:
                return True
            else:
                return False
        else:
            return False
    def isclear(self,direc): 
        """Evalua si la direccion indicada esta bloqueada. 
        CERO ES PARA FRONT, 1 PARA LEFT, -1 PARA RIGHT"""
        m=self.facing+direc
        if m not in range(4):
            if m>=4:
                m=0
            else:
                m=3
        if m==0:
            if [self.x+25,self.y] in muros:
                return False
        elif m==1:
            if [self.x,25+self.y] in muros:
                return False
        elif m==2:
            if [self.x-25,self.y] in muros:
                return False
        else:
            if [self.x,self.y-25] in muros:
                return False
        return True
    def turnoff(self):
        """Cambia el titulo a -karel se ha apagado-"""
        wn.title("Karel se ha apagado")

# ***************COMPILACION***********************
# ****************************************************
# ****************************************************
# ***********CAMBIAR EL ARCHIVO AQUI******************
# ****************************************************
# ****************************************************


miArchivo=open("AndresIsazaQuiz2 (2).txt","r")




macrobloques=miArchivo.read().split("BEGINNING-OF-EXECUTION") #Divide entre definiciones y ejecucion
numbep=9999
karel=Karel(0,0,0,numbep)

ejecucionraw=macrobloques[1].split("\n") #Divide la ejecucion entre lineas
definicionesraw=macrobloques[0].split("\n")

for i in range(len(definicionesraw)):
    while definicionesraw[i][len(definicionesraw[i])-1:]==" " or definicionesraw[i][len(definicionesraw[i])-1:]=="\t":
        definicionesraw[i]=definicionesraw[i][:-1]

linea=0
while linea<len(definicionesraw):
    while definicionesraw[linea]=="":
        definicionesraw.pop(linea)
        if linea+1>len(definicionesraw):
            break
    linea+=1
        
if definicionesraw[0]=="BEGINNING-OF-PROGRAM":
    definiciones=tolist(1,definicionesraw[1:])
else: karel.lexicerror()

diccionario={}
for i in definiciones: #AGREGA LAS DEFINICIONES A UN DICCIONARIO CUYA CLAVE ES LA NUEVA FUNCION
    if i[0][:22]=="DEFINE-NEW-INSTRUCTION":
        x=i[0].find(" AS")
        a=(i[0][23:x])
        diccionario[a+";"]=i[1:]
        
for i in range(len(ejecucionraw)):
    while ejecucionraw[i][len(ejecucionraw[i])-1:]==" " or ejecucionraw[i][len(ejecucionraw[i])-1:]=="\t":
        ejecucionraw[i]=ejecucionraw[i][:-1]
linea=0
while linea<len(ejecucionraw):
    while ejecucionraw[linea]=="":
        ejecucionraw.pop(linea)
        if linea+1>len(ejecucionraw):
            break
    linea+=1

ejecucion=tolist(2,ejecucionraw)


# ******************************INTERFAZ****************************
kl=turtle.Turtle()
kl.ht()
kl.penup()
wn=turtle.Screen()
bep=turtle.Turtle()
bep.ht()
wn.screensize(150,150)
wn.title("El mundo de Karel")
wn.bgcolor("White")
visualk=turtle.Turtle()
visualk.ht()
visualk.pencolor("Blue")
visualk.pensize(3)
visualk.penup()
visualk.goto(-250,-250)
visualk.pendown()
visualk.speed(0)
visualk.pensize(2)

for i in range(2):
    for i in range(5):
        visualk.forward(500)
        visualk.left(90)
        visualk.forward(100)
        visualk.back(50)
        visualk.left(90)
        visualk.forward(500)
        visualk.right(90)
        visualk.forward(50)
        visualk.right(90)
    visualk.right(90)
visualk.forward(500)
visualk.goto(-250,-250)
wn.title("SITUE LOS MUROS (CLICK, LUEGO ARRASTRAR LENTAMENTE). AL TERMINAR PRESIONE ESPACIO")
visualk.shape("square")
visualk.color("black")
visualk.penup()
muros=[]
beepers={}
wn.onclick(iracentro)
visualk.ondrag(situarmuros)
wn.onkey(exitf,"space")
wn.onkey(POSICIONAR,"Return")

wn.listen()
wn.mainloop()


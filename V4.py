def tolist(contador,listraw):
    newlist=[]
    i=0
    while (i)<len(listraw):
        listraw[i]=listraw[i][contador:]
        if len(listraw[i])!=0:
            if listraw[i]=="turnoff":
                for x in reversed(range(len(listraw)-i)):
                    listraw.append(listraw[len(listraw)-1-x])
                break
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
        self.facing=facing #0 es este, 1 es norte, 2 es oeste, 3 es sur.
        self.x=x 
        self.y=y 
        self.beepers=beepers
    def __str__(self): #Este metodo es mientras desarrollamos la interfaz para saber que hace Karel
        return "Facing: {0}, pos:({1},{2}), beepers:{3}".format(self.facing,self.x,self.y,self.beepers)
    
#     ********FUNCIONES BASICAS**********
    
    def move(self):
        if self.facing==0:
            self.x+=1
        elif self.facing==1:
            self.y+=1
        elif self.facing==2:
            self.x-=1
        else:
            self.y-=1
    def turnleft(self):
        if self.facing==3:
            self.facing=0
        else:
            self.facing+=1
    def pickbeeper(self):
        self.beepers+=1
    def putbeeper(self):
        self.beepers-=1
        
#     ********EJECUCION**********
    
    def execute(self,i):
        print(i)
        if i!="":
            if i=="move;":
                self.move()
            elif i=="turnleft;":
                self.turnleft()
            elif i=="pickbeeper;":
                self.pickbeeper()
            elif i=="putbeeper;":
                self.puteeper()
            elif i=="turnoff" or i=="turnoff":
                a=1
            elif type(i) is list:
                if i[0][:7]=="ITERATE":
                    x=i[0].find(" TIMES")
                    a=(i[0][8:x])
                    for q in range(int(a)):
                        for p in i[1:]:
                            self.execute(p)
                if i[0][:2]=="IF":
                    a=2
            else:
                    for y in diccionario[i]:
                        self.execute(y)  
        print(self)
        
#     ********ERRORES**********
    
    def lexicerror(self):
        raise ValueError("Error de lexico")
    def executionerror(self):
        raise ValueError("Error de ejecucion")
    
#     ********PRUEBAS LOGICAS**********
    
    def facingeast(self):
        if self.facing==0:
            return True
        else:
            return False
    def facingnorth(self):
        if self.facing==1:
            return True
        else:
            return False
    def facingwest(self):
        if self.facing==2:
            return True
        else:
            return False
    def facingsouth(self):
        if self.facing==3:
            return True
        else:
            return False
    #def turnoff(self):

miArchivo=open("AndresIsazaQuiz2.txt","r")
macrobloques=miArchivo.read().split("BEGINNING-OF-EXECUTION") #Divide entre definiciones y ejecucion
karel=Karel()
ejecucionraw=macrobloques[1].split("\n") #Divide la ejecucion entre lineas
definicionesraw=macrobloques[0].split("\n")
if definicionesraw[0]=="BEGINNING-OF-PROGRAM":
    definiciones=tolist(1,definicionesraw[1:])
else: karel.lexicerror()
diccionario={}
for i in definiciones: #AGREGA LAS DEFINICIONES A UN DICCIONARIO CUYA CLAVE ES LA NUEVA FUNCION
    if i[0][:22]=="DEFINE-NEW-INSTRUCTION":
        x=i[0].find(" AS")
        a=(i[0][23:x])
        diccionario[a+";"]=i[1:]
print(diccionario)
ejecucion=tolist(2,ejecucionraw)
print(ejecucion)
a=0
for i in ejecucion:
    karel.execute(i)
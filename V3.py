class Karel:
    def __init__(self,facing=0,x=0,y=0,beepers=0):
        self.facing=facing #0 es este, 1 es norte, 2 es oeste, 3 es sur.
        self.x=x 
        self.y=y 
        self.beepers=beepers
    def __str__(self): #Este metodo es mientras desarrollamos la interfaz para saber que hace Karel
        return "Facing: {0}, pos:({1},{2}), beepers:{3}".format(self.facing,self.x,self.y,self.beepers)
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
    def execute(self,i):
        if i!="":
            if i=="move;":
                self.move()
            elif i=="turnleft;":
                self.turnleft()
            elif i=="pickbeeper;":
                self.pickbeeper()
            elif i=="putbeeper;":
                self.puteeper()
#           elif i=="turnoff":
#                 self.turnoff()
            elif type(i) is list:
                if i[0][:7]=="ITERATE":
                    i[0]=i[0][:i[0].find(" TIMES")]
                    a=(i[0][8:])
                    for q in range(int(a)):
                        for p in i[1:]:
                            self.execute(p)
        print(self)
        
    def putbeeper(self):
        self.beepers-=1
    def lexicerror(self):
        raise ValueError("Error de lexico")
    def executionerror(self):
        raise ValueError("Error de ejecucion")
    #def turnoff(self):
    
miArchivo=open("AndresIsazaQuiz2.txt","r")
macrobloques=miArchivo.read().split("BEGINNING-OF-EXECUTION") #Divide entre definiciones y ejecucion
karel=Karel()
ejecucionraw=macrobloques[1].split("\n") #Divide la ejecucion entre lineas
print(ejecucionraw)

for i in reversed(range(len(ejecucionraw))): #Quita las lineas vacias y dos tabulaciones al cuerpo de ejecucion
    if ejecucionraw[i]!="\tEND-OF-EXECUTION": #Excepto END-OF-EXECUTION Y END-OF-PROGRAM
        if ejecucionraw[i]!="END-OF-PROGRAM":
            ejecucionraw[i]=ejecucionraw[i][2:]
    if ejecucionraw[i]=="":
        ejecucionraw.pop(i)
print(ejecucionraw)
i=0
ejecucion=[]
while i<len(ejecucionraw):
    if ejecucionraw[i]=="turnoff":
        ejecucion.append([ejecucionraw[i],ejecucionraw[i+1],ejecucionraw[i+2]])
        i+=3
    else:
        if ejecucionraw[i][len(ejecucionraw[i])-1]!=";":
            block=[]
            while ejecucionraw[i]!="END;":
                block.append(ejecucionraw.pop(i))
            block.pop(1)
            block[len(block)-1]+=";"
            for q in range(len(block)):
                if block[q][:1]=="\t":
                    block[q]=block[q][1:]
            ejecucion.append(block)
            ejecucionraw.pop(i)
        else:
            ejecucion.append(ejecucionraw[i])
            i+=1
print(ejecucion)
for i in ejecucion:
    karel.execute(i)

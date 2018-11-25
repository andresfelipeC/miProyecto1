# class Karel:
#     
#     def __init__(self,facing=0,x=0,y=0,beepers=0):
#         self.facing=facing #0 es este, 1 es norte, 2 es oeste, 3 es sur.
#         self.x=x 
#         self.y=y 
#         self.beepers=beepers
#     
#     def __str__(self): #Este metodo es mientras desarrollamos la interfaz para saber que hace Karel
#         return "Facing: {0}, pos:({1},{2}), beepers:{3}".format(self.facing,self.x,self.y,self.beepers)
#         
#     def move(self):
#         if self.facing==0:
#             self.x+=1
#         elif self.facing==1:
#             self.y+=1
#         elif self.facing==2:
#             self.x-=1
#         else:
#             self.y-=1
#             
#     def turnleft(self):
#         self.facing+=1
#         
#     def pickbeeper(self):
#         self.beepers+=1
#     
#     def putbeeper(self):
#         self.beepers-=1
#         
#     def lexicerror(self):
#         raise ValueError("Error de léxico")
#     
#     def executionerror(self):
#         raise ValueError("Error de ejecución")
# 
#     #def turnoff(self):
#         
# 
# miArchivo=open("AndresIsazaQuiz2.txt","r")
# lineas=miArchivo.read().split("\n")
# karel=Karel()
# for i in range(len(lineas)):
#     if lineas[i]=="\tBEGINNING-OF-EXECUTION":
#         definiciones=lineas[:i]
#         ejecucion=lineas[(i+1):]
#         
# print(definiciones)
# print(ejecucion)
# print(karel)
# tabcount=0
# ejecucion1=[]
# for i in ejecucion:
#     print(i)
#     if i[len(i)-1]==";":
#         ejecucion1+=i
#     print(ejecucion1)
# 
# for i in ejecucion:
#     if i=="move;":
#         karel.move()
#     elif i=="turnleft;":
#         karel.turnleft()
#     elif i=="pickbeeper;":
#         karel.pickbeeper()
#     elif i=="putbeeper;":
#         karel.puteeper()
#     
#     print(karel)
#         
print("banana".find("na"))
print("banana"[:2])

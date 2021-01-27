#-*-coding:Latin-1 -*
import os
import numpy as np

class tic:

 def __init__(self):
                      self.ticmat=np.full((3, 3), '*')



 def ticprnt(self):
                   j=0
                   print()
                   print("  0\t\t1\t\t2")
                   while j < 3:
                               print(j,"\t\t".join(self.ticmat[j]))
                               print()
                               j+=1

 def ticwin(self):
                  i=0
                  j=0
                  while i < 3:
                              if (("".join(self.ticmat[i]) == "XXX") or
                                 (("".join(self.ticmat[i]) == "OOO"))
 or ("".join(self.ticmat[j][i]) + "".join(self.ticmat[j+1][i]) + "".join(self.ticmat[j+2][i]) == "OOO")
 or ("".join(self.ticmat[j][i]) + "".join(self.ticmat[j + 1][i]) + "".join(self.ticmat[j + 2][i]) == "XXX")
 or ("".join(self.ticmat[0][0]) + "".join(self.ticmat[1][1]) + "".join(self.ticmat[2][2]) == "XXX")
 or ("".join(self.ticmat[0][0]) + "".join(self.ticmat[1][1]) + "".join( self.ticmat[2][2]) == "OOO")
or ("".join(self.ticmat[0][2]) + "".join(self.ticmat[1][1]) + "".join(self.ticmat[2][0]) == "XXX")
or ("".join(self.ticmat[0][2]) + "".join(self.ticmat[1][1]) + "".join(self.ticmat[2][0]) == "OOO")
                                                                           ):
                                                                              print("***************************************")
                                                                              if ("".join(self.ticmat[i])=="XXX"
                                                                              or "".join(self.ticmat[j][i])=="X"
                                                                              or "".join(self.ticmat[2][0])=="X"):
                                                                                                                  print("player1 win")
                                                                                                                  print(
                                                                                              "***************************************")
                                                                                                                  return True
                                                                                                                  break

                                                                              else:
                                                                                   print("player2 win")
                                                                                   print("***************************************")
                                                                                   return True
                                                                                   break



                              i += 1


 def ticplay(self):
                   print()
                   print("player1 : X\nplayer2 : O")
                   t.ticprnt()
                   j=0
                   while j<9:
                              print("\nlet's go player1")
                              self.ticmat[int(input("put index1:"))][int(input("put index2:"))]="X"
                              t.ticprnt()
                              if(t.ticwin()==True):
                                                   break
                              print("\nlet's go player2")
                              self.ticmat[int(input("put index1:"))][int(input("put index2:"))] = "O"
                              t.ticprnt()
                              if (t.ticwin() == True):
                                                      break

                              j=+1






while 1:
            t=tic()
            t.ticplay()
            newg = input('Replay the game put r // Exit put q : ')

            if newg.lower() != 'r':
                print("End game")
                break

os.system("pause")
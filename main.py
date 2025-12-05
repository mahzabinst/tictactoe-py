#loading modules
import pygame as pg #setting nickname for pygame
from sys import exit #importing the exit 

#initializing pygame
pg.init()


#creating SCREEN window
width=600
length=600
wind=pg.display.set_mode((width,length))#creating screen 
pg.display.set_caption("tictactoe")#naming screen name


#loading images+setting the rects
board_img=pg.image.load("assets/board.png").convert_alpha()#loading the png+as optimized

font=pg.font.Font("assets/arial.ttf",24)#loading the font

label_info=font.render("PLAYER 1 TURN",True,(255,255,255))#creating the text to apppear
label_info_rect=label_info.get_rect(center=(300,30))#setting the texts position

cross_img=pg.image.load("assets/cross.png").convert_alpha()
circle_img=pg.image.load("assets/circle.png").convert_alpha()
button_img=pg.image.load("assets/button.png").convert_alpha()

button_img_rect=button_img.get_rect(center=(300,550))

block_size=120  #since its a square shaped
is_p1_chance=True #always 1st turn is p1's
who_won=False #is it p1 /p2 /draw?

pos=(0,0)#position where the mouse clicked
chance_count=0 #max chance 9 , in 3x3 there are 9 boxes
result=None #result of whether 

pieces=[] #for every turn/clicks preserve it img +location
matrix=[
     ["-","-","-"],
     ["-","-","-"],
     ["-","-","-"]
]

clock=pg.time.Clock()#locking the fps


#function to check if the clicked position is a valid position 
def checkClickedpos(pos): #to check valid clicks
     if (pos[0]>120 and pos[0]<240) and (pos[1]>120 and pos[1]<240):
          return (1,1)
     elif (pos[0]>240 and pos[0]<360) and (pos[1]>120 and pos[1]<240):
           return (1,2)
     elif (pos[0]>360 and pos[0]<480) and (pos[1]>120 and pos[1]<240):
           return (1,3)
     elif (pos[0]>120 and pos[0]<240) and (pos[1]>240 and pos[1]<360):
          return (2,1)
     elif (pos[0]>240 and pos[0]<360) and (pos[1]>240 and pos[1]<360):
          return (2,2)
     elif (pos[0]>360 and pos[0]<480) and (pos[1]>240 and pos[1]<360):
           return(2,3)
     elif (pos[0]>120 and pos[0]<240) and (pos[1]>360 and pos[1]<480):
          return (3,1)
     elif (pos[0]>240 and pos[0]<360) and (pos[1]>360 and pos[1]<480):
          return (3,2)
     elif (pos[0]>360 and pos[0]<480) and (pos[1]>360 and pos[1]<480):
          return (3,3)
     return None



#function to check if someone wins 
def checkWinner(matrix):

     # for 3 rows:
     for i in range(0,3):#[i]=row here changing when loop runs
          if matrix[i][0]==matrix[i][1]==matrix[i][2]:
               if matrix[i][0]=="x":
                    winner="PLAYER 1 is winner"
               elif matrix[i][0]=="o":
                    winner="PLAYER 2 is winner"
               if matrix[i][0]!="-":
                    return winner,(120,120*(i+1)+60),(480,120*(i+1)+60) #this coordinates for strike line , for x: line starting, ending xi,xf are fixed (120 to 480)
               # strike line needed to place in the middle (+60), for each 3 rows :120,240,360

     #for 3 columns:
     for i in range(0,3):#[j]= colmn ,here changing when loop runs
          if matrix[0][i]==matrix[1][i]==matrix==[2][i]:
               if matrix[0][i]=="x":
                    winner="PLAYER 1 is winner"
               elif matrix[0][i]=="o":
                    winner="PLAYER 2 is winner"
               if matrix[0][i]!="-":
                    return winner,(120*(i+1)+60,120),(120*(i+1)+60,480)
     

     #for 1st diagonal:
     if matrix[0][0]==matrix[1][1]==matrix[2][2]:
          if matrix[0][0]=="x":
               winner="PLAYER 1 is winner"
          elif matrix[0][0]=="o":
               winner="PLAYER 2 is winner"
          if matrix[0][0]!="-":
               return winner,(120,120),(480,480)#as for diagonal (\) starting ending are fixed 
     


     #for 2nd diagonal:      
     if matrix[0][2]==matrix[1][1]==matrix[2][0]:
          if matrix[0][2]=="x":
               winner="PLAYER 1 is winner"
          elif matrix[0][2]=="o":
               winner="PLAYER 2 is winner"
          if matrix[0][2]!="-":
               return winner,(480,120),(120,480) #as for diagonal (/) starting ending are fixed 
     
     return "NO ONE IS WINNER",(0,0)

                  







#function to restart the game 
def restart():
     global is_p1_chance,who_won, pos,chance_count,result,pieces,matrix,label_info

     is_p1_chance=True #always 1st turn is p1's
     who_won=False  #is it p1 /p2 /draw?
     
     pos=(0,0) #position where the mouse clicked
     chance_count=0 #max chance 9 , in 3x3 there are 9 boxes
     result=None #result of whether 

     pieces=[] #for every turn/clicks preserve it img +location
     matrix=[
          ["-","-","-"],
          ["-","-","-"],
          ["-","-","-"]
     ]
     label_info=font.render("PLAYER 1 TURN",True,(255,255,255))




#GAME LOOP 
while True: #how long screen can stay open

     #event handling
     for event in pg.event.get():#accessing the recently happened event from a list format(pg syntax)
          if event.type==pg.QUIT:
               pg.quit()#exit from pygame environment
               exit() #calling the exit function

          if event.type==pg.MOUSEBUTTONUP:#check if mouse got clicked??+user released the mouse
               pos=pg.mouse.get_pos()#that clicked coordinate gets saved in pos tuple


          if event.type==pg.MOUSEBUTTONDOWN:
               if button_img_rect.collidepoint(pg.mouse.get_pos()):
                    restart()




     #check clicked position validation
     result=checkClickedpos(pos)


#logic to place cross and circle
     if result!= None:
          if matrix[result[0]-1][result[1]-1]=="-":
          #only if matrix is blank , then we can save x or o>>  


               if is_p1_chance:# when +for whom to append 
                    pieces.append([cross_img,block_size*result[1]+20,block_size*result[0]+20])
                    is_p1_chance=False#one time editable
                    matrix[result[0]-1][result[1]-1]="x" #saved it for cross

                    #now p1's chance/turn done , time for p2 :)
                    label_info=font.render("PLAYER 2 TURN",True,(255,255,255))
               
               else:
                    pieces.append([circle_img,block_size*result[1]+20,block_size*result[0]+20])
                    is_p1_chance=True
                    matrix[result[0]-1][result[1]-1]="o"#saved it for circle

                    #now p2's chance/turn done , agan time for p1 :)
                    label_info=font.render("PLAYER 1 TURN",True,(255,255,255))
               chance_count+=1


               score=checkWinner(matrix)
               if score[1]!=(0,0) :
                    label_info=font.render(score[0],True,(255,255,255))
                    who_won=True
                     
     #reset pos                
     pos=(0,0) #again ini the position,to avoid overlapping



########## draw everything on screen & display ########
##########                                     ########

     #blending the board color with the screen color
     wind.fill((18,18,18))

     #placing the board img 
     wind.blit(board_img,(120,120))
     wind.blit(label_info,label_info_rect) #displaying the label+where to display on?
     
     for piece in pieces:#displaying the X,O
          wind.blit(piece[0],(piece[1],piece[2]))
     

     #when to show the RESTART BUTTON ?
     if who_won==True or chance_count==9:
          if who_won: #draw the strike line 
               pg.draw.line(wind,(255,255,255),score[1],score[2])
          else:#when no one wins ,display "DRAW"
               label_info=font.render(score[0],True,(255,255,255))
     wind.blit(button_img,button_img_rect)#displaying the restart button n a rectangle
           
           
     
     pg.display.update()#in every turn,updating the screen 
     clock.tick(60) #locking fps by 60 frames

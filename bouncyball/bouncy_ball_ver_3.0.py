from vpython import *
from math import*
from random import *
from time import *

gravity=vector(0,0,-9.8)     #중력장

gravitation=-98
bound_force=55
mainball_diameter=2

choarow=arrow(pos=(-3,1.5,0),axis=(1,0,0),shaftwidth=0.1,color=color.yellow)

f=open('saved.txt','a')
f.close()

eastegg=0
copy_box=box(visible=False)

f=0.5   #저항

scene.userzoom=False
scene.userspin=False

class boxdata:
    def __init__(self,starslist=[],bumperslist=[]):
        self.starslist=starslist
        self.bumperslist=bumperslist



def mapmaking():
    global Xlines, Ylines, Zlines, Xarrows, Yarrows, Zarrows, game_making_list, boxes_making_list, gravitation,bound_force,mainball_diameter, copy_box
    
    Xlines=1
    Ylines=1
    Zlines=1
    Xarrows=[]
    Yarrows=[]
    Zarrows=[]
    game_making_list=[[[0]]]
    boxes_making_list=[[[box(visible=False)]]]

    Xarrows.append([arrow(pos=(0,0,0),axis=(1.2,0,0),shaftwidth=0.1,opacity=0.01),arrow(pos=(0,0,1),axis=(1,0,0),shaftwidth=0.1,opacity=0.01)])
    Xarrows.append([arrow(pos=(0,1,0),axis=(1.2,0,0),shaftwidth=0.1,opacity=0.01),arrow(pos=(0,1,1),axis=(1,0,0),shaftwidth=0.1,opacity=0.01)])
    Yarrows.append([arrow(pos=(0,0,0),axis=(0,1.2,0),shaftwidth=0.1,opacity=0.01),arrow(pos=(0,0,1),axis=(0,1,0),shaftwidth=0.1,opacity=0.01)])
    Yarrows.append([arrow(pos=(1,0,0),axis=(0,1.2,0),shaftwidth=0.1,opacity=0.01),arrow(pos=(1,0,1),axis=(0,1,0),shaftwidth=0.1,opacity=0.01)])
    Zarrows.append([arrow(pos=(0,0,0),axis=(0,0,1.2),shaftwidth=0.1,opacity=0.01),arrow(pos=(0,1,0),axis=(0,0,1),shaftwidth=0.1,opacity=0.01)])
    Zarrows.append([arrow(pos=(1,0,0),axis=(0,0,1.2),shaftwidth=0.1,opacity=0.01),arrow(pos=(1,1,0),axis=(0,0,1),shaftwidth=0.1,opacity=0.01)])

    choosebox=box(pos=(0.5,0.5,0.5),size=(1,1,1),color=color.cyan,opacity=0.5)

    chooseX=0
    chooseY=0
    chooseZ=0

    while True:

        print ("game started")

        c=scene.kb.getkey()
        if c=='f1':
            print('choose the area by up, down, right, left, up page, down page keys.\nand you can make or change box with space bar\n You can delete it with delete or back space')
            rate(1)
            print("you can use tab to see how and what you can change the box's charactor.")
        if c=='up':
            if chooseY>=Ylines-1:
                yincrease()
            chooseY+=1
            choosebox.pos.y+=1
            scene.center=choosebox.pos

        elif c=='down':
            if chooseY>0:
                chooseY-=1
                choosebox.pos.y-=1
                scene.center=choosebox.pos
            else:
                yminincrease()

        elif c=='right':
            if chooseX>=Xlines-1:
                xincrease()
            chooseX+=1
            choosebox.pos.x+=1
            scene.center=choosebox.pos

        elif c=='left':
            if chooseX>0:
                chooseX-=1
                choosebox.pos.x-=1
                scene.center=choosebox.pos
            else:
                xminincrease()

        elif c=='page up':
            if chooseZ>=Zlines-1:
                zincrease()
            chooseZ+=1
            choosebox.pos.z+=1
            scene.center=choosebox.pos

        elif c=='page down':
            if chooseZ>0:
                chooseZ-=1
                choosebox.pos.z-=1
                scene.center=choosebox.pos
            else:
                zminincrease()

        elif c=='back space' or c== 'delete':
            boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].visible=False
            boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]=box(visible=False)
            game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]=0

        elif c=='ctrl+c':
            box_copy=[game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)],boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]]

        elif c=='ctrl+v':
            game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]=box_copy[0]
            boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].visible=False
            if box_copy[0]==0:
                pass
            elif box_copy[0]==1:
                boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]=box(pos=choosebox.pos,num=1)
            elif box_copy[0]==2:
                pass
            elif box_copy[0]==3:
                boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]=sphere(pos=choosebox.pos,num=3,color=color.yellow,radius=box_copy[1].radius,diameter=box_copy[1].diameter)
            elif box_copy[0]==4:
                A=frame(num=4,pos=choosebox.pos,times=box_copy[1].times)
                c=(random(),random(),random())
                A1=box(pos=(0.3,0.3,0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                A2=box(pos=(0.3,0.3,-0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                A3=box(pos=(0.3,-0.3,0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                A4=box(pos=(-0.3,0.3,0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                A5=box(pos=(0.3,-0.3,-0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                A6=box(pos=(-0.3,-0.3,0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                A7=box(pos=(-0.3,0.3,-0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                A8=box(pos=(-0.3,-0.3,-0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                if A.times==2:
                    Acen=box(pos=(0,0,0),size=(0.4,0.4,0.4),frame=A,color=c)
                boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]=A

            elif box_copy[0]==5:
                boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]=box(size=(1,1,1),pos=choosebox.pos,num=5,color=box_copy[1].color,Ttimes=box_copy[1].Ttimes)

            elif box_copy[0]==6:
                A=frame(pos=choosebox.pos,num=6,thorn=box_copy[1].thorn,elv=box_copy[1].elv)
                if A.thorn==1:
                    A1=pyramid(pos=(0,0,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                    A2=pyramid(pos=(0.3,0.3,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                    A3=pyramid(pos=(0.3,-0.3,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                    A4=pyramid(pos=(-0.3,0.3,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                    A5=pyramid(pos=(-0.3,-0.3,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                    A6=pyramid(pos=(0.3,0,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                    A7=pyramid(pos=(0,0.3,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                    A8=pyramid(pos=(0,-0.3,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                    A9=pyramid(pos=(-0.3,0,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                    A10=box(pos=(0,0,-0.05+0.2*A.elv),size=(1,1,0.1),color=(0.5,1,0.5),frame=A)
                    A.center=A10
                elif A.thorn==-1:
                    B1=pyramid(pos=(0,0,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                    B2=pyramid(pos=(0.3,0.3,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                    B3=pyramid(pos=(0.3,-0.3,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                    B4=pyramid(pos=(-0.3,0.3,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                    B5=pyramid(pos=(-0.3,-0.3,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                    B6=pyramid(pos=(0.3,0,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                    B7=pyramid(pos=(0,0.3,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                    B8=pyramid(pos=(0,-0.3,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                    B9=pyramid(pos=(-0.3,0,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                    B10=box(pos=(0,0,0.05+0.2*A.elv),size=(1,1,0.1),color=(0.5,1,0.5),frame=A)
                    A.center=B10
                elif A.thorn==0:
                    C1=pyramid(pos=(0,0,-0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                    C2=pyramid(pos=(0.3,0.3,-0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                    C3=pyramid(pos=(0.3,-0.3,-0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                    C4=pyramid(pos=(-0.3,0.3,-0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                    C5=pyramid(pos=(-0.3,-0.3,-0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                    C6=pyramid(pos=(0.3,0,-0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                    C7=pyramid(pos=(0,0.3,-0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                    C8=pyramid(pos=(0,-0.3,-0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                    C9=pyramid(pos=(-0.3,0,-0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                    C10=box(pos=(0,0,0.2*A.elv),size=(1,1,0.1),color=(0.5,1,0.5),frame=A)
                    C11=pyramid(pos=(0,0,0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                    C12=pyramid(pos=(0.3,0.3,0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                    C13=pyramid(pos=(0.3,-0.3,0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                    C14=pyramid(pos=(-0.3,0.3,0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                    C15=pyramid(pos=(-0.3,-0.3,0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                    C16=pyramid(pos=(0.3,0,0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                    C17=pyramid(pos=(0,0.3,0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                    C18=pyramid(pos=(0,-0.3,0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                    C19=pyramid(pos=(-0.3,0,0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                    A.center=C10
                boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]=A

            elif box_copy[0]==7:
                A=frame(num=9,pos=choosebox.pos,velocity=vector(0,0,0), gen=box_copy[1].gen, trying=box_copy[1].trying)
                A1=box(pos=(0.3,0.3,0.3),size=(0.4,0.4,0.4),frame=A,color=(0.2,0.3,1),opacity=0.3)
                A2=box(pos=(0.3,0.3,-0.3),size=(0.4,0.4,0.4),frame=A,color=(0.2,0.3,1),opacity=0.3)
                A3=box(pos=(0.3,-0.3,0.3),size=(0.4,0.4,0.4),frame=A,color=(0.2,0.3,1),opacity=0.3)
                A4=box(pos=(-0.3,0.3,0.3),size=(0.4,0.4,0.4),frame=A,color=(0.2,0.3,1),opacity=0.3)
                A5=box(pos=(0.3,-0.3,-0.3),size=(0.4,0.4,0.4),frame=A,color=(0.2,0.3,1),opacity=0.3)
                A6=box(pos=(-0.3,-0.3,0.3),size=(0.4,0.4,0.4),frame=A,color=(0.2,0.3,1),opacity=0.3)
                A7=box(pos=(-0.3,0.3,-0.3),size=(0.4,0.4,0.4),frame=A,color=(0.2,0.3,1),opacity=0.3)
                A8=box(pos=(-0.3,-0.3,-0.3),size=(0.4,0.4,0.4),frame=A,color=(0.2,0.3,1),opacity=0.3)
                A9=box(pos=(0,0,0),size=(1,1,1),frame=A,opacity=0.3,color=(0.9,0.9,0.9))
                boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]=A

            elif box_copy[0]==8:
                A=frame(pos=choosebox.pos, eff=box_copy[1].eff, num=8)
                A0=box(size=(0.8,0.8,0.8),pos=(0,0,0),frame=A)
                if A.eff==0:
                    A1=arrow(pos=(0.2,0.4,0.45),axis=(0,0,-0.8),color=color.yellow,frame=A)
                    A2=arrow(pos=(-0.2,0.4,-0.45),axis=(0,0,0.8),color=color.yellow,frame=A)
                    A3=arrow(pos=(0.2,-0.4,-0.45),axis=(0,0,0.8),color=color.yellow,frame=A)
                    A4=arrow(pos=(-0.2,-0.4,0.45),axis=(0,0,-0.8),color=color.yellow,frame=A)
                    A5=arrow(pos=(0.4,-0.2,0.45),axis=(0,0,-0.8),color=color.yellow,frame=A)
                    A6=arrow(pos=(0.4,0.2,-0.45),axis=(0,0,0.8),color=color.yellow,frame=A)
                    A7=arrow(pos=(-0.4,-0.2,-0.45),axis=(0,0,0.8),color=color.yellow,frame=A)
                    A8=arrow(pos=(-0.4,0.2,0.45),axis=(0,0,-0.8),color=color.yellow,frame=A)
                elif A.eff==1:
                    B1=arrow(pos=(0,0.4,-0.25),axis=(0,0,0.5),color=color.red,frame=A)
                    B2=arrow(pos=(0,-0.4,-0.25),axis=(0,0,0.5),color=color.red,frame=A)
                    B3=arrow(pos=(0.4,0,-0.25),axis=(0,0,0.5),color=color.red,frame=A)
                    B4=arrow(pos=(-0.4,0,-0.25),axis=(0,0,0.5),color=color.red,frame=A)
                elif A.eff==2:
                    C1=arrow(pos=(0.4,0.2,0.45),axis=(0,-0.8,0),color=color.red,frame=A)
                    C2=arrow(pos=(0.4,-0.2,-0.45),axis=(0,0.8,0),color=color.red,frame=A)
                    C3=arrow(pos=(-0.4,-0.2,0.45),axis=(0,0.8,0),color=color.red,frame=A)
                    C4=arrow(pos=(-0.4,0.2,-0.45),axis=(0,-0.8,0),color=color.red,frame=A)
                    C5=arrow(pos=(-0.2,0.4,0.45),axis=(0.8,0,0),color=color.red,frame=A)
                    C6=arrow(pos=(0.2,0.4,-0.45),axis=(-0.8,0,0),color=color.red,frame=A)
                    C7=arrow(pos=(-0.2,-0.4,-0.45),axis=(0.8,0,0),color=color.red,frame=A)
                    C8=arrow(pos=(0.2,-0.4,0.45),axis=(-0.8,0,0),color=color.red,frame=A)
                boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]=A

            elif box_copy[0]==9:
                A=sphere(radius=box_copy[1].radius,color=box_copy[1].color,pos=choosebox.pos,num=11, diameter=box_copy[1].diameter, reforce=box_copy[1].reforce)
                boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]=A
                
        elif c==' ':
            game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]+=1
            game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]%=10
            boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].visible=False
            if game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==0:
               boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]=box(visible=False)
            elif game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==1:
                boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]=box(pos=choosebox.pos,size=(1,1,1),num=1)
            elif game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==2:
                boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]=text(pos=choosebox.pos,text='S',num=2,align='center',width=0.5,height=0.5)
            elif game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==3:
                boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]=sphere(pos=choosebox.pos,num=3,radius=0.2,color=color.yellow,diameter=4)
            elif game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==4:
                A=frame(num=4,pos=choosebox.pos,times=1)
                c=(random(),random(),random())
                A1=box(pos=(0.3,0.3,0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                A2=box(pos=(0.3,0.3,-0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                A3=box(pos=(0.3,-0.3,0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                A4=box(pos=(-0.3,0.3,0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                A5=box(pos=(0.3,-0.3,-0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                A6=box(pos=(-0.3,-0.3,0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                A7=box(pos=(-0.3,0.3,-0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                A8=box(pos=(-0.3,-0.3,-0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]=A
            
            elif game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==5:
                A=box(size=(1,1,1),pos=choosebox.pos,num=6,color=(1,0,0),Ttimes=0)                
                boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]=A
            
            elif game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==6:
                A=frame(num=8,pos=choosebox.pos,thorn=1,elv=-2)
                A1=pyramid(pos=(0,0,-0.4),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                A2=pyramid(pos=(0.3,0.3,-0.4),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                A3=pyramid(pos=(0.3,-0.3,-0.4),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                A4=pyramid(pos=(-0.3,0.3,-0.4),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                A5=pyramid(pos=(-0.3,-0.3,-0.4),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                A6=pyramid(pos=(0.3,0,-0.4),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                A7=pyramid(pos=(0,0.3,-0.4),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                A8=pyramid(pos=(0,-0.3,-0.4),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                A9=pyramid(pos=(-0.3,0,-0.4),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                A10=box(pos=(0,0,-0.45),size=(1,1,0.1),color=(0.5,1,0.5),frame=A)
                boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]=A
                
            elif game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==7:
                A=frame(num=9,pos=choosebox.pos,velocity=vector(0,0,0), gen=2, trying=0)
                A1=box(pos=(0.3,0.3,0.3),size=(0.4,0.4,0.4),frame=A,color=(0.2,0.3,1),opacity=0.3)
                A2=box(pos=(0.3,0.3,-0.3),size=(0.4,0.4,0.4),frame=A,color=(0.2,0.3,1),opacity=0.3)
                A3=box(pos=(0.3,-0.3,0.3),size=(0.4,0.4,0.4),frame=A,color=(0.2,0.3,1),opacity=0.3)
                A4=box(pos=(-0.3,0.3,0.3),size=(0.4,0.4,0.4),frame=A,color=(0.2,0.3,1),opacity=0.3)
                A5=box(pos=(0.3,-0.3,-0.3),size=(0.4,0.4,0.4),frame=A,color=(0.2,0.3,1),opacity=0.3)
                A6=box(pos=(-0.3,-0.3,0.3),size=(0.4,0.4,0.4),frame=A,color=(0.2,0.3,1),opacity=0.3)
                A7=box(pos=(-0.3,0.3,-0.3),size=(0.4,0.4,0.4),frame=A,color=(0.2,0.3,1),opacity=0.3)
                A8=box(pos=(-0.3,-0.3,-0.3),size=(0.4,0.4,0.4),frame=A,color=(0.2,0.3,1),opacity=0.3)
                A9=box(pos=(0,0,0),size=(1,1,1),frame=A,opacity=0.3,color=(0.9,0.9,0.9))
                boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]=A
                
            elif game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==8:
                A=frame(pos=choosebox.pos,num=10,eff=0)
                A0=box(size=(0.8,0.8,0.8),pos=(0,0,0),frame=A)
                A1=arrow(pos=(0.2,0.4,0.45),axis=(0,0,-0.8),color=color.yellow,frame=A)
                A2=arrow(pos=(-0.2,0.4,-0.45),axis=(0,0,0.8),color=color.yellow,frame=A)
                A3=arrow(pos=(0.2,-0.4,-0.45),axis=(0,0,0.8),color=color.yellow,frame=A)
                A4=arrow(pos=(-0.2,-0.4,0.45),axis=(0,0,-0.8),color=color.yellow,frame=A)
                A5=arrow(pos=(0.4,-0.2,0.45),axis=(0,0,-0.8),color=color.yellow,frame=A)
                A6=arrow(pos=(0.4,0.2,-0.45),axis=(0,0,0.8),color=color.yellow,frame=A)
                A7=arrow(pos=(-0.4,-0.2,-0.45),axis=(0,0,0.8),color=color.yellow,frame=A)
                A8=arrow(pos=(-0.4,0.2,0.45),axis=(0,0,-0.8),color=color.yellow,frame=A)
                boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]=A
                
            elif game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==9:
                A=sphere(radius=0.3,color=color.red,pos=choosebox.pos,num=11, diameter=60, reforce=12)
                boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]=A
           
        elif c=='\t':
            if game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==0 or game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==2:
                print('Warning! name "new" data can be rewritten. please check if there is a text name "new".\nyou can save this map Y/N')
                while 1:
                    a=scene.kb.getkey()
                    if a=='N' or a=='n':
                        break
                    elif a=='Y' or a =='y':
                        xminincrease()
                        xincrease()
                        yminincrease()
                        yincrease()
                        zminincrease()
                        zincrease()
                        savethemap()
                        for l in Yarrows:
                            for obj in l:
                                obj.visible=False
                        for l in Zarrows:
                            for obj in l:
                                obj.visible=False
                        for l in Xarrows:
                            for obj in l:
                                obj.visible=False
                        for l in boxes_making_list:
                            for ll in l:
                                for obj in ll:
                                    obj.visible=False
                        break
                
            elif game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==1:
                print('there is nothing that you can change. this is normal box.')

            elif game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==2:
                print("you can change the map's setting. click g, b or r to change start gravity, bound-force and mainball's radius")
                                
            elif game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==3:
                print ('you can choose the radius of this yellow ball with r.')
                
            elif game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==4:
                print('you can choose how many times the ball can bound on this box(0/1)')
                boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].visible=False
                if len(boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].objects)==8:
                    A=frame(num=4,pos=choosebox.pos,times=2)
                    c=(random(),random(),random())
                    A1=box(pos=(0.3,0.3,0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                    A2=box(pos=(0.3,0.3,-0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                    A3=box(pos=(0.3,-0.3,0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                    A4=box(pos=(-0.3,0.3,0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                    A5=box(pos=(0.3,-0.3,-0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                    A6=box(pos=(-0.3,-0.3,0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                    A7=box(pos=(-0.3,0.3,-0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                    A8=box(pos=(-0.3,-0.3,-0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                    Acen=box(pos=(0,0,0),size=(0.4,0.4,0.4),frame=A,color=c)
                    boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]=A
                else:
                    A=frame(num=4,pos=choosebox.pos,times=1)
                    c=(random(),random(),random())
                    A1=box(pos=(0.3,0.3,0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                    A2=box(pos=(0.3,0.3,-0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                    A3=box(pos=(0.3,-0.3,0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                    A4=box(pos=(-0.3,0.3,0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                    A5=box(pos=(0.3,-0.3,-0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                    A6=box(pos=(-0.3,-0.3,0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                    A7=box(pos=(-0.3,0.3,-0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                    A8=box(pos=(-0.3,-0.3,-0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                    boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]=A

                           
            elif game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==5:
                print('red:infinit, from green(less times) to blue(many times)')
                boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].Ttimes+=1
                boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].Ttimes%=11
                if boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].Ttimes!=0:
                    boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].color=(0,0.5,boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].Ttimes/10)
                else:
                    boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].color=(1,0,0)

            elif game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==6:
                print('e:pos up-down change, t:thorn forward change.')
                
            elif game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==7:
                print('you can choose the speed and the start_delay by s and t')
               
            elif game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==8:     #아이템
                print('you can change the kind of item with e')
                
            elif game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==9:
                print('you can change the diameter and reflecting-force by r and f.')

        elif game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==2:
            if c=='g':
                print ('choose the gravity(default=165)')
                gravitation=-int(input('gravity:'))
                    
            elif c=='b':
                print('choose the boundforce(default=100)')
                bound_force=int(input('boundforce:'))

            elif c=='r':
                print('choose the diameter of the mainball.(default=2)')
                mainball_diameter=int(input('diameter:'))

        elif game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==3:
            if c=='r':
                print('choose the diameter of this ball.(default=4)')
                boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].diameter=int(input('diameter:'))
                boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].radius=boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].diameter/20

        elif game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==6:
            if c=='e':
                boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].elv+=3
                boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].elv%=5
                boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].elv-=2
            elif c=='t':
                boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].thorn+=2
                boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].thorn%=3
                boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].thorn-=1
            for obj in boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].objects:
                obj.visible=False

            A=frame(pos=boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].pos,num=6,thorn=boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].thorn,elv=boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].elv)
            if A.thorn==1:
                A1=pyramid(pos=(0,0,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                A2=pyramid(pos=(0.3,0.3,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                A3=pyramid(pos=(0.3,-0.3,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                A4=pyramid(pos=(-0.3,0.3,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                A5=pyramid(pos=(-0.3,-0.3,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                A6=pyramid(pos=(0.3,0,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                A7=pyramid(pos=(0,0.3,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                A8=pyramid(pos=(0,-0.3,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                A9=pyramid(pos=(-0.3,0,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                A10=box(pos=(0,0,-0.05+0.2*A.elv),size=(1,1,0.1),color=(0.5,1,0.5),frame=A)
                A.center=A10
            elif A.thorn==-1:
                B1=pyramid(pos=(0,0,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                B2=pyramid(pos=(0.3,0.3,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                B3=pyramid(pos=(0.3,-0.3,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                B4=pyramid(pos=(-0.3,0.3,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                B5=pyramid(pos=(-0.3,-0.3,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                B6=pyramid(pos=(0.3,0,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                B7=pyramid(pos=(0,0.3,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                B8=pyramid(pos=(0,-0.3,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                B9=pyramid(pos=(-0.3,0,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                B10=box(pos=(0,0,0.05+0.2*A.elv),size=(1,1,0.1),color=(0.5,1,0.5),frame=A)
                A.center=B10
            elif A.thorn==0:
                C1=pyramid(pos=(0,0,-0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                C2=pyramid(pos=(0.3,0.3,-0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                C3=pyramid(pos=(0.3,-0.3,-0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                C4=pyramid(pos=(-0.3,0.3,-0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                C5=pyramid(pos=(-0.3,-0.3,-0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                C6=pyramid(pos=(0.3,0,-0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                C7=pyramid(pos=(0,0.3,-0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                C8=pyramid(pos=(0,-0.3,-0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                C9=pyramid(pos=(-0.3,0,-0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                C10=box(pos=(0,0,0.2*A.elv),size=(1,1,0.1),color=(0.5,1,0.5),frame=A)
                C11=pyramid(pos=(0,0,0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                C12=pyramid(pos=(0.3,0.3,0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                C13=pyramid(pos=(0.3,-0.3,0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                C14=pyramid(pos=(-0.3,0.3,0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                C15=pyramid(pos=(-0.3,-0.3,0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                C16=pyramid(pos=(0.3,0,0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                C17=pyramid(pos=(0,0.3,0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                C18=pyramid(pos=(0,-0.3,0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                C19=pyramid(pos=(-0.3,0,0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                A.center=C10
            boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]=A

        elif game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==7:
            if c=='s':
                print('speed of regen time(default:0)')
                boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].gen=2+int(input('speed of regen time:'))
                
            elif c=='t':
                print('first-delay time(default:0)')
                boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].trying=int(input('first-delay time:'))

        elif game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==8:
            if c=='e':
                A=boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]
                A.eff+=1
                A.eff%=3
                for obj in A.objects:
                    obj.visible=False
                A=frame(pos=boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].pos, eff=boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].eff, num=boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].num)
                A0=box(size=(0.8,0.8,0.8),pos=(0,0,0),frame=A)
                if A.eff==0:
                    A1=arrow(pos=(0.2,0.4,0.45),axis=(0,0,-0.8),color=color.yellow,frame=A)
                    A2=arrow(pos=(-0.2,0.4,-0.45),axis=(0,0,0.8),color=color.yellow,frame=A)
                    A3=arrow(pos=(0.2,-0.4,-0.45),axis=(0,0,0.8),color=color.yellow,frame=A)
                    A4=arrow(pos=(-0.2,-0.4,0.45),axis=(0,0,-0.8),color=color.yellow,frame=A)
                    A5=arrow(pos=(0.4,-0.2,0.45),axis=(0,0,-0.8),color=color.yellow,frame=A)
                    A6=arrow(pos=(0.4,0.2,-0.45),axis=(0,0,0.8),color=color.yellow,frame=A)
                    A7=arrow(pos=(-0.4,-0.2,-0.45),axis=(0,0,0.8),color=color.yellow,frame=A)
                    A8=arrow(pos=(-0.4,0.2,0.45),axis=(0,0,-0.8),color=color.yellow,frame=A)
                elif A.eff==1:
                    B1=arrow(pos=(0,0.4,-0.25),axis=(0,0,0.5),color=color.red,frame=A)
                    B2=arrow(pos=(0,-0.4,-0.25),axis=(0,0,0.5),color=color.red,frame=A)
                    B3=arrow(pos=(0.4,0,-0.25),axis=(0,0,0.5),color=color.red,frame=A)
                    B4=arrow(pos=(-0.4,0,-0.25),axis=(0,0,0.5),color=color.red,frame=A)
                elif A.eff==2:
                    C1=arrow(pos=(0.4,0.2,0.45),axis=(0,-0.8,0),color=color.red,frame=A)
                    C2=arrow(pos=(0.4,-0.2,-0.45),axis=(0,0.8,0),color=color.red,frame=A)
                    C3=arrow(pos=(-0.4,-0.2,0.45),axis=(0,0.8,0),color=color.red,frame=A)
                    C4=arrow(pos=(-0.4,0.2,-0.45),axis=(0,-0.8,0),color=color.red,frame=A)
                    C5=arrow(pos=(-0.2,0.4,0.45),axis=(0.8,0,0),color=color.red,frame=A)
                    C6=arrow(pos=(0.2,0.4,-0.45),axis=(-0.8,0,0),color=color.red,frame=A)
                    C7=arrow(pos=(-0.2,-0.4,-0.45),axis=(0.8,0,0),color=color.red,frame=A)
                    C8=arrow(pos=(0.2,-0.4,0.45),axis=(-0.8,0,0),color=color.red,frame=A)
                boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]=A

        elif game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==9:
            if c=='r':
                print('diameter of the bumper(default=60)')
                boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].diameter=int(input('diameter:'))
                boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].radius=boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].diameter/200
            elif c=='f':
                print('reflecting force of the bumper(default=12),(1~20)')
                boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].reforce=int(input('force:'))
                boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].color=(1,boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].reforce/20,0)

                
def savethemap():
    global game_making_list, boxes_making_list, Xlines, Ylines, Zlines, gravitation,bound_force,mainball_diameter
    f=open('new.txt','w')
    f.write('\t'.join([str(Xlines),str(Ylines),str(Zlines)]))
    f.write('\t')
    f.write('r.'+str(mainball_diameter)+'\t'+'g.'+str(-gravitation)+'\tb.'+str(bound_force))
    f.write('\n')
    for k in range(len(game_making_list)):      
        for j in range(len(game_making_list[0])):
            for i in range(len(game_making_list[0][0])):
                if game_making_list[k][j][i]==0:
                    f.write('0\t')
                elif game_making_list[k][j][i]==1:
                    f.write('1\t')
                elif game_making_list[k][j][i]==2:
                    f.write('2\t')
                elif game_making_list[k][j][i]==3:
                    f.write('3.r:'+str(boxes_making_list[k][j][i].diameter)+'\t')
                elif game_making_list[k][j][i]==4:
                    f.write('4.t:'+str(boxes_making_list[k][j][i].times)+'\t')
                        
                elif game_making_list[k][j][i]==5:
                    f.write('5.t:'+str(boxes_making_list[k][j][i].Ttimes)+'\t')
                    
                elif game_making_list[k][j][i]==6:
                    f.write('6.t:'+str(boxes_making_list[k][j][i].thorn)+'.e:'+str(boxes_making_list[k][j][i].elv)+'\t')
                elif game_making_list[k][j][i]==7:
                    f.write('7.t:'+str(boxes_making_list[k][j][i].trying)+'.s:'+str(boxes_making_list[k][j][i].gen)+'\t')
                elif game_making_list[k][j][i]==8:
                    f.write('8.e:'+str(boxes_making_list[k][j][i].eff)+'\t')
                elif game_making_list[k][j][i]==9:
                    f.write('9.r:'+str(boxes_making_list[k][j][i].diameter)+'.f:'+str(boxes_making_list[k][j][i].reforce)+'\t')
                
            f.write('\n')
                      
    

def xincrease():
    global Xlines, Ylines, Zlines, Xarrows, Yarrows, Zarrows, game_making_list , boxes_making_list
    
    for i in range(len(boxes_making_list)):
        for j in range(len(boxes_making_list[0])):
            boxes_making_list[i][j].append(box(visible=False))

    for l in range(len(game_making_list)):
        for m in range(len(game_making_list[0])):
            game_making_list[l][m].append(0)


    for l in Xarrows:
        for obj in l:
            obj.axis+=vector(1,0,0)
            obj.shaftwidth=0.1

    Yarrows.append([])
    for i in range(len(Yarrows[0])):
        Yarrows[len(Yarrows)-1].append(arrow(pos=Yarrows[len(Yarrows)-2][i].pos+vector(1,0,0),axis=Yarrows[0][0].axis,shaftwidth=0.1,opacity=0.01))

    Zarrows.append([])
    for i in range(len(Zarrows[0])):
        Zarrows[len(Zarrows)-1].append(arrow(pos=Zarrows[len(Zarrows)-2][i].pos+vector(1,0,0),axis=Zarrows[0][0].axis,shaftwidth=0.1,opacity=0.01))

    Xlines+=1

def yincrease():
    global Xlines, Ylines, Zlines, Xarrows, Yarrows, Zarrows, game_making_list,boxes_making_list

    for i in range(len(game_making_list)):
        boxes_making_list[i].append([])
        for j in range(len(boxes_making_list[0][0])):
            boxes_making_list[i][len(boxes_making_list[i])-1].append(box(visible=False))
    
    for i in range(len(game_making_list)):
        game_making_list[i].append([])
        for j in range(len(game_making_list[0][0])):
            game_making_list[i][len(game_making_list[i])-1].append(0)
        

    for l in Yarrows:
        for obj in l:
            obj.axis+=vector(0,1,0)
            obj.shaftwidth=0.1

    Xarrows.append([])
    for i in range(len(Xarrows[0])):
        Xarrows[len(Xarrows)-1].append(arrow(pos=Xarrows[len(Xarrows)-2][i].pos+vector(0,1,0),axis=Xarrows[0][0].axis,shaftwidth=0.1,opacity=0.01))

    for i in range(len(Zarrows)):
        Zarrows[i].append(arrow(pos=Zarrows[i][len(Zarrows[i])-1].pos+vector(0,1,0),axis=Zarrows[0][0].axis,shaftwidth=0.1,opacity=0.01))

    Ylines+=1

def zincrease():
    global Xlines, Ylines, Zlines, Xarrows, Yarrows, Zarrows, game_making_list,boxes_making_list

    boxes_making_list.append([])
    for i in range(len(boxes_making_list[0])):
        boxes_making_list[len(boxes_making_list)-1].append([])
        for j in range(len(boxes_making_list[0][0])):
            boxes_making_list[len(boxes_making_list)-1][len(boxes_making_list[len(boxes_making_list)-1])-1].append(box(visible=False))
                    

    game_making_list.append([])
    for i in range(len(game_making_list[0])):
        game_making_list[len(game_making_list)-1].append([])
        for j in range(len(game_making_list[0][0])):
            game_making_list[len(game_making_list)-1][len(game_making_list[len(game_making_list)-1])-1].append(0)

    for l in Zarrows:
        for obj in l:
            obj.axis+=vector(0,0,1)
            obj.shaftwidth=0.1

    for i in range(len(Xarrows)):
        Xarrows[i].append(arrow(pos=Xarrows[i][len(Xarrows[i])-1].pos+vector(0,0,1),axis=Xarrows[0][0].axis,shaftwidth=0.1,opacity=0.01))

    for i in range(len(Yarrows)):
        Yarrows[i].append(arrow(pos=Yarrows[i][len(Yarrows[i])-1].pos+vector(0,0,1),axis=Yarrows[0][0].axis,shaftwidth=0.1,opacity=0.01))

    Zlines+=1

def xminincrease():
    global Xlines, Ylines, Zlines, Xarrows, Yarrows, Zarrows, game_making_list , boxes_making_list

    for i in boxes_making_list:
        for j in i:
            for obj in j:
                obj.pos+=vector(1,0,0)
    
    for i in range(len(boxes_making_list)):
        for j in range(len(boxes_making_list[i])):
            boxes_making_list[i][j].insert(0,box(visible=False))


            
    for l in range(len(game_making_list)):
        for m in range(len(game_making_list[l])):
            game_making_list[l][m].insert(0,0)

    
    for l in Xarrows:
        for obj in l:
            obj.axis+=vector(1,0,0)
            obj.shaftwidth=0.1

    Yarrows.append([])
    for i in range(len(Yarrows[0])):
        Yarrows[len(Yarrows)-1].append(arrow(pos=Yarrows[len(Yarrows)-2][i].pos+vector(1,0,0),axis=Yarrows[0][0].axis,shaftwidth=0.1,opacity=0.01))

    Zarrows.append([])
    for i in range(len(Zarrows[0])):
        Zarrows[len(Zarrows)-1].append(arrow(pos=Zarrows[len(Zarrows)-2][i].pos+vector(1,0,0),axis=Zarrows[0][0].axis,shaftwidth=0.1,opacity=0.01))

    Xlines+=1

def yminincrease():
    global Xlines, Ylines, Zlines, Xarrows, Yarrows, Zarrows, game_making_list,boxes_making_list

    for i in boxes_making_list:
        for j in i:
            for obj in j:
                obj.pos+=vector(0,1,0)
                
    for i in range(len(game_making_list)):
        boxes_making_list[i].insert(0,[])
        for j in range(len(boxes_making_list[i][1])):
            boxes_making_list[i][0].insert(0,box(visible=False))
    
    for i in range(len(game_making_list)):
        game_making_list[i].insert(0,[])
        for j in range(len(game_making_list[i][1])):
            game_making_list[i][0].insert(0,0)
        

    for l in Yarrows:
        for obj in l:
            obj.axis+=vector(0,1,0)
            obj.shaftwidth=0.1

    Xarrows.append([])
    for i in range(len(Xarrows[0])):
        Xarrows[len(Xarrows)-1].append(arrow(pos=Xarrows[len(Xarrows)-2][i].pos+vector(0,1,0),axis=Xarrows[0][0].axis,shaftwidth=0.1,opacity=0.01))

    for i in range(len(Zarrows)):
        Zarrows[i].append(arrow(pos=Zarrows[i][len(Zarrows[i])-1].pos+vector(0,1,0),axis=Zarrows[0][0].axis,shaftwidth=0.1,opacity=0.01))

    Ylines+=1

def zminincrease():
    global Xlines, Ylines, Zlines, Xarrows, Yarrows, Zarrows, game_making_list,boxes_making_list

    for i in boxes_making_list:
        for j in i:
            for obj in j:
                obj.pos+=vector(0,0,1)
                
    boxes_making_list.insert(0,[])
    for i in range(len(boxes_making_list[1])):
        boxes_making_list[0].insert(0,[])
        for j in range(len(boxes_making_list[1][i])):
            boxes_making_list[0][0].insert(0,box(visible=False))
                    

    game_making_list.insert(0,[])
    for i in range(len(game_making_list[1])):
        game_making_list[0].insert(0,[])
        for j in range(len(game_making_list[1][i])):
            game_making_list[0][0].insert(0,0)

    for l in Zarrows:
        for obj in l:
            obj.axis+=vector(0,0,1)
            obj.shaftwidth=0.1

    for i in range(len(Xarrows)):
        Xarrows[i].append(arrow(pos=Xarrows[i][len(Xarrows[i])-1].pos+vector(0,0,1),axis=Xarrows[0][0].axis,shaftwidth=0.1,opacity=0.01))

    for i in range(len(Yarrows)):
        Yarrows[i].append(arrow(pos=Yarrows[i][len(Yarrows[i])-1].pos+vector(0,0,1),axis=Yarrows[0][0].axis,shaftwidth=0.1,opacity=0.01))

    Zlines+=1

def rotatearrow(choarow):
    choarow.rotate(angle=pi/50,axis=(1,0,0))

def gameload():
    f=open('saved.txt','r')
    stg=f.readlines()
    f.close()
    A=[]
    for I in range(len(stg)):
        A.append(stg[I].rsplit('\t',4))
        
                
    return A

def gamesave(gamenum,password,username='No name'):
    if username.isspace():
        username='No name'
    
    f=open('saved.txt','a')
    f.write(username)
    f.write('\t')
    while 1:
        A3=str(int(gamenum)*1000+int(999*random()))
        if int(A3)%2!=0 and int(A3)%3!=0 and int(A3) % 5!=0:
            break
    while 1:
        A2=str(int(random()*9900)+98)
        if int(A2)%2!=0 and int(A2)%3!=0 and int(A2)%5!=0:
            break
    A4=str(int(random()*8)+1)
    A1=str((int(A4+password)**int(A2))%int(A3))
    f.write(A1+'\t'+A2+'\t'+A3+'\t'+A4)
    f.write('\n')
    f.close()
    

def gamecall(gameplay):                 #맵 지형 정보 획득
    radiusofmainball=0.1
    g_force=vector(0,0,-9.8)
    b_force=5.5
    f=open(str(gameplay).zfill(2)+'.txt','r')
    stg=f.readline().split()
    Xlines=int(stg[0])
    Ylines=int(stg[1])
    Zlines=int(stg[2])          #txt파일 맨 위의 값 N은 x*y*z맵임을 명시
    if len(stg)>3:          #기타 추가 정보 있을 경우. 공의 반지름, 중력 크기, 뛰는 힘 등.
        for i in range(3,len(stg)):
            data=stg[i].split('.')
            if data[0]=='r':            #지름 추가 정보- 첫째열, r.74->지름 0.37. default=0.2
                radiusofmainball=int(data[1])/20
            elif data[0]=='g':          #중력 크기 정보- 첫째열, g.37->(0,0,-3.7). default=(0,0,-14)
                g_force=vector(0,0,-int(data[1])/10)
            elif data[0]=='b':          #뛰는 힘 크기 정보. 첫째열, b.37->3.7 .   default=65
                b_force=int(data[1])/10
    returning=[]
    for i in range(Zlines):
        returning.append([])
        for j in range(Ylines):
            returning[i].append([])
            stg=f.readline().strip().split()
            for k in range (Xlines):
                returning[i][j].append(stg[k].split('.'))     #리스트 1차 z, 2차 y, 3차 x, 4차-정보 '.'으로 구분.
    f.close()
    return radiusofmainball, g_force, b_force, returning
        
def makegame(gamelist,mainballsr):                 #gamelist[Z][Y][X]로 됨.
    Zlines=len(gamelist)
    Ylines=len(gamelist[0])
    Xlines=len(gamelist[0][0])
    stars=0                 #별 개수
    whereball=(0,0,0)       #공 시작 위치
    boxdatalist=[]          #주위 맵 정보를 확인하는데 쓴다.
    boxeslist=[]               #박스들 리스트
    movinglist=[]                 #움직이는 것 리스트
    makinglist=[]                   #만드는 것 리스트
    starlist=[]                     #별 리스트. 반환하지 않고 맵 정보 저장에 사용.
    bumperslist=[]                  #범퍼리스트. 별리스트와 마찬가지로 사용한다.
    for i in range(Zlines):
        boxeslist.append([])        
        for j in range(Ylines):
            boxeslist[i].append([])
            for k in range(Xlines):
                data=gamelist[i][j][k]
                if int(data[0])==0:        #0:빈 공간. 특수기능 없음
                    A=box(num=0,visible=False,pos=(k+0.5,j+0.5,i-0.5))
                    boxeslist[i][j].append(A)
                    gamelist[i][j][k]=0
                    continue
                elif int(data[0])==1:      #1:일반 박스. 특수기능 없음.
                    A=box(size=(1,1,1),pos=(k+0.5,j+0.5,i-0.5),num=1)
                    boxeslist[i][j].append(A)
                    gamelist[i][j][k]=1
                    
                elif int(data[0])==2:      #2:시작점
                    whereball=(k+0.5,j+0.5,i-0.5)
                    A=box(num=0,visible=False,pos=(k+0.5,j+0.5,i-0.5))
                    boxeslist[i][j].append(A)
                    gamelist[i][j][k]=0

                elif int(data[0])==3:      #3:먹어야 하는 노란빛(관계X)   2.r:13 이런식.          
                    A=sphere(pos=(k+0.5,j+0.5,i-0.7),radius=0.2,color=color.yellow,num=3,around=[])
                    if len(data)>1:         # 추가정보-노란공의 지름  default:0.4
                        for x in range(1,len(data)):
                            datus=data[x].split(':')
                            if datus[0]=='r':   #3.r:26-> 지름 1.3 (<1)
                                A.radius=int(datus[1])/20
                    starlist.append(A)
                    boxeslist[i][j].append(A)
                    stars=stars+1
                    gamelist[i][j][k]=0

                elif int(data[0])==4:      #4:튕기면 사라지는 발판. 추가정보-밟을 수 있는 횟수 default:1회.
                    A=frame(num=4,pos=(k+0.5,j+0.5,i-0.5),times=1)      #times=횟수
                    c=(random(),random(),random())
                    A1=box(pos=(0.3,0.3,0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                    A2=box(pos=(0.3,0.3,-0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                    A3=box(pos=(0.3,-0.3,0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                    A4=box(pos=(-0.3,0.3,0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                    A5=box(pos=(0.3,-0.3,-0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                    A6=box(pos=(-0.3,-0.3,0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                    A7=box(pos=(-0.3,0.3,-0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                    A8=box(pos=(-0.3,-0.3,-0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                    if len(data)>1:
                        for x in range(1,len(data)):
                            datus=data[x].split(':')
                            if datus[0]=='t':   #4.t:1 ->1회
                                if int(datus[1])==2: #4.t:2꼴일 경우
                                    Acen=box(pos=(0,0,0),size=(0.4,0.4,0.4),frame=A,color=c)
                                    A.times=2
                                    A.cen=Acen
                    boxeslist[i][j].append(A)
                    gamelist[i][j][k]=4

                elif int(data[0])==5:      #5:높이 뛰는 발판.  추가정보-밟을 수 있는 횟수. 색으로 표현된다. default:무한번
                    A=box(size=(1,1,1),pos=(k+0.5,j+0.5,i-0.5),num=5,color=(1,0,0),Ttimes=0)    #Ttimes: 남은 밟을 수 있는 횟수
                    if len(data)>1:
                        for x in range(1,len(data)):
                            datus=data[x].split(':')
                            if datus[0]=='t':       #t:밟는 횟수 제한. 1~10회  t:5->5회
                                A.Ttimes=int(datus[1])
                                if A.Ttimes!=0:
                                    A.color=(0,0.5,A.Ttimes/10)
                    boxeslist[i][j].append(A)
                    gamelist[i][j][k]=5

                elif int(data[0])==6:      #6: 가시. 닿으면 죽는다. 추가정보: 위쪽, 아래쪽 가시의 유무, 중심에서의 상대적 위치
                    A=frame(num=6,pos=(k+0.5,j+0.5,i-0.5),thorn=1, elv=-2)   #thorn: 1-위, -1-아래, 0-위와 아래, elv: 0-중심, 1,2-상대적 거리, 부호-위아래 
                    if len(data)>1:
                        for x in range(1,len(data)):
                            datus=data[x].split(':')
                            if datus[0]=='t':    #t: thorn. -1~1중 하나
                                A.thorn=int(datus[1])
                            elif datus[0]=='e':     #elv, -2~2 중 하나
                                A.elv=int(datus[1])
                    if A.thorn==1:
                        A1=pyramid(pos=(0,0,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                        A2=pyramid(pos=(0.3,0.3,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                        A3=pyramid(pos=(0.3,-0.3,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                        A4=pyramid(pos=(-0.3,0.3,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                        A5=pyramid(pos=(-0.3,-0.3,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                        A6=pyramid(pos=(0.3,0,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                        A7=pyramid(pos=(0,0.3,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                        A8=pyramid(pos=(0,-0.3,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                        A9=pyramid(pos=(-0.3,0,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                        A10=box(pos=(0,0,-0.05+0.2*A.elv),size=(1,1,0.1),color=(0.5,1,0.5),frame=A)
                        A.center=A10
                    elif A.thorn==-1:
                        B1=pyramid(pos=(0,0,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                        B2=pyramid(pos=(0.3,0.3,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                        B3=pyramid(pos=(0.3,-0.3,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                        B4=pyramid(pos=(-0.3,0.3,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                        B5=pyramid(pos=(-0.3,-0.3,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                        B6=pyramid(pos=(0.3,0,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                        B7=pyramid(pos=(0,0.3,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                        B8=pyramid(pos=(0,-0.3,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                        B9=pyramid(pos=(-0.3,0,0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                        B10=box(pos=(0,0,0.05+0.2*A.elv),size=(1,1,0.1),color=(0.5,1,0.5),frame=A)
                        A.center=B10
                    elif A.thorn==0:
                        C1=pyramid(pos=(0,0,-0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                        C2=pyramid(pos=(0.3,0.3,-0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                        C3=pyramid(pos=(0.3,-0.3,-0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                        C4=pyramid(pos=(-0.3,0.3,-0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                        C5=pyramid(pos=(-0.3,-0.3,-0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                        C6=pyramid(pos=(0.3,0,-0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                        C7=pyramid(pos=(0,0.3,-0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                        C8=pyramid(pos=(0,-0.3,-0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                        C9=pyramid(pos=(-0.3,0,-0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,-0.1),color=(0.5,1,0.5),frame=A)
                        C10=box(pos=(0,0,0.2*A.elv),size=(1,1,0.1),color=(0.5,1,0.5),frame=A)
                        C11=pyramid(pos=(0,0,0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                        C12=pyramid(pos=(0.3,0.3,0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                        C13=pyramid(pos=(0.3,-0.3,0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                        C14=pyramid(pos=(-0.3,0.3,0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                        C15=pyramid(pos=(-0.3,-0.3,0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                        C16=pyramid(pos=(0.3,0,0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                        C17=pyramid(pos=(0,0.3,0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                        C18=pyramid(pos=(0,-0.3,0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                        C19=pyramid(pos=(-0.3,0,0.05+0.2*A.elv),size=(0.1,0.3,0.3),axis=(0,0,0.1),color=(0.5,1,0.5),frame=A)
                        A.center=C10
                    gamelist[i][j][k]=6
                    boxeslist[i][j].append(A)

                elif int(data[0])==7:      #7 추가정보- trying:낙석 횟수. 5단위 내로 속도조절, 5단위 밖으로 타이밍 조절
                    A=box(num=7,visible=False,pos=(k+0.5,j+0.5,i-0.5),gen=2,trying=0)
                    if len(data)>1:
                        for x in range(1,len(data)):
                            datus=data[x].split(':')
                            if datus[0]=='t':       #t-낙석 초기 딜레이
                                A.trying=int(datus[1])/(10**len(datus[1]))    #t:371->0.371<1
                            elif datus[0]=='s':     #s-낙석 주기
                                A.gen=(int(datus[1])/10+2)        #1~...
                                
                    gamelist[i][j][k]=7
                    boxeslist[i][j].append(box(num=0,visible=False))
                    makinglist.append(A)

                elif int(data[0])==8:      #8: 아이템들. default-역중력 아이템. 추가정보-??
                    A=frame(pos=(k+0.5,j+0.5,i-0.5),num=8,eff=0)       #eff: 효과. -1:역중력, 1: 허공뛰기, 2: 탄환처럼 튀어나가기
                    if len(data)>1:
                        for x in range(1,len(data)):
                            datus=data[x].split(':')
                            if datus[0]=='e':           #e- 아이템 종류. -1:역중력, 1:허공뛰기, 2:탄환처럼 튀어나가기
                                A.eff=int(datus[1])
                    A0=box(size=(0.8,0.8,0.8),pos=(0,0,0),frame=A)
                    if A.eff==0:
                        A1=arrow(pos=(0.2,0.4,0.45),axis=(0,0,-0.8),color=color.yellow,frame=A)
                        A2=arrow(pos=(-0.2,0.4,-0.45),axis=(0,0,0.8),color=color.yellow,frame=A)
                        A3=arrow(pos=(0.2,-0.4,-0.45),axis=(0,0,0.8),color=color.yellow,frame=A)
                        A4=arrow(pos=(-0.2,-0.4,0.45),axis=(0,0,-0.8),color=color.yellow,frame=A)
                        A5=arrow(pos=(0.4,-0.2,0.45),axis=(0,0,-0.8),color=color.yellow,frame=A)
                        A6=arrow(pos=(0.4,0.2,-0.45),axis=(0,0,0.8),color=color.yellow,frame=A)
                        A7=arrow(pos=(-0.4,-0.2,-0.45),axis=(0,0,0.8),color=color.yellow,frame=A)
                        A8=arrow(pos=(-0.4,0.2,0.45),axis=(0,0,-0.8),color=color.yellow,frame=A)
                    elif A.eff==1:
                        B1=arrow(pos=(0,0.4,-0.25),axis=(0,0,0.5),color=color.red,frame=A)
                        B2=arrow(pos=(0,-0.4,-0.25),axis=(0,0,0.5),color=color.red,frame=A)
                        B3=arrow(pos=(0.4,0,-0.25),axis=(0,0,0.5),color=color.red,frame=A)
                        B4=arrow(pos=(-0.4,0,-0.25),axis=(0,0,0.5),color=color.red,frame=A)
                    elif A.eff==2:
                        C1=arrow(pos=(0.4,0.2,0.45),axis=(0,-0.8,0),color=color.red,frame=A)
                        C2=arrow(pos=(0.4,-0.2,-0.45),axis=(0,0.8,0),color=color.red,frame=A)
                        C3=arrow(pos=(-0.4,-0.2,0.45),axis=(0,0.8,0),color=color.red,frame=A)
                        C4=arrow(pos=(-0.4,0.2,-0.45),axis=(0,-0.8,0),color=color.red,frame=A)
                        C5=arrow(pos=(-0.2,0.4,0.45),axis=(0.8,0,0),color=color.red,frame=A)
                        C6=arrow(pos=(0.2,0.4,-0.45),axis=(-0.8,0,0),color=color.red,frame=A)
                        C7=arrow(pos=(-0.2,-0.4,-0.45),axis=(0.8,0,0),color=color.red,frame=A)
                        C8=arrow(pos=(0.2,-0.4,0.45),axis=(-0.8,0,0),color=color.red,frame=A)
                    boxeslist[i][j].append(A)
                    gamelist[i][j][k]=8

                elif int(data[0])==9:      #9:범퍼(?) 퉁기면 깨진다. 추가정보-반지름, 튕김힘
                    A=sphere(radius=0.3,color=color.red,pos=(k+0.5,j+0.5,i-0.5),num=9, reforce=1.2,around=[])
                    if len(data)>1:
                        for x in range(1,len(data)):
                            datus=data[x].split(':')
                            if datus[0]=='r':       #지름 추가정보. default=0.6 (12)
                                A.radius=int(datus[1])/200
                            elif datus[0]=='f':     #튕김힘 추가정보. default=1.2, 0.1단위
                                A.reforce=int(datus[1])/10
                                A.color=(1,A.reforce/2,0)
                    gamelist[i][j][k]=9
                    boxeslist[i][j].append(A)
                    bumperslist.append(A)
    boxdatalist=[]
    for i in range(len(gamelist)):
        boxdatalist.append([])
        for j in range(len(gamelist[0])):
            boxdatalist[i].append([])
            for k in range(len(gamelist[0][0])):
                boxdatalist[i][j].append(0)
    for i in range(Zlines):
        for j in range(Ylines):
            for k in range(Xlines):     #사각형 격자에서 구 안에 조금이라도 들어오는지 판별. 면 중앙과 꼭지점, 모서리 중앙을 판별한다.
                stararound=[]
                bumperaround=[]
                for obj in starlist:
                    dterminent=0
                    for l in arange(-0.5,1,0.5):
                        for m in arange(-0.5,1,0.5):
                            for n in arange(-0.5,1,0.5):
                                gpos=vector(boxeslist[i][j][k].pos+vector(l,m,n))
                                if abs(gpos-obj.pos)<obj.radius+mainballsr:
                                    stararound.append(obj)
                                    obj.around.append([i,j,k])
                                    dterminent=1
                                    break
                            if dterminent==1:
                                break
                        if dterminent==1:
                            break

                for obj in bumperslist:
                    dterminent=0
                    for l in arange(-0.5,1,0.5):
                        for m in arange(-0.5,1,0.5):
                            for n in arange(-0.5,1,0.5):
                                gpos=vector(boxeslist[i][j][k].pos+vector(l,m,n))
                                if abs(gpos-obj.pos)<obj.radius+mainballsr:
                                    bumperaround.append(obj)
                                    obj.around.append([i,j,k])
                                    dterminent=1
                                    break
                            if dterminent==1:
                                break
                        if dterminent==1:
                            break

                boxdatalist[i][j][k]=boxdata(stararound,bumperaround)

    return (boxdatalist,whereball,stars,boxeslist,movinglist,makinglist)    #지역정보리스트, 공 위치, 별들, 층별 프레임 리스트, 박스생성자 리스트 반환
                    
                    
                

def endgame(mainball,boxeslist,stars=1):
    global movinglist
    scene.userspin=False
    if stars:
        rate(1)
        for zlines in boxeslist:
            for ylines in zlines:
                for box in ylines:
                    box.visible=False
        for obj in movinglist:
            obj.visible=False
        
        mainball.color=color.red
        rate(1)
        mainball.visible=False
    else:
        rate(1)
        for zlines in boxeslist:
            for ylines in zlines:
                for box in ylines:
                    box.visible=False
        for obj in movinglist:
            obj.visible=False
        mainball.color=color.yellow
        rate(1)
        mainball.visible=False
    scene.userspin=True

def fellingmaking(boxmaker,gamelist,time,movinglist):
    for obj in boxmaker:
        if obj.num==7:
            if obj.gen*obj.trying/2<=time:
                A=frame(num=7,pos=obj.pos,velocity=vector(0,0,0))
                A1=box(pos=(0.3,0.3,0.3),size=(0.4,0.4,0.4),frame=A,color=(0.2,0.3,1))
                A2=box(pos=(0.3,0.3,-0.3),size=(0.4,0.4,0.4),frame=A,color=(0.2,0.3,1))
                A3=box(pos=(0.3,-0.3,0.3),size=(0.4,0.4,0.4),frame=A,color=(0.2,0.3,1))
                A4=box(pos=(-0.3,0.3,0.3),size=(0.4,0.4,0.4),frame=A,color=(0.2,0.3,1))
                A5=box(pos=(0.3,-0.3,-0.3),size=(0.4,0.4,0.4),frame=A,color=(0.2,0.3,1))
                A6=box(pos=(-0.3,-0.3,0.3),size=(0.4,0.4,0.4),frame=A,color=(0.2,0.3,1))
                A7=box(pos=(-0.3,0.3,-0.3),size=(0.4,0.4,0.4),frame=A,color=(0.2,0.3,1))
                A8=box(pos=(-0.3,-0.3,-0.3),size=(0.4,0.4,0.4),frame=A,color=(0.2,0.3,1))
                movinglist.append(A)
                obj.trying+=1

    return movinglist

def box_move(movinglist,gamelist):
    global gravity,dt
    stop=0
    for obj in movinglist:
        if obj.num==7:
            obj.pos+=obj.velocity*dt
            obj.velocity+=gravity*dt
            if obj.pos.z<-1 or obj.pos.z>len(gamelist):
                obj.visible=False
                movinglist.remove(obj)
            elif int(obj.pos.z+1)>=len(gamelist) or int(obj.pos.y)>=len(gamelist[0]) or int(obj.pos.x)>=len(gamelist[0][0]):
                obj.visible=False
            elif gamelist[int(obj.pos.z+1)][int(obj.pos.y)][int(obj.pos.x)] ==1 or gamelist[int(obj.pos.z+1)][int(obj.pos.y)][int(obj.pos.x)] ==4 or gamelist[int(obj.pos.z+1)][int(obj.pos.y)][int(obj.pos.x)] ==5 or gamelist[int(obj.pos.z+1)][int(obj.pos.y)][int(obj.pos.x)] ==6 or gamelist[int(obj.pos.z+1)][int(obj.pos.y)][int(obj.pos.x)] ==9:
                obj.visible=False
                movinglist.remove(obj)
            if obj.pos.x+0.5>mainball.pos.x>obj.pos.x-0.5 and obj.pos.y+0.5>mainball.pos.y>obj.pos.y-0.5 and obj.pos.z+0.5>mainball.pos.z>obj.pos.z-0.5:
                stop=1

    return (movinglist,stop)
                    


befstart=frame()



starttext=text(pos=(-2,1,0), align='left', text='Play',frame=befstart)
makingmap_text=text(pos=(-2,-1,0),align='left',text='Making Map',frame=befstart,width=0.7,height=0.8)
quittext=text(pos=(-2,-3,0), align='left',text='Quit',frame=befstart)


start_new=text(pos=(-2,51,-100),align='left',text='New',frame=befstart)
start_continue=text(pos=(-2,49,-100),align='left',text='Continue',frame=befstart)
start_back=text(pos=(-2,47,-100),align='left',text='Back',frame=befstart)
loadfiles=gameload()
n=0
for I in range(len(loadfiles)):
    A=text(text=loadfiles[I][0],pos=(-2,1-2*n,100),frame=befstart)
    n+=1
brack=text(text='Back',pos=(-2,1-2*n,100),frame=befstart)

white_box=box(pos=scene.center+vector(0,0,0.5),size=(0.1,10,10),axis=(0,0,1),opacity=0.5,color=color.black,visible=False)
keyview=text(text='password',pos=scene.center+vector(0,-1,1),align='left',width=0.7,height=0.4)
keyview.visible=False
passwordview=text(text='',pos=keyview.pos+vector(0,1,0),align='left',width=0.7,height=0.4)
passwordview.visible=False

cancelask=text(text='↑cancel',align='left',width=0.7,height=0.4)
continask=text(text='continue↓',align='left',width=0.7,height=0.4)
cancelask.visible=False
continask.visible=False

text_name_frame=frame(axis=(0,0,-1))
text_name=text(text='name',align='center',width=0.7,height=0.4,axis=(0,0,1),frame=text_name_frame)
text_password_frame=frame(axis=(0,0,-1))
text_password=text(text='password',align='center',width=0.7,height=0.4,frame=text_password_frame,axis=(0,0,1))
text_name.visible=False
text_password.visible=False

text_nameview_frame=frame(axis=(0,0,-1))
text_nameview=text(text='',align='center',width=0.7,height=0.4,axis=(0,0,1),frame=text_nameview_frame)
text_nameview.visible=False

text_passwordview_frame=frame(axis=(0,0,-1))
text_passwordview=text(text='',align='center',width=0.7,height=0.4,axis=(0,0,1),frame=text_passwordview_frame)
text_passwordview.visible=False

entery=1
entyy=1
enyyy=0
gameplay=0
playing=0
loading=0

while entyy:
    befstart.visible=True
    choarow.visible=True
    scene.range=4
    while entery:
        scene.center=choarow.pos+vector(3,0,0)
        scene.forward=(0,0,-1)
        rate(100)
        rotatearrow(choarow)
        if scene.kb.keys:
            c=scene.kb.getkey()
            if c=='up':
                if choarow.pos.y==1.5:
                    continue
                else:
                    choarow.pos.y=choarow.pos.y+2
            elif c=='down':
                if choarow.pos.y==-2.5:
                    continue
                else:
                    choarow.pos.y=choarow.pos.y-2
            elif c=='\n':
                if choarow.pos.y==-2.5:
                    entyy=0
                    entery=0
                    choarow.pos.y=1.5
                    scene.visible=False
                    break
                elif choarow.pos.y==1.5:
                    entery=0
                    timefor=100
                    while timefor:
                        rate(500)
                        rotatearrow(choarow)
                        scene.forward=(0,0,-1)
                        scene.range=4
                        befstart.pos.y=befstart.pos.y-1/2
                        befstart.pos.z=befstart.pos.z+1
                        timefor=timefor-1
                    enyyy=1
                elif choarow.pos.y==-0.5:
                    befstart.visible=False
                    choarow.visible=False
                    scene.userspin=True
                    scene.userzoom=True
                    mapmaking()
                    scene.userspin=False
                    scene.forward=(0,0,-1)
                    scene.userzoom=False
                    befstart.visible=True
                    choarow.visible=True
                    

    while enyyy:
        scene.center=choarow.pos+vector(3,0,0)
        scene.forward=(0,0,-1)
        scene.range=4
        k=4
        rate(100)
        rotatearrow(choarow)
        if scene.kb.keys:
            c=scene.kb.getkey()
            if c=='up':
                if choarow.pos.y==1.5:
                    continue
                else:
                    choarow.pos.y=choarow.pos.y+2
            elif c=='down':
                if choarow.pos.y==-2.5:
                    continue
                else:
                    choarow.pos.y=choarow.pos.y-2
            elif c=='\n':
                if choarow.pos.y==-2.5:
                    entery=1
                    enyyy=0
                    timefor=100
                    while timefor:
                        rate(500)
                        scene.forward=(0,0,-1)
                        scene.range=4
                        rotatearrow(choarow)
                        befstart.pos.y=befstart.pos.y+1/2
                        befstart.pos.z=befstart.pos.z-1
                        choarow.pos.y=1.5
                        timefor=timefor-1                       
                    break
                
                if choarow.pos.y==-0.5:
                    enyyy=0
                    loading=1
                    timefor=200
                    while timefor:
                        rate(500)
                        scene.forward=(0,0,-1)
                        scene.range=4
                        rotatearrow(choarow)
                        befstart.pos.z=befstart.pos.z-1
                        befstart.pos.y=befstart.pos.y+1/4
                        timefor=timefor-1
                    choarow.pos.y=1.5
                    break

                if choarow.pos.y==1.5:
                    enyyy=0
                    gameplay=1                  #게임 로드
                    playing=1                   #게임 시작
                    befstart.visible=False
                    choarow.visible=False
                    
    while loading:
        rate(100)
        scene.center=choarow.pos+vector(3,0,0)
        scene.forward=(0,0,-1)
        rotatearrow(choarow)
        if scene.kb.keys:
            c=scene.kb.getkey()
            if c=='up':
                if choarow.pos.y==1.5:
                    continue
                else:
                    choarow.pos.y=choarow.pos.y+2
            elif c=='down':
                if choarow.pos.y==(1.5-2*n):
                    continue
                else:
                    choarow.pos.y=choarow.pos.y-2
            elif c=='\n':
                if choarow.pos.y==1.5-2*n:
                    timefor=200
                    while timefor:
                        rate(500)
                        scene.forward=(0,0,-1)
                        scene.range=4
                        rotatearrow(choarow)
                        befstart.pos.z=befstart.pos.z+1
                        befstart.pos.y=befstart.pos.y-1/4
                        timefor=timefor-1
                    choarow.pos.y=1.5
                    loading=0
                    enyyy=1
                    break        
                else:
                    scene.range=4
                    white_box.pos=scene.center+vector(0,0,0.5)
                    white_box.visible=True
                    loadnum=int((1.5-choarow.pos.y)/2)
                    keyview.pos=scene.center+vector(-3,-1,1)
                    keyview.visible=True
                    passwordview.pos=keyview.pos+vector(2,1,0)
                    passwordview.visible=True
                    passwordview.text=''
                    password=''      
                    while len(passwordview.text)-4:
                        rate(100)
                        if scene.kb.keys:
                            c=scene.kb.getkey()
                            if c.isdecimal():
                                password+=c
                                passwordview.text='*'*len(passwordview.text)
                                passwordview.text+=c
                            elif c=='backspace':
                                password=password[:-1]
                                passwordview.text=passwordview.text[:-1]
                            else:
                                break
                    if len(password)-4==0:
                        if (int(loadfiles[loadnum][4].rstrip()+password)**int(loadfiles[loadnum][2]))%int(loadfiles[loadnum][3])==int(loadfiles[loadnum][1]):
                            cancelask.pos=passwordview.pos+vector(0,2,0)
                            continask.pos=passwordview.pos+vector(0,-3,0)
                            cancelask.visible=True
                            continask.visible=True
                            getkey_1=1
                            
                            
                            while getkey_1:
                                rate(100)
                                if scene.kb.keys:
                                    c=scene.kb.getkey()
                                    if c=='up':
                                        break
                                    elif c=='down':
                                        if password=='0011' and loadfiles[loadnum][0]=='No gravity':
                                            eastegg=1
                                        playing=1
                                        loading=0
                                        gameplay=int(loadfiles[loadnum][3])//1000
                                        getkey_1=0
                                        befstart.visible=False
                                        choarow.visible=False
                                        
                        
                    keyview.visible=False
                    white_box.visible=False
                    passwordview.visible=False
                    cancelask.visible=False
                    continask.visible=False
                    
                    
                            

                
    while playing:
        
        rate(100)
        
        (radius_mainball,gravity,power,gamelist)=gamecall(gameplay)
        (box_data_list,ballwhere,stars,boxeslist,movinglist,makinglist)=makegame(gamelist,radius_mainball)        #movinglist: 움직이는 박스 리스트
        mainball=sphere(pos=ballwhere,radius=radius_mainball,velocity=vector(0,0,0),item=0)
        dt=0.01
        opacswit=0

        ca=0
        t=0                 #시간        

        g=vector(0,0,0)
        
        scene.userspin=True
        
        while stars:                                                            #본게임
            
            rate(100)
            t=t+dt
            scene.center=mainball.pos                                           #중앙조절
            scene.forward=(0,scene.forward.y,scene.forward.z)                   #방향제한

            if scene.mouse.clicked:                               #마우스 클릭으로 화면 크기 조정
                c=scene.mouse.getclick()
                ca=(ca+1)%6
                scene.range=ca+1
                            
            if scene.kb.keys:                                                   #키입력
                c=scene.kb.getkey()
                
                if c=='up':
                    if mainball.velocity.y<-power*dt:
                        mainball.velocity.y+=power*dt
                    mainball.velocity.y+=power*dt
                    
                elif c=='down':
                    if mainball.velocity.y>power*dt:
                        mainball.velocity.y-=power*dt
                    mainball.velocity.y-=power*dt
                    
                elif c=='right':
                    if mainball.velocity.x<-power*dt:
                        mainball.velocity.x+=power*dt
                    mainball.velocity.x+=power*dt
                    
                elif c=='left':
                    if mainball.velocity.x>-power*dt:
                        mainball.velocity.x-=power*dt
                    mainball.velocity.x-=power*dt

                elif c=='shift+up':
                    if mainball.item==2:
                        mainball.velocity+=vector(0,power*1.2,0)
                        mainball.velocity.z=power*0.2*(gravity.z/abs(gravity.z))
                        
                    else:
                        if mainball.velocity.y<-power*dt:
                            mainball.velocity.y+=power*dt
                        mainball.velocity.y+=power*dt

                elif c=='shift+down':
                    if mainball.item==2:
                        mainball.velocity+=vector(0,-power*1.2,0)
                        mainball.velocity.z=power*0.2*(power*0.2*(gravity.z/abs(gravity.z)))

                    else:
                        if mainball.velocity.y>power*dt:
                            mainball.velocity.y-=power*dt
                        mainball.velocity.y-=power*dt

                elif c=='shift+right':
                    if mainball.item==2:
                        mainball.velocity+=vector(power*1.2,0,0)
                        mainball.velocity.z=power*0.2*gravity.z/abs(gravity.z)
                    else:
                        if mainball.velocity.x<-power*dt:
                            mainball.velocity.x+=power*dt
                        mainball.velocity.x+=power*dt

                elif c=='shift+left':
                    if mainball.item==2:
                        mainball.velocity+=vector(-power*1.2,0,0)
                        mainball.velocity.z=power*0.2*gravity.z/abs(gravity.z)
                    else:
                        if mainball.velocity.x>-power*dt:
                            mainball.velocity.x-=power*dt
                        mainball.velocity.x-=power*dt

                elif c==' ':        #아이템 사용
                    mainball.color=(1,1,1)
                    if mainball.item==1:    #허공뛰기
                        if gravity.z<0:
                            mainball.velocity.z=power
                        elif gravity.z>0:
                            mainball.velocity.z=-power
                    elif mainball.item==2:
                        nvec=vector(mainball.velocity.x,mainball.velocity.y,0)
                        nvec=nvec/abs(nvec)
                        mainball.velocity=nvec*power*1.2+vector(0,0,power*0.4*(gravity.z/abs(gravity.z)))
                    mainball.item=0

                elif c=='ctrl+c':         #투명도 스위치 on/off
                    opacswit+=1
                    opacswit%=2
                    for i in range(len(gamelist)):                                
                        for j in range(len(gamelist[0])):
                            for k in range(len(gamelist[0][0])):
                                distance=abs(boxeslist[i][j][k].x-int(mainball.pos.x))+abs(boxeslist[i][j][k].y-int(mainball.pos.y))+abs(boxeslist[i][j][k].z-int(mainball.pos.z+1))
                                if boxeslist[i][j][k].num==1 or boxeslist[i][j][k].num==5 or boxeslist[i][j][k].num==9 :                            
                                    boxeslist[i][j][k].opacity=1
                                elif boxeslist[i][j][k].num==4 or boxeslist[i][j][k].num==6 or boxeslist[i][j][k].num==8 :
                                    for obj in boxeslist[i][j][k].objects:
                                        obj.opacity=1               
                                   
                        

                elif c=='\t':                                           #중도 저장 -tap
                    scene.userspin=False
                    getout=1
                    scene.range=4
                    white_box.pos=scene.center-scene.range.x*scene.forward
                    white_box.visible=True
                    white_box.axis=-scene.forward
                    text_name_frame.pos=white_box.pos-0.4*vector(0,scene.forward.y,scene.forward.z)
                    text_name_frame.axis=scene.forward
                    text_name.visible=True
                    text_name_frame.visible=True
                    text_nameview_frame.pos=text_name.pos+0.4*vector(0,scene.forward.z,scene.forward.y)
                    text_nameview_frame.axis=text_name_frame.axis
                    text_nameview.visible=True
                    text_name_frame.visible=True
                    username=''
                    
                    while 1:
                        rate(100)
                        
                        if scene.kb.keys:
                            c=scene.kb.getkey()
                            if c=='\n':
                                break
                            elif c=='\t':
                                getout=0
                                break
                            elif c=='backspace':
                                if len(username):
                                    username=username[:-1]
                                    text_nameview.text=username
                            elif len(c)==1:
                                username+=c
                                text_nameview.text=username
                    text_name.visible=False
                    text_nameview.visible=False
                    
                    cymonkey=''
                    if getout:
                        text_password_frame.pos=text_name.pos
                        text_password_frame.axis=text_name_frame.axis
                        
                        text_passwordview_frame.pos=text_nameview.pos
                        text_passwordview_frame.axis=text_nameview_frame.axis
                        
                        text_passwordview.visible=True
                        text_password.visible=True
                        
                        
                        while 1:
                            rate(100)
                            if scene.kb.keys:
                                c=scene.kb.getkey()
                                if c.isdecimal():
                                    cymonkey+=c
                                    text_passwordview.text='*'*len(text_passwordview.text)
                                    text_passwordview.text+=c
                                elif c=='\t':
                                    username=''
                                    getout=0
                                    break
                                elif c=='backspace':
                                    if len(cymonkey):
                                        cymonkey=cymonkey[:-1]
                                        text_passwordview.text=cymonkey
                                elif c=='\n':                               
                                    if len(cymonkey)==4:
                                        gamesave(str(gameplay),str(cymonkey),str(username))
                                        if str(cymonkey)=='0011' and str(username)=='No gravity':
                                            eastegg=1
                                        text_nameview.text=''
                                        text_nameview.visible=False
                                        break
                                    else:
                                        text_nameview.pos=text_password.pos-0.4*vector(0,scene.forward.z,scene.forward.y)
                                        text_nameview.text='just 4keys'
                                        text_nameview.visible=True
                            
                    white_box.visible=False
                    text_name.visible=False
                    text_nameview.visible=False
                    text_password.visible=False
                    text_passwordview.visible=False
                    scene.range=ca+1
                    text_nameview.text=''
                    text_passwordview.text=''
                    scene.userspin=True
                elif eastegg==1:
                    if c=='insert':
                        (g,gravity)=(gravity,g)
                        if g!=vector(0,0,0) and gravity!=vector(0,0,0):
                            g=vector(0,0,0)

                    elif c=='page up':
                        if mainball.velocity.z<power*dt:
                            mainball.velocity.z+=power*dt
                        mainball.velocity.z+=power*dt

                    elif c=='page down':
                        if mainball.velocity.z>-power*dt:
                            mainball.velocity.z-=power*dt
                        mainball.velocity.z-=power*dt
                    
                    

            
            if mainball.velocity.x<0:                                   #속도변화
                mainball.velocity.x+=-mainball.velocity.x*f*dt+f*dt
                if mainball.velocity.x>0:
                    mainball.velocity.x=0
            elif mainball.velocity.x>0:
                mainball.velocity.x+=-mainball.velocity.x*f*dt-f*dt
                if mainball.velocity.x<0:
                    mainball.velocity.x=0
                    
            if mainball.velocity.y<0:
                mainball.velocity.y+=-mainball.velocity.y*f*dt+f*dt
                if mainball.velocity.y>0:
                    mainball.velocity.y=0
            elif mainball.velocity.y>0:
                mainball.velocity.y+=-mainball.velocity.y*f*dt-f*dt
                if mainball.velocity.y<0:
                    mainball.velocity.y=0

            if mainball.velocity.z<0:
                mainball.velocity.z+=-mainball.velocity.x*f*dt+f*dt
                if mainball.velocity.z>0:
                    mainball.velocity.z=0
            elif mainball.velocity.z>0:
                mainball.velocity.z+=-mainball.velocity.x*f*dt-f*dt
                if mainball.velocity.z<0:
                    mainball.velocity.z=0

                                
                    
            mainball.velocity+=gravity*dt

            
            if mainball.pos.z<-1:
                if gravity.z<0:
                    endgame(mainball,boxeslist)
                    break                   #맵 지우기 필요
                else:
                    pass
            elif mainball.pos.z>len(gamelist):
                if gravity.z<=0:
                    pass        #아무것도 하지 않는다.
                else:
                    endgame(mainball,boxeslist)
                    break
            elif mainball.pos.x<0 or mainball.pos.y<0:
                pass
            
            else:               #틀 내에 공이 존재!
                DZter=0
                DYter=0
                DXter=0
                for tries in range(3):
                    if mainball.velocity.z<0 and DZter==0 :           #공이 떨어지는중                        
                        if int(mainball.pos.z+1+mainball.velocity.z*dt)>=len(gamelist)or int(mainball.pos.y)>=len(gamelist[0]) or int(mainball.pos.x)>=len(gamelist[0][0]):
                            pass
                        
                        elif int(mainball.pos.z+1)>int(mainball.pos.z+mainball.velocity.z*dt+1):
                            if gamelist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)]==0:
                                pass
                            else:
                                DZter+=1
                                if gamelist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)]==1:
                                    if (gravity.z)<0:
                                        mainball.pos.z=int(mainball.pos.z)
                                        mainball.velocity.z=power
                                    else:
                                        mainball.velocity.z=-mainball.velocity.z*0.9
                                elif gamelist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)]==4:
                                    if boxeslist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)].times==1:
                                        if (gravity.z)<0:
                                            gamelist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)]=0
                                            boxeslist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)].visible=False
                                            mainball.pos.z=int(mainball.pos.z)
                                            mainball.velocity.z=power
                                        else:
                                            mainball.velocity.z=-mainball.velocity.z*0.9
                                    elif boxeslist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)].times==2:
                                        if (gravity.z)<0:
                                            boxeslist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)].times=1
                                            boxeslist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)].cen.visible=False
                                            mainball.pos.z=int(mainball.pos.z)
                                            mainball.velocity.z=power
                                        else:
                                            mainball.velocity.z=-mainball.velocity.z*0.9
                                    
                                elif gamelist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)]==5:
                                    if boxeslist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)].Ttimes==0:
                                        if gravity.z<0:
                                            mainball.pos.z=int(mainball.pos.z)
                                            mainball.velocity.z=power*1.3
                                        else:
                                            mainball.velocity.z=-mainball.velocity.z*0.9
                                    else:
                                        if gravity.z<0:
                                            boxeslist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)].Ttimes-=1
                                            boxeslist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)].color=(0,0.5,boxeslist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)].Ttimes/10)
                                            if boxeslist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)].Ttimes==0:
                                                boxeslist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)].visible=False
                                                gamelist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)]=0
                                            mainball.pos.z=int(mainball.pos.z)
                                            mainball.velocity.z=power*1.3
                                        else:
                                            mainball.velocity.z=-mainball.velocity.z*0.9
                                elif gamelist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)]==6:
                                    if boxeslist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)].thorn==-1:
                                        if boxeslist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)].elv==2:
                                            if gravity.z<0:
                                                mainball.pos.z=boxeslist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)].center.pos.z+boxeslist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)].pos.z+0.05
                                                mainball.velocity.z=power
                                            else:
                                                mainball.velocity.z=-mainball.velocity.z*0.9  
                                            
                        elif gamelist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)]==6:
                            if boxeslist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)].thorn==-1:
                                if boxeslist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)].pos.z+boxeslist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)].center.pos.z+0.05>=mainball.pos.z+mainball.velocity.z*dt>=boxeslist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)].center.pos.z+boxeslist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)].pos.z-0.05:
                                    DZter+=1
                                    if gravity.z<0:
                                        mainball.pos.z=boxeslist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)].center.pos.z+boxeslist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)].pos.z+0.05
                                        mainball.velocity.z=power
                                    else:
                                        mainball.velocity.z=-mainball.velocity.z*0.9  

                                
                                                
                    elif mainball.velocity.z>0 and DZter==0:
                        if int(mainball.pos.z+1+mainball.velocity.z*dt)>=len(gamelist)or int(mainball.pos.y)>=len(gamelist[0]) or int(mainball.pos.x)>=len(gamelist[0][0]):
                            pass
                        
                        elif int(mainball.pos.z+1)<int(mainball.pos.z+mainball.velocity.z*dt+1):                            
                            if gamelist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)]==0:
                                pass
                            else:
                                DZter+=1
                                if gamelist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)]==1:
                                    if gravity.z<=0:
                                        mainball.velocity.z=-mainball.velocity.z*0.9
                                    else:
                                        mainball.pos.z=int(mainball.pos.z+1)
                                        mainball.velocity.z=-power
                                elif gamelist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)]==4:
                                    if gravity.z<=0:
                                        mainball.velocity.z=-mainball.velocity.z*0.9
                                    elif boxeslist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)].times==1:
                                        gamelist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)]=0
                                        boxeslist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)].visible=False
                                        mainball.pos.z=int(mainball.pos.z+1)
                                        mainball.velocity.z=-power
                                    elif boxeslist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)].times==2:
                                        boxeslist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)].times=1
                                        boxeslist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)].cen.visible=False
                                        mainball.pos.z=int(mainball.pos.z+1)
                                        mainball.velocity.z=-power
                                

                                elif gamelist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)]==5:
                                    if gravity.z<=0:
                                        mainball.velocity.z=-mainball.velocity.z*0.9
                                    elif boxeslist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)].Ttimes==0:
                                        mainball.pos.z=int(mainball.pos.z+1)
                                        mainball.velocity.z=-power*1.3
                                    else:
                                        boxeslist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)].Ttimes-=1
                                        boxeslist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)].color=(0,0.5,boxeslist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)].Ttimes/10)
                                        if boxeslist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)].Ttimes==0:
                                            boxeslist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)].visible=False
                                            gamelist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)]=0
                                        mainball.pos.z=int(mainball.pos.z+1)
                                        mainball.velocity.z=-power*1.3

                                elif gamelist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)]==6:
                                    if boxeslist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)].thorn==1:
                                        if boxeslist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)].elv==-2:
                                            if gravity.z<=0:
                                                mainball.velocity.z=-mainball.velocity.z*0.9
                                            else:
                                                mainball.pos.z=boxeslist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)].center.pos.z+boxeslist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)].pos.z-0.05
                                                mainball.velocity.z=-power
                                        
                        elif gamelist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)]==6:
                            if boxeslist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)].thorn==1:
                                if boxeslist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)].center.pos.z+boxeslist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)].pos.z+0.05>=mainball.pos.z+mainball.velocity.z*dt>=boxeslist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)].pos.z+boxeslist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)].center.pos.z-0.05:
                                    DZter+=1
                                    if gravity.z<=0:
                                        mainball.velocity.z=-mainball.velocity.z*0.9
                                    else:
                                        mainball.pos.z=boxeslist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)].center.pos.z+boxeslist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x)].pos.z-0.05
                                        mainball.velocity.z=-power
                                
                                        

                    if mainball.velocity.y<0 and DYter==0:           #공이 위쪽 이동
                        if int(mainball.pos.y)>int(mainball.pos.y+mainball.velocity.y*dt):
                            if int(mainball.pos.z+1)>=len(gamelist)or int(mainball.pos.y+mainball.velocity.y*dt)>=len(gamelist[0]) or int(mainball.pos.x)>=len(gamelist[0][0]):
                                pass
                            elif gamelist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)]==0:
                                pass
                            elif gamelist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)]==1 or gamelist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)]==4 or gamelist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)]==5:
                                mainball.velocity.y=-mainball.velocity.y*0.9
                                DYter+=1
                            elif gamelist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)]==6:
                                if boxeslist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)].center.pos.z+boxeslist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)].pos.z+0.05>=mainball.pos.z>=boxeslist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)].center.pos.z-0.05+boxeslist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)].pos.z:
                                    mainball.velocity.y=-mainball.velocity.y*0.9
                                    DYter+=1

                    elif mainball.velocity.y>0 and DYter==0:
                        if int(mainball.pos.y)<int(mainball.pos.y+mainball.velocity.y*dt):
                            if int(mainball.pos.z+1)>=len(gamelist)or int(mainball.pos.y+mainball.velocity.y*dt)>=len(gamelist[0]) or int(mainball.pos.x)>=len(gamelist[0][0]):
                                pass
                            elif gamelist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)]==0:
                                pass
                            elif gamelist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)]==1 or gamelist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)]==4 or gamelist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)]==5:
                                mainball.velocity.y=-mainball.velocity.y*0.9
                                DYter+=1
                            elif gamelist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)]==6:
                                if boxeslist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)].center.pos.z+boxeslist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)].pos.z+0.05>=mainball.pos.z>=boxeslist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)].center.pos.z-0.05+boxeslist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)].pos.z:
                                    mainball.velocity.y=-mainball.velocity.y*0.9
                                    DYter+=1

                    if mainball.velocity.x<0 and DXter==0:           #공이 옆쪽 이동
                        if int(mainball.pos.x)>int(mainball.pos.x+mainball.velocity.x*dt):
                            if int(mainball.pos.z+1)>=len(gamelist)or int(mainball.pos.y+mainball.velocity.y*dt)>=len(gamelist[0]) or int(mainball.pos.x+mainball.velocity.x*dt)>=len(gamelist[0][0]):
                                pass
                            elif gamelist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)]==0:
                                pass
                            elif gamelist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)]==1 or gamelist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)]==4 or gamelist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)]==5:
                                mainball.velocity.x=-mainball.velocity.x*0.9
                                DXter+=1
                            elif gamelist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)]==6:
                                if boxeslist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)].center.pos.z+0.05+boxeslist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)].pos.z>=mainball.pos.z>=boxeslist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)].center.pos.z-0.05+boxeslist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)].pos.z:
                                    mainball.velocity.x=-mainball.velocity.x*0.9
                                    DXter+=1
                                
                            
                    elif mainball.velocity.x>0 and DXter==0:
                        if int(mainball.pos.x)<int(mainball.pos.x+mainball.velocity.x*dt):
                            if int(mainball.pos.z+1)>=len(gamelist)or int(mainball.pos.y+mainball.velocity.y*dt)>=len(gamelist[0]) or int(mainball.pos.x+mainball.velocity.x*dt)>=len(gamelist[0][0]):
                                pass
                            elif gamelist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)]==0:
                                pass
                            elif gamelist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)]==1 or gamelist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)]==4 or gamelist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)]==5:
                                mainball.velocity.x=-mainball.velocity.x*0.9
                                DXter+=1
                            elif gamelist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)]==6:
                                if boxeslist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)].pos.z+boxeslist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)].center.pos.z+0.05>=mainball.pos.z>=boxeslist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)].center.pos.z-0.05+boxeslist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)].pos.z:
                                    mainball.velocity.x=-mainball.velocity.x*0.9
                                    DXter+=1

                if DZter==0 and DYter==0:
                    if int(mainball.pos.z+1)!=int(mainball.pos.z+1+mainball.velocity.z*dt) and int(mainball.pos.y)!=int(mainball.pos.y+mainball.velocity.y*dt):
                        if int(mainball.pos.z+1+mainball.velocity.z*dt)>=len(gamelist) or int(mainball.pos.y+mainball.velocity.y*dt)>=len(gamelist[0]) or int(mainball.pos.x)>=len(gamelist[0][0]):
                            pass
                        elif gamelist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)]==0:
                            pass
                        elif gamelist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)]==1 or gamelist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)]==4 or gamelist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)]==5:
                            mainball.velocity=vector(mainball.velocity.x,-0.9*mainball.velocity.z,-0.9*mainball.velocity.y)
                            DZter+=1
                            DYter+=1
                if DZter==0 and DXter==0:
                    if int(mainball.pos.z+1)!=int(mainball.pos.z+1+mainball.velocity.z*dt) and int(mainball.pos.x)!=int(mainball.pos.y+mainball.velocity.y*dt):
                        if int(mainball.pos.z+1+mainball.velocity.z*dt)>=len(gamelist) or int(mainball.pos.y)>=len(gamelist[0]) or int(mainball.pos.x+mainball.velocity.x*dt)>=len(gamelist[0][0]):
                            pass
                        elif gamelist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)]==0:
                            pass
                        elif gamelist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)]==1 or gamelist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)]==4 or gamelist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)]==5:
                            mainball.velocity=vector(mainball.velocity.z*(-0.9),mainball.velocity.y,mainball.velocity.x*(0.9))
                            DZter+=1
                            DXter+=1
                if DXter==0 and DYter==0:
                    if int(mainball.pos.y)!=int(mainball.pos.y+mainball.velocity.y*dt) and int(mainball.pos.x)!=int(mainball.pos.x+mainball.velocity.x*dt):
                        if int(mainball.pos.z+1)>=len(gamelist) or int(mainball.pos.y+mainball.velocity.y*dt)>=len(gamelist[0]) or int(mainball.pos.x+mainball.velocity.x*dt)>=len(gamelist[0][0]):
                            pass
                        elif gamelist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x+mainball.velocity.x*dt)]==0:
                            pass
                        elif gamelist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x+mainball.velocity.x*dt)]==1 or gamelist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x+mainball.velocity.x*dt)]==4 or gamelist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x+mainball.velocity.x*dt)]==5:
                            mainball.velocity=vector(mainball.velocity.y*dt*(-0.9),-0.9*mainball.velocity.x,mainball.velocity.z)
                            DXter+=1
                            DYter+=1
                if DXter==0 and DYter==0 and DZter==0:
                    if int(mainball.pos.z+1+mainball.velocity.z*dt)!=int(mainball.pos.z+1) and int(mainball.pos.y)!=int(mainball.pos.y+mainball.velocity.y*dt) and int(mainball.pos.x)!=int(mainball.pos.x+mainball.velocity.x*dt):
                        if int(mainball.pos.z+1+mainball.velocity.z*dt)>=len(gamelist) or int(mainball.pos.y+mainball.velocity.y*dt)>=len(gamelist[0]) or int(mainball.pos.x+mainball.velocity.x*dt)>=len(gamelist[0][0]):
                            pass
                        elif gamelist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x+mainball.velocity.x*dt)]==0:
                            pass
                        elif gamelist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x+mainball.velocity.x*dt)]==1 or gamelist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x+mainball.velocity.x*dt)]==4 or gamelist[int(mainball.pos.z+1+mainball.velocity.z*dt)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x+mainball.velocity.x*dt)]==5:
                            mainball.velocity=-0.9*mainball.velocity
            
                            
                            
            mainball.pos=mainball.pos+mainball.velocity*dt                  #위치변화

            if opacswit:
                for i in range(len(gamelist)):                                  #투명도 조절
                    for j in range(len(gamelist[0])):
                        for k in range(len(gamelist[0][0])):
                            distance=abs(boxeslist[i][j][k].x-int(mainball.pos.x))+abs(boxeslist[i][j][k].y-int(mainball.pos.y))+abs(boxeslist[i][j][k].z-int(mainball.pos.z+1))
                            if boxeslist[i][j][k].num==1 or boxeslist[i][j][k].num==5 or boxeslist[i][j][k].num==9 :                            
                                if distance>4:
                                    boxeslist[i][j][k].opacity=0.05
                                else:
                                    boxeslist[i][j][k].opacity=1-0.2*distance
                            elif boxeslist[i][j][k].num==4 or boxeslist[i][j][k].num==6 or boxeslist[i][j][k].num==8 :
                                if distance>4:
                                    for obj in boxeslist[i][j][k].objects:
                                        obj.opacity=0.05                     #뭘로해야 적당하지?? 투명도
                                else:
                                    for obj in boxeslist[i][j][k].objects:
                                        obj.opacity=1-0.2*distance
                        
                            
                        

            if 0<=int(mainball.pos.x)<len(gamelist[0][0]) and 0<=int(mainball.pos.y)<len(gamelist[0]) and 0<=int(mainball.pos.z+1)<len(gamelist):   #현 위치에 대한 변화
                for starobj in box_data_list[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x)].starslist:
                    if abs(mainball.pos-starobj.pos)<=mainball.radius+starobj.radius:
                        starobj.visible=False
                        stars-=1
                        for boxarea in starobj.around:
                            box_data_list[boxarea[0]][boxarea[1]][boxarea[2]].starslist.remove(starobj)
                        if stars==0:
                            gameplay+=1
                            endgame(mainball,boxeslist,stars)
                for bumperobj in box_data_list[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x)].bumperslist:
                    if abs(mainball.pos-bumperobj.pos)<=mainball.radius+starobj.radius:
                        bumperobj.visible=False
                        for boxarea in bumperobj.around:
                            box_data_list[boxarea[0]][boxarea[1]][boxarea[2]].bumperslist.remove(bumperobj)
                        mainball.velocity=(2*(-mainball.velocity).dot(mainball.pos-boxeslist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x)].pos)*(mainball.pos-boxeslist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x)].pos))/(abs(mainball.pos-boxeslist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x)].pos)**2)+mainball.velocity+(boxeslist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x)].reforce-1)*(mainball.pos-boxeslist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x)].pos)
                        
                if gamelist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x)]==8:
                    boxeslist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x)].visible=False
                    gamelist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x)]=0
                    if boxeslist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x)].eff==0:      #역중력
                        gravity=-gravity

                    elif boxeslist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x)].eff==1:     #허공뛰기
                        mainball.item=1
                        mainball.color=color.magenta

                    elif boxeslist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x)].eff==2:
                        mainball.item=2
                        mainball.color=color.gray(0.8)
                        
                            
                elif gamelist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x)]==6:                            
                    GC=boxeslist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x)]
                    if GC.thorn>=0:
                        if GC.pos.z+GC.center.pos.z+0.05<mainball.pos.z<GC.pos.z+GC.center.pos.z+0.15:
                            endgame(mainball,boxeslist)
                            break
                    if GC.thorn<=0:
                        if GC.pos.z+GC.center.pos.z-0.05>mainball.pos.z>GC.pos.z+GC.center.pos.z-0.15:
                            endgame(mainball,boxeslist)
                            break

            movinglist=fellingmaking(makinglist,gamelist,t,movinglist)
            (movinglist,stop)=box_move(movinglist,gamelist)
            if stop==1:
                endgame(mainball,boxeslist)
                break
            
                            
                        

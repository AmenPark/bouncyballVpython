from vpython import *
from math import*
from random import *
from time import *

boundforce=vector(0,0,5.5)    #튀는힘

gravity=vector(0,0,-9.5)     #중력장



choarow=arrow(pos=(-3,1.5,0),axis=(1,0,0),shaftwidth=0.1,color=color.yellow)

f=open('saved.txt','a')
f.close()

eastegg=0

f=0.5   #저항

scene.userzoom=False
scene.userspin=False

def mapmaking():
    global Xlines, Ylines, Zlines, Xarrows, Yarrows, Zarrows, game_making_list, boxes_making_list
    
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
        c=scene.kb.getkey()
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

        elif c=='back space' or c== 'delete':
            boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].visible=False
            boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]=box(visible=False)
            game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]=0
            
        elif c=='f' or c=='s' or c=='+' or c=='-':
            if game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==8:
                if c=='f' and boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].gen<=5:
                    boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].gen+=1
                    print('speed='+str(boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].gen))
                elif c=='s' and boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].gen>=3:
                    boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].gen-=1
                    print('speed='+str(boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].gen))
                elif c=='+' and boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].trying<=3:
                    boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].delay+=1
                elif c=='-' and boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].trying>=1:
                    boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].delay-=1
                
            
        elif c==' ':
            game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]+=1
            game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]%=11
            boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].visible=False
            if game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==0:
               boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]=box(visible=False)
            elif game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==1:
                boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]=box(pos=choosebox.pos,size=(1,1,1),num=1)
            elif game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==2:
                boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]=text(pos=choosebox.pos,text='S',num=2,align='center',width=0.5,height=0.5)
            elif game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==3:
                boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]=sphere(pos=choosebox.pos,num=3,radius=0.2,color=color.yellow)
            elif game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==4:
                A=frame(num=4,pos=choosebox.pos)
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
                A=box(size=(1,1,1),pos=choosebox.pos,num=6,color=(1,0,0))
                boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]=A
            elif game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==6:
                A=box(size=(1,1,1),pos=choosebox.pos,num=7,color=(0,0.5,0.1),Ttimes=1)
                boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]=A
            elif game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==7:
                A=frame(num=8,pos=choosebox.pos)
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
                
            elif game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==8:
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
            elif game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==9:
                A=frame(pos=choosebox.pos,num=10)
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
            elif game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==10:
                A=sphere(radius=0.3,color=color.red,pos=choosebox.pos,num=11)
                boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]=A
        elif c=='\t':
            if game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==0 or game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==2:
                print('Warning! name "new" data can be rewritten. please check if there is a text name "new".\nyou can save this map Y/N')
                a=scene.kb.getkey()
                if a=='N':
                    pass
                elif a=='Y':
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
                print('nothing only')
                
            elif game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==3:
                print('nothing')
                
            elif game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==4:
                print('one more? or...')
                boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].visible=False
                if len(boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].objects)==8:
                    A=frame(num=5,pos=choosebox.pos)
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
                    A=frame(num=4,pos=choosebox.pos)
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
                print('nothing')
                
            elif game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==6:
                print('from green(less times) to blue(many times)')
                boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].Ttimes=boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].Ttimes%10+1
                boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].color=(0,0.5,boxes_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)].Ttimes/10)
            elif game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==7:
                print('nothing')
            elif game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==8:
                print('you can choose the speed and the start_delay by... f:faster, s:slower, +:start_delay plus, -:start_delay minus')
               
            elif game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==9:
                print('nothing')
                
            elif game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==10:
                print('nothing')
                
            elif game_making_list[int(choosebox.pos.z)][int(choosebox.pos.y)][int(choosebox.pos.x)]==11:
                print('nothing')

                
def savethemap():
    global game_making_list, boxes_making_list, Xlines, Ylines, Zlines
    f=open('new.txt','w')
    f.write('\t'.join([str(Xlines),str(Ylines),str(Zlines)])+'\n')
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
                    f.write('3\t')
                elif game_making_list[k][j][i]==4:
                    if len(boxes_making_list[k][j][i].objects)==8:
                        f.write('4\t')
                    else:
                        f.write('5\t')
                elif game_making_list[k][j][i]==5:
                    f.write('6\t')
                elif game_making_list[k][j][i]==6:
                    f.write(str(9+boxes_making_list[k][j][i].Ttimes)+'\t')
                elif game_making_list[k][j][i]==7:
                    f.write('7\t')
                elif game_making_list[k][j][i]==8:
                    f.write(str(boxes_making_list[k][j][i].trying*5+boxes_making_list[k][j][i].gen+18)+'\t')
                elif game_making_list[k][j][i]==9:
                    f.write('8\t')
                elif game_making_list[k][j][i]==10:
                    f.write('9\t')
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
    f=open(str(gameplay).zfill(2)+'.txt','r')
    stg=f.readline().split()
    Xlines=int(stg[0])
    Ylines=int(stg[1])
    Zlines=int(stg[2])          #txt파일 맨 위의 값 N은 x*y*z맵임을 명시
    returning=[]
    for i in range(Zlines):
        returning.append([])
        for j in range(Ylines):
            returning[i].append([])
            stg=f.readline().split()
            for k in range (Xlines):
                returning[i][j].append(int(stg[k]))     #리스트 1차 z, 2차 y, 3차 x
    f.close()
    return returning
        
def makegame(gamelist):                 #gamelist[Z][Y][X]로 됨.
    Zlines=len(gamelist)
    Ylines=len(gamelist[0])
    Xlines=len(gamelist[0][0])
    stars=0                 #별 개수
    whereball=(0,0,0)       #공 시작 위치
    boxeslist=[]               #박스들 리스트
    movinglist=[]                 #움직이는 것 리스트
    makinglist=[]                   #만드는 것 리스트 
    for i in range(Zlines):
        boxeslist.append([])        
        for j in range(Ylines):
            boxeslist[i].append([])
            for k in range(Xlines):
                if gamelist[i][j][k]==0:        #0:빈 공간
                    A=box(num=0,visible=False)
                    boxeslist[i][j].append(A)
                    continue
                elif gamelist[i][j][k]==1:      #1:일반 박스
                    A=box(size=(1,1,1),pos=(k+0.5,j+0.5,i-0.5),num=1)
                    boxeslist[i][j].append(A)
                    
                elif gamelist[i][j][k]==2:      #2:시작점
                    whereball=(k+0.5,j+0.5,i-0.5)
                    A=box(num=0,visible=False)
                    boxeslist[i][j].append(A)
                    gamelist[i][j][k]=0

                elif gamelist[i][j][k]==3:      #3:먹어야 하는 노란빛(관계X)                    
                    A=sphere(pos=(k+0.5,j+0.5,i-0.7),radius=0.2,color=color.yellow,num=3)
                    boxeslist[i][j].append(A)
                    stars=stars+1

                elif gamelist[i][j][k]==4:      #4:튕기면 사라지는 발판
                    A=frame(num=4,pos=(k+0.5,j+0.5,i-0.5))
                    c=(random(),random(),random())
                    A1=box(pos=(0.3,0.3,0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                    A2=box(pos=(0.3,0.3,-0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                    A3=box(pos=(0.3,-0.3,0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                    A4=box(pos=(-0.3,0.3,0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                    A5=box(pos=(0.3,-0.3,-0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                    A6=box(pos=(-0.3,-0.3,0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                    A7=box(pos=(-0.3,0.3,-0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                    A8=box(pos=(-0.3,-0.3,-0.3),size=(0.4,0.4,0.4),frame=A,color=c)
                    boxeslist[i][j].append(A)

                elif gamelist[i][j][k]==5:      #5:튕기면 사라지는 발판으로 변환한다.
                    A=frame(num=5,pos=(k+0.5,j+0.5,i-0.5))
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
                    boxeslist[i][j].append(A)

                elif gamelist[i][j][k]==6:      #6:높이 뛰는 발판, 색으로 횟수 제한. 
                    A=box(size=(1,1,1),pos=(k+0.5,j+0.5,i-0.5),num=6,color=(1,0,0))
                    boxeslist[i][j].append(A)

                elif 10<=gamelist[i][j][k]<20:      #10~19: 각각 color의 blue 값이 증가. 밟을수록 blue값 감소. 1~10회 가능.
                    A=box(size=(1,1,1),pos=(k+0.5,j+0.5,i-0.5),num=7,color=(0,0.5,(gamelist[i][j][k]-9)/10),Ttimes=gamelist[i][j][k]-9)
                    boxeslist[i][j].append(A)
                    gamelist[i][j][k]=7

                elif gamelist[i][j][k]==7:      #7: 가시. 닿으면 죽는다.
                    A=frame(num=8,pos=(k+0.5,j+0.5,i-0.5))
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
                    gamelist[i][j][k]=8
                    boxeslist[i][j].append(A)

                elif 20<=gamelist[i][j][k]<40:      #20~39: 낙석. 돌이 추락한다. 맞으면 사망. 리젠타임..., trying:낙석 횟수. 5단위 내로 속도조절, 5단위 밖으로 타이밍 조절
                    A=box(num=9,visible=False,pos=(k+0.5,j+0.5,i-0.5),gen=(((gamelist[i][j][k]-20)%5)+2)**1.5,trying=((gamelist[i][j][k]-19)//5)*0.25)
                    gamelist[i][j][k]=0
                    boxeslist[i][j].append(box(num=0,visible=False))
                    makinglist.append(A)

                elif gamelist[i][j][k]==8:      #8: 역중력 아이템
                    A=frame(pos=(k+0.5,j+0.5,i-0.5),num=10)
                    A0=box(size=(0.8,0.8,0.8),pos=(0,0,0),frame=A)
                    A1=arrow(pos=(0.2,0.4,0.45),axis=(0,0,-0.8),color=color.yellow,frame=A)
                    A2=arrow(pos=(-0.2,0.4,-0.45),axis=(0,0,0.8),color=color.yellow,frame=A)
                    A3=arrow(pos=(0.2,-0.4,-0.45),axis=(0,0,0.8),color=color.yellow,frame=A)
                    A4=arrow(pos=(-0.2,-0.4,0.45),axis=(0,0,-0.8),color=color.yellow,frame=A)
                    A5=arrow(pos=(0.4,-0.2,0.45),axis=(0,0,-0.8),color=color.yellow,frame=A)
                    A6=arrow(pos=(0.4,0.2,-0.45),axis=(0,0,0.8),color=color.yellow,frame=A)
                    A7=arrow(pos=(-0.4,-0.2,-0.45),axis=(0,0,0.8),color=color.yellow,frame=A)
                    A8=arrow(pos=(-0.4,0.2,0.45),axis=(0,0,-0.8),color=color.yellow,frame=A)
                    boxeslist[i][j].append(A)
                    gamelist[i][j][k]=10

                elif gamelist[i][j][k]==9:      #9:범퍼(?) 퉁기면 깨진다.
                    A=sphere(radius=0.3,color=color.red,pos=(k+0.5,j+0.5,i-0.5),num=11)
                    gamelist[i][j][k]=11
                    boxeslist[i][j].append(A)
                    

                    

    return (whereball,stars,boxeslist,movinglist,makinglist)             #공 위치, 별들, 층별 프레임 리스트, 박스생성자 리스트 반환
                    
                    
                

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
        if obj.gen*obj.trying/2<=time:
            A=frame(num=9,pos=obj.pos,velocity=vector(0,0,0))
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
        if obj.num==9:
            obj.pos+=obj.velocity*dt
            obj.velocity+=gravity*dt
            if obj.pos.z<-1 or obj.pos.z>len(gamelist):
                obj.visible=False
                movinglist.remove(obj)
            elif int(obj.pos.z+1)>=len(gamelist) or int(obj.pos.y)>=len(gamelist[0]) or int(obj.pos.x)>=len(gamelist[0][0]):
                obj.visible=False
            elif gamelist[int(obj.pos.z+1)][int(obj.pos.y)][int(obj.pos.x)] ==1 or gamelist[int(obj.pos.z+1)][int(obj.pos.y)][int(obj.pos.x)] ==4 or gamelist[int(obj.pos.z+1)][int(obj.pos.y)][int(obj.pos.x)] ==5 or gamelist[int(obj.pos.z+1)][int(obj.pos.y)][int(obj.pos.x)] ==6 or gamelist[int(obj.pos.z+1)][int(obj.pos.y)][int(obj.pos.x)] ==7 or gamelist[int(obj.pos.z+1)][int(obj.pos.y)][int(obj.pos.x)] ==8:
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

text_name=text(text='name',align='center',width=0.7,height=0.4)
text_password=text(text='password',align='center',width=0.7,height=0.4)
text_name.visible=False
text_password.visible=False

text_nameview=text(text='',align='center',width=0.7,height=0.4)
text_nameview.visible=False

text_passwordview=text(text='',align='center',width=0.7,height=0.4)
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
        
        gamelist=gamecall(gameplay)
        (ballwhere,stars,boxeslist,movinglist,makinglist)=makegame(gamelist)                 #movinglist: 움직이는 박스 리스트
        mainball=sphere(pos=ballwhere,radius=0.1,velocity=vector(0,0,0))
        dt=0.01
        power=5.5
        ca=0
        t=0                 #시간        
        gravity=vector(0,0,-9.5)
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

                elif c=='\t':                                           #중도 저장 -tap
                    scene.userspin=False
                    getout=1
                    scene.range=4
                    white_box.pos=scene.center-scene.range.x*scene.forward
                    white_box.visible=True
                    white_box.axis=-scene.forward
                    text_name.pos=white_box.pos-0.4*vector(0,scene.forward.y,scene.forward.z)
                    text_name.axis=-vector(scene.forward.z,0,0)
                    if scene.forward.y!=0:
                        text_name.rotate(angle=vector(-scene.forward).diff_angle(vector(0,0,1)),axis=(1,0,0))
                    text_name.visible=True
                    text_nameview.pos=text_name.pos+0.4*vector(0,scene.forward.z,scene.forward.y)
                    text_nameview.axis=text_name.visible
                    if scene.forward.y!=0:
                        text_nameview.rotate(angle=vector(-scene.forward).diff_angle(vector(0,0,1)),axis=(1,0,0))
                    text_nameview.visible=True
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
                        text_password.pos=text_name.pos
                        text_password.axis=text_name.axis
                        
                        text_passwordview.pos=text_nameview.pos
                        text_passwordview.axis=text_nameview.axis
                        
                        if scene.forward.y!=0:
                            text_password.rotate(angle=vector(-scene.forward).diff_angle(vector(0,0,1)),axis=(1,0,0))
                            text_passwordview.rotate(angle=vector(-scene.forward).diff_angle(vector(0,0,1)),axis=(1,0,0))
                        
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
                    if scene.forward.y!=0:
                        text_name.rotate(angle=vector(-scene.forward).diff_angle(vector(0,0,1)),axis=(-1,0,0))
                        text_nameview.rotate(angle=vector(-scene.forward).diff_angle(vector(0,0,1)),axis=(-1,0,0))
                        text_passwordview.rotate(angle=vector(-scene.forward).diff_angle(vector(0,0,1)),axis=(-1,0,0))
                        text_password.rotate(angle=vector(-scene.forward).diff_angle(vector(0,0,1)),axis=(-1,0,0))
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

            
            if mainball.pos.z<-2:
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
                        if int(mainball.pos.z+1)>int(mainball.pos.z+mainball.velocity.z*dt+1):
                            if int(mainball.pos.z+2+mainball.velocity.z*dt)-1>=len(gamelist)or int(mainball.pos.y)>=len(gamelist[0]) or int(mainball.pos.x)>=len(gamelist[0][0]):
                                pass
                            elif gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y)][int(mainball.pos.x)]==0:
                                pass
                            else:
                                DZter+=1
                                if gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y)][int(mainball.pos.x)]==1:
                                    if (gravity.z)<0:
                                        mainball.pos.z=int(mainball.pos.z)
                                        mainball.velocity.z=power
                                    else:
                                        mainball.velocity.z=-mainball.velocity.z*0.9
                                elif gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y)][int(mainball.pos.x)]==4:
                                    if (gravity.z)<0:
                                        gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y)][int(mainball.pos.x)]=0
                                        boxeslist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y)][int(mainball.pos.x)].visible=False
                                        mainball.pos.z=int(mainball.pos.z)
                                        mainball.velocity.z=power
                                    else:
                                        mainball.velocity.z=-mainball.velocity.z*0.9
                                elif gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y)][int(mainball.pos.x)]==5:
                                    if (gravity.z)<0:
                                        gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y)][int(mainball.pos.x)]=4
                                        boxeslist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y)][int(mainball.pos.x)].objects[4].visible=False
                                        mainball.pos.z=int(mainball.pos.z)
                                        mainball.velocity.z=power
                                    else:
                                        mainball.velocity.z=-mainball.velocity.z*0.9
                                elif gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y)][int(mainball.pos.x)]==6:
                                    if gravity.z<0:
                                        mainball.pos.z=int(mainball.pos.z)
                                        mainball.velocity.z=power*1.3
                                    else:
                                        mainball.velocity.z=-mainball.velocity.z*0.9
                                elif gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y)][int(mainball.pos.x)]==7:
                                    if gravity.z<0:
                                        boxeslist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y)][int(mainball.pos.x)].Ttimes=boxeslist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y)][int(mainball.pos.x)].Ttimes-1
                                        boxeslist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y)][int(mainball.pos.x)].color=(0,0.5,boxeslist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y)][int(mainball.pos.x)].Ttimes/10)
                                        if boxeslist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y)][int(mainball.pos.x)].Ttimes==0:
                                            boxeslist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y)][int(mainball.pos.x)].visible=False
                                            gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y)][int(mainball.pos.x)]=0
                                        mainball.pos.z=int(mainball.pos.z)
                                        mainball.velocity.z=power*1.3
                                    else:
                                        mainball.velocity.z=-mainball.velocity.z*0.9                                

                    elif mainball.velocity.z>0 and DZter==0:
                        if int(mainball.pos.z+1)<int(mainball.pos.z+mainball.velocity.z*dt+1):
                            if int(mainball.pos.z+2+mainball.velocity.z*dt)-1>=len(gamelist)or int(mainball.pos.y)>=len(gamelist[0]) or int(mainball.pos.x)>=len(gamelist[0][0]):
                                pass
                            elif gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y)][int(mainball.pos.x)]==0:
                                pass
                            else:
                                DZter+=1
                                if gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y)][int(mainball.pos.x)]==1:
                                    if gravity.z<=0:
                                        mainball.velocity.z=-mainball.velocity.z*0.9
                                    else:
                                        mainball.pos.z=int(mainball.pos.z+1)
                                        mainball.velocity.z=-power
                                elif gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y)][int(mainball.pos.x)]==4:
                                    if gravity.z<=0:
                                        mainball.velocity.z=-mainball.velocity.z*0.9
                                    else:
                                        gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y)][int(mainball.pos.x)]=0
                                        boxeslist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y)][int(mainball.pos.x)].visible=False
                                        mainball.pos.z=int(mainball.pos.z+1)
                                        mainball.velocity.z=-power
                                elif gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y)][int(mainball.pos.x)]==5:
                                    if gravity.z<=0:
                                        mainball.velocity.z=-mainball.velocity.z*0.9
                                    else:
                                        gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y)][int(mainball.pos.x)]=4
                                        boxeslist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y)][int(mainball.pos.x)].objects[4].visible=False
                                        mainball.pos.z=int(mainball.pos.z+1)
                                        mainball.velocity.z=-power

                                elif gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y)][int(mainball.pos.x)]==6:
                                    if gravity.z<=0:
                                        mainball.velocity.z=-mainball.velocity.z*0.9
                                    else:
                                        mainball.pos.z=int(mainball.pos.z+1)
                                        mainball.velocity.z=-power*1.3
                                        
                                elif gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y)][int(mainball.pos.x)]==7:
                                    if gravity.z<=0:
                                        mainball.velocity.z=-mainball.velocity.z*0.9
                                    else:
                                        boxeslist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y)][int(mainball.pos.x)].Ttimes=boxeslist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y)][int(mainball.pos.x)].Ttimes-1
                                        boxeslist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y)][int(mainball.pos.x)].color=(0,0.5,boxeslist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y)][int(mainball.pos.x)].Ttimes/10)
                                        if boxeslist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y)][int(mainball.pos.x)].Ttimes==0:
                                            boxeslist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y)][int(mainball.pos.x)].visible=False
                                            gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y)][int(mainball.pos.x)]=0
                                        mainball.pos.z=int(mainball.pos.z+1)
                                        mainball.velocity.z=-power*1.3

                                elif gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y)][int(mainball.pos.x)]==8:
                                    if gravity.z<=0:
                                        mainball.velocity.z=-mainball.velocity.z*0.9
                                    else:
                                        mainball.pos.z=int(mainball.pos.z+1)
                                        mainball.velocity.z=-power
                                
                            

                    if mainball.velocity.y<0 and DYter==0:           #공이 위쪽 이동
                        if int(mainball.pos.y)>int(mainball.pos.y+mainball.velocity.y*dt):
                            if int(mainball.pos.z+1)>=len(gamelist)or int(mainball.pos.y+mainball.velocity.y*dt)>=len(gamelist[0]) or int(mainball.pos.x)>=len(gamelist[0][0]):
                                pass
                            elif gamelist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)]==0:
                                pass
                            elif gamelist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)]==1 or gamelist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)]==4 or gamelist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)]==5 or gamelist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)]==6 or gamelist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)]==7:
                                mainball.velocity.y=-mainball.velocity.y*0.9
                                DYter+=1
                            elif gamelist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)]==8:
                                if boxeslist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)].pos.z-0.4>=mainball.pos.z:
                                    mainball.velocity.y=-mainball.velocity.y*0.9
                                    DYter+=1

                    elif mainball.velocity.y>0 and DYter==0:
                        if int(mainball.pos.y)<int(mainball.pos.y+mainball.velocity.y*dt):
                            if int(mainball.pos.z+1)>=len(gamelist)or int(mainball.pos.y+mainball.velocity.y*dt)>=len(gamelist[0]) or int(mainball.pos.x)>=len(gamelist[0][0]):
                                pass
                            elif gamelist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)]==0:
                                pass
                            elif gamelist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)]==1 or gamelist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)]==4 or gamelist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)]==5 or gamelist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)]==6 or gamelist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)]==7:
                                mainball.velocity.y=-mainball.velocity.y*0.9
                                DYter+=1
                            elif gamelist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)]==8:
                                if boxeslist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)].pos.z-0.4>=mainball.pos.z:
                                    mainball.velocity.y=-mainball.velocity.y*0.9
                                    DYter+=1

                    if mainball.velocity.x<0 and DXter==0:           #공이 옆쪽 이동
                        if int(mainball.pos.x)>int(mainball.pos.x+mainball.velocity.x*dt):
                            if int(mainball.pos.z+1)>=len(gamelist)or int(mainball.pos.y+mainball.velocity.y*dt)>=len(gamelist[0]) or int(mainball.pos.x+mainball.velocity.x*dt)>=len(gamelist[0][0]):
                                pass
                            elif gamelist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)]==0:
                                pass
                            elif gamelist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)]==1 or gamelist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)]==4 or gamelist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)]==5 or gamelist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)]==6 or gamelist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)]==7:
                                mainball.velocity.x=-mainball.velocity.x*0.9
                                DXter+=1
                            elif gamelist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)]==8:
                                if boxeslist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)].pos.z-0.4>=mainball.pos.z:
                                    mainball.velocity.x=-mainball.velocity.x*0.9
                                    DXter+=1
                                
                            
                    elif mainball.velocity.x>0 and DXter==0:
                        if int(mainball.pos.x)<int(mainball.pos.x+mainball.velocity.x*dt):
                            if int(mainball.pos.z+1)>=len(gamelist)or int(mainball.pos.y+mainball.velocity.y*dt)>=len(gamelist[0]) or int(mainball.pos.x+mainball.velocity.x*dt)>=len(gamelist[0][0]):
                                pass
                            elif gamelist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)]==0:
                                pass
                            elif gamelist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)]==1 or gamelist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)]==4 or gamelist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)]==5 or gamelist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)]==6 or gamelist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)]==7:
                                mainball.velocity.x=-mainball.velocity.x*0.9
                                DXter+=1
                            elif gamelist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)]==8:
                                if boxeslist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)].pos.z-0.4>=mainball.pos.z:
                                    mainball.velocity.x=-mainball.velocity.x*0.9
                                    DXter+=1

                if DZter==0 and DYter==0:
                    if int(mainball.pos.z+1)!=int(mainball.pos.z+2+mainball.velocity.z*dt)-1 and int(mainball.pos.y)!=int(mainball.pos.y+mainball.velocity.y*dt):
                        if int(mainball.pos.z+2+mainball.velocity.z*dt)-1>=len(gamelist) or int(mainball.pos.y+mainball.velocity.y*dt)>=len(gamelist[0]) or int(mainball.pos.x)>=len(gamelist[0][0]):
                            pass
                        elif gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)]==0 or gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)]==3 or gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)]==8 or gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)]==10 or gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)]==11:
                            pass
                        elif gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)]==1 or gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)]==4 or gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)]==5 or gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)]==6 or gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x)]==7:
                            mainball.velocity=vector(mainball.velocity.x,-0.9*mainball.velocity.z,-0.9*mainball.velocity.y)
                            DZter+=1
                            DYter+=1
                if DZter==0 and DXter==0:
                    if int(mainball.pos.z+1)!=int(mainball.pos.z+2+mainball.velocity.z*dt)-1 and int(mainball.pos.x)!=int(mainball.pos.y+mainball.velocity.y*dt):
                        if int(mainball.pos.z+2+mainball.velocity.z*dt)-1>=len(gamelist) or int(mainball.pos.y)>=len(gamelist[0]) or int(mainball.pos.x+mainball.velocity.x*dt)>=len(gamelist[0][0]):
                            pass
                        elif gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)]==0 or gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)]==3 or gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)]==8 or gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)]==10 or gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)]==11:
                            pass
                        elif gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)]==1 or gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)]==4 or gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)]==5 or gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)]==6 or gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y)][int(mainball.pos.x+mainball.velocity.x*dt)]==7:
                            mainball.velocity=vector(mainball.velocity.z*(-0.9),mainball.velocity.y,mainball.velocity.x*(0.9))
                            DZter+=1
                            DXter+=1
                if DXter==0 and DYter==0:
                    if int(mainball.pos.y)!=int(mainball.pos.y+mainball.velocity.y*dt) and int(mainball.pos.x)!=int(mainball.pos.x+mainball.velocity.x*dt):
                        if int(mainball.pos.z+1)>=len(gamelist) or int(mainball.pos.y+mainball.velocity.y*dt)>=len(gamelist[0]) or int(mainball.pos.x+mainball.velocity.x*dt)>=len(gamelist[0][0]):
                            pass
                        elif gamelist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x+mainball.velocity.x*dt)]==0 or gamelist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x+mainball.velocity.x*dt)]==3 or gamelist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x+mainball.velocity.x*dt)]==8 or gamelist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x+mainball.velocity.x*dt)]==10 or gamelist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x+mainball.velocity.x*dt)]==11:
                            pass
                        elif gamelist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x+mainball.velocity.x*dt)]==1 or gamelist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x+mainball.velocity.x*dt)]==4 or gamelist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x+mainball.velocity.x*dt)]==5 or gamelist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x+mainball.velocity.x*dt)]==6 or gamelist[int(mainball.pos.z+1)][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x+mainball.velocity.x*dt)]==7:
                            mainball.velocity=vector(mainball.velocity.y*dt*(-0.9),-0.9*mainball.velocity.x,mainball.velocity.z)
                            DXter+=1
                            DYter+=1
                if DXter==0 and DYter==0 and DZter==0:
                    if int(mainball.pos.z+2+mainball.velocity.z*dt)-1!=int(mainball.pos.z+1) and int(mainball.pos.y)!=int(mainball.pos.y+mainball.velocity.y*dt) and int(mainball.pos.x)!=int(mainball.pos.x+mainball.velocity.x*dt):
                        if int(mainball.pos.z+2+mainball.velocity.z*dt)-1>=len(gamelist) or int(mainball.pos.y+mainball.velocity.y*dt)>=len(gamelist[0]) or int(mainball.pos.x+mainball.velocity.x*dt)>=len(gamelist[0][0]):
                            pass
                        elif gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x+mainball.velocity.x*dt)]==0 or gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x+mainball.velocity.x*dt)]==3 or gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x+mainball.velocity.x*dt)]==8 or gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x+mainball.velocity.x*dt)]==10 or gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x+mainball.velocity.x*dt)]==11:
                            pass
                        elif gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x+mainball.velocity.x*dt)]==1 or gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x+mainball.velocity.x*dt)]==4 or gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x+mainball.velocity.x*dt)]==5 or gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x+mainball.velocity.x*dt)]==6 or gamelist[int(mainball.pos.z+2+mainball.velocity.z*dt)-1][int(mainball.pos.y+mainball.velocity.y*dt)][int(mainball.pos.x+mainball.velocity.x*dt)]==7:
                            mainball.velocity=-0.9*mainball.velocity
            
                            
                            
            mainball.pos=mainball.pos+mainball.velocity*dt                  #위치변화


            for i in range(len(gamelist)):                                  #투명도 조절
                for j in range(len(gamelist[0])):
                    for k in range(len(gamelist[0][0])):
                        distance=abs(boxeslist[i][j][k].x-int(mainball.pos.x))+abs(boxeslist[i][j][k].y-int(mainball.pos.y))+abs(boxeslist[i][j][k].z-int(mainball.pos.z+1))
                        if boxeslist[i][j][k].num==1 or boxeslist[i][j][k].num==6 or boxeslist[i][j][k].num==7 or boxeslist[i][j][k].num==11 :                            
                            if distance>4:
                                boxeslist[i][j][k].opacity=0.05
                            else:
                                boxeslist[i][j][k].opacity=1-0.2*distance
                        elif boxeslist[i][j][k].num==4 or boxeslist[i][j][k].num==5 or boxeslist[i][j][k].num==8 or boxeslist[i][j][k].num==10 :
                            if distance>4:
                                for obj in boxeslist[i][j][k].objects:
                                    obj.opacity=0.05                     #뭘로해야 적당하지?? 투명도
                            else:
                                for obj in boxeslist[i][j][k].objects:
                                    obj.opacity=1-0.2*distance
                        
                            
                        

            if 0<=int(mainball.pos.x)<len(gamelist[0][0]) and 0<=int(mainball.pos.y)<len(gamelist[0]) and 0<=int(mainball.pos.z+1)<len(gamelist):   #현 위치에 대한 변화
                if gamelist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x)]==3:
                    if abs(mainball.pos-boxeslist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x)].pos)<=boxeslist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x)].radius+mainball.radius:
                        boxeslist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x)].visible=False
                        stars=stars-1
                        gamelist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x)]=0
                        if stars==0:
                            gameplay+=1
                            endgame(mainball,boxeslist,stars)
                elif gamelist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x)]==10:
                    gravity=-gravity
                    boxeslist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x)].visible=False
                    gamelist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x)]=0
                            
                elif gamelist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x)]==8:                            
                    if boxeslist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x)].pos.z-0.3>=mainball.pos.z:                                
                        endgame(mainball,boxeslist)                                
                        break

                elif gamelist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x)]==11:
                    if abs(mainball.pos-boxeslist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x)].pos)<=mainball.radius+boxeslist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x)].radius:
                        mainball.velocity=1.05*(2*(-mainball.velocity).dot(mainball.pos-boxeslist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x)].pos)*(mainball.pos-boxeslist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x)].pos))/(abs(mainball.pos-boxeslist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x)].pos)**2)+mainball.velocity
                        boxeslist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x)].visible=False
                        gamelist[int(mainball.pos.z+1)][int(mainball.pos.y)][int(mainball.pos.x)]=0
            movinglist=fellingmaking(makinglist,gamelist,t,movinglist)
            (movinglist,stop)=box_move(movinglist,gamelist)
            if stop==1:
                endgame(mainball,boxeslist)
                break
            
                            
                        

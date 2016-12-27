import time;
from graphics import *


win = GraphWin("Lines 'n' Boxes", 600, 600)
win.setBackground('white')
num=0
for y in xrange(100,600,100):
    for x in xrange(100,600,100):
        c = Circle(Point(x,y), 15)
        c.setFill('#d8bfd8')
            
        c.draw(win)
        label = Text(Point(x,y), num)
        label.setTextColor('#d82e84')
        label.draw(win)
        num+=1
win.getMouse() # pause for click in window




co_ord=[]
temp=[]
for y in xrange(100,600,100):
    for x in xrange(100,600,100):
        temp=[x,y]
        co_ord.append(temp)

    
board = [[0 for x in xrange(25)] for x in xrange(25)] 

def display():
    for i in xrange(0,25):
        for j in xrange(0,25):
            print (board[i][j],' ')
        print ("\n")

        
def isBox(x,y,ch):
    score=0
    #for upper and lower boxes
    if(abs(x-y)==1):
        x1,x2,y1,y2=x+5,x-5,y+5,y-5
        l1=board[x][y]
        #checking lower box
        if(x1<=24) and (y1<=24):
            l2=board[x][x1]
            l3=board[y][y1]
            l4=board[x1][y1]
            if(l1+l2+l3+l4)==4:
                score+=1
                pass #remember to make box
                midx=(co_ord[x][0]+co_ord[y1][0])/2
                midy=(co_ord[x][1]+co_ord[y1][1])/2
                name_tag = Text(Point(midx,midy), ch)
                name_tag.setTextColor('#009933')
                name_tag.draw(win)
                
        #checking upper box
        if(x2>=0) and (y2>=0):
            l5=board[x][x2]
            l6=board[y][y2]
            l7=board[x2][y2]
            if(l1+l5+l6+l7)==4:
                score+=1
                pass #remember to make box
                midx=(co_ord[x][0]+co_ord[y2][0])/2
                midy=(co_ord[x][1]+co_ord[y2][1])/2
                name_tag = Text(Point(midx,midy), ch)
                name_tag.setTextColor('#009933')
                name_tag.draw(win)
        return score
    else:
         x1,x2,y1,y2=x+1,x-1,y+1,y-1
         l1=board[x][y]
        #checking right box
         if(x+y!=13) and (x+y!=23) and (x+y!=33) and (x+y!=43):
             l2=board[x][x1]
             l3=board[y][y1]
             l4=board[x1][y1]
             if(l1+l2+l3+l4)==4:
                 score+=1
                 pass #remember to make box
                 midx=(co_ord[x][0]+co_ord[y1][0])/2
                 midy=(co_ord[x][1]+co_ord[y1][1])/2
                 name_tag = Text(Point(midx,midy), ch)
                 name_tag.setTextColor('#009933')
                 name_tag.draw(win)
        #checking left box
         if(x+y!=5) and (x+y!=15) and (x+y!=25) and (x+y!=35):
             l5=board[x][x2]
             l6=board[y][y2]
             l7=board[x2][y2]
             if(l1+l5+l6+l7)==4:
                 score+=1
                 pass #remember to make box
                 midx=(co_ord[x][0]+co_ord[y2][0])/2
                 midy=(co_ord[x][1]+co_ord[y2][1])/2
                 name_tag = Text(Point(midx,midy), ch)
                 name_tag.setTextColor('#009933')
                 name_tag.draw(win)
         return score
        

def check_valid(x,y):
    flag=0
    if x>=0 and x<=24 and y>=0 and y<=24:       #checking range
        if abs(x-y)==1 or abs(x-y)==5:          #checking proximity
            flag=1

    if (x+y)==9 or (x+y)==19 or (x+y)==29 or (x+y)==39: #checking pseudo-proximity
                if abs(x-y)!=1:
                    flag=1
                else:
                    flag=0

    return flag


def game(ch):
    flag=1
    score=0
    status=''
    while flag==1:
        x=input('Input x ')
        y=input('Input y ')
        if(check_valid(x,y)==1):
            flag=0
        else:
            print ('Invalid inputs! Please input again')
    
    if(board[x][y]==0):
        board[x][y]+=1
        board[y][x]+=1
        print (x)
        print (y)
        #remember to draw a line
        if (x-y)==-1:
            px1=co_ord[x][0]+15
            px2=co_ord[y][0]-15
            line = Line(Point(px1,co_ord[x][1]), Point(px2,co_ord[y][1]))
            line.setFill('#a2cd5a')
            line.draw(win)
        if (x-y)==1:
            px1=co_ord[x][0]-15

            px2=co_ord[y][0]+15
            line = Line(Point(px1,co_ord[x][1]), Point(px2,co_ord[y][1]))
            line.setFill('#a2cd5a')
            line.draw(win)
        if (x-y)==-5:
            px1=co_ord[x][1]+15
            px2=co_ord[y][1]-15
            line = Line(Point(co_ord[x][0],px1), Point(co_ord[y][0],px2))
            line.setFill('#a2cd5a')
            line.draw(win)
        if (x-y)==5:
            px1=co_ord[x][1]-15
            px2=co_ord[y][1]+15
            line = Line(Point(co_ord[x][0],px1), Point(co_ord[y][0],px2))
            line.setFill('#a2cd5a')
            line.draw(win)

        
        #remember to draw a line
        score=isBox(x,y,ch)
        if(score!=0):
            status='b'
        else:
            status='nb'
            
    else:
        print ('Invalid move')
    return score,status


def main():


    fo=open('HighScores.txt','r')
    print (fo.read())
    count=0
    result=[]
    score1,score2=0,0
    ch1=raw_input('Choose a character for player 1: ')
    ch1=ch1.upper()
    ch2=raw_input('Choose a character for player 1: ')
    ch2=ch2.upper()
    info1,info2='Player1: %d','Player2: %d'
    while (score1+score2)<16:
        status1,status2='b','b'
        #Player 1
        while (status1=='b') and (score1+score2)<16:
            print ('PLAYER 1')
            result=game(ch1)
            score1+=result[0]
            status1=result[1]
            print ('player1 score %d' %score1)
            data = Text(Point(450,20), info1%score1)
            data.draw(win)
        #Player 2
        while (status2=='b') and (score1+score2)<16:
            print ('PLAYER 2')
            result=game(ch2)
            score2+=result[0]
            status2=result[1]
            print ('player2 score %d' %score2)
            data = Text(Point(450,40), info2%score2)
            data.draw(win)
    print (score1,score2)
    fo=open('HighScores.txt','w')
    localtime = time.asctime( time.localtime(time.time()) )
    fo.write('Highscore as on %s =>\nPlayer1 %d\nPlayer2 %d'%(localtime,score1,score2))
    fo.close()
    if score1>score2:
        print ('player1 wins')
        win_tag = Text(Point(300,250), 'Player 1 WINS!!!')
        win_tag.setSize(36)
        win_tag.setStyle('bold italic')
        win_tag.setTextColor('red')
        win_tag.draw(win)
    elif score1<score2:
        print ('player2 wins')
        win_tag = Text(Point(300,250), 'Player 2 WINS!!!')
        win_tag.setSize(36)
        win_tag.setStyle('bold italic')
        win_tag.setTextColor('red')
        win_tag.draw(win)
    else:
        print ('tie')
        win_tag = Text(Point(300,250), 'TIE :(')
        win_tag.setSize(36)
        win_tag.setStyle('bold italic')
        win_tag.setTextColor('red')
        win_tag.draw(win)

main()

time.sleep(5)
win.close()

##################
#All the images in this project are hand-drawn by me, 
#using freeform on my Ipad. There are no outside sources that I need to cite.
##################



from cmu_graphics import *
import math
from classes import *


# newgame sets the variables
def newGame(app):

    app.width = 1400
    app.height = 1000
    app.gameEnd = False
    app.holeList = [holeOne, holeTwo, holeThree, holeFour]
    app.currHole = 0

    #swing animations, not done drawing yet
    app.swings = [#driverswing:
              ['driverSwing/driverOne.jpg',
               'driverSwing/driverTwo.jpg', 
               'driverSwing/driverThree.jpg',
               'driverSwing/driverFour.jpg', 
               'driverSwing/driverFive.jpg', 
               'driverSwing/driverSix.jpg',
               'driverSwing/driverSeven.jpg'],

               

               #ironswing:
               ['ironSwing/ironOne.jpg',
                'ironSwing/ironTwo.jpg', 
                  'ironSwing/ironThree.jpg', 
                    'ironSwing/ironFour.jpg', 
                      'ironSwing/ironFive.jpg', 
                        'ironSwing/ironSix.jpg', 
                          'ironSwing/ironSeven.jpg'],


               #wedgeswing:
               ['wedgeSwing/wOne.jpg',
               'wedgeSwing/wTwo.jpg', 
               'wedgeSwing/wThree.jpg',
               'wedgeSwing/wFour.jpg', 
               'wedgeSwing/wFive.jpg', 
               'wedgeSwing/wSix.jpg',
               'wedgeSwing/wSeven.jpg' ],
               
               #putterswing:
               ['putting/puttOne.jpg', 
                'putting/puttTwo.jpg',
                'putting/puttThree.jpg',
                'putting/puttFour.jpg']
               ]


    app.terrainPics = ['terrainPics/teeBoxPic.jpg', 
               'terrainPics/fairwayPic.jpg',
               'terrainPics/greenPic.jpg',
               'terrainPics/roughPic.jpg',
               'terrainPics/bunkerPic.jpg']


    app.setMaxShapeCount(15000)
    #some of the swing controls
    app.finishHole = False
    app.startx = app.width//3.3
    app.starty = app.height//1.35
    app.startw = 200
    app.starth = 200

    app.drivingx = app.startx+300 
    app.drivingy = app.height//1.35
    app.drivingRangeList=[]


    app.swingImg =0 #this is to index animation
    app.swingOver = False #tells if swing is over in player view
    app.swingNow = False 
    app.playerSwingNow = False
    app.stepsPerSecond = 10
    app.i=0
    app.delayDuration =  1.5* app.stepsPerSecond
    

    app.is_rising = True  # Flag to track if the ball is rising
    app.gravity = 0.2  # Gravitational force
    app.velocity_y  = -18

    
    
    
    app.view = 'start'
    app.stepsPerSecond = 3
    app.currRegion = 'teeBox'
    app.viewSwitchx = app.width//1.10
    app.viewSwitchy = app.height//15
    app.switchLabel ='Player View'
    
    app.gravity = 0.2  # Gravitational force
    app.original_size = 3  # Store the original size
    app.is_rising = True  # Flag to track if the ball is rising
    app.showLabel = False
    app.inTraining = False

    #clubdisplay settings
    app.clubNum = 0
    app.clubNum = app.clubNum%13
    app.circlex = app.width//20
    app.circley = app.height/1.21
    app.tcirclex = app.width*0.88
    app.tcircley = app.height/1.21
    app.circler = 50

    #distance to pin
    app.distanceToPin = 319
    app.prevDistanceToPin = 319

    #powerstrip positioning
    app.stripLeft = app.width // 4.5 
    app.stripTop = app.height // 1.275
    app.stripFill = None  # Color of the strip
    app.stripWidth = 663
    app.stripHeight = app.height//10

    #powerbox settings
    app.powerBarMoving = False
    app.powerBx = 5+ app.width // 4.5 
    app.powerBy = 5+ app.height // 1.275
    app.powerWidth = 1
    app.powerHeight = app.height//10 -10
    app.powerColor = gradient('darkOliveGreen', 'darkOliveGreen',
                              'darkGreen', 'darkGreen', 'green',
                               'green', 'lime','lime', 'yellow', 'red',start='left')
    app.powerSpeed = 54
    app.powerTotalWidth = 649
    app.swingPower = -1
    app.swingDir = 0
    app.powerSelected = False

    #after pressed powerbox settings
    app.apowerx = 700+ app.width // 4.5 
    app.apowery = app.height // 1.275
    app.apowerWidth = app.height//10
    app.apowerHeight = app.height//10

    ## Stuff for Green only ##
    
    #powerstrip positioning for Green Only
    app.puttImg =0
    app.puttNow =False
    app.puttOver = False
    app.puttpower= -1
    app.holex = 788
    app.holey = 75 + (40-app.distanceToPin)*15
    app.puttAgain = False
    app.nextPuttSignx = app.width//2
    app.nextPuttSigny = app.height//2-50
    app.nextPuttSignLabel ='Press here to putt again'

    app.ballGreenx = 788
    app.ballGreeny = app.height//1.46
    app.ballGreenr = 7
    app.ballGreenShouldGo = 0



    #powerbox settings for Green Only
    app.gstripLeft =  app.width // 4.5 
    app.gstripTop = 75
    app.gstripFill = None  # Color of the strip
    app.gstripHeight = 600
    app.gstripWidth = app.height//10

    
    app.gpowerBarMoving = False
    app.gpowerBx = 5+ app.width // 4.5 
    app.gpowerBy = 75
    app.gpowerHeight = 1
    app.gpowerWidth = app.height//10 -10
    app.gpowerColor = gradient('darkOliveGreen', 'darkOliveGreen',
                              'darkGreen', 'darkGreen', 'green',
                               'green', 'lime','lime', 'yellow', 'red',start='bottom')
    app.gpowerSpeed = 54
    app.gpowerTotalHeight= 600

    #after pressed powerbox settings for Green Only
    app.gapowerx = 5+ app.width // 4.5 
    app.gapowery = 789
    app.gapowerWidth = app.height//10
    app.gapowerHeight = app.height//10
    app.gpowerSelected = False
    app.gswingDist = 0



    #direction bar settings
    app.dirbarMoving = True 
    app.dirbarX = 133
    app.dirbarY = 740
    app.dirbarRadius = 250
    app.dirArrowAngle = 90

    app.time=0
    app.dirArrowLen = 150 
    app.dirArrowex =app.dirbarX - app.dirArrowLen * math.cos(math.radians(app.dirArrowAngle))
    app.dirArrowey =app.dirbarY - app.dirArrowLen * math.sin(math.radians(app.dirArrowAngle))
    app.dirSelected = False

    app.backx = 100
    app.backy = 55
    app.instrx = app.startx + 600
    app.instry = app.starty

    playerOne.score = 0
    for hole in app.holeList:
        hole.playerScore =0





#onappstart calls newgame

def onAppStart(app):
    newGame(app)
    
#redraw all
def redrawAll(app):
    i1x, i1y = getImageSize(app.holeList[app.currHole].img)
    i2x, i2y = getImageSize('swing1.jpg')
    startx, starty = getImageSize('startScreen.jpg')
    if app.view =='start':
         drawImage('startScreen.jpg', app.width/2, app.height/2, 
              align='center', width=startx, height=starty)
         drawRect(app.startx, app.starty, app.startw,app.starth, fill='white', border = 'black', borderWidth = 5 ,align='center')
         drawLabel("Single Player", app.startx, app.starty, size=25)

         drawRect(app.startx+300, app.starty, app.startw,app.starth, fill='white', border = 'black', borderWidth = 5 ,align='center')
         drawLabel("Driving Range", app.startx+300, app.starty, size=25)

         drawRect(app.startx+600, app.starty, app.startw,app.starth, fill='white', border = 'black', borderWidth = 5 ,align='center')
         drawLabel("Instructions", app.instrx, app.starty, size=25)

    if app.view =='instructions':
        w,h = getImageSize('instr.jpg')

        drawImage('instr.jpg', app.width/2, app.height/2, align='center', width=w//1.2, height=h//1.2)
        drawRect(app.backx, app.backy, 100 ,50, fill='white', border = 'black', borderWidth = 2 ,align='center')

    if app.view == 'drivingRange':
        drawImage('drivingRange.jpg', app.width/2, app.height/2, 
              align='center', width=i1x//1.2, height=i1y//1.2)
        for item in app.drivingRangeList:
            x, y = item
            drawCircle(x, y, 3, fill='white', border = 'black')

        drawCircle(ballTwo.x, ballTwo.y, ballTwo.size, fill='white', border = 'black')
        drawCircle(playerTwo.x, playerTwo.y, 7, fill='grey', border = 'black')


        drawSwitchMode(app)


    
    if app.view=='end':
        drawImage('endscr.jpg', app.width/2, app.height/2, align='center')
        totalScore = playerOne.score +holeFour.playerScore

        drawLabel(f'Game over, your total score is {totalScore}', app.width/2, app.height/2, size=30)
        drawLabel(f'Hole1: {holeOne.playerScore-1} (Par {holeOne.par})', app.width/2, app.height/2 +30, size=30)
        drawLabel(f'Hole2: {holeTwo.playerScore-1} (Par {holeTwo.par})', app.width/2, app.height/2 +60, size=30)
        drawLabel(f'Hole3: {holeThree.playerScore-1} (Par {holeThree.par})', app.width/2, app.height/2 +90, size=30)
        drawLabel(f'Hole4: {holeFour.playerScore} (Par {holeFour.par})', app.width/2, app.height/2 +120, size=30)
        differenceToPar = totalScore - 16
        if differenceToPar>0:
            drawLabel(f'Oops, you were {differenceToPar} over PAR', app.startx, app.starty+100, size=30)
        elif differenceToPar<0:
            drawLabel(f'Great! You were {-differenceToPar} under PAR', app.startx, app.starty+100, size=30)
        else:
            drawLabel(f'Even PAR, not bad!', app.startx, app.starty+100, size=30)

        
        

    elif app.finishHole and app.gameEnd == False:
         if app.currHole<=2:
             drawImage('endscr.jpg', app.width/2, app.height/2, align='center')
             drawRect(app.nextPuttSignx, app.nextPuttSigny, 300,150, fill='white', border = 'black', align='center')
             drawLabel("Press here to start next hole", app.nextPuttSignx, app.nextPuttSigny+20, size=20)
             scoreToPar = app.holeList[app.currHole].playerScore - app.holeList[app.currHole].par
             label = ''
             if scoreToPar==-1:
                 label = 'a birdie'
             elif scoreToPar==0:
                 label = 'par'
             elif scoreToPar ==-2:
                 label= 'an eagle'
             elif scoreToPar ==1:
                 label='a bogey'
             elif scoreToPar ==2:
                 label = 'a double bogey'
             else:
                 label = '+' + str(scoreToPar)
                 
             drawLabel(f'Your scored: {app.holeList[app.currHole].playerScore}, which is {label}', app.nextPuttSignx, app.nextPuttSigny-20, size=20)
             
             
 
    
    elif app.view =='top':

        if app.swingNow==True:
            drawCircle(ballOne.x, ballOne.y, ballOne.size, fill='green')

        drawImage(app.holeList[app.currHole].img, app.width/2, app.height/2, 
              align='center', width=i1x//1.18, height=i1y//1.18)
        drawCircle(ballOne.x, ballOne.y, ballOne.size, fill='white', border = 'black')
        drawCircle(playerOne.x, playerOne.y, 7, fill='grey', border = 'black')
        drawRect(app.viewSwitchx, app.viewSwitchy+180, 250, 100, fill='white', border = 'black', align = 'center') 
        drawLabel(f'Your Total Score: {playerOne.score}', app.viewSwitchx, app.viewSwitchy+150)
        drawLabel(f'Player Score for this hole: {app.holeList[app.currHole].playerScore}', app.viewSwitchx, app.viewSwitchy+170)
        drawLabel(ballOne.terrainD, app.viewSwitchx, app.viewSwitchy+190)
        if ballOne.terrainD == 'Your ball got lost in a building' or ballOne.terrainD =='Boo! Your ball is lost in the drain!' or ballOne.terrainD =='You suck! Your ball is out of bounds':
             drawLabel('One stroke penalty, try that again', app.viewSwitchx, app.viewSwitchy+210)


        drawRect(app.viewSwitchx, app.viewSwitchy+75, 250, 50, fill='white', border = 'black', align = 'center') 
        drawLabel(f'{app.distanceToPin} YDS to the hole', app.viewSwitchx, app.viewSwitchy+75)

        #Draw aim direction arrows
        drawLabel('Click on the buttons to adjust aim', 1250, 750, size=20)
        drawRegularPolygon(1200, 800, 35, 3, rotateAngle=-90, fill='blue')
        drawRegularPolygon(1300, 800, 35, 3, rotateAngle=90, fill='blue')

        
        
        #drawGrid(app)

        #draw the correct map for the correct hole
        if app.currHole ==0:
            drawHoleOne()
            drawCircle(app.holeList[app.currHole].holeLocX, app.holeList[app.currHole].holeLocY, 5, fill='black')

        elif app.currHole ==1:
            drawHoleTwo()
            drawCircle(app.holeList[app.currHole].holeLocX, app.holeList[app.currHole].holeLocY, 5, fill='black')

        elif app.currHole ==2:
            drawHoleThree()
            drawCircle(app.holeList[app.currHole].holeLocX, app.holeList[app.currHole].holeLocY, 5, fill='black')

        elif app.currHole ==3:
            drawHoleFour()
            drawCircle(app.holeList[app.currHole].holeLocX, app.holeList[app.currHole].holeLocY, 5, fill='black')


        
       
        drawSwitchMode(app)
        drawLabel('Press g to skip this hole',app.viewSwitchx, app.viewSwitchy+280)
        drawLabel('Your score will be counted as two times par of this hole',app.viewSwitchx, app.viewSwitchy+290)




    elif app.view =='player':
        if app.inTraining==True:
            i=0
            i=i%3
            drawRect(0,0,app.width, app.height, fill=rgb(88, 121, 51))
            drawCircle(app.width/2, app.height/2-app.height/15, app.width//4.5, fill=rgb(214, 214, 213))
            drawCircle(app.width/2, app.height/2-app.height/15, app.width//5, fill=rgb(143, 210, 128))
            if app.clubNum%13 !=0 and app.clubNum%13 <=2:
                i = 0
            elif app.clubNum%13 >2 and app.clubNum%13 <=8:
                i =1
            elif app.clubNum%13 >8 and app.clubNum%13 <=12:
                i=2

            if app.swingImg<=6 and app.swingNow==False:
                drawImage(app.swings[i][app.swingImg], app.width/2, app.height/2-app.height/15, align='center',
                      width=i2x//2.6, height=i2y//2.6)
            else:
                drawImage(app.swings[i][6], app.width/2, app.height/2-app.height/15, align='center',
                      width=i2x//2.6, height=i2y//2.6)

            drawPlayerView(app)



        if app.inTraining ==False and ballOne.terrain == 'Green':
            
            drawGreenView(app)
            #draw the hole
            drawCircle(app.holex, app.holey, 15, fill='black')
            if app.puttAgain ==True:
                 drawRect(app.nextPuttSignx, app.nextPuttSigny, 200,100, fill='white', border = 'black', align='center')
                 drawLabel(app.nextPuttSignLabel, app.nextPuttSignx, app.nextPuttSigny, size=10)


        elif app.inTraining==False:
            i=0
            i=i%3
            drawRect(0,0,app.width, app.height, fill=rgb(88, 121, 51))
            drawCircle(app.width/2, app.height/2-app.height/15, app.width//4.5, fill=rgb(214, 214, 213))
            drawCircle(app.width/2, app.height/2-app.height/15, app.width//5, fill=rgb(143, 210, 128))
            if app.clubNum%13 !=0 and app.clubNum%13 <=2:
                i = 0
            elif app.clubNum%13 >2 and app.clubNum%13 <=8:
                i =1
            elif app.clubNum%13 >8 and app.clubNum%13 <=12:
                i=2

            if app.swingImg<=6 and app.swingNow==False:
                drawImage(app.swings[i][app.swingImg], app.width/2, app.height/2-app.height/15, align='center',
                      width=i2x//2.6, height=i2y//2.6)
            else:
                drawImage(app.swings[i][6], app.width/2, app.height/2-app.height/15, align='center',
                      width=i2x//2.6, height=i2y//2.6)

            drawPlayerView(app)
            i3x, i3y = getImageSize(app.holeList[app.currHole].mapimg)
            #show the fullmap of the hole
            drawImage(app.holeList[app.currHole].mapimg, app.width//1.12, app.height//1.75, align='center', width=i3x//3.5, height=i3y//3.5)
            drawRect(app.viewSwitchx, app.viewSwitchy+75, 250, 50, fill='white', border = 'black', align = 'center') 
            drawLabel(f'{app.distanceToPin} YDS to the hole', app.viewSwitchx, app.viewSwitchy+75)


    
            
         
        drawSwitchMode(app)

    if app.view!='start':
        drawRect(app.backx, app.backy, 100 ,50, fill='white', border = 'black', borderWidth = 2 ,align='center')
        drawLabel("Back to Home Screen", app.backx, app.backy, size=9)

#draws the player view when the ball is on the green             
def drawGreenView(app):
    ix, iy = getImageSize('putting/puttOne.jpg')
    
    drawRect(0,0,app.width, app.height, fill=rgb(186,220,147))  
    drawImage(app.swings[3][0], app.width//2, app.height//1.5, align='center', width=ix//4, height=iy//4)  
    

    if app.puttImg<=3 and app.puttNow == False:
        drawImage(app.swings[3][app.puttImg], app.width//2, app.height//1.5, align='center',
                     width=ix//4, height=iy//4)
    else:
        drawImage(app.swings[3][3], app.width//2, app.height//1.5, align='center',
                      width=ix//4, height=iy//4)
        
    ## This what the ball looks like on the green
    drawCircle(app.ballGreenx, app.ballGreeny, app.ballGreenr, fill='white', border = 'black')

    i3x, i3y = getImageSize(app.holeList[app.currHole].mapimg)

    #drawBottomBoxes
    drawRect(0, app.height//1.20, app.width, app.height//5, fill='white', opacity = 80)
    drawRect(0, app.height-app.width//5-app.height//6, app.width//5, app.width//5, fill='white',  border='black', opacity = 80)
    #drawLines
    drawLine(app.width//5, app.width, app.width//5, app.height//1.2)
    drawLine((app.width//5)*4, app.width, (app.width//5)*4, app.height//1.2)
    drawLine(app.width//5,app.height//1.20, app.width, app.height//1.20)

    #display club usage box
    drawCircle(app.circlex, app.circley, app.circler, fill='white', border='black')
    drawImage(clubList[12].image ,app.circlex, app.circley, width=67, height=67, align='center')
    drawLabel('Please Use Putter on Green', app.width//20+120, app.height/1.15, size=10, align='center')
    drawLabel(clubList[12].name, app.width//20+120, app.height/1.10, size=30, align='center')
    drawLabel(f'{clubList[12].fullDist} YDS', app.width//20+120, app.height/1.05, size=15)

    #draw current terrain 
    drawCircle(app.tcirclex, app.circley, app.circler, fill='white', border='black')

    if ballOne.terrain =='teeBox':
        imageNum = 0
        shownMessage = 'Get ready to tee off!'
        t = 'Tee Box'
    elif ballOne.terrain == 'Green':
        imageNum =2
        shownMessage = 'Get it in the hole!'
        t='Green'
    elif ballOne.terrain == 'Rough':
        imageNum = 3
        shownMessage = "+20'%' friction (your shot will be shorter)"
        t='Rough'
    elif ballOne.terrain =='Bunker':
        imageNum = 4
        shownMessage = "+40'%' friction (your shot will be shorter)"
        t='Bunker'
    else:
        imageNum=1
        shownMessage = 'Trust your yardages!'
        t='Fairway'

    drawImage(app.terrainPics[imageNum], app.tcirclex, app.circley, width=67, height=67, align='center')

    drawLabel('Your current terrain is', app.tcirclex +120, app.height/1.15, size=10, align='center')
    drawLabel(t, app.tcirclex +120, app.height/1.10, size=30, align='center')
    drawLabel(shownMessage, app.tcirclex +120, app.height/1.05, size=12)

    #display power box
    drawRect(app.gstripLeft, app.gstripTop, app.gstripWidth, app.gstripHeight, fill=app.gpowerColor, border='black', borderWidth=3)
    drawRect(app.gpowerBx, app.gpowerBy, app.gpowerWidth, app.gpowerHeight, fill='white',opacity = 50, border = 'black', borderWidth = 3)

    #display afterpower box
    drawRect(app.gapowerx, app.gapowery, app.gapowerWidth, app.gapowerHeight, fill='white', border='black', borderWidth=3)
    drawLabel('Press SpaceBar', app.gapowerx+ app.gapowerWidth//2, app.gapowery+15)
    drawLabel('to stop', app.gapowerx+ app.gapowerWidth//2, app.gapowery+25)
    if app.dirSelected and app.gpowerSelected:
        drawLabel(f'{app.puttpower} YDS', app.gapowerx+ app.gapowerWidth//2, app.gapowery+ app.gapowerWidth//2+15, size=15)


    #show the fullmap of the hole
    drawImage(app.holeList[app.currHole].mapimg, app.width//1.12, app.height//1.75, align='center', width=i3x//3.5, height=i3y//3.5)
    

    #display direction bar
    drawArc(app.dirbarX, app.dirbarY, app.dirbarRadius, app.dirbarRadius+100, 50, 80, 
            fill='white', border='black')
    drawLine(app.dirbarX, app.dirbarY, app.dirArrowex, app.dirArrowey)

    #afterdirection box
    drawRect(app.dirbarX, 510, 150, 60, fill='white', border='black', borderWidth=3, align = 'center')
    drawLabel('Press Enter to stop', app.dirbarX, 500)
    
    if app.dirSelected:
        showNum = "{:.2f}".format(abs(app.swingDir))
        if app.swingDir <0:
            drawLabel(f'{showNum} degrees left', app.dirbarX, app.dirbarY-225 ,size=15)
        else:
            drawLabel(f'{showNum} degrees right', app.dirbarX, app.dirbarY-225 ,size=15)  
    
    #draw box on the top right
    drawRect(app.viewSwitchx, app.viewSwitchy+180, 250, 100, fill='white', border = 'black', align = 'center') 
    drawLabel(f'Player Score to Par: {playerOne.score}', app.viewSwitchx, app.viewSwitchy+150)
    drawLabel(f'Player Score for this hole: {app.holeList[app.currHole].playerScore}', app.viewSwitchx, app.viewSwitchy+170)
    drawLabel(ballOne.terrainD, app.viewSwitchx, app.viewSwitchy+190)


    drawRect(app.viewSwitchx, app.viewSwitchy+75, 250, 50, fill='white', border = 'black', align = 'center') 
    drawLabel(f'{app.distanceToPin} YDS to the hole', app.viewSwitchx, app.viewSwitchy+75)

    if app.view!='start':
        drawRect(app.backx, app.backy, 100 ,50, fill='white', border = 'black', borderWidth = 2 ,align='center')
        drawLabel("Back to Home Screen", app.backx, app.backy, size=9)

#draws the player view before the ball is on the green
def drawPlayerView(app):

    #drawBottomBoxes
    drawRect(0, app.height//1.20, app.width, app.height//5, fill='white', opacity = 80)
    drawRect(0, app.height-app.width//5-app.height//6, app.width//5, app.width//5, fill='white',  border='black', opacity = 80)
    #drawLines
    drawLine(app.width//5, app.width, app.width//5, app.height//1.2)
    drawLine((app.width//5)*4, app.width, (app.width//5)*4, app.height//1.2)
    drawLine(app.width//5,app.height//1.20, app.width, app.height//1.20)

    #display club usage box
    drawCircle(app.circlex, app.circley, app.circler, fill='white', border='black')
    drawImage(clubList[app.clubNum%13].image ,app.circlex, app.circley, width=67, height=67, align='center')
    drawLabel('Click on club to change club', app.width//20+120, app.height/1.15, size=10, align='center')
    drawLabel(clubList[app.clubNum%13].name, app.width//20+120, app.height/1.10, size=30, align='center')
    drawLabel(f'{clubList[app.clubNum%13].fullDist} YDS', app.width//20+120, app.height/1.05, size=15)

    #draw current terrain 
    drawCircle(app.tcirclex, app.circley, app.circler, fill='white', border='black')

    if ballOne.terrain =='teeBox':
        imageNum = 0
        shownMessage = 'Get ready to tee off!'
        t = 'Tee Box'
    elif ballOne.terrain == 'Green':
        imageNum =2
        shownMessage = 'Get it in the hole!'
        t='Green'
    elif ballOne.terrain == 'Rough':
        imageNum = 3
        shownMessage = "distance -20%"
        t='Rough'
    elif ballOne.terrain =='Bunker':
        imageNum = 4
        shownMessage = "distance -40%"
        t='Bunker'
    else:
        imageNum=1
        shownMessage = 'Trust your yardages!'
        t='Fairway'

    drawImage(app.terrainPics[imageNum], app.tcirclex, app.circley, width=67, height=67, align='center')

    drawLabel('Your current terrain is', app.tcirclex +120, app.height/1.15, size=10, align='center')
    drawLabel(t, app.tcirclex +120, app.height/1.10, size=30, align='center')
    drawLabel(shownMessage, app.tcirclex +120, app.height/1.05, size=12)

    #display power box
    drawRect(app.stripLeft, app.stripTop, app.stripWidth, app.stripHeight, fill=app.powerColor, border='black', borderWidth=3)
    drawRect(app.powerBx, app.powerBy, app.powerWidth, app.powerHeight, fill='white',opacity = 50, border = 'black', borderWidth = 3)

    #display afterpower box
    drawRect(app.apowerx, app.apowery, app.apowerWidth, app.apowerHeight, fill='white', border='black', borderWidth=3)
    drawLabel('Press SpaceBar', app.apowerx+ app.apowerWidth//2, app.apowery+15)
    drawLabel('to stop', app.apowerx+ app.apowerWidth//2, app.apowery+25)
    if app.swingPower != -1:
        drawLabel(f'{app.swingPower-1} %', app.apowerx+ app.apowerWidth//2, app.apowery+ app.apowerWidth//2+15, size=25)

    

    #display direction bar
    drawArc(app.dirbarX, app.dirbarY, app.dirbarRadius, app.dirbarRadius+100, 50, 80, 
            fill='white', border='black')
    drawLine(app.dirbarX, app.dirbarY, app.dirArrowex, app.dirArrowey)

    #afterdirection box
    drawRect(app.dirbarX, 510, 150, 60, fill='white', border='black', borderWidth=3, align = 'center')
    drawLabel('Press Enter to stop', app.dirbarX, 500)
    
    if app.dirSelected:
        showNum = "{:.2f}".format(abs(app.swingDir))
        if app.swingDir <0:
            drawLabel(f'{showNum} degrees left', app.dirbarX, app.dirbarY-225 ,size=15)
        else:
            drawLabel(f'{showNum} degrees right', app.dirbarX, app.dirbarY-225 ,size=15)

#draws the button that can be used to switch between player and top view mode
def drawSwitchMode(app):

    drawRect(app.viewSwitchx, app.viewSwitchy, 100, 50, fill='white', border = 'black', align = 'center') 
    drawLabel(app.switchLabel, app.viewSwitchx, app.viewSwitchy, fill = 'black', align='center')


               
#Includes things that need to move repeatedly
#1. the distance bar and direction bars that the players need to control
#2. the ballAnim (physics engine) function is called here
#3. the rolling of the ball on the putting green
#4. animating the swing plus time delay

def onStep(app):
    app.stepsPerSecond = 50
    
        

    if app.currHole ==3 and app.finishHole==True:
        app.view='end'
        app.gameEnd = True
        app.finishHole= False
        
    
        

    #animate the powerbar
    if app.view == 'player' and app.powerBarMoving:
        if app.powerWidth >= app.powerTotalWidth:
            app.powerSpeed = -app.powerSpeed
        elif app.powerWidth <= 3:
            app.powerSpeed = abs(app.powerSpeed)

        app.powerWidth+=app.powerSpeed

    #animate the green's powerbar
    if app.view == 'player' and ballOne.terrain =='Green' and app.gpowerBarMoving:
        if app.gpowerHeight <= 1:
            app.powerSpeed = abs(app.powerSpeed)
        elif app.gpowerHeight >= 540:
            app.powerSpeed = - app.powerSpeed

        app.gpowerHeight += app.powerSpeed
        


    #animate the direction bar
    if app.view == 'player' and app.dirbarMoving:
        app.dirArrowAngle = 90+ 30 * math.sin(app.i)
        app.dirArrowex = app.dirbarX - app.dirArrowLen * math.cos(math.radians(app.dirArrowAngle))
        app.dirArrowey = app.dirbarY - app.dirArrowLen * math.sin(math.radians(app.dirArrowAngle))


#animate the swing but with appropriate delay
    #regular swing
    if app.playerSwingNow:
        if not app.inTraining:
            if app.swingImg<=7:
                app.swingImg+=1
                app.swingOver = True

            if app.swingOver== True and app.i>app.delayDuration:
                app.swingImg=0
                app.view ='top'
                dirx, diry = playerOne.getShiftAim()
                if playerOne.aim<0:
                    dirx *=-1
                ballAnim(app, dirx, diry ,(app.swingDir/5))
        else:
            if app.swingImg<=7:
                app.swingImg+=1
                app.swingOver = True

            if app.swingOver== True and app.i>app.delayDuration:
                app.swingImg=0
                app.view ='drivingRange'
                dirx, diry = playerTwo.getShiftAim()
                if playerTwo.aim<0:
                    dirx *=-1
                ballAnimDrivingRange(app, dirx, diry ,(app.swingDir/5))

    
    #putting
    if app.puttNow:
        app.puttAgain = False
        if app.puttImg<=4:
            app.puttImg+=1
            app.puttOver = True
        if app.ballGreeny > app.ballGreenShouldGo:
             app.ballGreeny-=15
             app.ballGreenx+= app.swingDir
             if isInHole(app):
                  app.ballGreenr = 3

                  resetPutt(app)
                  app.finishHole = True
        elif app.ballGreeny <= app.ballGreenShouldGo and app.finishHole==False:
             app.distanceToPin = dist(app.ballGreenx, app.holex, app.ballGreeny, app.holey)//15
             app.puttAgain = True
             
             
             
    
    
    app.i+=1
    
        

#ball animation -- Main Physics Engine
#Although there are not very complex physics involved, this function animates
#the ball flight and does the physics calculations that take into account
#the player's aim and power and animates the ball flight in top down view
def ballAnim(app, dirx , diry, dirAimed):
    
    app.stepsPerSecond = 2000
    app.distanceToPin = int(calcDistToPin(app, ballOne.x, ballOne.y, app.currHole)/1.9 +1)
    
    if ballOne.size != 3:
            app.velocity_y += 0.20  # Adjust this damping factor to kinda show air resistence
            
    if app.is_rising:
        # Ball is rising
        ballOne.y += app.velocity_y
        ballOne.y += diry
        app.velocity_y += app.gravity

        ballOne.size += 0.15
        ballOne.x+= dirAimed*3 + dirx

        # Check if ball reaches its apex
        if app.velocity_y >= 0:
            app.is_rising = False  # Change direction to falling

    else:
        # Ball is falling
        ballOne.x += dirAimed/2 + dirx/5
        ballOne.y -=app.velocity_y
        ballOne.y += diry
        app.velocity_y -= app.gravity  # Decrease velocity due to air resistance
        


        if ballOne.size > 3:
            ballOne.size -= 0.15
        else:
            # Stop ball
    
            app.velocity_y = 0 
            boardj = int((ballOne.x-450) //10)
            boardi = int(ballOne.y //10)
       
            if app.holeList[app.currHole].board[boardi][boardj] == 'grey':
                 ballOne.terrainD = 'Excellent, you are on the Green!'
                 ballOne.terrain = 'Green'
                 ballOne.previousx = ballOne.x
                 ballOne.previousy = ballOne.y
                 app.prevDistanceToPin = app.distanceToPin
                 app.holeList[app.currHole].playerScore+=1
     
                 
            elif app.holeList[app.currHole].board[boardi][boardj] == 'lightGreen':
                 ballOne.terrainD = 'Great! You are on the Fairway'
                 ballOne.terrain = 'Fairway'
                 ballOne.previousx = ballOne.x
                 ballOne.previousy = ballOne.y
                 app.prevDistanceToPin = app.distanceToPin
                 app.holeList[app.currHole].playerScore+=1

                 
            elif app.holeList[app.currHole].board[boardi][boardj] == 'darkGreen':
                 ballOne.terrainD = 'Oops, you are in the Rough'
                 ballOne.terrain = 'Rough'
                 ballOne.previousx = ballOne.x
                 ballOne.previousy = ballOne.y
                 app.prevDistanceToPin = app.distanceToPin
                 app.holeList[app.currHole].playerScore+=1
 

            elif app.holeList[app.currHole].board[boardi][boardj] == 'yellow':
                 ballOne.terrainD = 'Dang, your ball is in a bunker'
                 ballOne.terrain = 'Bunker'
                 ballOne.previousx = ballOne.x
                 ballOne.previousy = ballOne.y
                 app.prevDistanceToPin = app.distanceToPin
                 app.holeList[app.currHole].playerScore+=1
                        

            else:
                if app.holeList[app.currHole].board[boardi][boardj] == 'pink':
                    ballOne.terrainD = 'Your ball got lost in a building'
                    ballOne.terrain = app.holeList[app.currHole].getTerrain(ballOne.previousx, ballOne.previousy)

                    ballOne.x = ballOne.previousx
                    ballOne.y = ballOne.previousy

                    app.distanceToPin = app.prevDistanceToPin
                    
                    app.holeList[app.currHole].playerScore+=2
                    

                elif app.holeList[app.currHole].board[boardi][boardj] == 'blue':
                    ballOne.terrain = app.holeList[app.currHole].getTerrain(ballOne.previousx, ballOne.previousy)
                    ballOne.terrainD = 'Boo! Your ball is lost in the drain!'
                    ballOne.x = ballOne.previousx
                    ballOne.y = ballOne.previousy
                    app.holeList[app.currHole].playerScore+=2
                    app.distanceToPin = app.prevDistanceToPin
                 
                elif app.holeList[app.currHole].board[boardi][boardj] == None:
                    ballOne.terrain = app.holeList[app.currHole].getTerrain(ballOne.previousx, ballOne.previousy)
                    ballOne.terrainD = 'You suck! Your ball is out of bounds'
                    ballOne.x = ballOne.previousx
                    ballOne.y = ballOne.previousy
                    app.holeList[app.currHole].playerScore+=2
                    app.distanceToPin = app.prevDistanceToPin

             

            if app.playerSwingNow:
                
                app.is_rising = True  
                app.swingNow = False 
                app.playerSwingNow = False 
                app.swingOver = not app.swingOver
                app.powerBarMoving = False
                app.dirbarMoving = True
                app.swingPower = -1
                playerOne.y =ballOne.y
                playerOne.x = ballOne.x-13
                app.dirSelected = False
                app.powerSelected = False
                app.switchLabel = 'Player View'
    

#ball animation for driving range only-- Main Physics Engine
#Although there are not very complex physics involved, this function animates
#the ball flight and does the physics calculations that take into account
#the player's aim and power and animates the ball flight in top down view
def ballAnimDrivingRange(app, dirx , diry, dirAimed):
    
    app.stepsPerSecond = 2000
    app.distanceTravelled = int(dist(ballTwo.x, 725, ballTwo.y, 780)/1.9)
    
    if ballTwo.size != 3:
            app.velocity_y += 0.20  # Adjust this damping factor to kinda show air resistence
            
    if app.is_rising:
        # Ball is rising
        ballTwo.y += app.velocity_y
        ballTwo.y += diry
        app.velocity_y += app.gravity

        ballTwo.size += 0.15
        ballTwo.x+= dirAimed*3 + dirx

        # Check if ball reaches its apex
        if app.velocity_y >= 0:
            app.is_rising = False  # Change direction to falling

    else:
        # Ball is falling
        ballTwo.x += dirAimed/2 + dirx/5
        ballTwo.y -=app.velocity_y
        ballTwo.y += diry
        app.velocity_y -= app.gravity  # Decrease velocity due to air resistance
        


        if ballTwo.size > 3:
            ballTwo.size -= 0.15
        else:
            # Stop ball
            app.velocity_y = 0 
            newBallPos = ballTwo.x, ballTwo.y
            app.drivingRangeList.append(newBallPos)
            ballTwo.x = 725
            ballTwo.y = 780

       

            if app.playerSwingNow:
                
                app.is_rising = True  
                app.swingNow = False 
                app.playerSwingNow = False 
                app.swingOver = not app.swingOver
                app.powerBarMoving = False
                app.dirbarMoving = True
                app.swingPower = -1
                app.dirSelected = False
                app.powerSelected = False
                app.switchLabel = 'Player View'







# regular onkeypress function

def onKeyPress(app, key):

    #stopping the powerbar
    if key=='space' and ballOne.terrain != 'Green' and app.powerBarMoving:
        app.powerBarMoving = False
        app.i=0
        index = clubList[app.clubNum%13].distIndex
      
        swingp= int((app.powerWidth*110)//app.powerTotalWidth)
        app.swingPower = int((app.powerWidth*135)//app.powerTotalWidth)
        

        # different terrain have different friction
        if ballOne.terrain == 'Bunker':
            app.velocity_y = (index-(swingp//50)) * 0.60 
        elif ballOne.terrain =='Rough':
            app.velocity_y = (index-(swingp//50)) * 0.80 
        else:
            app.velocity_y = index-(swingp//50) 




        app.powerSelected = True
        if app.dirSelected ==True:
            app.playerSwingNow = True
    
    elif key=='space' and ballOne.terrain == 'Green' and app.gpowerBarMoving:
         app.gpowerBarMoving = False
         app.puttpower = int(int((1-app.gpowerHeight/app.gpowerTotalHeight)*100)*0.4)
         app.ballGreenShouldGo = app.gpowerHeight +75
         app.puttNow = True
         app.gpowerSelected = True

    
        

    #stopping the directionbar
    if key=='enter' and ballOne.terrain != 'Green' and app.dirbarMoving:
        app.dirbarMoving = False
        app.dirSelected =True
        index = clubList[app.clubNum%13].distIndex
      
        app.swingDir = (app.dirArrowAngle-90)/10
        
        app.powerBarMoving = True

    if key=='enter' and ballOne.terrain == 'Green' and app.dirbarMoving:
        app.dirbarMoving = False
        app.dirSelected =True
        index = clubList[12].distIndex
      
        app.swingDir = (app.dirArrowAngle-90)/10
        app.gpowerBarMoving = True

    if key=='g':
        if app.currHole!=3:
            app.holeList[app.currHole].playerScore = 2*app.holeList[app.currHole].par
            playerOne.addStroke(app.holeList[app.currHole].playerScore)
            resetPutt(app)
            app.currHole+=1
            ballOne.x = 725
            ballOne.y= 800
            playerOne.x =725 -13
            playerOne.y = 800
            ballOne.terrain = 'teeBox'
            ballOne.terrainD = 'You are ready to tee off from the Tee Box'
            ballOne.previousx = 725
            ballOne.previousy = 800
            app.distanceToPin = app.holeList[app.currHole].length
            app.prevDistanceToPin = app.holeList[app.currHole].length
            app.view = 'top'
            app.switchLabel = 'Player View'
            app.finishHole = False
        else:
            app.holeList[3].playerScore = 8
            app.view='end'
            app.gameEnd=True

                


#regular distance function
def dist(x1, x2, y1, y2):
    distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
    return distance

#calculates the distance to pin before ball reaches green
def calcDistToPin (app, x,y, holeNum):
     return dist(x, app.holeList[holeNum].holeLocX, y, app.holeList[holeNum].holeLocY)


#regular onMousepress function for users to click on buttons
def onMousePress(app, mouseX, mouseY):
    if app.view!= 'start' and app.view!='end' and abs(mouseX- app.backx) <=50 and abs(mouseY-app.backy)<=25:
        app.view='start'

    if app.inTraining==True and abs(mouseX- app.backx) <=50 and abs(mouseY-app.backy)<=25:
        app.view='start'
        app.drivingRangeList = []
        app.inTraining = False
    

    if app.view=='end' and abs(mouseX- app.backx) <=50 and abs(mouseY-app.backy)<=25:
        newGame(app)

    if app.inTraining==False:
        if abs(mouseX- app.viewSwitchx) <=50 and abs(mouseY-app.viewSwitchy)<=25:
            if app.switchLabel=='Player View':
                app.view = 'player'
                if ballOne.terrain =='Green':
                    distLeft = app.distanceToPin
                    if distLeft>40:
                        distLeft = 40
                    app.holex = 788
                    app.holey = 75 + (40-distLeft)*15
                app.switchLabel = 'Top View'
            else:
                app.view = 'top'
                app.switchLabel = 'Player View'

    if app.inTraining:
        if abs(mouseX- app.viewSwitchx) <=50 and abs(mouseY-app.viewSwitchy)<=25:
            if app.switchLabel=='Player View':
                app.view = 'player'
                app.switchLabel = 'Top View'
            else:
                app.view = 'drivingRange'
                ballTwo.terrain = 'teeBox'
                app.switchLabel = 'Player View'


    
    
    if app.view=='start' and abs(mouseX- app.instrx) <=100 and abs(mouseY-app.instry)<=100:
        app.view='instructions'
    
    if app.view=='start' and abs(mouseX- app.drivingx) <=100 and abs(mouseY-app.drivingy)<=100:
        app.view='drivingRange'
        app.inTraining = True


    if app.view=='player':
        if dist(mouseX, app.circlex,  mouseY, app.circley) <= app.circler:
            app.clubNum +=1

    leftAimPressed = abs(mouseX-1200) <=35 and abs(mouseY-800) <=35
    rightAimPressed = abs(mouseX-1300) <=35 and abs(mouseY-800) <=35

    if app.view=='top' and leftAimPressed:
         playerOne.shiftAim(0.001, -1)


    if app.view=='top' and rightAimPressed:
         playerOne.shiftAim(0.001, 1)


    
    if app.view=='player' and app.puttAgain:
         if abs(mouseX-app.nextPuttSignx)<=100 and abs(mouseY-app.nextPuttSigny<=50):
              resetPutt(app)
        
    if app.view=='start':
         if abs(mouseX-app.startx)<=(app.startw//2) and abs(mouseY-app.starty)<=(app.starth//2):
              app.view='top'
    
    ## Move on to next Hole
    if app.finishHole and app.currHole<=2:
        if abs(mouseX-app.nextPuttSignx)<=(150) and abs(mouseY-app.nextPuttSigny)<=(75):
            playerOne.addStroke(app.holeList[app.currHole].playerScore)
            resetPutt(app)
            app.currHole+=1
            ballOne.x = 725
            ballOne.y= 800
            playerOne.x =725 -13
            playerOne.y = 800
            ballOne.terrain = 'teeBox'
            ballOne.terrainD = 'You are ready to tee off from the Tee Box'
            ballOne.previousx = 725
            ballOne.previousy = 800
            app.distanceToPin = app.holeList[app.currHole].length
            app.prevDistanceToPin = app.holeList[app.currHole].length
            app.view = 'top'
            app.switchLabel = 'Player View'
            app.finishHole = False
    
      
    
    
        
#a reset of the player mode green view when the player misses a putt
def resetPutt(app):
    app.holeList[app.currHole].playerScore+=1
    app.gstripLeft =  app.width // 4.5 
    app.gstripTop = 75
    app.gstripFill = None  # Color of the strip
    app.gstripHeight = 600
    app.gstripWidth = app.height//10

    
    app.gpowerBarMoving = False
    app.gpowerBx = 5+ app.width // 4.5 
    app.gpowerBy = 75
    app.gpowerHeight = 1
    app.gpowerWidth = app.height//10 -10
    app.gpowerColor = gradient('darkOliveGreen', 'darkOliveGreen',
                              'darkGreen', 'darkGreen', 'green',
                               'green', 'lime','lime', 'yellow', 'red',start='bottom')
    app.gpowerSpeed = 54
    app.gpowerTotalHeight= 600

    #after pressed powerbox settings for Green Only
    app.gapowerx = 5+ app.width // 4.5 
    app.gapowery = 789
    app.gapowerWidth = app.height//10
    app.gapowerHeight = app.height//10
    app.gpowerSelected = False
    app.gswingDist = 0



    #direction bar settings
    app.dirbarMoving = True 
    app.dirbarX = 133
    app.dirbarY = 740
    app.dirbarRadius = 250
    app.dirArrowAngle = 90    
    
    app.puttImg =0
    app.puttNow =False
    app.puttOver = False
    app.puttpower= -1
    app.holex = 788
    app.holey = 75 + (40-app.distanceToPin)*15

    app.puttAgain = False
    app.nextPuttSignx = app.width//2
    app.nextPuttSigny = app.height//2-50
    app.nextPuttSignLabel ='Press here to putt again'

    app.ballGreenx = 788
    app.ballGreeny = 685
    app.ballGreenr = 7
    app.ballGreenShouldGo = 0

    app.swingDir =0



#checks if a ball is in the hole to signify end of the hole   
def isInHole(app):
     if dist(app.ballGreenx, app.holex, app.ballGreeny, app.holey)<=15:
          return True     




#helpers to visualize grid when I code them

def drawGrid(app):
    for row in range(app.holeList[app.currHole].rows):
        for col in range(app.holeList[app.currHole].cols):
            drawCell(row, col, app.holeList[app.currHole].board[row][col])

def drawCell(row, col, color):
    cellLeft, cellTop = getCellLeftTop(row, col)
    cellWidth, cellHeight = 10, 10
    drawRect(cellLeft, cellTop, cellWidth, cellHeight,
             fill= color, border='black',
             borderWidth=1)

def getCellLeftTop(row, col):
    cellWidth, cellHeight = 10, 10
    cellLeft =  450+ col * cellWidth
    cellTop =  row * cellHeight
    return (cellLeft, cellTop)


#run everything here
def main():
    runApp()

main()
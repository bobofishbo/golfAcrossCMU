import math

#Clubs class

class clubs:
    #initialize self with its variables
    def __init__(self, name, dista, distIndex, mindex, imagelink):
        self.name = name
        self.fullDist = dista
        self.distIndex = distIndex
        self.missIndex = mindex
        self.image = imagelink
        self.canUse = dict()
        self.swingAnimation = []

    def setSwingAnimation(self, listA):
        self.swingAnimation = listA
    
    #wrapper function to return the stuff in function
    def __repr__(self):
        return f'You are using the {self.name}.'



#creating the clubs
driver = clubs('Driver', 250, -17.8, 2, 'clubPics/diverPic.jpg')
threeWood = clubs('3 Wood', 230, -17, 1.9 , 'clubPics/twPic.jpg')
hybrid = clubs('Hybrid', 215, -16.3, 1.8, 'clubPics/hybridPic.jpg')
fourIron = clubs('4 Iron', 190, -16, 1.75, 'clubPics/fouriPic.jpg')
fiveIron = clubs('5 Iron', 185, -15.5, 1.7, 'clubPics/fiveiPic.jpg')
sixIron = clubs('6 Iron', 175, -14.5, 1.5, 'clubPics/sixiPic.jpg')
sevenIron = clubs('7 Iron', 160, -13.8, 1.4, 'clubPics/seveniPic.jpg')
eightIron = clubs('8 Iron', 145, -13.2, 1.3, 'clubPics/eightiPic.jpg')
nineIron = clubs('9 Iron', 130, -12.7, 1.2, 'clubPics/nineiPic.jpg')
pWedge = clubs('P Wedge', 100, -11.5, 1.1, 'clubPics/pwPic.jpg')
fiftysixWedge = clubs('56 Wedge', 80, -10 , 1.1, 'clubPics/fswPic.jpg')
sixtyWedge = clubs('60 Wedge', 35, -5, 1, 'clubPics/swPic.jpg')
putter = clubs('Putter', 40, -1, 1, 'clubPics/puttPic.jpg')

clubList=[driver, threeWood, hybrid, fourIron,
          fiveIron, sixIron, sevenIron, eightIron,
          nineIron, pWedge, fiftysixWedge,sixtyWedge, putter]



#ball class
#ball's position is important
class ball:
    #initialize self with its variables
    def __init__(self, x, y):
        self.x = x
        self.y =y
        self.blocki = 0
        self.blocki = 0
        self.terrainD = 'You are ready to tee off from the Tee Box'
        self.terrain = 'teeBox'
        self.size = 3
        self.previousx = 725
        self.previousy = 800

    

ballOne  = ball(725, 800) 

ballTwo  = ball(725, 780) 


    

#Player class
#Players have name, starting position, and position properties
#They have total score

class player:
    #initialize self with its variables
    def __init__(self, name, x, y):
        self.x = x
        self.y =y
        self.name = name
        self.score = 0
        self.aim = 0
        self.dir = 0

    def addStroke(self, holeScore):
        self.score+= holeScore
    
    def shiftAim(self, degrees, dir):
         self.aim += degrees*dir
         
         xshift = math.cos(math.degrees(self.aim))
         yshift = math.sin(math.degrees(self.aim))

         self.x = ballOne.x- 13*xshift
         self.y = ballOne.y- 13*yshift
         
         
    def getShiftAim(self):
         xshift = (1-math.cos(self.aim)) *100000
         yshift = (math.sin(self.aim))*100
         
         return xshift, yshift

playerOne = player('Pat', 725 -13  ,800)
playerTwo = player('practing', 725-13, 780)



#Hole class
#Every hole has some properties like the par, 
#and the score of the player on this hole.

class hole:
    #initialize self with its variables
    def __init__(self, num, name, par,length, img, mapimg, holeLocX, holeLocY):
        self.num = num
        self.name = name
        self.length = length
        self.par = par
        self.playerScore =0
        self.rows = 100
        self.cols = 60
        self.cellBorderWidth = 10
        self.board = [([None] * self.cols) for row in range(self.rows)]
        self.img =img
        self.mapimg = mapimg
        self.holeLocX = holeLocX
        self.holeLocY = holeLocY


    #add objects like water, rough, sand
    def getTerrain(self, x, y):
        boardJ = int((x-450) //10)
        boardI = int(y//10)
        return self.board[boardI][boardJ]

    
    #wrapper function to return the stuff in function
    def __repr__(self):
        pass


holeOne = hole(1, 'Entropy Rush', 4, 319, 'holeOne.jpg', 'holeOneMap.jpg', 835, 205)
holeTwo = hole(2, 'City Of Rivers', 5, 388, 'holeTwo.jpg', 'holeTwoMap.jpg', 780, 135)
holeThree = hole(3, 'Staying Alive', 3, 198, 'holeThree.jpg', 'holeThreeMap.jpg', 750, 375)
holeFour = hole(4, 'Escape 112', 4, 376, 'holeFour.jpg', 'holeFourMap.jpg', 775, 165)




  
# The following four functions are used together to 
# color-code each pixel of the map into 
# fairway, rough, water, green, etc. It was done manually
#as I did not know of a better idea when i did it

def drawHoleOne():

    for i in range(26,45):
        for j in range(3,7):
            holeOne.board[j][i]='darkGreen'

    for i in range(41,74):
        for j in range(38,53):
            holeOne.board[i][j]='darkGreen'

    for i in range(51,80):
        for j in range(10, 19):
            holeOne.board[i][j]='darkGreen'

    for i in range(18,51):
        for j in range(7, 16):
            holeOne.board[i][j]='darkGreen'

    for i in range(7,19):
        for j in range(16, 29):
            holeOne.board[i][j]='darkGreen'

    for i in range(12,18):
        for j in range(11, 16):
            holeOne.board[i][j]='darkGreen'

    for i in range(74, 88):
        for j in range(31, 60):
            holeOne.board[i][j]='darkGreen'

    for i in range(74, 88):
        for j in range(6, 23):
            holeOne.board[i][j]='darkGreen'

    for j in range(14, 18):
            holeOne.board[j][10]='darkGreen'
    for j in range(15, 18):
            holeOne.board[j][9]='darkGreen'
    holeOne.board[17][8]='darkGreen'

    for j in range(8, 12):
            holeOne.board[j][15]='darkGreen'
    for j in range(9, 12):
            holeOne.board[j][14]='darkGreen'
    for j in range(10, 12):
            holeOne.board[j][13]='darkGreen'
    holeOne.board[11][12]='darkGreen'

    for i in range(4, 7):
        for j in range(18, 26):
            holeOne.board[i][j]='darkGreen'

    for j in range(7, 11):
            holeOne.board[j][29]='darkGreen'
    for j in range(7, 10):
            holeOne.board[j][30]='darkGreen'
    for j in range(7, 9):
            holeOne.board[j][31]='darkGreen'
    holeOne.board[7][32]='darkGreen'
    holeOne.board[7][33]='darkGreen'
    holeOne.board[7][44]='darkGreen'
    for j in range(4, 8):
            holeOne.board[j][45]='darkGreen'
    for j in range(5, 9):
            holeOne.board[j][46]='darkGreen'
    for j in range(5, 10):
            holeOne.board[j][47]='darkGreen'
    for j in range(6, 11):
            holeOne.board[j][48]='darkGreen'
    for j in range(6, 12):
            holeOne.board[j][49]='darkGreen'
    for j in range(7, 14):
            holeOne.board[j][50]='darkGreen'
    for j in range(8, 20):
            holeOne.board[j][51]='darkGreen'
    for j in range(9, 41):
            holeOne.board[j][51]='darkGreen'
    for j in range(9, 41):
            holeOne.board[j][52]='darkGreen'
    for j in range(10, 30):
            holeOne.board[j][53]='darkGreen'
    for j in range(11, 25):
            holeOne.board[j][54]='darkGreen'
    for j in range(15, 23):
            holeOne.board[j][55]='darkGreen'
    for j in range(15, 23):
            holeOne.board[j][55]='darkGreen'

    for j in range(33, 41):
            holeOne.board[j][50]='darkGreen'
    for j in range(36, 41):
            holeOne.board[j][49]='darkGreen'
    for j in range(37, 41):
            holeOne.board[j][48]='darkGreen'
    for j in range(38, 41):
            holeOne.board[j][47]='darkGreen'
    holeOne.board[40][46]='darkGreen'
    holeOne.board[40][45]='darkGreen'
    holeOne.board[40][44]='darkGreen'
    
    for i in range(56, 74):
         for j in range(19,22):
              holeOne.board[i][j] = 'darkGreen'

    for j in range(53,56):
              holeOne.board[j][19] = 'darkGreen'
    for j in range(54,56):
            holeOne.board[j][20] = 'darkGreen'
    for j in range(47,51):
            holeOne.board[j][6] = 'darkGreen'
    holeOne.board[50][5] = 'darkGreen'
    for j in range(54,69):
            holeOne.board[j][4] = 'darkGreen'
    for j in range(59,66):
            holeOne.board[j][3] = 'darkGreen'
    holeOne.board[48][16] = 'darkGreen'
    holeOne.board[49][16] = 'darkGreen'
    holeOne.board[50][16] = 'darkGreen'
    holeOne.board[50][17] = 'darkGreen'
    holeOne.board[44][16] = 'darkGreen'
    holeOne.board[38][18] = 'darkGreen'
    holeOne.board[38][19] = 'darkGreen'
    holeOne.board[38][20] = 'darkGreen'
    holeOne.board[38][21] = 'darkGreen'
    holeOne.board[38][22] = 'darkGreen'
    holeOne.board[39][18] = 'darkGreen'
    holeOne.board[39][19] = 'darkGreen'
    holeOne.board[39][20] = 'darkGreen'
    holeOne.board[40][18] = 'darkGreen'
    holeOne.board[40][19] = 'darkGreen'
    holeOne.board[41][18] = 'darkGreen'


    for i in range(78,82):
        for j in range(25, 29):
            holeOne.board[i][j]='red'


    
    #water tennis courts
    for i in range(18,33):
        for j in range(16, 27):
            holeOne.board[i][j]='blue'

    for i in range(19, 29):
        for j in range(27, 29):
            holeOne.board[i][j]='darkGreen'

    for j in range(29, 32):
        holeOne.board[j][27]='darkGreen'

    for i in range(51,72):
        for j in range(5, 10):
            holeOne.board[i][j]='darkGreen'

    for i in range(72,74):
        for j in range(6, 10):
            holeOne.board[i][j]='darkGreen'

    for j in range(16, 27):
        holeOne.board[33][j]='darkGreen'
    for j in range(16, 26):
        holeOne.board[34][j]='darkGreen'
    for j in range(16, 25):
        holeOne.board[35][j]='darkGreen'

    for j in range(16, 25):
        holeOne.board[36][j]='pink'
    for j in range(16, 25):
        holeOne.board[37][j]='pink'

    for i in range(38,43):
        for j in range(16, 18):
            holeOne.board[i][j]='pink'

    holeOne.board[43][16]='pink'

    for i in range(38,40):
        for j in range(23, 25):
            holeOne.board[i][j]='pink'

    for i in range(36,47):
        for j in range(33, 36):
            holeOne.board[i][j]='pink'

    for i in range(58,66):
        for j in range(32, 38):
            holeOne.board[i][j]='pink'

    for i in range(51,58):
        for j in range(32, 34):
            holeOne.board[i][j]='pink'
    holeOne.board[51][34]='pink'
    
    #sand traps
    for i in range(22,24):
        for j in range(33, 36):
            holeOne.board[i][j]='yellow'

    for i in range(24,26):
        for j in range(35, 38):
            holeOne.board[i][j]='yellow'
    holeOne.board[24][34]='yellow'
    holeOne.board[23][36]='yellow'
    holeOne.board[23][37]='yellow'
    holeOne.board[24][38]='yellow'
    holeOne.board[21][34]='yellow'
    holeOne.board[21][35]='yellow'
    holeOne.board[20][34]='yellow'
    holeOne.board[20][35]='yellow'

    for i in range(24,26):
        for j in range(40, 45):
            holeOne.board[i][j]='yellow'
    for j in range(40, 44):
            holeOne.board[26][j]='yellow'

    for i in range(20,25):
        for j in range(49, 52):
            holeOne.board[i][j]='yellow'
    for i in range(23,26):
        for j in range(47, 51):
            holeOne.board[i][j]='yellow'


    for i in range(9,23):
        for j in range(37, 47):
            holeOne.board[i][j]='grey'
    for j in range(9, 19):
            holeOne.board[j][36]='grey'

    #The hole
    holeOne.board[20][38]='black'

    for i in range(15,18):
        for j in range(33, 36):
            holeOne.board[i][j]='blue'

    for i in range(7, 87):
        for j in range(16,51):
             if holeOne.board[i][j]==None:
                  holeOne.board[i][j]='lightGreen'



def drawHoleTwo():
    #drawRough 
    for i in range(8, 16):
         for j in range(20, 45):
              holeTwo.board[i][j] = 'darkGreen'
    
    for i in range(8, 28):
         for j in range(8, 23):
              holeTwo.board[i][j] = 'darkGreen'

    for i in range(8, 48):
         for j in range(45, 53):
              holeTwo.board[i][j] = 'darkGreen'

    for i in range(27, 49):
         for j in range(6, 19):
              holeTwo.board[i][j] = 'darkGreen'

    for i in range(22, 29):
         for j in range(3, 8):
              holeTwo.board[i][j] = 'darkGreen'

    for i in range(17, 22):
         for j in range(5, 8):
              holeTwo.board[i][j] = 'darkGreen'

    #drawWater
    for i in range(29, 38):
         for j in range(3, 8):
              holeTwo.board[i][j] = 'blue'

    for i in range(29, 44):
         for j in range(5, 13):
              holeTwo.board[i][j] = 'blue'

    for i in range(28, 33):
         for j in range(13, 24):
              holeTwo.board[i][j] = 'blue'

    for i in range(49, 52):
         for j in range(6, 52):
              holeTwo.board[i][j] = 'blue'

    for j in range(30, 52):
            holeTwo.board[48][j] = 'blue'
    for j in range(31, 52):
            holeTwo.board[47][j] = 'blue'

    for i in range(28, 52):
         for j in range(33, 37):
              holeTwo.board[i][j] = 'blue'
    
    for i in range(28, 30):
         for j in range(24, 40):
              holeTwo.board[i][j] = 'blue'
    
    for i in range(25, 28):
         for j in range(37, 40):
              holeTwo.board[i][j] = 'blue'
    holeTwo.board[24][39] ='blue'
    holeTwo.board[26][36] ='blue'
    holeTwo.board[27][36] ='blue'
    holeTwo.board[27][35] ='blue'

    for i in range(33, 35):
            holeTwo.board[i][17] = 'blue'
    for i in range(33, 37):
            holeTwo.board[i][18] = 'blue'
    for i in range(33, 51):
            holeTwo.board[i][19] = 'blue'
    for i in range(37, 51):
            holeTwo.board[i][20] = 'blue'
    for i in range(42, 51):
            holeTwo.board[i][21] = 'blue'

    for i in range(35, 41):
         for j in range(26, 29):
              holeTwo.board[i][j] = 'blue'
    for i in range(32, 45):
              holeTwo.board[i][29] = 'blue'
    for i in range(34, 43):
              holeTwo.board[i][28] = 'blue'
    for i in range(31, 36):
              holeTwo.board[i][30] = 'blue'
    for i in range(30, 35):
              holeTwo.board[i][31] = 'blue'
    for i in range(30, 33):
              holeTwo.board[i][32] = 'blue'
    for i in range(43, 47):
              holeTwo.board[i][32] = 'blue'
    for i in range(42, 47):
              holeTwo.board[i][31] = 'blue'
    for i in range(40, 46):
              holeTwo.board[i][30] = 'blue'
    for i in range(32, 37):
              holeTwo.board[i][25] = 'blue'
    for i in range(39, 44):
              holeTwo.board[i][25] = 'blue'
    for i in range(33, 42):
              holeTwo.board[i][26] = 'blue'
    for i in range(31, 37):
              holeTwo.board[i][24] = 'blue'
    for i in range(40, 45):
              holeTwo.board[i][24] = 'blue'
    for i in range(42, 47):
              holeTwo.board[i][23] = 'blue'
              holeTwo.board[33][23] = 'blue'
    
    for i in range(43, 49):
              holeTwo.board[i][22] = 'blue'
    
    #drawbuildings
    for i in range(9,27):
            for j in range(9, 20):
                holeTwo.board[i][j]='pink'
    for i in range(6,10):
            for j in range(22, 44):
                holeTwo.board[i][j]='pink'
    for i in range(20,33):
            for j in range(45, 54):
                holeTwo.board[i][j]='pink'
    for i in range(23,30):
            for j in range(40, 50):
                holeTwo.board[i][j]='pink'
    for i in range(52,84):
            for j in range(5, 19):
                holeTwo.board[i][j]='pink'
    holeTwo.board[53][19]='pink'
    holeTwo.board[54][19]='pink'
    for i in range(52,86):
            for j in range(35, 52):
                holeTwo.board[i][j]='pink'
    for i in range(52,54):
            for j in range(32, 35):
                holeTwo.board[i][j]='pink'



    #drawTeeBox
    for i in range(77,82):
            for j in range(24, 29):
                holeTwo.board[i][j]='red'

    #drawGreen
    for i in range(11, 16):
            for j in range(23, 44):
                holeTwo.board[i][j]='grey'
    
    #drawHole
    holeTwo.board[13][32]='black'

    for i in range(15,86):
            for j in range(10, 49):
                if holeTwo.board[i][j]==None:
                      holeTwo.board[i][j] = 'lightGreen'
                   


def drawHoleThree():
        #drawWater
        for i in range(21, 48):
           for j in range(13, 47):
              holeThree.board[i][j] = 'blue'
        #drawGreen
        for i in range(27,29):
              holeThree.board[i][15] = 'grey'
        for i in range(26,30):
              holeThree.board[i][16] = 'grey'
        for i in range(25,31):
              holeThree.board[i][17] = 'grey'
        for i in range(26,31):
              holeThree.board[i][18] = 'grey'
        for i in range(27,32):
              holeThree.board[i][19] = 'grey'
        for i in range(28,33):
              holeThree.board[i][20] = 'grey'
        for i in range(28,34):
              holeThree.board[i][21] = 'grey'
              
        i=29
        for j in range(22, 37):
                if j==27:
                          i-=1
                for k in range(i, i+6):
                    holeThree.board[k][j]='grey'
                    
                i+=1

        for i in range(42,47):
              holeThree.board[i][37] = 'grey'
        for i in range(43,46):
              holeThree.board[i][38] = 'grey'
              holeThree.board[44][39] = 'grey'

        #draw teebox
        for i in range(78,82):
                for j in range(25, 29):
                        holeThree.board[i][j]='red'
        #drawrough
        for i in range(48, 80):
              for j in range(7, 51):
                    holeThree.board[i][j] = 'darkGreen'
              



def drawHoleFour():
        #drawWater
        for i in range(10, 32):
           for j in range(15, 49):
              holeFour.board[i][j] = 'blue'
        for i in range(35, 37):
              for j in range(13, 33):
                    holeFour.board[i][j]='blue'
        for j in range(32, 41):
                    holeFour.board[34][j]='blue'
        for j in range(32, 41):
                    holeFour.board[35][j]='blue'
        for j in range(41, 48):
                    holeFour.board[32][j]='blue'
        for j in range(41, 46):
                    holeFour.board[33][j]='blue'

        #drawGreen
        for i in range(15, 20):
              for j in range(26, 36):
                    holeFour.board[i][j]='grey'
        #drawHole
        holeFour.board[16][32]='black'

        #drawFairway
        for i in range(32, 35):
              for j in range(14, 33):
                    holeFour.board[i][j]='lightGreen'
        for j in range(32, 41):
                    holeFour.board[32][j]='lightGreen'
        for j in range(32, 41):
                    holeFour.board[33][j]='lightGreen'
        for i in range(39, 55):
              for j in range(22, 29):
                    holeFour.board[i][j]='lightGreen'
        
        #draw bunker
        for i in range(39, 55):
              for j in range(16, 20):
                    holeFour.board[i][j]='yellow'


        #draw buildings & teeBox
        for i in range(59, 80):
              for j in range(10, 46):
                    holeFour.board[i][j]='pink'
        for i in range(78,82):
                for j in range(25, 29):
                        holeFour.board[i][j]='red'
        for i in range(57, 59):
              for j in range(24, 29):
                    holeFour.board[i][j]='pink'
        for i in range(41, 64):
              for j in range(8, 13):
                    holeFour.board[i][j]='pink'
        for i in range(55, 59):
              for j in range(32, 35):
                    holeFour.board[i][j]='pink'
        for i in range(38, 45):
              for j in range(32, 43):
                    holeFour.board[i][j]='pink'
        for j in range(41, 44):
                    holeFour.board[j][31]='pink'
        for j in range(41, 45):
                    holeFour.board[j][43]='pink'
        for j in range(37, 43):
                    holeFour.board[45][j]='pink'
        for j in range(37, 40):
                    holeFour.board[46][j]='pink'

        for i in range(47, 59):
              for j in range(38, 43):
                    holeFour.board[i][j]='pink'
        for i in range(56, 59):
              for j in range(36, 38):
                    holeFour.board[i][j]='pink'
        for j in range(35, 44):
                    holeFour.board[49][j]='pink'
        for j in range(32, 40):
                    holeFour.board[50][j]='pink'
        for j in range(32, 40):
                    holeFour.board[51][j]='pink'
        for j in range(32, 43):
                    holeFour.board[52][j]='pink'
        for j in range(32, 35):
                    holeFour.board[53][j]='pink'

        #draw rough
        for i in range(32, 70):
              for j in range(5,49):
                    if holeFour.board[i][j]== None:
                          holeFour.board[i][j]= 'darkGreen'
        
        

        









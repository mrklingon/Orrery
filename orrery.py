import time
import random
import neopixel
import board
import touchio


def setperiod():
   return [24, 62, 100, 188]

def rndperiod():
   return [random.randrange(20)+10,
        random.randrange(50)+30,
        random.randrange(80)+30,
        random.randrange(150)+90]

def setcolor():
    return [(16,16,16), (64,60,7), (0, 62, 0), (36, 0, 0)]


def rndcolor():
    return [(random.randrange(100),random.randrange(20),random.randrange(20)),
            (random.randrange(20),random.randrange(20),random.randrange(100)),
            (random.randrange(20),random.randrange(100),random.randrange(20)),
            (random.randrange(50),random.randrange(40),random.randrange(30))]

touch1 = touchio.TouchIn(board.TOUCH1)
touch2 = touchio.TouchIn(board.TOUCH2)

period= setperiod()

planets = ["Mercury", "Venus", "Earth", "Mars"]
pix = setcolor()
loc = [0, 0 ,0,0]
counter = [0,0,0,0]
pixels = neopixel.NeoPixel(board.NEOPIXEL, 4, auto_write=True)

def clearplanets(lcx):
    for i in range(4):
        pixels[i] = (0,0,0)
def showplanets(lcx):

    for p in range(4):
        pixels[loc[p]] = pix[p]

def mvplanet(planet):
    pixels[loc[planet]]=(0,0,0)
    loc[planet] = (loc[planet]+1)%4
    pixels[loc[planet]]=pix[planet]

locate = 2 # start at Earth

showplanets(loc)
while True:
    Val = 0
    if touch1.value:
        Val = Val + 1
        
    if touch2.value:
        Val = Val + 2

    if Val == 2:
        period = rndperiod()
        pix = rndcolor()

    if Val == 1:
        period = setperiod()
        pix = setcolor()

    showplanets(loc)

    for p in range(4):
        counter[p] = counter[p]+1
        print (str(planets[p])+":"+str(counter[p])+":"+str(loc[p]))
        if counter[p]>period[p]:
            mvplanet(p)
            counter[p]=0

#    time.sleep(.01)




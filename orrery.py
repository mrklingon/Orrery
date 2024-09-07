from adafruit_circuitplayground import cp
import time
import random
import board


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


period = setperiod()
planets = ["Mercury", "Venus", "Earth", "Mars"]
pix = setcolor()

loc = [0, 0 ,0,0]
counter = [0,0,0,0]
def clearplanets(lcx):
    for i in range(10):
        cp.pixels[i] = (0,0,0)
def showplanets(lcx):

    for p in range(4):
        cp.pixels[loc[p]] = pix[p]
        
def mvplanet(planet):
    cp.pixels[loc[p]]=(0,0,0)
    loc[planet] = (loc[planet]+1)%10
    cp.pixels[loc[p]]=pix[p]

locate = 2 # start at Earth


showplanets(loc)
while True:
    showplanets(loc)
    if cp.button_a:
        period = setperiod()
        pix = setcolor()
        
    if cp.button_b:
        period = rndperiod()
        pix = rndcolor()

    for p in range(4):
        counter[p] = counter[p]+1
        print (str(planets[p])+":"+str(counter[p])+":"+str(loc[p]))
        if counter[p]>period[p]:
            mvplanet(p)
            counter[p]=0
            
#    time.sleep(.01)
    

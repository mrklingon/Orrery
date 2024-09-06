input.onGesture(Gesture.Shake, function () {
    state = 0
    music.magicWand.playUntilDone()
    light.showAnimation(light.rainbowAnimation, 500)
    period = [24, 62, 100, 188]
    planets = ["Mercury", "Venus", "Earth", "Mars"]
    pix = [light.rgb(10, 10, 10), Colors.Yellow, Colors.Green, Colors.Red]
    loc = [Math.randomRange(0, 9), Math.randomRange(0, 9), Math.randomRange(0, 9), Math.randomRange(0, 9)]
    counter = [0, 0, 0, 0]
    light.setAll(0x000000)
    showPlanets()
    state = 1
    orrery()
})
function orrery () {
    if (1 == state) {
        showPlanets()
        for (let p = 0; p <= 3; p++) {
            counter[p] = 1 + counter[p]
            if (period[p] <= counter[p]) {
                counter[p] = 0
                light.setPixelColor(loc[p], 0x000000)
                x = 1 + loc[p]
                loc[p] = x % 10
            }
        }
    }
}
function showPlanets () {
    for (let index = 0; index <= 3; index++) {
        light.setPixelColor(loc[index], pix[index])
    }
}
input.buttonA.onEvent(ButtonEvent.Click, function () {
    if (0 == state) {
        state = 1
        orrery()
    } else {
        state = 0
    }
})
input.buttonB.onEvent(ButtonEvent.Click, function () {
    state = 0
    pix = [light.rgb(Math.randomRange(0, 100), Math.randomRange(0, 100), Math.randomRange(0, 100)), light.rgb(Math.randomRange(0, 100), Math.randomRange(0, 100), Math.randomRange(0, 100)), light.rgb(Math.randomRange(0, 100), Math.randomRange(0, 100), Math.randomRange(0, 100)), light.rgb(Math.randomRange(0, 100), Math.randomRange(0, 100), Math.randomRange(0, 100))]
    period = [Math.randomRange(10, 30), Math.randomRange(30, 80), Math.randomRange(50, 100), Math.randomRange(100, 200)]
    state = 1
    orrery()
})
let x = 0
let state = 0
let counter: number[] = []
let loc: number[] = []
let pix: number[] = []
let planets: string[] = []
let period: number[] = []
period = [24, 62, 100, 188]
planets = ["Mercury", "Venus", "Earth", "Mars"]
pix = [light.rgb(20, 20, 20), Colors.Yellow, Colors.Green, Colors.Red]
loc = [Math.randomRange(0, 9), Math.randomRange(0, 9), Math.randomRange(0, 9), Math.randomRange(0, 9)]
counter = [0, 0, 0, 0]
state = 0
showPlanets()
state = 1
orrery()
forever(function () {
    if (1 == state) {
        orrery()
    }
})

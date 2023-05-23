radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 0) {
        ezker = true
    } else if (receivedNumber == 1) {
        eskuin = true
    } else if (receivedNumber == 2) {
        ezker = false
        eskuin = false
        kurba = false
    }
    basic.showLeds(`
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        `)
})
input.onButtonPressed(Button.A, function () {
    basic.clearScreen()
    radio.sendValue("kurba", 1)
    radio.sendNumber(0)
})
input.onButtonPressed(Button.B, function () {
    basic.clearScreen()
    radio.sendValue("kurba", 1)
    radio.sendNumber(1)
})
radio.onReceivedValue(function (name, value) {
    if (name == "kurba" && value == 1) {
        kurba = true
    } else if (name == "kurba" && value == 0) {
        kurba = false
    }
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    basic.clearScreen()
    radio.sendValue("kurba", 0)
    radio.sendNumber(2)
})
let eskuin = false
let ezker = false
let kurba = false
radio.setGroup(1)
kurba = false
ezker = false
basic.showLeds(`
    # # # # #
    # # # # #
    # # # # #
    # # # # #
    # # # # #
    `)
basic.forever(function () {
    if (ezker) {
        basic.showArrow(ArrowNames.West)
        basic.clearScreen()
        basic.pause(100)
    }
    if (eskuin) {
        basic.showArrow(ArrowNames.East)
        basic.clearScreen()
        basic.pause(100)
    }
    if (kurba) {
        music.playMelody("C5 C - - - - - - ", 400)
    }
})

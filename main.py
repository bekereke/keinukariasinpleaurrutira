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
    radio.sendValue("kurba", input.rotation(Rotation.Pitch))
    radio.sendNumber(0)
})
input.onButtonPressed(Button.AB, function () {
    radio.sendValue("serial number", control.deviceSerialNumber())
})
input.onButtonPressed(Button.B, function () {
    basic.clearScreen()
    radio.sendValue("kurba", input.rotation(Rotation.Pitch))
    radio.sendNumber(1)
})
radio.onReceivedValue(function (name, value) {
    if (name == "kurba") {
        kurba = value
    }
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    basic.clearScreen()
    radio.sendValue("kurba", 0)
    radio.sendNumber(2)
})
let eskuin = false
let ezker = false
let kurba = 0
radio.setGroup(1)
radio.setTransmitSerialNumber(true)
kurba = false
ezker = false
basic.forever(function () {
    if (ezker) {
        basic.showArrow(ArrowNames.West)
        basic.clearScreen()
        basic.pause(100)
    }
})
basic.forever(function () {
    if (kurba) {
        music.playMelody("C5 C - - - - - - ", 400)
    }
})
basic.forever(function () {
    if (eskuin) {
        basic.showArrow(ArrowNames.East)
        basic.clearScreen()
        basic.pause(100)
    }
})

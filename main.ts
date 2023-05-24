radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 0) {
        ezker = true
    } else if (receivedNumber == 1) {
        eskuin = true
    } else if (receivedNumber == 2) {
        ezker = false
        eskuin = false
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
    radio.sendNumber(0)
})
input.onButtonPressed(Button.B, function () {
    basic.clearScreen()
    radio.sendNumber(1)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    basic.clearScreen()
    radio.sendNumber(2)
})
let eskuin = false
let ezker = false
radio.setGroup(1)
radio.setTransmitSerialNumber(true)
let angelua = 0
ezker = false
eskuin = false
basic.forever(function () {
    if (ezker) {
        basic.showArrow(ArrowNames.West)
        basic.clearScreen()
        basic.pause(100)
    }
})
basic.forever(function () {
    if (eskuin) {
        basic.showArrow(ArrowNames.East)
        basic.clearScreen()
        basic.pause(100)
    }
})
basic.forever(function () {
    if (ezker || eskuin) {
        angelua = Math.abs(input.rotation(Rotation.Pitch))
        music.playMelody("C5 C - - - - - - ", 400)
        if (angelua < 30 && angelua < -30) {
            radio.sendNumber(2)
        }
    }
})

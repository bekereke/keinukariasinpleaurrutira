radio.onReceivedNumber(function (receivedNumber) {
    // EZKERRERA
    // ESKUINERA
    // GELDITU
    // MANILARRA NEURTU
    if (receivedNumber == 0) {
        ezker = true
        eskuin = false
    } else if (receivedNumber == 1) {
        eskuin = true
        ezker = false
    } else if (receivedNumber == 2) {
        ezker = false
        eskuin = false
        neurtu_inklinazioa = false
    } else if (receivedNumber == 3) {
        ezker = false
        eskuin = false
        neurtu_inklinazioa = true
    }
    // MEZUA JASO BADU, MORROIA DA. HASIERAN, ETA GERO, INKLINAZIOA NEURTU BEHAR EZ BALDIN BADU ERE BAI.
    if (!(neurtu_inklinazioa)) {
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
    }
})
input.onButtonPressed(Button.A, function () {
    basic.clearScreen()
    radio.sendNumber(0)
    basic.showLeds(`
        . . . # .
        . . # . .
        . # # . .
        # . # . .
        . . # . .
        `)
})
input.onButtonPressed(Button.B, function () {
    basic.clearScreen()
    radio.sendNumber(1)
    basic.showLeds(`
        . # . . .
        . . # . .
        . . # # .
        . . # . #
        . . # . .
        `)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    basic.clearScreen()
    // KEINUKARIA GELDITU
    radio.sendNumber(2)
    basic.showLeds(`
        . . . . .
        # # # # #
        . . # . .
        . . # . .
        . . # . .
        `)
})
let neurtu_inklinazioa = false
let eskuin = false
let ezker = false
radio.setGroup(1)
radio.setTransmitSerialNumber(true)
let angelua = 0
ezker = false
eskuin = false
neurtu_inklinazioa = false
basic.showLeds(`
    . . . . .
    # # # # #
    . . # . .
    . . # . .
    . . # . .
    `)
basic.forever(function () {
    if (ezker) {
        basic.showArrow(ArrowNames.West)
        basic.clearScreen()
        basic.pause(100)
        // ESKATU MANILARRARI ANGELUA NEURTZEKO
        radio.sendNumber(3)
    }
})
basic.forever(function () {
    if (eskuin) {
        basic.showArrow(ArrowNames.East)
        basic.clearScreen()
        basic.pause(100)
        // ESKATU MANILARRARI ANGELUA NEURTZEKO
        radio.sendNumber(3)
    }
})
basic.forever(function () {
    if (neurtu_inklinazioa) {
        angelua = Math.abs(input.rotation(Rotation.Pitch))
        music.playMelody("C5 C - - - - - - ", 400)
        if (angelua < 30 && angelua < -30) {
            // KEINUKARIA GELDITU
            radio.sendNumber(2)
            basic.showLeds(`
                . . . . .
                # # # # #
                . . # . .
                . . # . .
                . . # . .
                `)
        }
    }
})

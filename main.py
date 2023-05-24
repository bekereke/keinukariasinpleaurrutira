def on_received_number(receivedNumber):
    global ezker, eskuin, neurtu_inklinazioa
    # EZKERRERA
    # ESKUINERA
    # GELDITU
    # MANILARRA NEURTU
    if receivedNumber == 0:
        ezker = True
    elif receivedNumber == 1:
        eskuin = True
    elif receivedNumber == 2:
        ezker = False
        eskuin = False
        neurtu_inklinazioa = False
    elif receivedNumber == 3:
        ezker = False
        eskuin = False
        neurtu_inklinazioa = True
    # MEZUA JASO BADU, MORROIA DA. HASIERAN, ETA GERO, INKLINAZIOA NEURTU BEHAR EZ BALDIN BADU ERE BAI.
    if not (neurtu_inklinazioa):
        basic.show_leds("""
            # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
        """)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    basic.clear_screen()
    radio.send_number(0)
    basic.show_leds("""
        . . . # .
                . . # . .
                . # # . .
                # . # . .
                . . # . .
    """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.clear_screen()
    radio.send_number(1)
    basic.show_leds("""
        . # . . .
                . . # . .
                . . # # .
                . . # . #
                . . # . .
    """)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    basic.clear_screen()
    # KEINUKARIA GELDITU
    radio.send_number(2)
    basic.show_leds("""
        . . . . .
                # # # # #
                . . # . .
                . . # . .
                . . # . .
    """)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

neurtu_inklinazioa = False
eskuin = False
ezker = False
radio.set_group(1)
radio.set_transmit_serial_number(True)
angelua = 0
ezker = False
eskuin = False
neurtu_inklinazioa = False
basic.show_leds("""
    . . . . .
        # # # # #
        . . # . .
        . . # . .
        . . # . .
""")

def on_forever():
    if ezker:
        basic.show_arrow(ArrowNames.WEST)
        basic.clear_screen()
        basic.pause(100)
        # ESKATU MANILARRARI ANGELUA NEURTZEKO
        radio.send_number(3)
basic.forever(on_forever)

def on_forever2():
    if eskuin:
        basic.show_arrow(ArrowNames.EAST)
        basic.clear_screen()
        basic.pause(100)
        # ESKATU MANILARRARI ANGELUA NEURTZEKO
        radio.send_number(3)
basic.forever(on_forever2)

def on_forever3():
    global angelua
    if neurtu_inklinazioa:
        angelua = abs(input.rotation(Rotation.PITCH))
        music.play_melody("C5 C - - - - - - ", 400)
        if angelua < 30 and angelua < -30:
            # KEINUKARIA GELDITU
            radio.send_number(2)
            basic.show_leds("""
                . . . . .
                                # # # # #
                                . . # . .
                                . . # . .
                                . . # . .
            """)
basic.forever(on_forever3)

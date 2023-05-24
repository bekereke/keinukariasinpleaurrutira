def on_received_number(receivedNumber):
    global ezker, eskuin, kurba
    if receivedNumber == 0:
        ezker = True
    elif receivedNumber == 1:
        eskuin = True
    elif receivedNumber == 2:
        ezker = False
        eskuin = False
        kurba = False
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
    radio.send_value("kurba", 1)
    radio.send_number(0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.clear_screen()
    radio.send_value("kurba", 1)
    radio.send_number(1)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_received_value(name, value):
    global kurba
    if name == "kurba" and value == 1:
        kurba = True
    elif name == "kurba" and value == 0:
        kurba = False
radio.on_received_value(on_received_value)

def on_logo_pressed():
    basic.clear_screen()
    radio.send_value("kurba", 0)
    radio.send_number(2)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

eskuin = False
ezker = False
kurba = False
radio.set_group(1)
kurba = False
ezker = False

def on_forever():
    if ezker:
        basic.show_arrow(ArrowNames.WEST)
        basic.clear_screen()
        basic.pause(100)
basic.forever(on_forever)

def on_forever2():
    if kurba:
        music.play_melody("C5 C - - - - - - ", 400)
basic.forever(on_forever2)

def on_forever3():
    if eskuin:
        basic.show_arrow(ArrowNames.EAST)
        basic.clear_screen()
        basic.pause(100)
basic.forever(on_forever3)

def on_button_pressed_a():
    pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_pin_pressed_p1():
    global points
    points += 1
    basic.show_number(points)
    music._play_default_background(music.built_in_playable_melody(Melodies.BA_DING),
        music.PlaybackMode.IN_BACKGROUND)
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

points = 0
basic.show_number(0)
points = 0

def on_forever():
    global points
    if points == 10:
        points = 0
        basic.show_string("YouWin!")
        music._play_default_background(music.built_in_playable_melody(Melodies.FUNK),
            music.PlaybackMode.UNTIL_DONE)
        basic.show_number(0)
basic.forever(on_forever)

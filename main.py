def on_button_pressed_a():
    for index in range(10):
        music.play(music.string_playable("C E F E F E F G ", 120),
            music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    basic.show_leds("""
        # . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
   
    basic.show_leds("""
        . . . . .
        . . . . .
        # . . . .
        . . . . .
        . . . . .
        """)
  
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        # . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . # . . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . # . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . # .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . #
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . #
        . . . . .
        . . . . .
        """)
    basic.clear_screen()
basic.forever(on_forever)

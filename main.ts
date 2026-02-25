input.onButtonPressed(Button.A, function () {
	
})
input.onPinPressed(TouchPin.P1, function () {
    points += 1
    music._playDefaultBackground(music.builtInPlayableMelody(Melodies.BaDing), music.PlaybackMode.InBackground)
    basic.showNumber(points)
})
let points = 0
basic.showNumber(0)
points = 0
basic.forever(function () {
    if (points == 10) {
        points = 0
        basic.pause(1000)
        music.setVolume(255)
        music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Funk), music.PlaybackMode.InBackground)
        basic.showString("YouWin!")
        basic.showNumber(0)
        music.setVolume(128)
    }
})

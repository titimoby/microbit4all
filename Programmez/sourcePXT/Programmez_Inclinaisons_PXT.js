let inclinaisonY = 0
let inclinaisonX = 0
while (true) {
    inclinaisonX = input.acceleration(Dimension.X)
    inclinaisonY = input.acceleration(Dimension.Y)
    if (inclinaisonX > 550) {
        basic.showLeds(`
            . . # . .
            . . . # .
            # # # # #
            . . . # .
            . . # . .
            `)
    } else {
        if (inclinaisonX < -550) {
            basic.showLeds(`
                . . # . .
                . # . . .
                # # # # #
                . # . . .
                . . # . .
                `)
        } else {
            if (inclinaisonY > 550) {
                basic.showLeds(`
                    . . # . .
                    . # # # .
                    # . # . #
                    . . # . .
                    . . # . .
                    `)
            } else {
                if (inclinaisonY < -550) {
                    basic.showLeds(`
                        . . # . .
                        . . # . .
                        # . # . #
                        . # # # .
                        . . # . .
                        `)
                } else {
                    basic.showLeds(`
                        . . . . .
                        . . . . .
                        . # # # .
                        . . . . .
                        . . . . .
                        `)
                }
            }
        }
    }
}

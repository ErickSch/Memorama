"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
taps = 0
writer = Turtle()
tracer(False)
animales = [
    "🐶",  # Dog
    "🐱",  # Cat
    "🐭",  # Mouse
    "🐹",  # Hamster
    "🐰",  # Rabbit
    "🦊",  # Fox
    "🐻",  # Bear
    "🐼",  # Panda
    "🐨",  # Koala
    "🐯",  # Tiger
    "🦁",  # Lion
    "🐮",  # Cow
    "🐷",  # Pig
    "🐸",  # Frog
    "🐵",  # Monkey
    "🦄",  # Unicorn
    "🐔",  # Chicken
    "🐧",  # Penguin
    "🐦",  # Bird
    "🐤",  # Baby Chick
    "🦉",  # Owl
    "🦆",  # Duck
    "🐥",  # Front-Facing Baby Chick
    "🦜",  # Parrot
    "🦢",  # Swan
    "🕊️",  # Dove
    "🦚",  # Peacock
    "🦃",  # Turkey
    "🐍",  # Snake
    "🐢",  # Turtle
    "🦎",  # Lizard
    "🐊",   # Crocodile
    "🐶",  # Dog
    "🐱",  # Cat
    "🐭",  # Mouse
    "🐹",  # Hamster
    "🐰",  # Rabbit
    "🦊",  # Fox
    "🐻",  # Bear
    "🐼",  # Panda
    "🐨",  # Koala
    "🐯",  # Tiger
    "🦁",  # Lion
    "🐮",  # Cow
    "🐷",  # Pig
    "🐸",  # Frog
    "🐵",  # Monkey
    "🦄",  # Unicorn
    "🐔",  # Chicken
    "🐧",  # Penguin
    "🐦",  # Bird
    "🐤",  # Baby Chick
    "🦉",  # Owl
    "🦆",  # Duck
    "🐥",  # Front-Facing Baby Chick
    "🦜",  # Parrot
    "🦢",  # Swan
    "🕊️",  # Dove
    "🦚",  # Peacock
    "🦃",  # Turkey
    "🐍",  # Snake
    "🐢",  # Turtle
    "🦎",  # Lizard
    "🐊"   # Crocodile
]



def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    # color('black', 'white')
    color("navyblue", "orange")
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global taps
    taps += 1
    spot = index(x, y)
    mark = state['mark']

    # Mark is None -> es la primera carta que se destapa
    # mark == spot -> estoy dando click obre la misma carta
    # tiles[mark] != tiles[spot] -> son diferentes las cartas 1 != 1
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else: # Se forma un par
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        if hide.count(False) > 63:
            print("Ganaste!!")
            writer.up()
            # Se mueve a la posición indicada
            writer.goto(-150,-250)
            # Le asigna color al lápiz
            writer.color('black')
            # Escribe lo que se indica (Texto, align=lado al que estará pegado, font=Tipo de letra)
            writer.write('Ganaste un auto!!, Felicidades', align='left',font=('Arial',14,'normal'))


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()
    # Dibuja la memoria de abajo hacia arriba, de izquierda a derecha
    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    # Saca el contenido de state, ya que tenemos destapada una carta
    mark = state['mark']

    # Si si se tiene una carta detapada, 
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        # Muestra el contenido de la carta
        write(animales[mark], font=('Arial', 12, 'normal'))


    # Todo lo que esta en el buffer de dibujo se actualiza en la ventana
    update()
    # 
    ontimer(draw, 100)


def info_alumnos():
    # Esconde el triangulo de turtle
    writer.hideturtle()
    # Levanta el lápiz
    writer.up()
    # Se mueve a la posición indicada
    writer.goto(-100,190)
    # Le asigna color al lápiz
    writer.color('blue')
    # Escribe lo que se indica (Texto, align=lado al que estará pegado, font=Tipo de letra)
    writer.write('Erick Schiller Echavarria A01740804', align='left',font=('Arial',10,'normal'))
    # Se dirige a la posición indicada
    writer.goto(-100,170)
    # Escribe lo que se indica (Texto, align=lado al que estará pegado, font=Tipo de letra)
    writer.write('Emilio Rizo de la Mora A01721612', align='left',font=('Arial',10,'normal'))
    

info_alumnos()
# shuffle(tiles)
setup(420, 600, 370, 0)
bgcolor('lightblue')
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
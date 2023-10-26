

from random import *
from turtle import *

from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
taps = 0


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', '#F0FFFF')
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
    spot = index(x, y)
    mark = state['mark']

    if spot >= 0 and spot <= 63:
        taps += 1

        # Mark is None -> es la primera carta que se destapa
        # mark == spot -> estoy dando click obre la misma carta
        # tiles[mark] != tiles[spot] -> son diferentes las cartas 1 != 1
        if mark is None or mark == spot or tiles[mark] != tiles[spot]:
            state['mark'] = spot
        else: # Se forma un par
            hide[spot] = False
            hide[mark] = False
            state['mark'] = None


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
        write(tiles[mark], font=('Arial', 30, 'normal'))

    up()
    goto(100, 225)
    write('taps:', align='left',font=('Arial',10,'normal'))
    goto(130, 225)
    write(taps)

    if hide.count(True) == 0:
        onscreenclick(None)

    # Todo lo que esta en el buffer de dibujo se actualiza en la ventana
    update()
    # 
    ontimer(draw, 100)

writer = Turtle()
tracer(False)
def info_alumnos():
    # Esconde el triangulo de turtle
    writer.hideturtle()
    # Levanta el lápiz
    writer.up()
    writer.goto(-80, 270)
    writer.color('blue')
    writer.write('Memorama', font=('Arial', 20, 'normal'))
    # Se mueve a la posición indicada
    writer.goto(-200,235)
    # Le asigna color al lápiz
    writer.color('black')
    # Escribe lo que se indica (Texto, align=lado al que estará pegado, font=Tipo de letra)
    writer.write('Erick Schiller Echavarria A01740804', align='left',font=('Arial',10,'normal'))
    # Se dirige a la posición indicada
    writer.goto(-200,215)
    # Escribe lo que se indica (Texto, align=lado al que estará pegado, font=Tipo de letra)
    writer.write('Eugenia Uresti Arriaga A01284839', align='left',font=('Arial',10,'normal'))
    

title('Erick Schiller y Eugenia Uresti')
bgcolor('#B0E0E6')
info_alumnos()
#shuffle(tiles)
setup(420, 620, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
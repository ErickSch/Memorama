# Actividad 3: Memorama
## Autores:
- Eugenia Uresti Arriaga A01284839.
- Erick Schiller Echavarría, A01740804.

## Modificaciones

### Taps y color de fondo
- Cuenta y despliega el numero de taps y cambia el color de fondo de la memorama 
- Autor: Eugenia Uresti.
- Código:

```python
taps = 0
def square(x, y):
    color('black', '#F0FFFF')

def tap(x, y):
    global taps

    if spot >= 0 and spot <= 63:
        taps += 1

def draw():
    up()
    goto(100, 225)
    write('taps:', align='left',font=('Arial',10,'normal'))
    goto(130, 225)
    write(taps)

    if hide.count(True) == 0:
        onscreenclick(None)

bgcolor('#B0E0E6')
```

### Nombres de los integrantes del equipo
- Despliega los nombres de los integrantes en una parte fuera de la memorama y cambia el nombre de la ventana por los nombres de los integrantes
- Autor: Eugenia Uresti.
- Código:

```python
writer = Turtle()
tracer(False)
def info_alumnos():
    writer.hideturtle()
    writer.up()
    writer.goto(-80, 270)
    writer.color('blue')
    writer.write('Memorama', font=('Arial', 20, 'normal'))
    writer.goto(-200,235)
    writer.color('black')
    writer.write('Erick Schiller Echavarria A01740804', align='left',font=('Arial',10,'normal'))
    writer.goto(-200,215)
    writer.write('Eugenia Uresti Arriaga A01284839', align='left',font=('Arial',10,'normal'))

title('Erick Schiller y Eugenia Uresti')
info_alumnos()
```

### Detectar si todos los cuadros se han destapado
- Detecta cuando se completó el memorama y despliega un mensaje.
- Autor: Erick Schiller.
- Código:

```python
        # Si el numero de cuadros escondidos es igual o mayor al total, desplegar el mensaje
        if hide.count(False) > 63:
            # Levantar el lápiz
            writer.up()
            # Se mueve a la posición indicada
            writer.goto(-150,-250)
            # Le asigna color al lápiz
            writer.color('black')
            # Escribe lo que se indica (Texto, align=lado al que estará pegado, font=Tipo de letra)
            writer.write('Ganaste un auto!!, Felicidades', align='left',font=('Arial',14,'normal'))
```

### Agregar emojis al texto de los cuadrados del memorama
- Muestra un emoji diferente en cada cuadro del memorama al voltearlos.
- Autor: Erick Schiller
- Código:

```python
# Lista con el Unicode para los emojis de los animales
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

    ...

    # Al voltear el recuadro mostrar el emoji correspondiente a ese índice
    write(animales[mark], font=('Arial', 12, 'normal'))
]
```

## GIF del funcionamiento:
![GIF Ejemplo](GIF_Memorama.gif)

## Videos
- Eugenia Uresti: https://drive.google.com/file/d/1ySRabsxG4LuKTnGe4KhDwn2OAscq8jhX/view?usp=sharing
- Erick Schiller: https://drive.google.com/file/d/1RHwUdSL4p7RVdY_dmH2PfqKegJVO_xNx/view?usp=sharing

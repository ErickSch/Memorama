# Actividad 3: Memorama
## Autores:
- Eugenia Uresti Arriaga A01284839.
- Erick Schiller Echavarría, A01740804.

## Modificaciones

### Título...
- Descripción...
- Autor: Eugenia Uresti.
- Código:

```python
    # Agregar el código
```

### Título...
- Descripción...
- Autor: Eugenia Uresti.
- Código:

```python
    # Agregar el código
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
import turtle
turtle.speed(0)


def getfile():
    try:
        filename = input('Enter name of file:\n')
        if filename == 'quit':
            return 'quit'
        file = open(filename)
    except FileNotFoundError:
        print('File does not exist.')
    return file


def executefile(f):
    for line in f:
        y = line.split(',')
        shapename = y[0].strip().lower()
        y.pop(0)
        drawshape(shapename, y)
    return None


def drawshape(shapename, args):
    try:
        if shapename == 'circle':
            if len(args) != 4:
                raise IndexError('Incorrect number of arguments.\n')
            drawcircle(*args)
        elif shapename == 'rect':
            if len(args) != 5:
                raise IndexError('Incorrect number of arguments.\n')
            drawrect(*args)
        elif shapename == 'line':
            if len(args) != 5:
                raise IndexError('Incorrect number of arguments.\n')
            drawline(*args)
        else:
            print('invalid command')
    except IndexError as excpt:
        print(excpt)
        print(args)
    except ValueError:
        print('Could not convert an argument to int')
        print(args)
    return None


def drawcircle(x, y, radius, color):
    try:
        turtle.penup()
        turtle.setheading(0)
        turtle.goto((int(x)), int(y) - int(radius))
        turtle.pen(fillcolor=color.strip().lower(), pencolor=color.strip().lower())
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(int(radius))
        turtle.end_fill()
        turtle.penup()
    except ValueError:
        raise ValueError
    return None


def drawrect(x, y, width, height, color):
    try:
        turtle.penup()
        turtle.goto(int(x), int(y))
        turtle.pen(fillcolor=color.strip().lower(), pencolor=color.strip().lower())
        turtle.pendown()
        turtle.begin_fill()
        turtle.setheading(0)
        turtle.forward(int(width))
        turtle.setheading(270)
        turtle.forward(int(height))
        turtle.setheading(180)
        turtle.forward(int(width))
        turtle.setheading(90)
        turtle.forward(int(height))
        turtle.end_fill()
        turtle.penup()
    except ValueError:
        raise ValueError
    return None


def drawline(x, y, heading, length, color):
    try:
        turtle.penup()
        turtle.goto(int(x), int(y))
        turtle.pen(pencolor=color.strip().lower())
        turtle.pendown()
        turtle.setheading(float(heading))
        turtle.forward(float(length))
        turtle.penup()
    except ValueError:
        raise ValueError
    return None


execute = True
while execute is True:
    f = getfile()
    if f == 'quit':
        execute = False
        break
    executefile(f)
    f.close()
    turtle.clear()
    




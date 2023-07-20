from turtle import Turtle

print(
"""\
TURTLE GAME

Comandos:
    move X Y
    move steps
    turn angle (default 90)
    draw shape size (line | circle)
    color line body (trocar cores da tartaruga)
    clear (limpar a tela)
    reset (reseta o programa)
    stop | exit | quit
"""
)

turtle = Turtle()
turtle.shape("turtle")
turtle.speed(3)
turtle.color('red', 'blue')
turtle.shapesize(3,3)
turtle.penup()


while True:
    command: list[str] = input('🐢>').strip().split()
        
    match command:
    
        case ['color', line, body]:
            turtle.color(line, body)
        
        case ['move', *points]:
            match points:
                case [x,y]:
                    turtle.goto(float(x), float(y))
                case [steps]:
                    turtle.forward(float(steps))
                
        case ['turn', *options]:
            match options:
                case [angle]:
                    turtle.right(float(angle))
                case _:
                    turtle.right(90)
                    
        case ['draw', shape, size]:
            turtle.pendown()
            match shape:
                case 'circle':
                    turtle.circle(float(size))
                case 'line':
                    turtle.forward(float(size))
            turtle.penup()
                    
        case ['write', text]:
            turtle.write(' '.join(text), None, 'center', '12pt')
            
        case ['clear']:
            turtle.clear()
            
        case ['reset']:
            turtle.reset()
            turtle.shape("turtle")
            turtle.speed(3)
            turtle.color('red', 'blue')
            turtle.shapesize(3,3)
            turtle.penup()
            
        case ['exit'|'stop'|'quit']:
            break
        
        case _:
            print('COMANDO INVALIDO!')
        
        
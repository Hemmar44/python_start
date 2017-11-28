import turtle

t=turtle.Pen()

t.reset()

def kwadrat(rozmiar):
    
    for i in range(0,4):
        t.forward(rozmiar)
        t.left(90)

t.reset()
kwadrat(20)
kwadrat(40)
kwadrat(80)
kwadrat(160)
kwadrat(320)

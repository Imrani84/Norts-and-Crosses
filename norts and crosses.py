from ursina import *
app = Ursina()


Board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

player = "X"
gameover = False
status = Text(text = "Player X's turn", color = color.red, origin = (0,0), position = (0,0.4), scale = 5)
champion = None
spaces = 9

#winner checker
def combowin(Board):
  global champion,b1,b2,b3,b4,b5,b6,b7,b8,b9
  if Board[0] == Board[1] == Board[2] and Board[0] != "-":         #first row
    champion = Board[0]
    for i in (b1,b2,b3):
        i.color = color.gold
  elif Board[3] == Board[4] == Board[5] and Board[3] != "-":       #second row
    champion = Board[3]
    for i in (b4,b5,b6):
        i.color = color.gold
  elif Board[6] == Board[7] == Board[8] and Board[6] != "-":       #third row
    champion = Board[6]
    for i in (b7,b8,b9):
        i.color = color.gold
  elif Board[0] == Board[3] == Board[6] and Board[0] != "-":       #first collumn
    champion = Board[0]
    for i in (b1,b4,b7):
        i.color = color.gold
  elif Board[1] == Board[4] == Board[7] and Board[1] != "-":       #second collumn
    champion = Board[1]
    for i in (b2,b5,b8):
        i.color = color.gold
  elif Board[2] == Board[5] == Board[8] and Board[2] != "-":       #third collumn
    champion = Board[2]
    for i in (b3,b6,b9):
        i.color = color.gold
  elif Board[0] == Board[4] == Board[8] and Board[0] != "-":       #diagonal \
    champion = Board[0]
    for i in (b1,b5,b9):
        i.color = color.gold
  elif Board[2] == Board[4] == Board[6] and Board[2] != "-":       #diagonal /
    champion = Board[2]
    for i in (b3,b5,b7):
        i.color = color.gold


def again():
  global Board,gameover,champion,player,spaces
  for i in range(len(Board)):
    Board[i] = "-"
  for j in (b1,b2,b3,b4,b5,b6,b7,b8,b9):
    destroy(j)
  createbuttons()
  spaces = 9
  gameover = False
  champion = None
  againbutton.enabled = False
  status.text = "Player X's turn"
  player = "X"
  status.color = color.red


againbutton = Button(text = "PLAY AGAIN", text_color = color.black, color = color.green, scale = (0.3,0.1), position = (0,-0.4), collider = "box", enabled = False, on_click = again)




#gameplay
def select(button, number):
  global player, status, gameover, spaces
  if gameover == True or Board[number] != "-":
    return
  Board[number] = player
  button.text = player
  if player == "X":
    button.color = color.red
    status.text = "Player O's turn"
    status.color = color.blue
    player = "O"
  elif player == "O":
    button.color = color.blue
    status.text = "Player X's turn"
    status.color = color.red
    player = "X"

  combowin(Board)
  spaces -= 1


  if champion != None:
    status.text = "PLAYER " + champion + " WINS"
    status.color = color.gold
    gameover = True
    againbutton.enabled = True
  elif spaces == 0:
    status.text = "IT'S A TIE"
    status.color = color.black
    gameover = True
    againbutton.enabled = True




def createbuttons():
  global b1,b2,b3,b4,b5,b6,b7,b8,b9
  #top row
  b1 = Button(text = "-", text_color = color.black, text_size = 4, color = color.white, scale = 0.2, position = (-0.21,0.21), parent = camera.ui, collider = "box")
  b1.on_click = Func(select, b1, 0)
  b2 = Button(text = "-", text_color = color.black, text_size = 4, color = color.white, scale = 0.2, position = (0,0.21), parent = camera.ui, collider = "box")
  b2.on_click = Func(select, b2, 1)
  b3 = Button(text = "-", text_color = color.black, text_size = 4, color = color.white, scale = 0.2, position = (0.21,0.21), parent = camera.ui, collider = "box")
  b3.on_click = Func(select, b3, 2)
  #middle row
  b4 = Button(text = "-", text_color = color.black, text_size = 4, color = color.white, scale = 0.2, position = (-0.21,0.0), parent = camera.ui, collider = "box")
  b4.on_click = Func(select, b4, 3)
  b5 = Button(text = "-", text_color = color.black, text_size = 4, color = color.white, scale = 0.2, position = (0,0), parent = camera.ui, collider = "box")
  b5.on_click = Func(select, b5, 4)
  b6 = Button(text = "-", text_color = color.black, text_size = 4, color = color.white, scale = 0.2, position = (0.21,0), parent = camera.ui, collider = "box")
  b6.on_click = Func(select, b6, 5)
  #bottom row
  b7 = Button(text = "-", text_color = color.black, text_size = 4, color = color.white, scale = 0.2, position = (-0.21,-0.21), parent = camera.ui, collider = "box")
  b7.on_click = Func(select, b7, 6)
  b8 = Button(text = "-", text_color = color.black, text_size = 4, color = color.white, scale = 0.2, position = (0,-0.21), parent = camera.ui, collider = "box")
  b8.on_click = Func(select, b8, 7)
  b9 = Button(text = "-", text_color = color.black, text_size = 4, color = color.white, scale = 0.2, position = (0.21,-0.21), parent = camera.ui, collider = "box")
  b9.on_click = Func(select, b9, 8)

createbuttons()

app.run()
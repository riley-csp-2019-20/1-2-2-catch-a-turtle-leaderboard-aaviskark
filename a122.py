# a122_catch_a_turtle.py

#-----import statements-----
import turtle as trtl 
import random 
import leaderboard as lb

#-----game configuration----
shape = "turtle"
color= ["darkorange", "white","green", "red", "blue", "yellow", "black", "brown", "purple", "indigo", "pink", "silver"]
    #list of the random color choices
size= 4
score=0

font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#leaderboard variables
leaderboard_file_name= "a122_leaderboard.txt"
leader_names_list= []
leader_scores_list= []
player_name= input("Please enter your name")


#-----initialize turtle-----
turt = trtl.Turtle(shape = shape)
turt.color(random.choice(color))
turt.shapesize(size)
turt.speed(8)

scoretrl= trtl.Turtle()
scoretrl.ht()
scoretrl.up()
scoretrl.goto(-370,270)
font= ("Arial", 30, "bold")
scoretrl.pencolor("white")
scoretrl.write(score, font= font)

counter =  trtl.Turtle()
counter.pencolor("white")
counter.speed(0)
counter.up()
counter.goto(350,300)
counter.ht()
#-----game functions--------
def turtle_click(x,y):
    print("bruh")
    change_position()
    add_score()
    scoretrl.clear()
    scoretrl.write(score, font= font)
    change_color()
    
def change_position():
    turt.up()
    turt.ht()
    new_xpos= random.randint(-400,400)
    new_ypos= random.randint(-300,300)
    turt.goto(new_xpos, new_ypos)
    turt.st()

def add_score():
    global score
    score+=1
    print(score)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    game_end()
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 


def change_color():               #function for the random color change
  turt.color(random.choice(color))

def game_end():
    turt.ht()
    wn.bgcolor("gray")
    turt.goto(-1000,1000)
    counter.goto(0,0)

# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global turt

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, turt, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, turt, score)


    
#-----events----------------
turt.onclick(turtle_click)
wn= trtl.Screen() 
wn.ontimer(countdown, counter_interval) 
wn.bgcolor("black") #changes bg color
wn.mainloop()
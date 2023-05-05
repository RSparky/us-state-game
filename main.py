import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
# turtle.screensize(800, 800)

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
GAMESTART= True
guess = 0 
guessed_state=[]

state_data = pandas.read_csv("50_states.csv")   #read date from csv file
state_list = state_data.state.to_list()         # making a list of the states

while GAMESTART:
    answer_input = screen.textinput(title=f"{guess}/50 states correct", prompt="What's another state name")
    answer_input = answer_input.lower().title()
    if answer_input =="Exit":
        missing_state =[state for state in state_list if state not in guessed_state]
        # for state in state_list:
        #     if state not in guessed_state:
        #         missing_state.append(state)
        new_data=pandas.DataFrame(missing_state)
        new_data.to_csv("States_to_learn.csv")
        break
    if answer_input in state_list:
        guess+=1
        guessed_state.append(answer_input)
        # write correct guesses in the map
        state_row = state_data[state_data.state == answer_input]# this give the row of the said state
        turtle.penup()
        turtle.goto(int(state_row.x), int(state_row.y))
        turtle.pendown()
        turtle.write(answer_input)
        turtle.penup()
        turtle.goto(0,0)


# states_to_learn = list(set(state_list) - set(guessed_state))
# df=pandas.DataFrame(states_to_learn)
# df.to_csv("States_to_learn.csv")

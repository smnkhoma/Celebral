
# import modules and packages
import pandas as pd
import time
from bokeh.io import show
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.transform import factor_cmap
from celebral_classes import *
from rich import print


# Thus function creates the mathematical problems
def generate_problems():
    my_problems = []  # This list holds the 9 mathermatical problems generated in current round
    for i in range(3):
        my_problems.append(myMultiplicationProblems())
        my_problems.append(myAdditionProblems())
        my_problems.append(mySubtractionProblems())
    return my_problems

# function for getting and keeping responses from player
def solve_problem(problem, player_response):
    if player_response == "":
        raise exitGame("You did not enter anything. I assume you are done for the day. Thanks for Playing Celebral!")
    problem.players_response = player_response
    try:
        the_response = int(problem.players_response)
    except ValueError as e:
        print(f"A ValueError occurred: {e}. Anyway, lets proceed.")
    except:
        print("Well, err, lets just proceed")
    else:
        if the_response == problem.correctAnswer:
            problem.isCorrect = "Correct answers"
    return problem

# packages data on time taken to give responses as well as correctness of responses into a dataframe
def create_dataframe(my_problems):
    x = list(range(1,len(my_problems)+1))
    y=[]
    z=[]

    for i in my_problems:
        y.append(i.time_to_response)
        z.append(i.isCorrect)

    return pd.DataFrame({'x': x, 'y': y, 'z': z})

def plot_data(df): # function for plotting graphs
    source = ColumnDataSource(data=dict(x=df['x'].astype(str), y=df['y'], z=df['z']))
    my_pallete = ["blue", "red"]
    p = figure(x_range=df['x'].astype(str), height=350, toolbar_location=None, title="Celebral! The game: Time taken per question",
               x_axis_label='Problem', y_axis_label='Seconds')
    p.vbar(x='x', top='y', width=0.5, source=source, legend_field='z', line_color='white',
           fill_color=factor_cmap('z', palette=my_pallete, factors=list(set(df['z']))))

    p.xgrid.grid_line_color = None
    p.legend.orientation = "horizontal"
    p.legend.location = "top_center"
    show(p)

def play_game():
    my_problems = generate_problems()

    for problem in my_problems:
        #console.print("Next question:", style="bold red")
        time_0 = time.time()
        player_response = input(f"Type the answer: {problem.num1} {problem.operationSign} {problem.num2} = ")
        problem.time_to_response = time.time() - time_0
        solve_problem(problem, player_response)

    df = create_dataframe(my_problems)
    plot_data(df)
from flask import Flask, url_for, render_template, request 
from markupsafe import Markup

import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)


@app.route("/")
def render_main():
    return render_template('home.html')
    
@app.route("/graphmath")
def render_main_graph_math():
    states = get_state_options()
    state = ""
    if 'state' in request.args:
        state = request.args['state']
    else: 
        state = 'AL'
    mathscore = get_math_scores(state)
    print(state)
    place = "Verbal Scores in " + state + ", from 2005 to 2015."
    return render_template('graphmath.html', graph_math_points = mathscore,  state_options=states, title=place)

@app.route("/graphverbal")
def render_main_graph_verbal():
    states = get_state_options()
    state = ""
    if 'state' in request.args:
        state = request.args['state']
    else: 
        state = 'AL'
    verbalscore = get_verbal_scores(state)
    print(state)
    place = "Verbal Scores in " + state + ", from 2005 to 2015."
    return render_template('graphverbal.html', graph_verbal_points = verbalscore, state_options=states, title=place)

@app.route("/mathscorebystate")
def render_main_mathscorebystates():
    states = get_state_options()
    state = ""
    if 'state' in request.args:
        state = request.args['state']
    else: 
        state = 'AL'
    print(state)    
    averagescore = get_avg_math_score(state)
    line = "The average math score in " + state + ", is " + str(averagescore) + " from 2005 to 2015."
    return render_template('mathscorebystate.html', title=line, state_options=states)        
    
def get_state_options():
    with open('school_scores.json') as scores_data:
        state = json.load(scores_data)
    states=[]
    for c in state:
        if c["State"]["Code"] not in states:
            states.append(c["State"]["Code"])
    print(states)        
    options=""
    for s in states:
        options += Markup("<option value=\"" + s + "\">" + s + "</option>") #Use Markup so <, >, " are not escaped lt, gt, etc.
    return options

def get_math_scores(state):
    with open('school_scores.json') as scores_data:
        sat_scores = json.load(scores_data)
    mathscore={}
    for m in sat_scores:      
        if m['State']['Code']== state:
            mathscore[str(m['Year'])] = m['Total']['Math']
    print(mathscore)
    graph_math_points= ""
    for key, value in mathscore.items():
        graph_math_points= graph_math_points + Markup('{ x: ' + str(key) + ', y: ' + str(value) + ' },')        
    return graph_math_points 
    
def get_verbal_scores(state):
    with open('school_scores.json') as scores_data:
        sat_scores = json.load(scores_data)
    verbalscore={}
    for v in sat_scores:      
        if v['State']['Code']== state:
            verbalscore[v['Year']] = v['Total']['Verbal']
    print(verbalscore)  
    graph_verbal_points= ""
    for key, value in verbalscore.items():
        graph_verbal_points = graph_verbal_points + Markup('{ x: ' + str(key) + ', y: ' + str(value) + ' },')
    return graph_verbal_points

def get_avg_math_score(state):
    with open('school_scores.json') as scores_data:
        sat_scores = json.load(scores_data)
    mathavgscore = 0
    for m in sat_scores:      
        if m['State']['Code']== state:
            mathavgscore = mathavgscore + m['Total']['Math']
    mathavgscore = mathavgscore /len(sat_scores)    
    print(mathavgscore)
    return mathavgscore   
    
"""numbers = [40, 58, 20, 19, 33, 70]
avg = 0
for num in numbers:
    avg = avg + num
avg = avg / len(numbers)"""



if __name__=="__main__":
    app.run(debug=True)

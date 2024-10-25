from flask import Flask, url_for, render_template, request 
from markupsafe import Markup

import os
import json
from datetime import datetime

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')
    
@app.route("/graphmath")
def render_main_graph_math():
    states = get_state_options()
    state = request.args.get('state')
    mathscore = get_math_scores(state)
    return render_template('graphmath.html', graph_math_points = mathscore,  state_options=states)

@app.route("/graphverbal")
def render_main_graph_verbal():
    states = get_state_options()
    state = request.args.get('state')
    verbalscore = get_verbal_scores(state)
    place = "Verbal Scores in " + state + ", from 2005 to 2015."
    return render_template('graphverbal.html', graph_verbal_points = verbalscore, state_options=states, title=place)    
    
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
    

if __name__=="__main__":
    app.run(debug=True)

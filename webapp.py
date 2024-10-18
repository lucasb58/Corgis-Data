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
    mathscore = get_math_scores()
    return render_template('graphmath.html', graph_math_points = mathscore)
    
    
@app.route("/graphverbal")
def render_main_graph_reading():
    return render_template('graphverbal.html')
    
def get_math_scores():
    with open('school_scores.json') as scores_data:
        sat_scores = json.load(scores_data)
    mathscore={}
    for m in sat_scores:      
        if m['State']['Code']== 'CA':
            mathscore[m['Year']] = m['Total']['Math']
    print(mathscore)
    graph_math_points= ""
    for key, value in mathscore.items():
        graph_math_points= graph_math_points + Markup('{ x: ' + str(key) + ', y: ' + str(value) + ' },')
        
    return graph_math_points 
    
def get_math_scores():
    with open('school_scores.json') as scores_data:
        sat_scores = json.load(scores_data)
    verbalscore={}
    for v in sat_scores:      
        if v['State']['Code']== 'CA':
            verbalscore[v['Year']] = v['Total']['Math']
    print(verbalscore)
    graph_verbal_points= ""
    for key, value in verbalscore.items():
        graph_verbal_points = graph_verbal_points + Markup('{ x: ' + str(key) + ', y: ' + str(value) + ' },')
        
    return graph_verbal_points  
    

if __name__=="__main__":
    app.run(debug=True)

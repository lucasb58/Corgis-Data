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
    return render_template('graphmath.html')
    
@app.route("/graphverbal")
def render_main_graph_reading():
    return render_template('graphverbal.html')
    
def get_sat_math_scores ():   
    with open('school_scores(1).json') as sat_scores_data:
        math_scores = json.load(sat_scores_data)
    year = {}
    sat_math_score = {}
    
    retrn sat_math_score
    
    
    for key in data:
        if s[“Year”] == year and s[“Population”] > pop:
            pop = s[“Population”]
            state = s[“State”]
    return render_template('graphmath.html', state = state)
    
def graph_math_points 
        graph_sat_math_points= ""

    

if __name__=="__main__":
    app.run(debug=True)

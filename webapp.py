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
    
def get_math_scores():
	with open('school_scores(1).json') as scores_data:
    	sat_scores = json.load(scores_data)
		for data in scores_data:
 			if data['Year'] == 2005:       
 				if data['State'][]== CA:
	print(data[mathscore])       
        
    

if __name__=="__main__":
    app.run(debug=True)

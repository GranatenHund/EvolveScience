"""
Title: EvolveScience

Description: EvolveScience is a website that contains information regarding cosmic objects such as active galaxies, black holes, stars, planets, asteroids, and their descriptions and examples within.

Programmers:

-Jewel Evangemin Velasquez
-Rhea Angel Antoque
-Ericka Bobarez
-Mike Laurence Luceriaga
-Vincent Santaygillo
-John Kim Alcantara

Date Submitted: October 20, 2022
"""


from flask import Flask, redirect, url_for, request, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/galaxies')
def galaxies():
    return render_template('galaxies.html') 

@app.route('/blackhole')
def blackhole():
    return render_template('blackhole.html')     

@app.route('/stars')
def stars():
    return render_template('stars.html') 

@app.route('/planets')
def planets():
    return render_template('planets.html')   

@app.route('/asteroids')
def asteroids():
    return render_template('asteroids.html')       

if __name__ == "__main__":
    app.run(debug = True)
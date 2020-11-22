from flask import Flask, render_template, request, jsonify
from searchMovie import searchByCategory, searchByYear, searchByWinner, searchByName, data
from imdbURL import giveURL
import json

app = Flask(__name__)



    
@app.route('/imbdbURL', methods=['GET', 'POST'])
# have java script on page call this endpoint to get imdb information
def imdb():
    print("getting url")
    if request.method == "GET":
        mname=request.args['mname']
        return giveURL(mname)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "GET":
        return render_template('home.html')
    elif request.method =="POST":
        
        category=False
        year=False
        winner=False
        name=False
        
        if not request.form['mname'] == "":
            name=str(request.form['mname'])
        if not request.form['category'] == "":
            category=str(request.form['category'])
        if not request.form['year'] == "":
            year=int(request.form['year'])
        if not request.form['winner'] == "":
            winner=True
            
        if name :
            arr=searchByName(name, data)
        elif category and year and winner:
            arr=searchByWinner(winner, searchByYear(year, searchByCategory(category, data)))
        elif category and winner:
            arr=searchByWinner(winner, searchByCategory(category, data))
        elif category and year:
            arr=searchByYear(year, searchByCategory(category, data)) 
        elif year and winner:
            arr=searchByWinner(winner, searchByYear(year, data)) 
        elif category:
            print(category)
            arr=searchByCategory(category, data)
        elif year:
            arr=searchByYear(year, data)
        else:
            return render_template('home.html')
            
            
        return render_template('display.html', movies=arr)
        #return render_template('home.html', selection=request.form['rad'])
        
@app.route('/search', methods=['GET'])
# how to test: type 'http://127.0.0.1:5000/search?category=direction&winner=True&year=1987' into url
def search():
    category=False
    year=False
    winner=False
    name=False
    if 'category' in request.args:
        category = str(request.args["category"])
    if 'year' in request.args:
        year = int(request.args["year"])
    if 'winner' in request.args:
        winner = bool(request.args["winner"])
    if 'name' in request.args:
        name = str(request.args["name"])
    
    if name :
        return jsonify(searchByName(name, data))
    elif category and year and winner:
        return jsonify( searchByWinner(winner, searchByYear(year, searchByCategory(category, data))) )
    elif category and winner:
        return jsonify( searchByWinner(winner, searchByCategory(category, data)) )
    elif category and year:
        return jsonify( searchByYear(year, searchByCategory(category, data)) )
    elif year and winner:
        return jsonify( searchByWinner(winner, searchByYear(year, data)) )
    elif category:
        return jsonify(searchByCategory(category, data))
    elif year:
        return jsonify(searchByYear(year, data))
    
        
# endpoint for returning collection reasource
@app.route('/movies/categories/bestpicture/1997', methods=['GET'])
def getColletion():
    year = 1997
    category = "BEST PICTURE"
    # search function goes here
    return jsonify( searchByCategory(category, searchByYear(year, data)) )

# endpoint for returning singleton reasource
@app.route('/movies/categories/bestpicture/1997/winner', methods=['GET'])
def getSingleton():
    category="BEST PICTURE"
    year = 1997
    winner = True
    # search function goes here
    return jsonify( searchByWinner(True, searchByYear(year, searchByCategory(category, data))) )

if __name__ == '__main__':
    app.run(debug=True)
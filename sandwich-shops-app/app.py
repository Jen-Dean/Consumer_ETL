from flask import Flask, render_template
from config import postgres_pwd
import sqlalchemy
from sqlalchemy import create_engine, func
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
# engine = create_engine("sqlite:///titanic.sqlite")
rds_connection_string = f"postgres:{postgres_pwd}@localhost:5432/for_now"
engine = create_engine(f'postgresql://{rds_connection_string}')

#################################################

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Routes
#################################################
def retrieve_data(post_query):
    results = engine.execute(post_query)
    results_lst = []
    for result in results:
        results_dict ={
            'Restaurant' : result[1],
            'Sandwich_Name' : result[2],
            'Bread_Type' : result[3],
            'Sandwich_Length' : result[4],
            'Sandwich_Description' : result[5],
            'Calories' : result[6],
            'Calories_From_Fat' : result[7],
            'Total_Fat' : result[8],
            'Protein' : result[9],
            'Saturated_Fat' : result[10],
            'Trans_Fat' : result[11],
            'Cholesterol' : result[12],
            'Sodium' : result[13],
            'Total_Carbs' :result[14],
            'Dietary_Fiber' : result[15],
            'Sugars' : result[16]
        }
        results_lst.append(results_dict)
    return results_lst
@app.route("/panera")
def panera():
    query = "SELECT * FROM  sandwiches WHERE restaurant_name = 'Panera'"
    results = retrieve_data (query)
    return render_template("panera.html",  sandwiches = results)

@app.route("/")
def home():
    query = "SELECT * FROM  sandwiches"
    results = retrieve_data (query)
    return render_template("index.html",  sandwiches = results)


@app.route("/jimmyjohns")
def jimmyjohns():
    query = "SELECT * FROM  sandwiches WHERE restaurant_name = 'Jimmy Johns'"
    results = retrieve_data (query)
    return render_template("jimmyjohns.html",  sandwiches = results)

@app.route("/subway")
def subway():
    query = "SELECT * FROM  sandwiches WHERE restaurant_name = 'Subway'"
    results = retrieve_data (query)
    return render_template("subway.html",  sandwiches = results)

@app.route("/quiznos")
def quiznos():
    query = "SELECT * FROM  sandwiches WHERE restaurant_name = 'Quiznos'"
    results = retrieve_data (query)
    return render_template("quiznos.html",  sandwiches = results)      

if __name__ == "__main__":
    app.run(debug=True)
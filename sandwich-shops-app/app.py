from flask import Flask, render_template

from config import postgres_pwd
import sqlalchemy

from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
# engine = create_engine("sqlite:///titanic.sqlite")
rds_connection_string = f"postgres:{postgres_pwd}@localhost:5432/programming_db"
engine = create_engine(f'postgresql://{rds_connection_string}')

#################################################


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Routes
#################################################
@app.route("/")
def home():
    return render_template("index.html", text="Sandwich shops")

@app.route("/api")
def api():
    results = engine.execute("select * from  programming_languages")
    results_lst = []
    for result in results:
        results_dict ={
            'id' : result[0],
            'language' : result[1],
            'rating': result[2]
        }
        results_lst.append(results_dict)
    return jsonify(results_lst)

if __name__ == "__main__":
    app.run(debug=True)
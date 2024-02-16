from flask import Flask, request, render_template
import pickle

# Load the model
with open('Olympic Analysis.pkl', 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)


@app.route("/", methods=["GET"])
def root():
    return render_template('index.html')


@app.route("/predict", methods=["GET"])
def predict():
    try:
        # Get the values entered by the user
        sex = str(request.args.get("Sex"))
        age = float(request.args.get("Age"))
        height = float(request.args.get("Height"))
        weight = float(request.args.get("Weight"))

        year = float(request.args.get("Year"))
        city = str(request.args.get("City"))

        sport = str(request.args.get("Sport"))

        team = str(request.args.get("Team"))
        gdp = float(request.args.get("GDP"))
        population = float(request.args.get("Population"))
        country_host = str(request.args.get("Country_Host"))

        # Make prediction using the loaded model
        prediction = model.predict([[sex, age, height, weight, year, city,
                                     sport, team, gdp, population, country_host]])

        if prediction[0] == 1:
            result = "The Player has higher chance to win in Olympic games."
        else:
            result = "The Player has lesser chance to win in Olympic games."

        return render_template('result.html', result=result)
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

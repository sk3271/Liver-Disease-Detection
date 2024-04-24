from flask import Flask, render_template, request 
import pickle 
import numpy as np 

app = Flask(__name__)

# Load the model from the pickle file
with open("D:/Internship/Rubixe/Liver-Disease-Detection/Model/random_forest.pkl", "rb") as file:
    model = pickle.load(file)


@app.route("/", methods=["GET"])
def home():
    return render_template('index.html')


@app.route("/predict", methods=["POST"])

def predict():
    if request.method == "POST":
        Age = int(request.form["Age"])
        Gender = int(request.form['Gender'])
        Total_Bilirubin = float(request.form['Total_Bilirubin'])
        Alkaline_Phosphotase = int(request.form['Alkaline_Phosphotase'])
        Alamine_Aminotransferase = int(request.form['Alamine_Aminotransferase'])
        Aspartate_Aminotransferase = int(request.form['Aspartate_Aminotransferase'])
        Total_Protiens = float(request.form['Total_Protiens'])
        Albumin = float(request.form['Albumin'])
        Albumin_and_Globulin_Ratio = float(request.form['Albumin_and_Globulin_Ratio'])

        values = np.array([[Age,Gender,Total_Bilirubin,Alkaline_Phosphotase,Alamine_Aminotransferase,Aspartate_Aminotransferase,Total_Protiens,Albumin,Albumin_and_Globulin_Ratio]])
        prediction = model.predict(values)

        return render_template('predict.html', prediction=prediction)



if __name__ == "__main__":
    app.run(debug=True)
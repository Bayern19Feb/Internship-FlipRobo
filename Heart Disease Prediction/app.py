from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the XGB CLassifier model
filename = 'Heart_Fail_XGB.pkl'
classifier = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template("index.html")

@app.route('/predict',methods=["POST"])

def predict():
    
    if request.method == "POST":
        
        age = float(request.form['Age'])
        rest_bp = float(request.form['RestingBP'])
        cholesterol = float(request.form['Cholesterol'])
        max_hr = float(request.form['MaxHR'])
        old = float(request.form['Oldpeak'])
        sex = int(request.form['Sex'])
        cpt = int(request.form['ChestPainType'])
        fbs = int(request.form['FastingBS'])
        ecg = int(request.form['RestingECG'])
        exercise = int(request.form['ExerciseAngina'])
        slope = int(request.form['ST_Slope'])
        
        output = np.array([[age,rest_bp,cholesterol,max_hr,old,sex,cpt,fbs,ecg,exercise,slope]])
        
        my_prediction = classifier.predict(output)
        
        return render_template('results.html', prediction=my_prediction)
        
        
            
        
	



if __name__ == '__main__':
	app.run(debug=True)
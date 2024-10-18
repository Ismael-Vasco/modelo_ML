# pip install flask
from flask import Flask, render_template, request
# pip install pickle4
import pickle

# pip install nltk
# import nltk

# pip install scikit_learn
from sklearn.naive_bayes import MultinomialNB

# inicializar app de Flask
app =  Flask(__name__)

# cargar el modelo
with open('modelo.pkl', 'rb') as f:
    modelo_tfdf = pickle.load(f)

# rutas de Flask para las rutas web
# ruta home
@app.route("/")
def home():
    return render_template("index.html")

# correr el programa
if __name__ == "__main__":
    app.run(debug=True)

# ejecutar en cmd de VSC: python app.py
# ctrl + c -> para terminar el proceso de run

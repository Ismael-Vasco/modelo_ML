# pip install flask
from flask import Flask, render_template, request
# 
import pickle

# pip install nltk
# import nltk

# inicializar app de Flask
app =  Flask(__name__)

# cargar el modelo
with open('modelo.pkl', 'rb') as f:
    modelo_tfdf = pickle.load(f)

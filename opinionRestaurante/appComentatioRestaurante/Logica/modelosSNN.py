from django.urls import reverse
import pandas as pd
from sklearn.pipeline import Pipeline
import pickle
from tensorflow.python.keras.models import load_model, model_from_json
from keras import backend as K
import numpy as np
import numpy as np
import re
from sklearn.pipeline import Pipeline
import pickle
import seaborn as sns
import copy
import nltk
import pickle
nltk.download('stopwords')
nltk.download('wordnet') 
nltk.download('omw-1.4')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from string import punctuation
from keras.models import load_model

from keras.preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
from nltk.stem.wordnet import WordNetLemmatizer
from django.urls import reverse
import pandas as pd
import pickle
pickle.HIGHEST_PROTOCOL = 4
print('Librerias importadas')

class modelosSNN():
    def cargarTokenizer(self, nombreArchivo):
        with open(nombreArchivo+'.pickle','rb')as handle:
            pipeline=pickle.load(handle)
        print ("tokenizer Cargador")
        return pipeline
    def cargarRNN(self, nombreRnn):
        model=load_model(nombreRnn+'.h5')
        print("Red neuronal cargada")
        return model
    

    def predecir_comentario(comentario_texto, comentario_numeros):
        model = load_model("C:/Users/PCX/opinionRestaurante/Recursos/modelo_entrenado.h5")
        print("RNN cargada")
        with open('C:/Users/PCX/opinionRestaurante/Recursos/Pipetokenizercuatro.pickle', 'rb') as handle:
          pipeline = pickle.load(handle)
        
        print('Picke cargado correctamente')
    # Tokenizar y convertir texto en secuencias
        new_data_text = pipeline.texts_to_sequences([comentario_texto])
        new_data_text = pad_sequences(new_data_text, maxlen=100)

    # Convertir números en un arreglo numpy
        new_data_num = np.array([comentario_numeros])

    # Combinar texto y números
        new_data = np.concatenate((new_data_text, new_data_num), axis=1)

    # Hacer la predicción con el modelo
        predictions = model.predict(new_data)
        class_index = np.argmax(predictions, axis=1)
        labels = ["mal comentario", "buen comentario", "excelente comentario"]
        predicted_labels = [labels[i] for i in class_index]
    
        return predicted_labels[0]




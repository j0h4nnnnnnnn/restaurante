from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import json
from django.http import JsonResponse
from appComentatioRestaurante.Logica import modelosSNN
from rest_framework.decorators import api_view

import os
from django.conf import settings

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'opinionRestaurante.settings')
print("Liberias de views importadas")

def home(request):
    return render(request, 'home.html')

class Clasificacion():
    def determinarCategoria(request):
        return render(request, "comentarioTipo.html")
    @api_view(['GET','POST'])
    def predecir(request):
        try:
            print("Ingresa a predecir")
            print(" ")
            print(request.POST)
            resultados = []
            comentario = str(request.POST.get('comentario'))
            servicio=int(request.POST.get('servicio'))
            comida=int(request.POST.get('comida'))
            ambiente=int(request.POST.get('ambiente'))
            resultados.append(servicio)
            resultados.append(comida)
            resultados.append(ambiente)
            #Consumo de la lógica para predecir si se aprueba o no el crédito
            resul=modelosSNN.modelosSNN.predecir_comentario(comentario,resultados)
            if(servicio>5 or comida>5 or ambiente>5 ):
            #resul=modelosSNN.modelosSNN.predecir_comentario(comentario,resultados)
                resul='Datos invalidos'
        except:
            if(servicio>5 or comida>5 or ambiente>5 ):
            #resul=modelosSNN.modelosSNN.predecir_comentario(comentario,resultados)
                resul='Datos invalidos'        
        
        if(resul=="buen comentario"):
            return render(request, "informe.html",{"e":resul  + " \n Gracias por su buen comentario"} )
        elif(resul=="mal comentario"):
            return render(request, "informe.html",{"e":resul  + " \n Disculpe por el mal momento. Mejoraremos nuestro servicio"} )
        elif(resul=="excelente comentario"):
            return render(request, "informe.html",{"e":resul  + " \n Gracias por su excelente comentario :)"} )


        
        
            
    @csrf_exempt
    @api_view(['GET','POST'])
    def predecirIOJson(request):
        print(request)
        print('***')
        print(request.body)
        print('***')
        body = json.loads(request.body.decode('utf-8'))
        #Formato de datos de entrada
        comentario=str(body.get("comentario"))
        servicio = int(body.get("servicio"))
        comida = int(body.get("comida"))
        ambiente = int(body.get("ambiente"))

        print(comentario)
        print(servicio)
        print(comida)
        print(ambiente)
       
        resul=modelosSNN.modeloSNN.predecirComentario(modelosSNN.modelosSNN,comentario=comentario, servicio=servicio,ambiente=ambiente, comida=comida)
        data = {'result': resul}
        resp=JsonResponse(data)
        resp['Access-Control-Allow-Origin'] = '*'
        return resp


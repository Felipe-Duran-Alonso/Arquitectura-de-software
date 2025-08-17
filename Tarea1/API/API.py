from fastapi import FastAPI
import random
import logging
from logging.handlers import RotatingFileHandler
import os
DIR = os.path.normpath("/app/logs")
NAME = "logsAPI.log"
os.makedirs(DIR, exist_ok=True)
app = FastAPI()

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    log_path = os.path.join(DIR, NAME)
    handler = RotatingFileHandler(log_path, maxBytes=5_000_000, backupCount=3)
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.propagate = False
    return logger

def set_info(string):
    global LOGS
    LOGS.info(string)
    for h in LOGS.handlers:
        h.flush()
    return None

LOGS = get_logger("API_logs")

@app.get("/random/{cantidad}/{inicio}/{tope}")
def read_root(cantidad: int, inicio: int,tope: int):
    global LOGS
    NAME = "ARR-"
    dict = {}
    #LOGS.info(f"Solicitud de {cantidad} listas de largo aleatorio. Con numeros entre {inicio} y {tope}")
    set_info(f"Solicitud de {cantidad} listas de largo aleatorio. Con numeros entre {inicio} y {tope}")
    try:
        for i in range(0,cantidad):
            largo = random.randint(3, 7)
            lista = largo*[0]
            for j in range(0,largo):
                lista[j] = random.randint(inicio, tope)
            nombre = NAME + str(i+1)
            dict[nombre] = lista
        #LOGS.info(f"El resultado: {dict}")
        set_info(f"El resultado: {dict}")
    except Exception as e:
        #LOGS.info(f"Error: {e}")
        set_info(f"Error: {e}")
    return dict


@app.get("/fibonacci/{num}")
def read_item(num: int):
    NAME = "F_"
    dict = {}
    #LOGS.info(f"Fibonacci de {num}")
    set_info(f"Fibonacci de {num}")
    if num <0:
        #LOGS.info(f"Error en la entrada, menor a 0")
        set_info(f"Error en la entrada, menor a 0")
    else:
        try:
            resultado = fib({},num)[0]
            keys = sorted(resultado.keys())
            for i in keys:
                dict[NAME + str(i)] = resultado[i]
            #LOGS.info(f"El resultado: {dict}")
            set_info(f"El resultado: {dict}")
        except Exception as e:
            #LOGS.info(f"Error: {e}")
            set_info(f"Error: {e}")
    return dict

#Fibonacci que reforna los valores en un diccionario
def fib(diccionario,iteracion):
    str_it = iteracion
    if iteracion ==0:
        diccionario[str_it] = 0
        return diccionario, 0
    elif iteracion == 1 or iteracion == 2:
        diccionario[str_it] = 1
        return diccionario, 1
    else:
        diccionario[str_it]= fib(diccionario,iteracion-1)[1]+fib(diccionario,iteracion-2)[1]
        return diccionario, diccionario[str_it]
    

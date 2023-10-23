"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd

import re

def quitar_espacio(texto):
  patron = re.compile(r'\s+')
  texto = re.sub(pattern = patron, repl= ' ',string = texto)
  texto = re.sub(r'\.', repl= '',string = texto)
  return texto

def quitar_porcentaje(texto):
  patron = re.compile(r'(\d+),(\d+)\s%')
  texto = re.sub(pattern=patron, repl=r'\1.\2', string=texto)
  texto = float(texto)
  return texto

def ingest_data():
    
    df = pd.read_fwf("clusters_report.txt", skiprows=4, header = None)
    
    df.columns = ['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave']
    
    df['principales_palabras_clave']=df.ffill().groupby('cluster')['principales_palabras_clave'].transform(lambda x: ' '.join(x))
    df=df.dropna().reset_index(drop=True)
    
    df['principales_palabras_clave'] = df['principales_palabras_clave'].apply(quitar_espacio)
    
    df['porcentaje_de_palabras_clave'] = df['porcentaje_de_palabras_clave'].apply(quitar_porcentaje)

    return df


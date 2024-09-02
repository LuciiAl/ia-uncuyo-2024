# Ejemplo de uso

from environment import *
from agent import *
import time 
import csv
import copy

def guardar_resultados_csv(resultados, nombre_archivo='resultados.csv'):
    # Definir las cabeceras
    cabeceras = ['size', 'dirtrate', 'performance', 'time']
    
    # Abrir el archivo CSV en modo escritura
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
        writer = csv.DictWriter(archivo_csv, fieldnames=cabeceras)
        
        # Escribir la fila de cabeceras
        writer.writeheader()
        
        # Escribir los datos de cada fila
        for resultado in resultados:
            writer.writerow(resultado)

if __name__ == "__main__":
    results=[]
    for j in range(1,5):
        if j==1:
            dirtrate=0.1
        elif j==2:
            dirtrate=0.2
        elif j==3:
            dirtrate=0.4
        else:
            dirtrate=0.8
        for i in range (1, 11):
            #print(f'Iteración {i}')
            size=2
            start=time.time()
            x= random.randint(1, size)
            y= random.randint(1, size)
            # Crear el entorno con tamaño 2*2, posición inicial en (x, y) y tasa de suciedad del 10%
            env = Environment(size , size, x-1, y-1, dirtrate)
            # Crear el agente
            ag = Agent(env)
            for action in range (1000):
                ag.think()
            #env.print_environment()
            end = time.time()
            results.append({
            'size': size,
            'dirtrate': dirtrate,
            'performance': env.get_performance(),
            'time': end-start
            })
    #print(results)
    guardar_resultados_csv(results)
    
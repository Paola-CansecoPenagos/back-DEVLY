import numpy as np
import pandas as pd
def statistical_calculator(arr_sorted):
    media = round(sum(arr_sorted) / len(arr_sorted),2)

    desviacion = 0
    for elemento in arr_sorted:
        desviacion += abs(elemento - media)
    desviacion_media = round(desviacion / len(arr_sorted), 2)

    varianza_resultado = 0
    for elemento in arr_sorted:
        valor = pow(abs(elemento - media),2)
        varianza_resultado = varianza_resultado + valor
    varianza = round(varianza_resultado/len(arr_sorted),2)

    desviacion_estandar = (varianza ** .5)
    moda_dict = {}  # Diccionario para almacenar la frecuencia de cada valor
    moda = []  # Lista para almacenar los valores modales
    max_frequency = 0

    for value in arr_sorted:
        if value in moda_dict:
            moda_dict[value] += 1
        else:
            moda_dict[value] = 1
        # Actualizar el valor de moda y su frecuencia máxima
        if moda_dict[value] > max_frequency:
            moda = [value]
            max_frequency = moda_dict[value]
        elif moda_dict[value] == max_frequency and value not in moda:
            moda.append(value)

    arr_ordenate = np.sort(arr_sorted)

    K = 1 + (3.322 * np.log10(len(arr_sorted)))
    K_round = round(K)
    print(f"K = 1 + 3.322 log10({len(arr_sorted)}) = {K}")
    print(f"K = {K_round}")
    R =arr_ordenate[-1] - arr_ordenate[0]
    print(f"R = Xmax - Xmin = {arr_ordenate[-1]} - {arr_ordenate[0]} = {R}")
    A = R/K_round
    print(f"A = {R}/{K_round} = {A}")
    A_round = round(A+0.1)
    print(f"A = {A_round}")
    #! table
    variabilidad = 0 # !importante dependiendo la lista de datos
    valor_min = arr_ordenate[0]
    datos = np.zeros((6, 6))  # ! fila, columna
    table_frecuency = pd.DataFrame(
        datos, columns=["LimInf", "LimSup", "Frecuencia", "Marca de clase", "LimInfExacta", "LimSupExacta"])

    table_frecuency.iloc[0, 0] = round(valor_min,2)
    table_frecuency.iloc[0, 1] = round(valor_min+A_round-variabilidad,2)
    for i in range(1, table_frecuency.shape[0]):
        table_frecuency.iloc[i, 0] = table_frecuency.iloc[i-1, 1] + 1  # type: ignore
        table_frecuency.iloc[i, 1] = table_frecuency.iloc[i, 0]+A_round-variabilidad
        table_frecuency.iloc[:, 1] = round(table_frecuency.iloc[:, 1], 2)
        table_frecuency.iloc[:, 0] = round(table_frecuency.iloc[:, 0], 2)
        table_frecuency.iloc[:, 2] = [np.sum((arr_ordenate >= table_frecuency.iloc[i, 0]) & (  # type: ignore
            arr_sorted <= table_frecuency.iloc[i, 1])) for i in range(table_frecuency.shape[0])]
        table_frecuency.iloc[:, 3] = round((table_frecuency["LimInf"] + table_frecuency["LimSup"]) / 2,2)
        table_frecuency.iloc[:, 3] = round(table_frecuency.iloc[:, 3], 2)
        
        table_frecuency.iloc[:, 4] = round((table_frecuency["LimInf"]-(variabilidad/2)),2)
        table_frecuency.iloc[:, 5] = round((table_frecuency["LimSup"]+(variabilidad/2)),2)


    return desviacion_media, media, varianza, desviacion_estandar, arr_ordenate, table_frecuency, moda
import pandas as pd
from certifi import where
from sodapy import Socrata


def crearCliente():
    client = Socrata("www.datos.gov.co", None )
    return client



def leerDatos(**filtrosUsados):
    client = crearCliente()

    try:
        resultados = client.get("ch4u-f3i5",**filtrosUsados)
        return resultados
    except Exception as e:
        print(f"Ocurrió un error al leer los datos: {e}")
        return []



def generarEstructuraDeDatos(filtrosUsados):
    resultados = leerDatos(**filtrosUsados)
    resultsDataFrame = pd.DataFrame.from_records(resultados)
    imprimirEstructura(resultsDataFrame,filtrosUsados)



def imprimirEstructura(resultsDataFrame,filtrosUsados):
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    print(resultsDataFrame[['departamento','municipio','cultivo','topografia']])
    obtenerMedianas(filtrosUsados)



def obtenerMedianas(filtrosUsados):
    obtenerDatosPH(filtrosUsados)
    obtenerDatosFosforo(filtrosUsados)
    obtenerDatosPotasio(filtrosUsados)



def obtenerDatosPH(filtrosUsados):
    whereCondition = (
        "ph_agua_suelo_2_5_1_0 > '1'"
    )
    filtrosUsados['where'] = whereCondition
    resultadosPH = leerDatos(**filtrosUsados)
    dataframePH = pd.DataFrame.from_records(resultadosPH)
    encontrarMedianaPH(dataframePH)
def encontrarMedianaPH(dataframe):
    columna_interes = dataframe['ph_agua_suelo_2_5_1_0']  # Accediendo a la columna

    columna_interes = pd.to_numeric(columna_interes, errors='coerce')  # Convertir a numérico

    mediana = columna_interes.median()

    if pd.isnull(mediana):
        print("No se pudo calcular la mediana (sin datos válidos).")
    else:
        print("Mediana calculada de la columna 'ph':")
        print(mediana)



def obtenerDatosFosforo(filtrosUsados):
    whereCondition = (
        "f_sforo_p_bray_ii_mg_kg > '0'"
    )
    filtrosUsados['where'] = whereCondition
    resultadosFosforo = leerDatos(**filtrosUsados)
    dataframeFosforo = pd.DataFrame.from_records(resultadosFosforo)
    encontrarMedianaFosforo(dataframeFosforo)


def encontrarMedianaFosforo(dataframe):
    columna_interes = dataframe['f_sforo_p_bray_ii_mg_kg']  # Accediendo a la columna

    columna_interes = pd.to_numeric(columna_interes, errors='coerce')  # Convertir a numérico

    mediana = columna_interes.median()

    if pd.isnull(mediana):
        print("No se pudo calcular la mediana (sin datos válidos).")
    else:
        print("Mediana calculada de la columna 'Fosforo':")
        print(mediana)



def obtenerDatosPotasio(filtrosUsados):
    whereCondition = (
        "potasio_k_intercambiable_cmol_kg > '0'"
    )
    filtrosUsados['where'] = whereCondition
    resultadosPotasio = leerDatos(**filtrosUsados)
    dataframePotasio = pd.DataFrame.from_records(resultadosPotasio)
    encontrarMedianaPotasio(dataframePotasio)



def encontrarMedianaPotasio(dataframe):

    columna_interes = dataframe['potasio_k_intercambiable_cmol_kg']

    columna_interes = pd.to_numeric(columna_interes, errors='coerce')


    mediana = columna_interes.median()

    if pd.isnull(mediana):
        print("No se pudo calcular la mediana (sin datos válidos).")
    else:
        print("Mediana calculada de la columna 'potasio:")
        print(mediana)



import pandas as pd

# Lee el archivo CSV y guárdalo en un DataFrame
df = pd.read_csv('USA_Housing.csv')

# Define una función que acepte una fila del DataFrame como argumento y realice las operaciones deseadas
def procesar_fila(fila):
    resultado = fila['Avg. Area House Age'] + fila['Avg. Area Number of Rooms']
    return resultado

# Utiliza el método iterrows() del DataFrame para aplicar la función definida a cada fila del DataFrame
for index, row in df.iterrows():
    resultado = procesar_fila(row)
    print(resultado)

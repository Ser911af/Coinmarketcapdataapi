import pandas as pd

# Cargar datos desde el archivo Excel
df = pd.read_excel('cryptocurrencies.xlsx')

# Lista de columnas que representan porcentajes
columns_to_fix = ['quote.USD.percent_change_1h', 
                  'quote.USD.percent_change_24h', 
                  'quote.USD.percent_change_7d', 
                  'quote.USD.percent_change_30d', 
                  'quote.USD.percent_change_60d', 
                  'quote.USD.percent_change_90d']

# Corregir el formato de las columnas de porcentajes
for column in columns_to_fix:
    df[column] = df[column] / 100

# Guardar los datos corregidos en un nuevo archivo Excel con el formato de porcentaje
with pd.ExcelWriter('cryptocurrencies_fixed.xlsx', engine='xlsxwriter') as writer:
    df.to_excel(writer, index=False, float_format='%.8f')  # Utilizamos float_format para especificar el formato de porcentaje

print("Datos corregidos guardados en 'cryptocurrencies_fixed.xlsx'")

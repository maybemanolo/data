import pandas as pd

# pandas tiene la habilidad para leer y modificar archivos, aqui
# vamos a hacer esto con csv excel html

# ahora podemos leer archivos asi, y lo hacemos dataframe

pd.read_csv('csv.csv')

# para modificar un csv usamos el metodo

df.to_csv('csv_n.csv', index=False)

# indicamos como se va llamar el nuevo archivo, y le ponemos 
# index=False para que no se modifque nada

# para leer archivos excel, lo cual pandas le cada sheet
# como un dataframe

pd.read_excel('excel.xlsx', sheetname='Sheet1')

# le decimos donde esta el archivo y el nombre del sheet que
# queremos como dataframe

# para poder guardar el el archivo como dataframe, le pasamos
# el excel y el nombre de la sheet

df.to_excel('excel_n.xlsx', sheet_name='NewSheet')

# html

html_pd = pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')

# esto va buscar los elementos <table> dentro del html y a
# parit de ellos crear el dataframe, nos va regresaar una lista
# de dataframesa, para cceder al que queremos es, muchas veces
# no se copia exactamente

html_pd[0]
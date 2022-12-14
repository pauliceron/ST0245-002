import pandas as pd
from general import general
import gmplot

df = pd.read_csv('calles_de_medellin_con_acoso.csv', sep=';')
dataframe = df.fillna({"harassmentRisk": df['harassmentRisk'].mean()})
mapa = gmplot.GoogleMapPlotter(6.2115169, -75.5728593, 14)

for i in range(3):
    ruta = general.dijkstra(general.grafo(dataframe, i), "(-75.5778046, 6.2029412)", "(-75.5762232, 6.266327)")
    latitud = []
    longitud = []

    for j in range(len(ruta)):
        valores = str(ruta[j])
        longitud.append(float(valores[1:valores.find(",")]))
        latitud.append(float(valores[valores.find(",") + 2:len(valores) - 1]))
        mapa.scatter(latitud, longitud, size=20, marker=False)
        mapa.plot(latitud, longitud, edge_width=7)

mapa.draw('ST0245-002/codigo')

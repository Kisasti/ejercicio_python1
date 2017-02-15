# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 19:07:00 2017

@author: kisasti
"""

# INSTRUCCION
# Es necesario instalar el paquete Basemap desde Anaconda Navigator
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# MODIFICABLE
# Debeis ajustar las coordenadas del mapa a la localizacion de la especie
# La ayuda esta en: http://matplotlib.org/basemap/api/basemap_api.html#module-mpl_toolkits.basemap
map = Basemap(projection='mill', resolution='l', llcrnrlon=110, llcrnrlat=10, urcrnrlon=150, urcrnrlat=50)

# MODIFICABLE
# Opciones del mapa
# Muchas mas en: http://matplotlib.org/basemap/api/basemap_api.html#module-mpl_toolkits.basemap
map.drawcoastlines(linewidth=0.9)
map.drawcountries(linewidth=0.2)
map.fillcontinents(alpha=0.9)
map.drawmapboundary()
map.drawmeridians(np.arange(0, 360, 30), labels=[False, False, False, True], linewidth=0.3)
map.drawparallels(np.arange(-90, 90, 30), labels=[False, True, False, False], linewidth=0.3)

# INSTRUCCION
# Debeis descargaros un fichero csv con un conjunto de registros (records) de una especie
# desde la pagina del OBIS: http://www.iobis.org y leerla en un DataFrame de pandas
# Ese DataFrame se debe llamar specie
speciePa =pd. read_csv('Occurrence_Pa.csv' , sep=';',
header=0, error_bad_lines=False, na_values=' ')
print(speciePa)

specieOka =pd. read_csv('Occurrence_Oka.csv' , sep=';',
header=0, error_bad_lines=False, na_values=' ')
print(specieOka)

# Datos de latitud y longitud de la especie
lonPa, latPa = map(list(speciePa['longitude']), list(speciePa['latitude']))
lonOka, latOka = map(list(specieOka['longitude']), list(specieOka['latitude']))

# MODIFICABLE
# Opciones de visualizacion de la especie
# Muchas mas en: http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot
map.drawcoastlines(linewidth=0.9)
map.drawcountries(linewidth=0.2)
map.fillcontinents(alpha=0.9)
map.drawmapboundary()
map.drawmeridians(np.arange(0, 360, 30), labels=[False, False, False, True], linewidth=0.3)
map.drawparallels(np.arange(-90, 90, 30), labels=[False, True, False, False], linewidth=0.3)
map.plot(lonPa, latPa, 'ro', markersize=3.8, markeredgecolor='none', label='Paralichthys olivaceus')
map.plot(lonOka, latOka, 'g*', markersize=4.259621, markeredgecolor='none', label='Okamejei kenojei')
plt.legend(loc='lower right', fontsize='small')
plt.title('Distribution map')
plt.savefig("distribution_map.pdf")

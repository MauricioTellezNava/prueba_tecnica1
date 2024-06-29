# Sobre el programa MilenioScraper


Este script de Python realiza web scraping en la página principal de Milenio.com para obtener información sobre los artículos publicados.

## Librerías utilizadas

- BeautifulSoup: para analizar el contenido HTML de la página y extraer información.
- requests: para realizar una solicitud HTTP a la página y obtener su contenido.
- pandas: para crear un DataFrame con la información extraída y exportarlo a un archivo .csv.
- numpy: para realizar operaciones con arrays.
- datetime: para obtener la fecha y hora actual y utilizarla en el nombre del archivo .csv.

## Funcionamiento

1. Se crea un header para simular una solicitud desde un navegador web.
2. Se realiza una solicitud HTTP a la página de Milenio.com utilizando la librería `requests` y se obtiene su contenido HTML.
3. Se crea un objeto `soup` utilizando `BeautifulSoup` para analizar el contenido HTML.
4. Se busca en el objeto `soup` todos los elementos `a` con la clase `"board-module__a"`, que corresponden a los artículos publicados en la página principal.
5. Para cada elemento encontrado, se extrae su nombre, enlace y categoría y se guarda en un diccionario `article`.
6. Cada diccionario `article` se agrega a una lista `articles`.
7. Se crea un DataFrame `df` con la lista `articles` y las columnas `'name'`, `'link'` y `'category'`.
8. Se obtiene la fecha y hora actual utilizando la librería `datetime` y se formatea como una cadena de texto.
9. Se crea el nombre del archivo .csv utilizando el prefijo `'noticias_'`, seguido de la fecha y hora formateada.
10. Se exporta el DataFrame `df` a un archivo .csv con el nombre creado anteriormente.

## Resultado

El resultado es un archivo .csv con el nombre `'noticias_HHMM_DDMMYYYY.csv'`, donde `HHMM` es la hora y minuto actual y `DDMMYYYY` es la fecha actual. 
El archivo contiene información sobre los artículos publicados en la página principal de Milenio.com, con las columnas `'name'`, `'link'` y `'category'`.

## Aspectos a considerar

Es esta primera versión, el programa todavía no puede extraer información respecto al autor del artículo, la fecha de publicación, el resumen o el contenido completo del artículo.
En este sentido, el programa necesita ser escalado pero también actualizado constantemente, para adaptarse a posibles cambios en la página de Milenio.com.

















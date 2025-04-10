# Reto Técnico: Procesamiento de Transacciones Bancarias (CLI)

## Introducción:
El proposito de este reto es desarrollar una aplicación de línea de comandos (CLI) que procese un archivo CSV con transacciones bancarias y genere un reporte.

## Instrucciones de Ejecución:
Es necesario tener instalado previamente python(+v2.7). 
   1. Agregar el archivo .csv a utilizar en la carpeta input (formato indicado en el enunciado del reto).
   1. Abrir una consola de comandos en la raiz del proyecto.
   2. Ejecutar el comando `python processing.py` seguido del nombre del archivo. (e.g `python processing.py data.csv`)

## Enfoque y Solución:
El enfoque de este proyecto es de brindar al usuario la posibilidad de indicar el archivo a utilizar y realizar el procesamiento del mismo en caso el archivo se encuentre. Caso contrario sera notificado del error. Al finalizar el procesamiento se mostrarán resultados siguiendo el formato recibido.

## Estructura del Proyecto:
El proyecto cuenta con dos archivos en la raiz
   - **processing.py** - Lógica del programa
   - **README.md** - Documentación

Adicionalmente se encuentra la carpeta input. La cual contiene los archivos .csv que serán utilizados por el programa.

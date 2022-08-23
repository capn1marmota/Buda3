Este es un optimizador de estaciones de metro.
Las estaciones pueden ser generadas modelandolas a 
partir de 2 archivos .tsv: Estaciones.tsv para representar estaciones
y Conexiones.tsv para representar... adivinaste, conexiones.
Simplemente edita los archivos especificados añadiendo los atributos indicados en los respectivos encabezados de columna.
("Estacion" y "color" para Estaciones.tsv y "Origen" y "Destino" para Conexiones.tsv).
Los archivos ya tienen una red modelada por defecto, asi que el programa está listo para utilizarse, solo ejecute "main.py" y 
otorgue los parametros solicitados.
Tanto "main.py" como "Estaciones.tsv" y "Conexiones.tsv" se encuentra en la carpeta src
El programa incluye
configuraciones para testeos automaticos por medio de
los modulos mypy, pytest y flake8

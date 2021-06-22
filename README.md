# Comparador de rostros
## Autor
Valerie Jiménez Meza (valerie.jimenez@sansano.usm.cl)  

## Descripción
Este programa recibe dos imagenes, una por defecto de Luke Skywalker ("rostro.jpg") y otras encontradas en un bucket s3, y devuelve el porcentaje de similitud entre los rostros. Como input recibe el nombre de un bucket s3 el cual debe contener una imagen llamada "rostro.jpg" y cualquier otra imagen con la que hacer la comparación.  El output entrega el número de coincidencias y el porcentaje de similitud.
```sh
nombre_imagen
Face matches: numero_de_matches Porcentaje de similitud:  porcentaje
```

## Tecnología
- `Python3.9`
- `aws-Rekognition`

## Instalación
Para este programa se utilizó `python3.9`, por lo que solo se asegura el correcto funcionamiento en dicha versión. Si no cuenta con ella, puede descargarlo en el siguiente link https://www.python.org/ftp/python/3.9.4/python-3.9.4-amd64.exe.    
Para utilizar este programa es necesario contar con las credenciales necesaria, para ello seguir el tutorial encontrado en el siguiente link https://docs.aws.amazon.com/rekognition/latest/dg/setup-awscli-sdk.html.  
Es necesario instalas el paquete `boto3`, a través del siguiente comando
```sh
pip install boto3
```
También se instaló un toolkit de aws para VSCode.

## Instrucciones de uso
Una vez descargada la carpeta, configuradas las credenciales y descargados los paquetes:
1. Desde una terminal: ir a la carpeta que contiene el código y ejecutar el siguiente comando
```sh
python3 aws.py
```
2. Desde VS code: abrir el archivo `aws.py` y presionar el botón de play que aparece en la esquina superior derecha.

Una vez realizada alguna de las acciones anteriores el programa le pedirá ingresar el nombre del bucket en el que se encuentran las imagenes. Luego, el programa revisará y comparará con cada imagen encontrada en el bucket.

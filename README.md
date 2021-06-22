# Comparador de rostros

## Descripción
Este programa recibe dos imagenes, una por defecto de Luke Skywalker ("rostro.jpg") y otras encontradas en un bucket s3, y devuelve el porcentaje de similitud entre los rostros. Este programa recibe el nombre de un bucket s3. Este debe contener una imagen llamada "rostro.jpg" y cualquier otra imagen con la que hacer la comparación.  

## Tecnología
- `Python3.9`
- `aws-Rekognition`

## Instalación
Para este programa se utilizó `python3.9`, por lo que solo se asegura el correcto funcionamiento en dicha versión. Si no cuenta con ella, puede descargarlo en el siguiente link https://www.python.org/ftp/python/3.9.4/python-3.9.4-amd64.exe.    
Para utilizar este programa es necesario contar con las credenciales necesaria, para ello seguir el tutorial encontrado en el siguiente link https://docs.aws.amazon.com/rekognition/latest/dg/setup-awscli-sdk.html.  
Es necesario instalas el paquete `boto3`, a través del siguiente comando
``` pip install boto3
```
También se instaló un toolkit de aws para VSCode.

## Instrucciones de uso
Una vez descargada la carpeta
1. Desde una terminal: ir a la carpeta que contiene el código y ejecutar el siguiente comando
```sh
python3 Main.py
```
2. Desde símbolos del sistema (windows): ir a la carpeta que contiene el código y ejecutar alguno de los siguientes comandos
```sh
python Main.py
py Main.py
Main.py
```
3. Doble click izquierdo sobre el archivo `Main.py`

#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
import datetime
import boto3

def compare_faces(sourceFile, targetFile):

    client=boto3.client('rekognition')
   
    imageSource=sourceFile
    imageTarget=targetFile

    response=client.compare_faces(SimilarityThreshold=80,
                                  SourceImage=imageSource,
                                  TargetImage=imageTarget)
    
    if len(response['FaceMatches'])==0:
        similarity='0'

    for faceMatch in response['FaceMatches']:
        position = faceMatch['Face']['BoundingBox']
        similarity = str(faceMatch['Similarity'])

    return len(response['FaceMatches']), similarity          

def main():
    log = open("log.txt", "w")
    log.write(str(datetime.datetime.now()))
    log.write(" Inicio ejecución"+"\n")

    s3=boto3.resource('s3')

    bucket=input("ingrese nombre del bucket: ")
    names=[]
    for i in s3.Bucket(bucket).objects.all():
        names.append(i.key)

    for i in names:
        source_file={
            'S3Object':{
                'Bucket':bucket,
                'Name': 'rostro.jpg'
            }
        }
        target_file={
            'S3Object':{
                'Bucket':bucket,
                'Name': i
            }
        }
        print("\n"+i)
        try:
            face_matches=compare_faces(source_file, target_file)
            print("Face matches: " + str(face_matches[0])+" Porcentaje de similitud: ", face_matches[1])
            info = str(datetime.datetime.now())+" Entrada a: rostro.jpg; Entrada b: "+i+" Resultado "+face_matches[1]+ "\% de similitud"+"\n"
        except:
            print("Ha ocurrido un error")
            info = str(datetime.datetime.now())+" Entrada a: rostro.jpg; Entrada b: "+i+" Resultado (No válido)"+"\n"
        log.write(info)
    log.close()

if __name__ == "__main__":
    main()
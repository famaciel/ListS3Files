import boto3

s3 = boto3.resource('s3')

def list_files(bucketName):
    files=[]
    bucket = s3.Bucket(bucketName)
    for imagem in bucket.objects.all():
        files.append(imagem.key)
    return files

print(list_files('logo-comics'))
inport boto3

s3 = boto3.resource('s3')

for bucket in s3.bucket.all():
    print(bucket.name)
    
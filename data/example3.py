import boto3

cliant = boto3.cliant('route53')

response = cliant.create_hosted_zone(

 Name='test.pyarashiro.com',
 CallerReference='2018042001'
    
)

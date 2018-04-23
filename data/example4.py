import boto3

cliant = boto3.cliant('route53')

response = cliant.change_resource_record_sets(
    HostedZoneId='Z2HBN7K2VNLICZ',
    changeBatch={
        'changes':[
            {
                'Action': 'CREATE',
                'ResourceRecordset':{
                    'name': 'test',
                    'type': 'A',
                    'ResourceRecords': [
                        {
                            '192.168.0.1'
                        },
                    ],
                }
            }
        ]
    }

)

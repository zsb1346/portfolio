import os, json
from qcloud_cos import CosConfig, CosS3Client

cred_path = os.path.expanduser('~/.tccli/default.credential')
with open(cred_path) as f:
    cred = json.load(f)

config = CosConfig(Region='ap-guangzhou', SecretId=cred['secretId'], SecretKey=cred['secretKey'])
client = CosS3Client(config)

bucket = 'portfolio-1460494365'
try:
    objects = client.list_objects(Bucket=bucket)
    if 'Contents' in objects:
        for obj in objects['Contents']:
            key = obj['Key']
            client.delete_object(Bucket=bucket, Key=key)
            print(f'Deleted: {key}')
    client.delete_bucket(Bucket=bucket)
    print('Old portfolio bucket deleted successfully')
except Exception as e:
    print(f'Already deleted or error: {e}')

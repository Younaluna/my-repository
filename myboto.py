import boto3

# sts example
# sts = boto3.client('sts')

# response = sts.get_caller_identity()

# print(response)

# s3 example
# s3 = boto3.resource('s3')

# for bucket in s3.buckets.all():
#     print(bucket.name)

# ec2 example
# ec2 = boto3.resource('ec2')
# for instance in ec2.instances.all():
#     print(instance.id, instance.state)

# another ec2 example
# ec2 = boto3.resource('ec2')
# ec2.create_instances(
#     ImageId = 'ami-09d95fab7fff3776c',
#     MinCount=1,
#     MaxCount=2,
#     InstanceType='t2.micro'
# )

# another sts example

# import boto3
# sts = boto3.client('sts')
# response = sts.get_caller_identity()
# user = response['UserId']
# account = response['Account']
# print(f'Hello you are logged in as user {user} to account {account}')

# s3 = boto3.client('s3')
# mybucketname = 'youna-0001'

# response = s3.create_bucket(
# Bucket = mybucketname,
# )
# location = response['Location']
# try:
#     print(f'Your bucket was created here: {location}')

# except:
#     print(f'An error occurred creating {mybucketname}')


s3 = boto3.client('s3')
mybucketname = 'youna-0001'
try:
    response = s3.delete_bucket(
        Bucket=mybucketname
    )
except:
    print(f'An error occurred deleting your bucket')


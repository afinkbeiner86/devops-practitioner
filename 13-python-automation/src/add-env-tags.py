import boto3

ec2_client_frankfurt = boto3.client('ec2', region_name="eu-central-1")
ec2_resource_frankfurt = boto3.resource('ec2', region_name="eu-central-1")

ec2_client_paris = boto3.client('ec2', region_name="eu-west-1")
ec2_resource_paris = boto3.resource('ec2', region_name="eu-west-1")

instances_ids_frankfurt = []
instances_ids_paris = []

reservations_frankfurt = ec2_client_frankfurt.describe_instances()['Reservations']
for res in reservations_frankfurt:
    instances = res['Instances']
    for ins in instances:
        instances_ids_frankfurt.append(ins['InstanceId'])

response = ec2_resource_frankfurt.create_tags(
    Resources=instances_ids_frankfurt,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'prod'
        }
    ]
)

reservations_paris = ec2_client_paris.describe_instances()['Reservations']
for res in reservations_paris:
    instances = res['Instances']
    for ins in instances:
        instances_ids_paris.append(ins['InstanceId'])

response = ec2_resource_paris.create_tags(
    Resources=instances_ids_paris,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'env'
        }
    ]
)
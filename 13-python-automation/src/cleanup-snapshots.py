import boto3
from operator import itemgetter

ec2_client = boto3.client('ec2', region_name="eu-central-1")

snapshots = ec2_client.describe_snapshots(
    OwnerIds=['self']
)

volumes = ec2_client.describe_volumes(
    Filters=[
        {
            'Name': 'tag:environment',
            'Values': ['prod']
        }
    ]
)

for volume in volumes['Volumes']:
    snapshots = ec2_client.describe_snapshots(
    OwnerIds=['self']
    Filters=[
        {
            'Name': 'volume-id',
            'Values': [volume['VolumeId']]
        }
    ]
    )

snapshots_by_date = sorted(snapshots['Snapshots'], key=itemgetter('StartTime'), reverse=True)

for snapshot in snapshots_by_date[:2]:
    response = ec2_client.delete_snapshot(
        SnapshotId=snap['SnapshotId']
    )
    print(response)
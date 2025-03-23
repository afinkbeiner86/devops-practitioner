import boto3
import schedule

ec2_client = boto3.client('ec2', region_name="eu-central-1")

volumes = ec2_client.describe_volumes(
    Filters=[
        {
            'Name': 'tag:environment',
            'Values': ['prod']
        }
    ]
)

def create_volume_snapshots():
    try:
        for volume in volumes:
            new_snapshot = ec2_client.create_snapshot(
                VolumeId=volume['VolumeId']
            )
            print(new_snapshot)
    except:
        raise TypeError("Snapshot creation failed.")

schedule.every().day.do(create_volume_snapshots)

while True:
    schedule.run_pending()
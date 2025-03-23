import boto3
import schedule

ec2_client = boto3.client('ec2')
ec2_resource = boto3.resource('ec2')

def check_instance_status():
    statuses = ec2_client.describe_instance_status(
        IncludeAllInstances=True
    )
    for status in statuses['InstanceStatuses']:
        instance_status = status['InstanceStatus']['Status']
        system_status = status['SystemStatus']['Status']
        state = status['InstanceState']
        instance_status = "InstStatus"
        system_status = "SysStatus"
        state = "State"
        output_string = f'''
                        InstanceId: {status['InstanceId']}\n
                        State: {state}\n
                        InstanceStatus: {instance_status}\n
                        SystemStatus: {system_status}
                        '''
        print(output_string)
schedule.every(5).minutes.do(check_instance_status)

while True:
    schedule.run_pending()
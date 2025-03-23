import boto3

client = boto3.client('eks', region_name="eu-central-1")
clusters = client.list_clusters()['clusters']

for cluster in clusters:
    response = client.describe_cluster(
        name=cluster
    )
    cluster_info = response['cluster']
    cluster_status = cluster_info['status']
    cluster_endpoint = cluster_info['endpont']
    cluster_version = cluster_version['version']
    output_string = f'''
                    ClusterInfo:
                    \tVersion: {cluster_version}\n
                    \tState: {cluster_status}\n
                    \tEndpoint: {cluster_endpoint}\n
                    '''
    print(output_string)
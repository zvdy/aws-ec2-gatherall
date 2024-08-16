import boto3

def get_instances_with_name_containing_apigee():
    client = boto3.client('ec2')

    # Retrieve all instances that are running
    instances = client.describe_instances(
        Filters=[
            {'Name': 'instance-state-name', 'Values': ['running']}
        ]
    )

    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_name = 'N/A'
            if 'Tags' in instance:
                for tag in instance['Tags']:
                    if tag['Key'] == 'Name' and '$FILTER'  in tag['Value'].lower(): # Replace $FILTER with the keyword you want to search for or remove this condition to get all instances
                        instance_name = tag['Value']
                        break

            # Skip instances that do not contain "$FILTER" in their name
            if instance_name == 'N/A':
                continue

            instance_id = instance['InstanceId']
            instance_type = instance['InstanceType']
            private_ip = instance.get('PrivateIpAddress', 'N/A')
            region = instance['Placement']['AvailabilityZone']
            subnet_id = instance.get('SubnetId', 'N/A')
            vpc_id = instance.get('VpcId', 'N/A')
            network_interfaces = [ni['NetworkInterfaceId'] for ni in instance.get('NetworkInterfaces', [])]

            volume_ids = [vol['Ebs']['VolumeId'] for vol in instance['BlockDeviceMappings'] if 'Ebs' in vol]
            volume_details = []
            for volume_id in volume_ids:
                volume = client.describe_volumes(VolumeIds=[volume_id])['Volumes'][0]
                volume_details.append(f"Volume ID: {volume['VolumeId']}, Size: {volume['Size']} GiB, Type: {volume['VolumeType']}")

            # Retrieve subnet CIDR block
            subnet_cidr = 'N/A'
            if subnet_id != 'N/A':
                subnet = client.describe_subnets(SubnetIds=[subnet_id])['Subnets'][0]
                subnet_cidr = subnet['CidrBlock']

            # Formatting output for readability
            print(f"Instance ID: {instance_id}")
            print(f"Instance Type: {instance_type}")
            print(f"Private IP: {private_ip}")
            print(f"Instance Name: {instance_name}")
            print(f"Region: {region}")
            print(f"Subnet ID: {subnet_id} - {subnet_cidr}")
            print(f"VPC ID: {vpc_id}")
            print(f"Network Interfaces: {', '.join(network_interfaces)}")
            print(f"Attached Volume IDs: {', '.join(volume_ids)}")
            print("Volume Details:")
            for detail in volume_details:
                print(f"  - {detail}")
            print("\n" + "="*80 + "\n")  # Separator for each instance

if __name__ == "__main__":
    get_instances_with_name_containing_apigee()
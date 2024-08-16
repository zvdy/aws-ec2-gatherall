import boto3
import argparse

def get_instances(client, ip_list=None, name_filter=None):
    filters = [{'Name': 'instance-state-name', 'Values': ['running']}]

    if name_filter:
        filters.append({'Name': 'tag:Name', 'Values': [f"*{name_filter}*"]})

    instances = client.describe_instances(Filters=filters)

    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_name = 'N/A'
            if 'Tags' in instance:
                for tag in instance['Tags']:
                    if tag['Key'] == 'Name':
                        instance_name = tag['Value']
                        break

            private_ip = instance.get('PrivateIpAddress', 'N/A')
            if ip_list and private_ip != 'N/A':
                if private_ip not in ip_list:
                    continue

            instance_id = instance['InstanceId']
            instance_type = instance['InstanceType']
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

def main():
    parser = argparse.ArgumentParser(description="Retrieve EC2 instance information.")
    parser.add_argument('--ip-list', help="Comma-separated list of IP addresses to filter instances by.")
    parser.add_argument('--name', help="Filter instances by name containing this keyword.")
    args = parser.parse_args()

    ip_list = args.ip_list.split(',') if args.ip_list else None

    if not ip_list and not args.name:
        confirm = input("No filters provided. This will query all running instances. Do you want to continue? (y/n): ")
        if confirm.lower() != 'y':
            print("Operation cancelled.")
            return

    client = boto3.client('ec2')

    get_instances(client, ip_list=ip_list, name_filter=args.name)

if __name__ == "__main__":
    main()
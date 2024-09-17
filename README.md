
# EC2 Instance Query CLI Tool
![aws](https://img.shields.io/badge/Amazon_AWS-232F3E?style=flat&logo=amazon-web-services&logoColor=white) ![py](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)

This CLI tool allows you to query AWS EC2 instances based on IP range and instance name using command-line arguments.

## Prerequisites

- Python 3.x
- `boto3` library

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/zvdy/aws-ec2-gatherall
    cd aws-ec2-gatherall
    ```

2. **Install dependencies**:
    ```bash
    pip install boto3
    ```

## Usage

### Query all running instances

To query all running instances (with a warning):
```bash
python main.py
```

### Filter by IP range

To filter instances by IP range:
```bash
python main.py --ip-range 192.168.1. 10.0.0.
```

### Filter by name

To filter instances by name:
```bash
python main.py --name apigee
```

### Filter by both IP range and name

To filter instances by both IP range and name:
```bash
python main.py --ip-range 192.168.1. 10.0.0. --name apigee
```

## Example Output

```
Instance ID: i-1234567890abcdef0
Instance Type: t2.micro
Private IP: 192.168.1.10
Instance Name: MyInstance
Region: us-west-2a
Subnet ID: subnet-12345678 - 192.168.1.0/24
VPC ID: vpc-12345678
Network Interfaces: eni-12345678
Attached Volume IDs: vol-12345678
Volume Details:
  - Volume ID: vol-12345678, Size: 8 GiB, Type: gp2

================================================================================
```

## Notes

- Ensure you have the necessary AWS credentials configured. You can set up your credentials by running `aws configure` or by setting environment variables.
- I recommend using a `venv` and/or run it on `aws cloudshell` directly.
- The script will print a warning if no filters are provided and will query all running instances.

## License

This project is licensed under the MIT License.

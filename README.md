# AWS EC2 Instance Information Script 

This Python script utilizes the `boto3` library to interact with AWS EC2 instances. It's designed to retrieve and display detailed information about EC2 instances that have a specific keyword in their name.

## Features

- **List EC2 Instances**: Retrieves all running EC2 instances.
- **Filter by Name**: Specifically looks for instances where the name contains a predefined keyword.
- **Detailed Information**: Outputs detailed information about each filtered instance, including:
  - Instance ID
  - Instance Type
  - Private IP
  - Instance Name
  - Region
  - Subnet ID
  - VPC ID
  - Network Interfaces
  - Attached Volume IDs
  - Volume Details

## Requirements

To run this script, you'll need:

- Python 3.x
- `boto3` library

## Installation

1. Ensure Python 3.x is installed on your system.
2. Install `boto3` using pip:

```bash
pip install boto3
```

> As a best practice, you can use a [virtial environment](https://docs.python.org/3/library/venv.html)

## Usage 
To use the script, simply run:

Make sure you have configured your AWS credentials beforehand, as boto3 requires them to interact with your AWS resources.

## Contributing 
Contributions, issues, and feature requests are welcome!

## License 
This project is open-source and available under the MIT License.
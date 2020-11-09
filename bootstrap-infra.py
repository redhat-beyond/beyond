#!/usr/bin/env python3
import os

import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv

# will be used when creating a new group on aws.
GROUP_NAME = 'bootstrapped_group'


def main():
    load_dotenv()
    ec2 = boto3.client('ec2')
    security_groups = os.getenv("SECURITY_GROUPS")
    group_permissions = [
        {
            'IpProtocol': 'tcp',
            'FromPort': 80,
            'ToPort': 80,
            'IpRanges': [
                {
                    'CidrIp': '0.0.0.0/0'
                }
            ]
        },
        {
            'IpProtocol': 'tcp',
            'FromPort': 22,
            'ToPort': 22,
            'IpRanges': [
                {
                    'CidrIp': '0.0.0.0/0'
                }
            ]
        }
    ]

    # this is needed for case when security_groups not found on aws
    response = ec2.describe_vpcs()

    try:
        response = ec2.describe_security_groups(GroupIds=[security_groups])
        existing_group_names = [i['GroupName'] for i in response['SecurityGroups']]
        if GROUP_NAME in existing_group_names:
            response = ec2.describe_security_groups(GroupNames=[GROUP_NAME])
            security_groups = response.get('SecurityGroups', [{}])[0].get('GroupId', '')

        data = ec2.authorize_security_group_ingress(
            GroupId=security_groups,
            IpPermissions=group_permissions
        )
        print('Ingress Successfully Set %s' % data)

    except ClientError as e:
        print(e)
        if 'already exists' not in e.response['Error']['Message']:
            vpc_id = response.get('Vpcs', [{}])[0].get('VpcId', '')
            response = ec2.create_security_group(
                GroupName=GROUP_NAME,
                Description='DESCRIPTION',
                VpcId=vpc_id
            )
            security_groups = response['GroupId']
            print('Security Group Created %s in vpc %s.' % (security_groups, vpc_id))

        if 'already exists' in e.response['Error']['Message']:
            security_groups = response.get('SecurityGroups', [{}])[0].get('GroupId', '')
        try:
            data = ec2.authorize_security_group_ingress(
                GroupId=security_groups,
                IpPermissions=group_permissions
            )
            print('Ingress Successfully Set %s' % data)
        except ClientError as e:
            print(e)


if __name__ == '__main__':
    main()

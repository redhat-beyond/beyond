#!/usr/bin/env python3
import os
import random
import string

import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv


def main():
    def random_string(string_length):
        """
        Generating random string which is used as a group name, when creating a new security group.
        :param string_length: (int) String length to be generated. For example 3 for 'abc'
        :return: Random string
        """
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(string_length))

    load_dotenv()
    ec2 = boto3.client('ec2')
    security_groups = os.getenv("SECURITY_GROUPS")
    group_permissions = [
        {'IpProtocol': 'tcp',
         'FromPort': 5000,
         'ToPort': 5000,
         'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
        {'IpProtocol': 'tcp',
         'FromPort': 22,
         'ToPort': 22,
         'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
    ]

    # this is needed for case when security_groups not found on aws
    response = ec2.describe_vpcs()

    try:
        response = ec2.describe_security_groups(GroupIds=[security_groups])

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
                GroupName=random_string(5),
                Description='DESCRIPTION',
                VpcId=vpc_id
            )
            security_group_id = response['GroupId']
            print('Security Group Created %s in vpc %s.' % (security_group_id, vpc_id))

        if 'already exists' in e.response['Error']['Message']:
            security_group_id = response.get('SecurityGroups', [{}])[0].get('GroupId', '')
        try:
            data = ec2.authorize_security_group_ingress(
                GroupId=security_group_id,
                IpPermissions=group_permissions
            )
            print('Ingress Successfully Set %s' % data)
        except ClientError as e:
            print(e)


if __name__ == '__main__':
    main()

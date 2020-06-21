#!/usr/bin/env python3

import boto3


def main():

    client = boto3.client('ec2')
    output = client.describe_instances()
    print(output)


if __name__ == '__main__':
    main()

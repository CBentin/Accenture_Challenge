# Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

import boto3

def create_bucket(bucket_name):
    """Create an S3 bucket in a specified region

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).

    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """

    s3_client = boto3.client('s3',
    aws_access_key_id = "ASIA26X47IGZ73HMJFP3",
        aws_secret_access_key= "v4iRFYhx6bwddPnNdMtOFsI1FezvyaCZ2+rEEEOO",
        aws_session_token="FQoGZXIvYXdzEPP//////////wEaDHVmlgUeT5fGO7fF2iKBAmGlbVM1FKHNhMxEL1QbXhICt8M1YGwENglLxPt8Tmi/As+8uVTWF+BPPfMIhSmsR0/iLGLzYwvPzLg8FWZC4rgNOzwJNuGz1Te9y1gV3sCtgkxOvTK76W2m6jaJG6qlTmhYcB8mEiy8rxTcnzuoO0cNEwzLHJVUeOkKZlBOxf/OUCb1KHVUe9H+aKrBcGySIydrvzxMDxShej5Ud/gU7pGblTbpmQEoMSIKY/E71uumOKv5XfdCaP7JGpTIUKMRwoYMDkc3XAslbRomP0RvQc81rV+IM8A4KzzvucIsN5LuegllNcGIqxDpEB/6xWEPhYCPxcrPNMuO7RcmJUgKbsJlKMX17+0F",
        region_name='us-east-1'
    )
    s3_client.create_bucket(Bucket=bucket_name)

def main():
    """Exercise create_bucket() method"""
    create_bucket('christian.accenture.challenge')

if __name__ == '__main__':
    main()
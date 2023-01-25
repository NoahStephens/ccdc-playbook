import boto3

def iam_client:
    return boto3.client('iam')

def create_user(client, name):
    client.create_user(UserName=name)

def create_bulk_users(client, users):
    # users is a python list of userNames

    for username in users:
        create_user(client, username)

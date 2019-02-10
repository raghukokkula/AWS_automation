#These Commands are used to create a user in AWS
import boto3
iam = boto3.client('iam')
responce = iam.create_user(UserName = 'raghukokkula')
print(responce)

#This command is used to get ARN number for that user
responce['User']['Arn']

#To get a list of the users in our AWS account
paginator = iam.get_paginator('list_users')
for responce in paginator.paginate():
	print(responce)

#This command is used to update user's name
iam.update_user(
	UserName = 'boto3-user',
	NewUserName = 'boto-user-changed'
)


#This command is used to delete a user
iam.delete_user(
	UserName = 'boto3-user-changed'
)

#!/bin/bash
#List all Instances In all regions.
for region in $(aws ec2 describe-regions --output text | cut -f3)
do
     aws ec2 describe-instances --region "$region" --output text --query 'Reservations[*].Instances[*].[Placement.AvailabilityZone, InstanceId, InstanceType, ImageId, PublicIpAddress ]'
done

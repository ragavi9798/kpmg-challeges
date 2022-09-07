import json
import boto3

def print_function(variable):
    ec2 = boto3.client('ec2')
    #specify the instance id for getting metadata
    instance_id = 'xyz'
    response = ec2.describe_instances(InstanceIds=[instance_id]) 
    print(response)
    try:
        print('Requested Individual Data Key : ', variable)
        print('Requested Individual Data Value: ', response['Reservations'][0]['Instances'][0][variable])
    
    except:
        print("Requested Key doesn't exist, please pass a new key")

#change the variable to required key to retrive the value
pass_variable = 'InstanceId'
print_function(pass_variable)

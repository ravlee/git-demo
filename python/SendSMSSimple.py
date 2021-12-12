import json
import boto3

#print('Loading function')
region = 'us-east-1'
phoneNumber = '+1111111111111'
msg = 'what is up?'

snsClient = boto3.client('sns')

def lambda_handler(event, context):
    # TODO implement
    snsResponse = sendText(phoneNumber, msg)
    print(json.dumps(snsResponse))
    return snsResponse
    
    
# Funtion to send a text message to the customer. Number retrieved from DynamoDB table  
def sendText(phoneNumber, msg):
    # print("insideSendText")
    snsClient = boto3.client("sns", region)
    snsResponse = snsClient.publish(PhoneNumber = phoneNumber, Message = msg)
    # print(json.dumps(snsResponse))
    return snsResponse

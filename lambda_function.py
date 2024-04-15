import json

def lambda_handler(event, context):
    # TODO implement
    print("This is my first sample git-lambda function demo py file")
    print("Here i am adding few lines to print code so that to show this is git-lamda demo")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

import boto3
import json

dynamodb = boto3.resource('dynamodb', region_name="us-east-1")

def handler(event, context):
    print(event)
    id=event["queryStringParameters"]["id"]
    table = dynamodb.Table('employee')
    response = table.get_item(Key={
    "id": id,
    "department": "engineering"
    })
    employee=response.get("Item")
    if employee==None:
        return{
        "body":"id is not valid",
        "statusCode": 404
        }
        
    return{
    "body":json.dumps(employee)
    }


def handler(event, context):
    print(event)
    item=event.get('body')
    print(type(item))
    item = json.loads(item)
    print(type(item))
    if item.get("id")==None:
      return{
    "body":"parameter missing",
    "statusCode":400
    }
      
    table = dynamodb.Table('employee')
    response = table.put_item(
    Item=item
    )
    return{
    "body":json.dumps(item),
    "statusCode":201
    }
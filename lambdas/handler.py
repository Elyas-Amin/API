import requests
import json
from notion import NotionAPI

def lambda_handler(event, context):
    # TODO implement
    inputInfo = json.loads(event["body"])
    
    body= json.dumps({"me": "I am not working"})
    if event["httpMethod"] == "POST" :
        jobName = inputInfo["job_name"]
        jobURL = inputInfo["job_url"]
        status = inputInfo["status"]
        databaseID = inputInfo["database_id"]
        notionApi = NotionAPI(databaseID)
        response = notionApi.send(jobName, jobURL, status)
        print(response)
    elif event["httpMethod"] == "GET":
        body =  json.dumps({"me": "this is GET"})  
    
    return {
        'isBase64Encoded': False, 
        'statusCode': 200,
        "headers": {"Access-Control-Allow-Headers" : "Content-Type", "Access-Control-Allow-Origin": "*", "Access-Control-Request-Method": "OPTIONS,POST,GET"},
        'body': body,      
    }
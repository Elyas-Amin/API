import requests
import json
import os

class NotionAPI:
    def __init__(self, databaseID):
        self.databaseID = databaseID
    def send(self, jobName, jobURL, status):
        payload = json.dumps({
            "parent": {
                "database_id": self.databaseID
            },
            "icon": {
                "emoji": "🖕🏼"
            },
            "cover": {
                "external": {
                "url": "https://upload.wikimedia.org/wikipedia/commons/6/62/Tuscankale.jpg"
                }
            },
            "properties": {
                "Job Name": {
                "title": [
                    {
                    "type": "text",
                    "text": {
                        "content": jobName
                    }
                    }
                ]
                },
                "Status": {
                "select": {
                    "name": status
                }
                },
                "Job Link": {
                "rich_text": [
                    {
                    "type": "text",
                    "text": {
                        "content": jobURL
                    }
                    }
                ]
                }
            }
            })
        headers = {
        'Authorization': 'Bearer ' + os.environ['mynotionapi'],
        'Content-Type': 'application/json',
        'Notion-Version': '2022-06-28'
        }
        response = requests.request("POST", "https://api.notion.com/v1/pages", headers=headers, data=payload)
        return response
                    
                    
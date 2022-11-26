import requests
import json

def lambda_handler(event, context):
    # TODO implement


    url = "https://api.notion.com/v1/pages"

    payload = json.dumps({
    "parent": {
        "database_id": "dfde6175175e424ab8cbceefb59173fb"
    },
    "icon": {
        "emoji": "🥬"
    },
    "cover": {
        "external": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/6/62/Tuscankale.jpg"
        }
    },
    "properties": {
        "Name": {
        "title": [
            {
            "text": {
                "content": "Tuscan Kale"
            }
            }
        ]
        }
    },
    "children": [
        {
        "object": "block",
        "type": "heading_2",
        "heading_2": {
            "rich_text": [
            {
                "type": "text",
                "text": {
                "content": "Lacinato kale"
                }
            }
            ]
        }
        },
        {
        "object": "block",
        "type": "paragraph",
        "paragraph": {
            "rich_text": [
            {
                "type": "text",
                "text": {
                "content": "Lacinato kale is a variety of kale with a long tradition in Italian cuisine, especially that of Tuscany. It is also known as Tuscan kale, Italian kale, dinosaur kale, kale, flat back kale, palm tree kale, or black Tuscan palm.",
                "link": {
                    "url": "https://en.wikipedia.org/wiki/Lacinato_kale"
                }
                }
            }
            ]
        }
        }
    ]
    })
    headers = {
    'Authorization': 'Bearer secret_qxLrZ7PeNbvgar57iAWQJndNSRYKNN2Qw3nh306kXZ0',
    'Content-Type': 'application/json',
    'Notion-Version': '2022-06-28'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    
    return {
        'statusCode': 200,
        'body': json.dumps({"me" : "Hello World"})
    }
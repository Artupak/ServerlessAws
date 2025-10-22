import json

def lambda_handler(event, context):
    
    try:
        name = event['queryStringParameters']['name']
    except (KeyError, TypeError):
        name = 'dostum'
            
    message = f"Merhaba {name}, bu fonksiyon bulutta çalışıyor!"
    
    response_body = {
        "message": message,
        "input_event": event
    }
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(response_body, ensure_ascii=False)
    }

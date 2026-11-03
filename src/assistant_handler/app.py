import json


def lambda_handler(event, context):
    body = {
        "message": "assistant scaffold is deployed",
        "step": 1,
        "input_event_present": bool(event),
    }
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body),
    }

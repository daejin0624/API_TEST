import json

def handler(event, context):
    # 금융결제원에서 전달된 데이터 처리
    try:
        request_body = json.loads(event['body'])
        print("Received data:", request_body)
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Callback received successfully"})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }

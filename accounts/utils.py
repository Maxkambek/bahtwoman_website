import requests


def verify(phone, code):
    url = "http://notify.eskiz.uz/api/message/sms/send"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDI0ODQ0NDMsImlhdCI6MTY5OTg5MjQ0Mywicm9sZSI6InVzZXIiLCJzdWIiOiIxMDUzIn0.UzXB5cWC0vANpL-fEicXZVMQIjLOab7bbCZ0rZQfXqo"}
    data = {
        'mobile_phone': phone,
        'message': code,
        'from': "4546",
        'callback_url': 'http://0.0.0.0.uz/test.php'
    }

    response = requests.post(url=url, data=data, headers=headers)
    return response

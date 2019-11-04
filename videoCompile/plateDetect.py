import boto3

def getPlate(img):
    # Change the value of bucket to the S3 bucket that contains your image file.
    # Change the value of photo to your image file name.
    client=boto3.client('rekognition',
        aws_access_key_id="ASIA26X47IGZUQCQYIUT",
        aws_secret_access_key="uEirj5f1KLxGl52ZbqG6gdIJU/hkEhEviPmATEeF",
        aws_session_token="FQoGZXIvYXdzEPz//////////wEaDNPTu/5uV11qUdEPBSKBAmh/79CDznZhzz1k/hFVlgHTHQcUAWX55xG7J5fZ0oGIF1iNEvSIfL2khOeL1kONiAf29FHvNgWs7mY8pP70X7gGOjnwB57woQVh4McBZaL4tsOKeLSRZsbporFlbI9Q77uu1vj1yoErBmY3Kt1lCN3k8hp/XjMQnuH8eTFMvBb3ZwVIPJQXBYAyjyyYi1I6O1y2lzLvDE6oXB8I5iOwrrqnzzbHVGRpJqzqnu/DI9NV76BkNPgisBRbZJItWSrfOYZNqovVd+QSNUpnga3H8GLfB7grHxYyh1ueqtq9f5/v9acIasTzjSRdc5TJAkx640XbAhCCPFuYr1tzRkQNcKvnKIX28e0F",
        region_name='us-east-1'
    )

    response=client.detect_text(Image={'Bytes': img})                
    textDetections=response['TextDetections']
    for text in textDetections:   
        for letters in text['DetectedText']:
            if(letters == '-'):
                return text['DetectedText']
    return ""
import boto3
import base64
import cv2

def downloadFrame(objectName):
    s3 = boto3.client('s3',
        aws_access_key_id="ASIA26X47IGZUQCQYIUT",
        aws_secret_access_key="uEirj5f1KLxGl52ZbqG6gdIJU/hkEhEviPmATEeF",
        aws_session_token="FQoGZXIvYXdzEPz//////////wEaDNPTu/5uV11qUdEPBSKBAmh/79CDznZhzz1k/hFVlgHTHQcUAWX55xG7J5fZ0oGIF1iNEvSIfL2khOeL1kONiAf29FHvNgWs7mY8pP70X7gGOjnwB57woQVh4McBZaL4tsOKeLSRZsbporFlbI9Q77uu1vj1yoErBmY3Kt1lCN3k8hp/XjMQnuH8eTFMvBb3ZwVIPJQXBYAyjyyYi1I6O1y2lzLvDE6oXB8I5iOwrrqnzzbHVGRpJqzqnu/DI9NV76BkNPgisBRbZJItWSrfOYZNqovVd+QSNUpnga3H8GLfB7grHxYyh1ueqtq9f5/v9acIasTzjSRdc5TJAkx640XbAhCCPFuYr1tzRkQNcKvnKIX28e0F",
        region_name='us-east-1'
    )
    response = s3.get_object(Bucket='christian.accenture.challenge',Key=objectName)
    return response

def main():
    for i in range(1,46):
        stream = downloadFrame("Frame_"+str(i))
        data = stream['Body'].read()
        filename = 'dFrame.jpg'  # I assume you have a way of picking unique filenames
        f = open(filename, 'wb')
        f.write(data)
        f.close()
        img = cv2.imread(filename)
        cv2.imshow("preview", img)
        cv2.waitKey(1)
        print(stream['Metadata']['plate'])

if __name__ == "__main__":
    main()
import plateDetect as p
import boto3
import cv2

def uploadFrame(objectName, img,plate):
    s3 = boto3.client('s3',
        aws_access_key_id="ASIA26X47IGZUQCQYIUT",
        aws_secret_access_key="uEirj5f1KLxGl52ZbqG6gdIJU/hkEhEviPmATEeF",
        aws_session_token="FQoGZXIvYXdzEPz//////////wEaDNPTu/5uV11qUdEPBSKBAmh/79CDznZhzz1k/hFVlgHTHQcUAWX55xG7J5fZ0oGIF1iNEvSIfL2khOeL1kONiAf29FHvNgWs7mY8pP70X7gGOjnwB57woQVh4McBZaL4tsOKeLSRZsbporFlbI9Q77uu1vj1yoErBmY3Kt1lCN3k8hp/XjMQnuH8eTFMvBb3ZwVIPJQXBYAyjyyYi1I6O1y2lzLvDE6oXB8I5iOwrrqnzzbHVGRpJqzqnu/DI9NV76BkNPgisBRbZJItWSrfOYZNqovVd+QSNUpnga3H8GLfB7grHxYyh1ueqtq9f5/v9acIasTzjSRdc5TJAkx640XbAhCCPFuYr1tzRkQNcKvnKIX28e0F",
        region_name='us-east-1'
    )
    s3.put_object(Bucket='christian.accenture.challenge',Key=objectName,Body=img,Metadata={'plate':plate})


def main():
    vc = cv2.VideoCapture("./videos/parkEntry.mp4")
    count = 0
    while vc.isOpened():
        count += 1
        _,frame = vc.read()    
        frame = cv2.resize(frame, (640,480), interpolation = cv2.INTER_AREA)
        cv2.imwrite("frame.jpg", frame)
        imageTarget=open("frame.jpg",'rb')
        target = imageTarget.read()
        if(count%5 == 0):
            plate = p.getPlate(target)
        else:
            plate = ""
        uploadFrame("Frame_"+str(count), target, plate)
        print(type(target))
        print(plate, " ", count)
        key = cv2.waitKey(100)
        cv2.imshow("preview", frame)
        if key == 27: # exit on ESC
            break
    print("Uploaded " + str(count) + " frames to bucket")

if __name__ == "__main__":
    main()
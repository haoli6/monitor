import requests
import base64
import cv2 as cv


# opencv 图片
def vehicle_detect(img):
    request_url1 = "https://aip.baidubce.com/rest/2.0/image-classify/v1/vehicle_detect"
    request_url2 = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_attr"
    _, encoded_image = cv.imencode('.jpg', img)
    base64_image = base64.b64encode(encoded_image)
    params = {"image":base64_image}
    access_token = '24.659d11721ba5a9040695e494f4320b47.2592000.1722490428.282335-89975938'
    request_url1 = request_url1 + "?access_token=" + access_token
    request_url2 = request_url2 + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response1 = requests.post(request_url1, data=params, headers=headers)
    response2 = requests.post(request_url2, data=params, headers=headers)
    num1 = 0
    num2 = 0
    if response1:
        data1 = response1.json()
        num1 = data1['vehicle_num']['car']
        for item in data1['vehicle_info']:
            location = item['location']
            x1 = location['left']
            y1 = location['top']
            x2 = x1 + location['width']
            y2 = y1 + location['height']
            cv.rectangle(img,(x1,y1),(x2,y2),(209,206,0),1)
        # 定义要绘制的文字
            text = item['type']
            position = (x1, y1-2)
            font = cv.FONT_HERSHEY_SIMPLEX
            font_scale = 1
            color = (0, 0, 255)  # 红色
            thickness = 1
            img = cv.putText(img, text, position, font, font_scale, color, thickness, cv.LINE_AA)
            # cv.imshow('Rectangle', img)
            # return img
    if response2:
        data2 = response2.json()
        num2 = data2['person_num']
        for item in data2['person_info']:
            location = item['location']
            x1 = location['left']
            y1 = location['top']
            x2 = x1 + location['width']
            y2 = y1 + location['height']
            cv.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

            # 定义要绘制的文字
            text = item['attributes']['gender']['name']
            if text=="男性":
                text="male"
            elif text=="女性":
                text="female"
            else:
                text="unkonw"
            position = (x1, y1 - 2)
            font = cv.FONT_HERSHEY_SIMPLEX
            font_scale = 1
            color = (0, 255, 0)  # 红色
            thickness = 1
            img = cv.putText(img, text, position, font, font_scale, color, thickness, cv.LINE_AA)

    return img, num1,num2


import base64

from aip import AipFace

""" 你的 APPID AK SK """
APP_ID = '17392564'
API_KEY = 'rXidKnUZtmtUfjm7BFuARI9V'
SECRET_KEY = 'rH5XQf1z4sYeaMAMTzsMKRqtRL4xvOTH'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)

with open("D:\\pycharmWorkProject\\peom\\files\\timg.jpg", 'rb') as f:
    base64_data = base64.b64encode(f.read())
    s = base64_data.decode()
    print('data:image/jpeg;base64,%s'%s)
    image = s

    imageType = "BASE64"

    """ 调用人脸检测 """

    options = {}
    options["face_field"] = "age,expression,gender,glasses,race,emotion"
    options["max_face_num"] = 2
    options["face_type"] = "LIVE"
    options["liveness_control"] = "LOW"
    res =client.detect(image, imageType,options)
    print(res)


import cv2
import dropbox
import time
import random
start_time.time()

def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        #read the frames while the camera is on
        ret,frame = videoCaptureObject.read()
        #cv2.imwrite() method is used to save an image to any storage device
        img_name="img"+str(number)+".g"
        cv2.imwrite("img_name",frame)
        start_time = time.time
        result = False
    return img_name
    print("snapshot taken")
    #releasing the camera
    videoCaptureObject.release()
    #to close all the windows that might be opened while this process
    cv2.destroyAllWindows()
    def upload_file(img_name):
         access_token = "sl.BCE-0YuNCtZ5ncb_3rB1EWTZm0mS-vvK311-5dLLGhCeSWj1IOP8Tnqh_9otXNQSE7NeRxAdIO3D1hCbl8F86RWLyx3Loxt2Uwu-WiXlAQpZ_00bc7yaSucTVuXHvGKeg7HFBbU" 
         file =img_name
         file_from = file 
         file_to="/testFolder/"+(img_name) 
         dbx = dropbox.Dropbox(access_token)
         with open(file_from, 'rb') as f:
                 dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
                 print("file uploaded")
    def main():
        while(True):
               if ((time.time() - start_time) >= 5):
                    name = take_snapshot()
                    upload_file(name)
    main()
try:
    import tweepy
    import os
    import glob2
    import time
    import configparser
    import datetime
except:
    print ("Modules not installed. Run 'pip install -r requirements.txt'")


def changeAvi(image):
    """
    Handles authentication and 
    uploading of selected image
    """

    auth = tweepy.OAuthHandler(parser.get("Credentials", "api_key"), parser.get("Credentials", "api_secret"))
    auth.set_access_token(parser.get("Credentials", "access_token"), parser.get("Credentials", "access_token_secret"))
    api = tweepy.API(auth)

    try:
        api.update_profile_image(image)
        print ("Succesfully uploaded image file", os.path.basename(image))
        uploadInterval()
    except Exception as e:
        print ("Image file", os.path.basename(image) + " failed to upload:\n" + str(e) + "\n")
        

def uploadInterval():
    """
    Sets a delay between
    every image change
    in minutes
    """

    interval = int(parser.get("Upload_Interval", "interval"))
    nextuploadtime = datetime.datetime.now() + datetime.timedelta(hours=0, minutes=interval, seconds=0)
    print ("Waiting for next upload at " + str(nextuploadtime) + "\n")
    time.sleep(interval * 60)


def getImage():
    """
    Verifies that the supplied image
    format and size is supported and 
    returns an image at a time
    """
        
    path = glob2.glob(os.path.join(os.getcwd(), "images", "*"))

    i = 0
    while i < len(path) + 1:
        if i < len(path):
            if int(os.stat(path[i]).st_size) <= 700000: 
                if os.path.basename(path[i]).lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                    changeAvi(path[i])
                    i += 1
                else:
                    print (os.path.basename(path[i]), "is not a supported file type.\nSkipping upload\n")
                    i += 1
            else:
                print (os.path.basename(path[i]), "file size is too big.\nSkipping upload\n")
                i += 1
        else:
            i = 0


parser = configparser.ConfigParser()
parser.read("config.ini")
getImage()

import requests
import json
import sys
import pprint
from base64 import b64encode

########################################################
# must enter image file name as first arguement
########################################################

#This is where you enter the web server address
web_server = ""
#This is where you enter the authentication key
auth_key = ""


#This sends the encoded license picture to the web service      
def parse_image(image_b64):
        data ={"authKey":auth_key, "data":image_b64}
        response = requests.post(web_server, json=data)
        pprint.pprint(response.text)
        print "status code = " + str(response.status_code)
        if response.status_code != 200:
                raise RuntimeError('Server did not return a \'200 OK\' status code, instead, it returned ' +str(response.status_code))
        elif response.json()["ParseImageResult"]["ErrorMessage"]=="Object reference not set to an instance of an object.":
                raise RuntimeError('Error message:Object reference not set to an instance of an object. This may mean the image in the database is of too poor quality to be parsed')

#This is the main function, it encodes the text and picture into base64
def main():
        if len(sys.argv) != 2:
                raise RuntimeError('Wrong number of arguements, this program accepts one arguement, the name of an image file')
        else:
                f = open(sys.argv[1], 'rb').read()
                image_b64 = b64encode(f)
                parse_image(image_b64)

if __name__ == "__main__":
        main()
        

import requests
import urllib.parse
import sys


def test_url(URL,Task_ID,PSW):
    username = Task_ID
    password = PSW
    username_encoded = urllib.parse.quote(username)
    URL = ("https://%s:%s@"+str(URL)) % (username_encoded, password)

    try:
        req=requests.get(URL)
        status=str(req.status_code)
        
    except:
        status=str(404)
        
    print(status)
    return status

# Pass URL, ID and Password and HTTP test will return Status code

if __name__ == "__main__":
    URL = sys.argv[1]
    Task_ID = sys.argv[2]
    PSW = sys.argv[3]
 
    test_url(URL,Task_ID,PSW)

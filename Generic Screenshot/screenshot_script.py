import pyautogui
import sys

def Screenshot(path):
    try:
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(path)
        status='Success'
    except Exception as e:
        status=e
    print(status)
    return status

'''
path="C:\\Users\\BrunoHenriqueNunes\\Desktop\\test-screenshot\\test.png"
Screenshot(path)
'''

if __name__ == "__main__":
    path = sys.argv[1]
    Screenshot(path)

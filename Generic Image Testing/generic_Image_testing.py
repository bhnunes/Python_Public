import time
import pyautogui
import sys


def check_image(image_path,confidence_level):

    try:
        time.sleep(2)
        alpha=pyautogui.locateOnScreen(str(image_path), confidence=float(confidence_level))
        if alpha!=None:
            status=str("Image Found")
        else:
            status=str("Image Not Found")
    except Exception as e:
        status=str(e)

    print(status)
    
    return status

#pip install open CV required

if __name__ == "__main__":
    image_path = sys.argv[1]
    confidence_level = sys.argv[2]
    check_image(image_path,confidence_level)
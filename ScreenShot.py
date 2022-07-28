import time

import pyscreenshot as ImageGrab
import schedule

from PIL import ImageGrab
from datetime import datetime


def take_screenshot():
    print("Taking screenshot...")

    
    screenshot = ImageGrab.grab()

    

    screenshot.save('screenshot_PIL.png')

    print("Screenshot taken...")

    return screenshot


def main():
    schedule.every(5).seconds.do(take_screenshot)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()
